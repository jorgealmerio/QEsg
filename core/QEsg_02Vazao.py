# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QEsg_02Vazao
                                 A QGIS plugin
 Plugin para Calculo de redes de esgotamento sanitario
                              -------------------
        begin                : 2016-03-15
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Jorge Almerio
        email                : jorgealmerio@yahoo.com.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.core import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.utils import *
import os.path
from QEsg_00Model import *
from QEsg_04Estilos import *
#        from qgis.gui import QgsMessageBar

class QEsg_02Vazao:
    def CalcVazao(self):
        proj = QgsProject.instance()
        ProjVar=proj.readEntry("QEsg", 'PIPES')[0]
        vLayer=QgsMapLayerRegistry.instance().mapLayersByName(ProjVar)[0]
        if not self.VerificaNulos(vLayer):
            return False
        EmOrdem, msg = self.VerificaOrdem(vLayer)
        if not EmOrdem:
            print msg
            self.Ordena(vLayer)
        Lini,Lfim = self.CompVirtualRede(vLayer)#Extensao da rede 1a e 2a etapas
        QiniTot,QfimTot = self.Vazoes()#Vazao total inicio e fim de plano
        if Lini==0:#Caso de Interceptor
            QdisIni=0
        else:
            QdisIni=QiniTot/Lini
        if Lfim==0:#Caso de Interceptor
            QdisFim=0
        else:
            QdisFim=QfimTot/Lfim
        Qinfilt=float(proj.readEntry("QEsg", 'COEF_INF')[0])
        vLayer.startEditing()
        for feat in vLayer.getFeatures():
            ext=feat['LENGTH']
            QconcIni=feat['Q_CONC_INI']
            QconcFim=feat['Q_CONC_FIM']
            oPVM=feat['PVM']
            pontaSeca=feat['PONTA_SECA']
            lados=feat['CONTR_LADO']
            if pontaSeca=='S':
                QmontIni = QmontFim = 0
            else:
                QmontIni, QmontFim, Valido=self.VazaoTrechosMont(vLayer, oPVM)
                if not Valido:
                    aviso = QCoreApplication.translate('QEsg',u'Não é permitido PV com mais de uma saída! Identifique os \'Ponta Seca\'')
                    self.FeicaoSelecionaMostraAvisa(vLayer, feat.id(), aviso)
                    return False
            QtrIni=QmontIni+QconcIni+(Qinfilt+QdisIni*lados/2)*ext
            QtrFim=QmontFim+QconcFim+(Qinfilt+QdisFim*lados/2)*ext
            feat['Q_INI']=QtrIni
            feat['Q_FIM']=QtrFim
            vLayer.updateFeature(feat)
        EstiloClasse=Estilos()
        EstiloClasse.CarregaEstilo(vLayer, 'rede_vazao.qml')
        iface.mapCanvas().refresh()
        iface.messageBar().pushMessage("QEsg:", QCoreApplication.translate('QEsg',u'Vazões calculadas com sucesso!'), level=QgsMessageBar.INFO, duration=4)
    def VazaoTrechosMont(self,vLayer,pvm):
        #somar as vazoes dos trechos que desaguam em pvm
        QmontIni=QmontFim=0
        for feat in vLayer.getFeatures():
            if feat['PVJ']==pvm:
                if feat['Q_INI']==NULL or feat['Q_FIM']==NULL:
                    return 0,0, False
                QmontIni+=feat['Q_INI']
                QmontFim+=feat['Q_FIM']
        return QmontIni, QmontFim, True
    def Vazoes(self):
        proj = QgsProject.instance()
        popini=float(proj.readEntry("QEsg", 'POPINI')[0])
        popfim=float(proj.readEntry("QEsg", 'POPFIM')[0])
        perCapt=float(proj.readEntry("QEsg", 'PERCAPTA')[0])
        k1=float(proj.readEntry("QEsg", 'K1_DIA')[0])
        k2=float(proj.readEntry("QEsg", 'K2_HORA')[0])
        coefRet=float(proj.readEntry("QEsg", 'COEF_RET')[0])
        Qini=popini*perCapt*k2*coefRet/86400
        Qfim=popfim*perCapt*k1*k2*coefRet/86400
        return Qini,Qfim
    def CompVirtualRede(self,vLayer):
        tot1a=tot2a=0
        for feat in vLayer.getFeatures():
            ext=feat['LENGTH']
            if ext == NULL or ext==0:
                return 0,0 #'Campo LENGTH com valor zero ou nulo'
            lados=feat['CONTR_LADO']
            if lados==NULL:
                return 0,0 #'Campo CONTR_LADO com valor zero ou nulo'
            etapa=feat['ETAPA']
            lVirtual=ext*lados/2
            if etapa==1:
                tot1a+=lVirtual
                tot2a+=lVirtual
            elif etapa==2:
                tot2a+=lVirtual
        return tot1a,tot2a

    def VerificaNulos(self,vLayer):#retorna Falso se houver trecho com identificacao nula
        CamposVerif=['DC_ID','Coletor','Trecho','PVM','PVJ','Q_CONC_INI','Q_CONC_FIM']
        Invalidos=[NULL,None,'']
        for feat in vLayer.getFeatures():
            for campo in CamposVerif:
                oValor=feat[campo]
                if oValor in Invalidos:
                    aviso=QCoreApplication.translate('QEsg',u'\'{}\' com valor Nulo! Utilize a Ferramenta de Numeração ou Preenchimento').format(campo)
                    self.FeicaoSelecionaMostraAvisa(vLayer, feat.id(), aviso)
                    return False
        return True

    def FeicaoSelecionaMostraAvisa(self,Layer,FeicaoID,aviso):
        Layer.select(FeicaoID)
        mapCanvas = iface.mapCanvas()
        mapCanvas.zoomToSelected(Layer)
        iface.messageBar().pushMessage("QEsg:", aviso, level=QgsMessageBar.WARNING, duration=4)

    def VerificaOrdem(self,vLayer):
        #vLayer=iface.activeLayer()
        cont=0
        msg=''
        for feat in vLayer.getFeatures():
            cont+=1
            if cont>1:
                ClAtual=feat['Coletor']
                TrAtual=feat['Trecho']
                if ClAtual==Coletor:#Se o coletor atual é igual ao anterior
                    if TrAtual<=Trecho:
                        msg='Trecho ' + str(TrAtual)+' duplicado ou fora de ordem!'
                        return False,msg
                    elif TrAtual-Trecho>1:
                        msg='Trecho ' + str(Trecho+1)+' Faltando!'
                        return False,msg
                    else:
                        msg='ok'
                elif (Coletor-ClAtual==1) and (TrAtual==1):
                    msg='ok-novo trecho'
                else:
                    msg='Coletor ' + str(ClAtual)+' duplicado ou fora de ordem!'
                    return False,msg
            Coletor=feat['Coletor']
            Trecho=feat['Trecho']
            print cont, Coletor, Trecho, msg
        return True, msg
    def Ordena(self,vLayer):
        dp=vLayer.dataProvider()
        fldColetor=dp.fieldNameIndex('Coletor')
        fldTrecho=dp.fieldNameIndex('Trecho')
        vLayer.setSubsetString('')
        ColMax=vLayer.maximumValue(fldColetor)

        #Looping decrescente nos coletores
        featList = []
        request = QgsFeatureRequest()
        for i in xrange(ColMax,0,-1):
            vLayer.setSubsetString('"Coletor" =' +str(i))
            TrMax=vLayer.maximumValue(fldTrecho)
            #Looping crescente nos trechos
            for j in xrange(TrMax):
                request.setFilterExpression( '"Trecho" ='+str(j+1) )
                iterator=vLayer.getFeatures( request )
                for feicao in iterator:
                    featList.append(feicao.id())

        vLayer.setSubsetString('')
        vLayer.startEditing()
        for fid in featList:
            #Criei um filtro para poder copiar a feicao desejada 
            request = QgsFeatureRequest().setFilterFids([fid])
            iterator=vLayer.getFeatures( request )
            for feicao in iterator:
                geom=feicao.constGeometry()
                attrs=feicao.attributes()
                fet = QgsFeature()
                fet.setGeometry( geom)
                fet.setAttributes(attrs)
                if not(vLayer.addFeature(fet,False)):#False=not update extent
                    QMessageBox.warning(None,'QEsg',QCoreApplication.translate('QEsg',u'Falha ao adicionar feição'))
                    return
        
        #featList.sort(key=lambda x: x[2])
        vLayer.updateExtents()
        #Apago as feicoes originais, pois ja as copiei na ordem desejada
        for fid in featList:
            vLayer.deleteFeature(fid)
                