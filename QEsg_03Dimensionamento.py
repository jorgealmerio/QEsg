# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QEsg_03Dimensionamento
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
import math


class QEsg_03Dimens:
    def Dimensiona(self):
        proj = QgsProject.instance()
        ProjVar=proj.readEntry("QEsg", 'PIPES')[0]
        vLayer=QgsMapLayerRegistry.instance().mapLayersByName(ProjVar)[0]
        if not self.VerificaNulos(vLayer):
            return False
        if not self.Verifica_InterfsNulos():
            return False
        if not self.Verifica_TrechosExistentes(vLayer):
            return False
        Trechos=vLayer.getFeatures()
        vLayer.startEditing()
        diam_min0=float(proj.readEntry("QEsg", "DN_MIN","150")[0])
        q_min=float(proj.readEntry("QEsg", "Q_MIN","1.50")[0])
        max_forcar=float(proj.readEntry("QEsg", "MAX_FORCAR","0.30")[0])#altura max para forcar a jusante
        deg_ignore=float(proj.readEntry("QEsg", "DEG_IGNORE","0.02")[0])#degrau para ser desprezado
        deg_min=float(proj.readEntry("QEsg", "DEG_MIN","0.00")[0])#degrau minimo
        Diam_progress=proj.readNumEntry("QEsg", "DIAM_PROGRESS",1)[0]#diametros progressivos
        tubosMat=proj.readEntry("QEsg", "TUBOS_MAT","0")[0]
        if tubosMat=='0':#se nao tiver lista de diametros definidas
            iface.messageBar().pushMessage("QEsg:", QCoreApplication.translate('QEsg',u'Lista de diâmetros indefinida!'), 
                                           level=QgsMessageBar.WARNING, duration=4)
            return False
        else:
            tubos=eval(tubosMat)
        diam_minTAB,nTAB=[[d,n] for d,n in tubos if d >= diam_min0][0]

        #Lista as interfencias de todos os trechos apenas uma vez
        lstIds,lstTr_inter=self.Lista_Interferencias(vLayer)
        for trecho in Trechos:
            obs=''
            diam_min=diam_minTAB
            n=nTAB
            ctm=float(trecho['CTM'])
            ctj=float(trecho['CTJ'])
            qini=float(trecho['Q_INI'])
            qfim=float(trecho['Q_FIM'])
            rec_min=float(trecho['REC_MIN'])
            lam_max=float(trecho['LAM_MAX'])#relacao y/d max
            Etapa=int(trecho['ETAPA'])
            ext=float(trecho['LENGTH'])
            #Inicio If da ETAPA>0 (rede projetada)
            if Etapa>0:
                CCM_max=ctm-rec_min-diam_min/1000.
                CCM_Mont_min, NAMontMin=self.pegaCotasMinTrechosMont(vLayer,trecho['PVM'],CCM_max,ctm)
                CCM_max=min(CCM_max,CCM_Mont_min)
                CCJ_max=ctj-rec_min-diam_min/1000.
                if trecho['PONTA_SECA']=='S':
                    NAMontMin=ctm
                else:
                    if Diam_progress:
                        diamMont,n=self.pegaDiamMaxTrechosMont(vLayer, trecho['PVM'], diam_min,n)
                        diam_min=diamMont
                    #ccm=self.pegaNAMinColetorMont(vLayer,trecho['PVM'],CCM_max)
                ccm=CCM_max
                #calcula declividade economica            
                Ieco=(ccm-CCJ_max)/ext
                #calcula declividade minima 1.5L/s
                Imin=0.0055*max(qini,q_min)**(-0.47)
                #escolhe a maior das duas declividade
                Io=max(Ieco,Imin)
                
                #calcula declividade maxima para v=5.0m/s, verificar essa formula
                Imax=4.65*qfim**(-2./3.)
                
                #Se a declividade for maior que maxima usa a maxima e calcula a cota do ccm, baixando-a
                if Io>=Imax:
                    Io=Imax
                    ccm=CCJ_max+ext*Io #Tenta usar a declividade maxima
                    if ccm>CCM_max:
                        ccm=CCM_max
                        Io=(ccm-CCJ_max)/ext
                    #verificar profundidade maxima do PV e se superar, usar lamina igual a 0.50 como recomenda
                    #a norma para situacoes de v > vcritica
                
                diam_calc=self.CalcDiametro(qfim, n, Io, lam_max)
                diam=diam_min
                if diam<diam_calc:#se o diam nao atende com a declividade
                    if max_forcar>0 and Io<Imax: #se nao estiver com a declividade Io=Imax tenta aprofundar a jusante
                        CCJ_forcado=CCJ_max-max_forcar
                        Iforcado=max(min((ccm-CCJ_forcado)/ext,Imax),Imin)
                        while diam<diam_calc:
                            diam_calc=self.CalcDiametro(qfim, n, Iforcado, lam_max)
                            if diam>diam_calc:
                                #Se for verdadeiro, é possivel resolver aprofundando em ate 'max_forcar' a jusante sem mudar diametro
                                #calcular a declividade minima que passa sem precisar aumentar o diametro
                                #Pega o primeiro diametro maior ou igual ao calculado
                                diam,n=[[d,n] for d,n in tubos if d >= diam_calc and d>=diam_min][0]
                                Iajust=self.CalcDecl(qfim, n, diam, lam_max)
                                Io=Iajust
                            else:
                                if diam_calc>tubos[-1][0]:#Verifica se o maior tubo é insuficiente
                                    diam=tubos[-1][0]
                                    n=tubos[-1][1]
                                    obs=u'DIAM É INSUFICIENTE '
                                    diam_calc=0 #para sair do looping
                                else:
                                    #Pega o proximo diametro maior que o anterior e calcula o diametro com a declividade minima
                                    diam,n=[[d,n] for d,n in tubos if d > diam][0]
                                    Io=Imin
                                    diam_calc=self.CalcDiametro(qfim, n, Io, lam_max)
                    else: #nao vai tentar rebaixar jusante
                        while diam<diam_calc:
                            if diam_calc>tubos[-1][0]:#Verifica se o maior tubo é insuficiente
                                diam=tubos[-1][0]
                                n=tubos[-1][1]
                                obs=u'DIAM É INSUFICIENTE '
                                diam_calc=0
                            else:
                                #Pega o primeiro diametro maior ou igual ao calculado
                                diam,n=[[d,n] for d,n in tubos if d >= diam_calc][0]
                                diam_calc=self.CalcDiametro(qfim, n, Io, lam_max)
                ccj=ccm-ext*Io
                diam_m=diam/1000.

                #Verifica Interferencias
                tr_id=trecho.id()
                #lista as interferencias apenas do trecho
                interfs=[[distMont,cs,ci] for id,distMont,cs,ci,tipoInt in lstTr_inter if id == tr_id]
                ccm_p=ccm
                ccj_p=ccj
                Ip=Io
                for distMont,cs,ci in interfs:
                    #Cota da geratriz superior e inferior do coletor no local da interferencia
                    ccGI_inter=ccm_p-Ip*distMont
                    ccGS_inter=ccGI_inter+diam_m
                    if (ci<ccGS_inter<cs) or (ci<ccGI_inter<cs): #verifica se ha choque com a interferencia
                        QgsMessageLog.logMessage('Interf em choque tr:'+trecho['DC_ID']+
                                                 ' distMont:{0:.2f}'.format(distMont), 'QEsg_03Dimensionamento',
                                                  QgsMessageLog.INFO)
                        #if distMont<(ext/2.) or True:#se a interferencia esta mais proxima de montante; forcei aqui para sempre modificar montante
                        if Ip==Imin:
                            #aprofundar ccm e ccj igualmente
                            degInt=ccGS_inter-ci
                            ccm_p=ccm_p-degInt
                            ccj_p=ccj_p-degInt
                        else:
                            #fixa jusante e calcula declividade (menor) entre ci-diam_m e ccj
                            Ip=((ci-diam_m)-ccj_p)/(ext-distMont)
                            Ip=max(Ip,Imin)
                            diam_calc=self.CalcDiametro(qfim, n, Ip, lam_max)
                            if diam_calc<diam:
                                if Ip>Imin:
                                    ccm_p=ccj_p+Ip*ext
                                else:#Ip=Imin
                                    ccGS_inter2=ci
                                    ccGI_inter2=ccGS_inter2-diam_m
                                    ccm_p=ccGI_inter2+Ip*distMont
                                    ccj_p=ccm_p-ext*Ip
                            else:
                                Ip=Io
                                #aprofundar ccm e ccj igualmente
                                degInt=ccGS_inter-ci
                                ccm_p=ccm_p-degInt
                                ccj_p=ccj_p-degInt
                ccm=ccm_p
                ccj=ccj_p
                Io=Ip
                #Fim das interferencias
    
                theta_ini=self.CalcTheta(max(qini,q_min), n, Io, diam, 0.00000001)
                y_d_ini=0.5*(1.-math.cos(theta_ini/2.))
                theta_fim=self.CalcTheta(max(qfim,q_min), n, Io, diam, 0.00000001)
                y_d_fim=0.5*(1.-math.cos(theta_fim/2.))
                
                y=y_d_fim*diam_m
                NAmon=ccm+y
                degNA=NAmon-NAMontMin
                if degNA>deg_ignore:#se verdade, existe um degrau negativo no NA maior que o degrau a ser desprezado, entao 
                           #rebaixa ccm, Namon e ccj do trecho em calculo
                    degfim=max(degNA,deg_min)
                    ccmDegFim=ccm-degfim
                    if ccmDegFim<ccm:
                        ccm-=degfim
                        ccj-=degfim
                        NAmon=ccm+y
                NAjus=ccj+y
            else: #else ETAPA=0 (Rede existente)
                ccm=trecho['CCM']
                ccj=trecho['CCJ']
                Io=(ccm-ccj)/ext
                diam=trecho['DIAMETER']
                diam_m=diam/1000.
                n=trecho['MANNING']

                theta_ini=self.CalcTheta(max(qini,q_min), n, Io, diam, 0.00000001)
                y_d_ini=0.5*(1.-math.cos(theta_ini/2.))
                theta_fim=self.CalcTheta(max(qfim,q_min), n, Io, diam, 0.00000001)
                y_d_fim=0.5*(1.-math.cos(theta_fim/2.))
                
                y=y_d_fim*diam_m
                NAmon=ccm+y
                NAjus=ccj+y
                obs='EXISTENTE/'
            #fim do if ETAPA

            #calcula Am,Rh,veloc, veloc_critiva, trativa, etc
            Amini=diam_m**2.*(theta_ini-math.sin(theta_ini))/8.
            Amfim=diam_m**2.*(theta_fim-math.sin(theta_fim))/8.
            v_ini=max(qini,q_min)/1000./Amini
            v_fim=max(qfim,q_min)/1000./Amfim
            
            Rh_ini=diam_m*(theta_ini-math.sin(theta_ini))/(4.*theta_ini)
            Rh_fim=diam_m*(theta_fim-math.sin(theta_fim))/(4.*theta_fim)
            v_crit=6.*(9.81*Rh_fim)**0.5
            trativa=10000*Rh_ini*Io

            #Insere os resultados na tabela
            trecho['NA_MON']=NAmon
            trecho['NA_JUS']=NAjus
            trecho['PRFM']=ctm-ccm
            trecho['PRFJ']=ctj-ccj
            trecho['VEL_INI']=v_ini
            trecho['VEL_FIM']=v_fim
            trecho['VEL_CRI']=v_crit
            trecho['TRATIVA']=trativa
            trecho['LAM_INI']=y_d_ini
            trecho['LAM_FIM']=y_d_fim
            trecho['DIAMETER']=diam
            trecho['MANNING']=n
            trecho['DECL']=Io
            trecho['CCM']=ccm
            trecho['CCJ']=ccj
            trecho['OBS']=obs
            vLayer.updateFeature(trecho)
        #end for Trechos

        Trechos=vLayer.getFeatures()
        #faz loop novamente para medir o degraus
        for trecho in Trechos:
            obs=trecho['OBS']
            pvj=trecho['PVJ']
            ccj=trecho['CCJ']
            CCM_MinJus=self.pegaCotaMinTrechosJus(vLayer, pvj,ccj)
            degCC=ccj-CCM_MinJus
            if degCC>0:
                if degCC>0.5: # quedas maiores que 0.50 usa TQ segundo Norma Brasileira
                    tipo='TQ'
                else:
                    tipo='DG'
                trecho['OBS']=(obs if obs else '')+tipo+'={:.3f}m'.format(degCC)

            vLayer.updateFeature(trecho)
        EstiloClasse=Estilos()
        EstiloClasse.CarregaEstilo(vLayer, 'rede_dimensionamento.qml')
        iface.mapCanvas().refresh()
        iface.messageBar().pushMessage("QEsg:", QCoreApplication.translate('QEsg',u'Rede dimensionada com sucesso!'), 
                                       level=QgsMessageBar.INFO, duration=4)

    #Lista as interferecias associando-as ao trecho mais proximo encontrado
    #incluindo a distancia ao PV de montante
    def Lista_Interferencias(self,pipeLayer):
        interfLayer=self.PegaQEsgLayer('INTERFERENCES')
        if interfLayer==False:
            return [],{}
        interfFeats=interfLayer.getFeatures()#
        
        pipeFeats=pipeLayer.getFeatures()#
        spIndex = QgsSpatialIndex() #create spatial index object
        feat = QgsFeature()
        # insert features to index
        while pipeFeats.nextFeature(feat):
            spIndex.insertFeature(feat)
        
        
        lstTr_inter=[]#Lista dos ids,distToMont dos trechos com interferencias
        lstIds=[]
        Invalidos=[NULL,None,'']
        aviso=''
        while interfFeats.nextFeature(feat):
            cs=feat['CS']
            ci=feat['CI']
            tipoInt=feat['TIPO_INT']
            geometry = feat.geometry()
            pt=geometry.asPoint()
            # QgsSpatialIndex.nearestNeighbor (QgsPoint point, int neighbors)
            nearestIds = spIndex.nearestNeighbor(pt,1) # we need only one neighbour
            nearestId=nearestIds[0]
            lstIds.append(nearestId)
            
            lineIter = pipeLayer.getFeatures(QgsFeatureRequest().setFilterFid(nearestId))
            ftr = QgsFeature()
            lineIter.nextFeature(ftr)
            #setup distance
            distance = QgsDistanceArea()
            distToMont=distance.measureLine(pt, ftr.geometry().asPolyline()[0])#poderia usar computeDistanceFlat
            lstTr_inter.append([nearestId,distToMont,cs,ci,tipoInt])
#         pipeLayer.setSelectedFeatures(lstIds)
#         print lstTr_inter
        return lstIds,lstTr_inter

    def PegaQEsgLayer(self,aForma):
        proj = QgsProject.instance()
        #aForma='PIPES'
        ProjVar=proj.readEntry("QEsg", aForma)[0]
        if ProjVar=='':
#             msgTxt=QCoreApplication.translate('QEsg','Layer Indefinido: ') +aForma
#             QMessageBox.warning(None,'QEsg',msgTxt)
            return False
        LayerLst=QgsMapLayerRegistry.instance().mapLayersByName(ProjVar)
        if LayerLst:
            layer = QgsMapLayerRegistry.instance().mapLayersByName(ProjVar)[0]
            return layer
        else:
#             msgTxt=aForma+'='+ProjVar+QCoreApplication.translate('QEsg',u' (Layer não encontrado)')
#             QMessageBox.warning(None,'QEsg',msgTxt)
            return False

    def Verifica_TrechosExistentes(self,vLayer):#retorna Falso se houver trecho com identificacao nula
        Invalidos=[NULL,None,'']
        request = QgsFeatureRequest()
        request.setFilterExpression('"ETAPA"=0')
        i=0
        for feat in vLayer.getFeatures(request):
            if i==0:
                vLayer.startEditing()
            i+=1
            ccm=feat['CCM']
            ccj=feat['CCJ']
            ctm=feat['CTM']
            ctj=feat['CTJ']
            prfm=feat['PRFM']
            prfj=feat['PRFJ']
            diam=feat['DIAMETER']
            n=feat['MANNING']
            if n in Invalidos:
                aviso=QCoreApplication.translate('QEsg',u'\'{}\' com valor Nulo em Trecho Existente!').format('MANNING')
                self.FeicaoSelecionaMostraAvisa(vLayer, feat.id(), aviso)
                return False
            if diam in Invalidos:
                aviso=QCoreApplication.translate('QEsg',u'\'{}\' com valor Nulo em Trecho Existente!').format('DIAMETER')
                self.FeicaoSelecionaMostraAvisa(vLayer, feat.id(), aviso)
                return False
            if (ccm in Invalidos) and (prfm in Invalidos): 
                aviso=QCoreApplication.translate('QEsg',u'\'{}\' e \'{}\' com valores Nulos em Trecho Existente!').format('CCM','PRFM')
                self.FeicaoSelecionaMostraAvisa(vLayer, feat.id(), aviso)
                return False
            else:
                if ccm in Invalidos:
                    feat['CCM']=ctm-prfm
                else:
                    feat['PRFM']=ctm-ccm
                vLayer.updateFeature(feat)
            if (ccj in Invalidos) and (prfj in Invalidos): 
                aviso=QCoreApplication.translate('QEsg',u'\'{}\' e \'{}\' com valores Nulos em Trecho Existente!').format('CCJ','PRFJ')
                self.FeicaoSelecionaMostraAvisa(vLayer, feat.id(), aviso)
                return False
            else:
                if ccj in Invalidos:
                    feat['CCJ']=ctj-prfj
                else:
                    feat['PRFJ']=ctj-ccj
                vLayer.updateFeature(feat)
        return True

    def Verifica_InterfsNulos(self):#retorna Falso se houver trecho com identificacao nula
        interfLayer=self.PegaQEsgLayer('INTERFERENCES')
        if interfLayer!=False:
            CamposVerif=['CS','CI'] #QEsgModel.COLUMNS['INTERFERENCES']
            Invalidos=[NULL,None,'']
            for feat in interfLayer.getFeatures():
                for campo in CamposVerif:
                    oValor=feat[campo]
                    if oValor in Invalidos:
                        aviso=QCoreApplication.translate('QEsg',u'\'{}\' com valor Nulo!').format(campo)
                        self.FeicaoSelecionaMostraAvisa(interfLayer, feat.id(), aviso)
                        return False
        return True

    
    def VerificaNulos(self,vLayer):#retorna Falso se houver trecho com identificacao nula
        CamposVerif=['DC_ID','Coletor','Trecho','PVM','PVJ','CTM','CTJ','Q_CONC_INI','Q_CONC_FIM','Q_INI','Q_FIM','REC_MIN','LAM_MAX','LENGTH','PONTA_SECA']
        Invalidos=[NULL,None,'']
        for feat in vLayer.getFeatures():
            for campo in CamposVerif:
                oValor=feat[campo]
                if oValor in Invalidos:
                    aviso=QCoreApplication.translate('QEsg',u'\'{}\' com valor Nulo! Utilize a Ferramenta de Preenchimento').format(campo)
                    self.FeicaoSelecionaMostraAvisa(vLayer, feat.id(), aviso)
                    return False
        return True

    def FeicaoSelecionaMostraAvisa(self,Layer,FeicaoID,aviso):
        Layer.select(FeicaoID)
        mapCanvas = iface.mapCanvas()
        mapCanvas.zoomToSelected(Layer)
        iface.messageBar().pushMessage("QEsg:", aviso, level=QgsMessageBar.WARNING, duration=4)

    def pegaCotaMinTrechosJus(self,vLayer,pvj,ccj):
        CCM_min=ccj
        for feat in vLayer.getFeatures():
            if feat['PVM']==pvj:
                CCM_min=min(CCM_min,feat['CCM'])
        return CCM_min
    def pegaCotasMinTrechosMont(self,vLayer,pvm, CCM_max,NAMax):
        CCM_min=CCM_max
        NAMontMin=NAMax
        for feat in vLayer.getFeatures():
            if feat['PVJ']==pvm:
                CCM_min=min(CCM_min,feat['CCJ'])
                NAMontMin=min(NAMontMin,feat['NA_JUS'])
        return CCM_min,NAMontMin
    def pegaDiamMaxTrechosMont(self,vLayer, pvm, diam_min,n):
        diam_max=diam_min
        manning=n
        for feat in vLayer.getFeatures():
            if feat['PVJ']==pvm:
                if feat['DIAMETER']>diam_max:
                    diam_max=feat['DIAMETER']
                    manning=feat['MANNING']
        return diam_max, manning
    def CalcDecl(self,q_ls,n,D, y_d):
        #Ariovaldo Nuvolari, Esgoto sanitário, pagina 50
        theta=2*math.acos(1.-2.*y_d)
        Am_D2=(theta-math.sin(theta))/8.
        Rh_D=(theta-math.sin(theta))/(4.*theta)
        DeclCalc=(n*(q_ls/1000.)/(Am_D2*Rh_D**(2./3.)*(D/1000.)**(8./3.)))**(2.)
        return DeclCalc
    def CalcDiametro(self,q_ls,n,Io, y_d):
        #Ariovaldo Nuvolari, Esgoto sanitário, pagina 50
        theta=2*math.acos(1.-2.*y_d)
        Am_D2=(theta-math.sin(theta))/8.
        Rh_D=(theta-math.sin(theta))/(4.*theta)
        DiamCalc=((n*(q_ls/1000.)/(Io**0.5*Am_D2*Rh_D**(2./3.)))**(3./8.))*1000
        return DiamCalc
    def CalcTheta(self,q_ls,n,Io, diam, precisao):
        diam_m=float(diam)/1000.
        M=n*(float(q_ls)/1000.)/(Io**0.5*diam_m**(8./3.))
        MaxIter = 1000
        #'0<x<2Pi
        theta_s = 5.27810713800479
        if M >= 0.335282:
            aviso=QCoreApplication.translate('QEsg','Trecho em carga! Verifique a rede')
            iface.messageBar().pushMessage("QEsg:", aviso, level=QgsMessageBar.WARNING, duration=4)
            return math.pi*2
        theta_i = 0
        conclui=True
        cont=0
        while conclui:
            theta = (theta_s + theta_i) / 2.
            M1 = ((theta - math.sin(theta)) / 8.) * ((theta - math.sin(theta)) / (4 * theta)) ** (2. / 3.)
            if M1 > M and M1 < 0.335282:
                theta_s = theta
            else:
                theta_i = theta
            cont += 1
            conclui = not ((abs(M1 - M) <= precisao) or (cont >= MaxIter))
        if cont >= MaxIter:
            print ' (erro=' + Abs(M1 - M) + ')'
        return theta
    def CriaNos(self,prefixo,Adiciona):
        #Codigo adaptado do plugin Networks
        #copyright            : (C) 2014 by CEREMA Nord-Picardie
        #email                : patrick.palmier@cerema.fr
        #layer=self.iface.activeLayer()
        proj = QgsProject.instance()
        ProjVar=proj.readEntry("QEsg", 'PIPES')[0]
        layer=QgsMapLayerRegistry.instance().mapLayersByName(ProjVar)[0]
        uriPath=layer.dataProvider().dataSourceUri()
        baseName = os.path.split(uriPath)[0]
        #baseName = fileInfo.baseName()
        #os.getcwd()
        nome_arquivo=QFileDialog.getSaveFileName(caption=QCoreApplication.translate('QEsg',u'Salvar o layer de nós como:'),
                                                 directory=baseName,filter="ESRI Shape File (*.shp)")
        if not nome_arquivo:
            #QMessageBox.information(None,'QEsg',u'Operação cancelada!')
            return
        
        #Apenas para lidar com o bug do QT4 no linux, que nao coloca a extensao automaticamente no filename
#         if not nome_arquivo.endswith('.shp'):
#             nome_arquivo+='.shp'

        campos=QgsFields()
        for campo in QEsgModel.COLUMNS['JUNCTIONS']:
            campos.append(QgsField(campo, QEsgModel.CAMPOSDEF[campo][0],
                                           QEsgModel.CAMPOSDEF[campo][1],
                                           QEsgModel.CAMPOSDEF[campo][2], 
                                           QEsgModel.CAMPOSDEF[campo][3])
                              )
        layer_nos=QgsVectorFileWriter(nome_arquivo,"UTF-8",campos,QGis.WKBPoint,layer.crs(),"ESRI Shapefile")
        if layer_nos.hasError() != QgsVectorFileWriter.NoError:
            msgTxt=layer_nos.errorMessage()
            QgsMessageLog.logMessage(msgTxt,'QEsg_03Dimensionamento',level=QgsMessageLog.CRITICAL)
            QMessageBox.critical(None,'QEsg',msgTxt)
            return 
        nos={}
        cotasTN={}
        lines=layer.getFeatures()
        for linha in lines:
            glinha=linha.geometry()
            if glinha.wkbType()==QGis.WKBMultiLineString:
                g=glinha.asMultiPolyline()
                na=g[0][0]
                nb=g[-1][-1]
            elif glinha.wkbType()==QGis.WKBLineString:
                g=glinha.asPolyline()
                na=g[0]
                nb=g[-1]
            if (na not in nos):
                nos[na]=linha['PVM']
                cotasTN[na]=linha['CTM']
            if (nb not in nos):
                nos[nb]=linha['PVJ']
                cotasTN[nb]=linha['CTJ']
        
        #outs=open("c:/temp/nos.txt","w")
        for i,n in enumerate(nos):
            node=QgsFeature()
            node.setGeometry(QgsGeometry.fromPoint(QgsPoint(n[0],n[1])))
            if cotasTN[n]:
                CotaTN=float(cotasTN[n])
            else:
                CotaTN=None
            node.setAttributes([nos[n],CotaTN])#str(nos[n]) passou a dar erro em qgis 2.16
            layer_nos.addFeature(node)
        #outs.write(str(n)+";"+str(nos[n])+"\n")
        #outs.close()
        del layer_nos
        if Adiciona:
            nome_camada=os.path.splitext(os.path.basename(nome_arquivo))[0]
            vlayer=QgsVectorLayer(nome_arquivo,nome_camada,'ogr')   
            QgsMapLayerRegistry.instance().addMapLayer(vlayer)

            EstiloClasse=Estilos()
            EstiloClasse.CarregaEstilo(vlayer, 'nos_nomes.qml')
            proj.writeEntry("QEsg", "JUNCTIONS", nome_camada)