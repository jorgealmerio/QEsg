# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QEsg_01Campos
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
from qgis.gui import QgsMessageBar
from QEsg_04Estilos import *

class QEsg_01Campos:
#     def __init__(self):
#         self.initGui()
    def CarregaCampos(self):
        self.proj = QgsProject.instance()
        ProjVar=self.proj.readEntry("QEsg", 'PIPES')[0]
        if ProjVar!='':
            self.RedeLayer=QgsMapLayerRegistry.instance().mapLayersByName(ProjVar)[0]
            dp=self.RedeLayer.dataProvider()
            return [field.name() for field in dp.fields()]
        #print self.fieldNames
    def Verifica(self, Opcao):
        proj = QgsProject.instance()
        Formas=QEsgModel.GIS_SHAPES
        msgTxt=''
        for aForma in Formas:
            ProjVar=proj.readEntry("QEsg", aForma)[0]
            if ProjVar!='':
                #msgTxt+=QCoreApplication.translate('QEsg','Layer Indefinido: ') +aForma+ '\n'
            #else:
                vLayerLst=QgsMapLayerRegistry.instance().mapLayersByName(ProjVar)
                if vLayerLst:
                    vLayer=vLayerLst[0]
                    #msgTxt+=aForma+ '='+vLayer.name()+ '\n' #dataProvider().dataSourceUri()
                    if Opcao=='Criar':
                        self.CriaCampos(aForma,vLayer)
                    elif Opcao=='Preencher' and aForma=='PIPES': #so estou preenchendo o layer de tubos por enquanto
                        self.Preenche(aForma,vLayer)
                else:
                    msgTxt+=aForma+'='+ProjVar+QCoreApplication.translate('QEsg',u' (Layer não encontrado)')+'\n'
        if msgTxt!='':
            iface.messageBar().pushMessage("QEsg:", msgTxt, level=QgsMessageBar.WARNING, duration=4)
            #QMessageBox.information(None,'QEsg',msgTxt)
    def CriaCampos(self, aForma, vLayer, SilentRun=False):
        field_names = [field.name() for field in vLayer.pendingFields()]
        attributes=[]
        dP = vLayer.dataProvider()
        msgTxt=QCoreApplication.translate('QEsg','Campos ausentes em ')+ vLayer.name()+':\n'
        CamposAusentes=False
        for campo in QEsgModel.COLUMNS[aForma]:#COLUMNS
            if campo not in field_names:
                #print campo, QEsgModel.COLUMN_TYPES[campo]
                CamposAusentes=True
                msgTxt+=campo+'\n'
                attributes.append(QgsField(campo, QEsgModel.CAMPOSDEF[campo][0],
                                           QEsgModel.CAMPOSDEF[campo][1],
                                           QEsgModel.CAMPOSDEF[campo][2], 
                                           QEsgModel.CAMPOSDEF[campo][3])
                                  )
        #vLayer.startEditing()
        #vLayer.beginEditCommand('Criando campos')
        if CamposAusentes:
            if SilentRun:
                dP.addAttributes(attributes)
                vLayer.updateFields()
            else:
                resp=QMessageBox.question(None,'QEsg',msgTxt+QCoreApplication.translate('QEsg','Deseja criar os campos?'),
                                          QMessageBox.Yes, QMessageBox.No)
                if resp==QMessageBox.Yes:
                    vLayer.startEditing()
                    for campo in attributes:
                        vLayer.addAttribute(campo)
#                     dP.addAttributes(attributes)
#                     vLayer.updateFields()
        else:
            if not SilentRun:
                QMessageBox.information(None,'QEsg',QCoreApplication.translate('QEsg',u'Os campos necessários já existem em ')+vLayer.name())

    def Preenche(self, aForma, vLayer):
        if vLayer.selectedFeatureCount()==0:
            feicoes=vLayer.getFeatures()
        else:
            resp=QMessageBox.question(None,'QEsg',QCoreApplication.translate('QEsg','Preencher apenas os registros selecionados?'),
                                      QMessageBox.Yes, QMessageBox.No)
            if resp==QMessageBox.Yes:
                feicoes=vLayer.selectedFeatures()
            else:
                feicoes=vLayer.getFeatures()
        #camposPadroes=['DIAMETER','MANNING','Q_CONC_INI','Q_CONC_FIM', 'REC_MIN']# No futuro usar: QEsgModel.COLUMNS[aForma]
        proj = QgsProject.instance()
        dn_min=float(proj.readEntry("QEsg", "DN_MIN","150")[0])
        tubosMat=proj.readEntry("QEsg", "TUBOS_MAT","0")[0]
        if tubosMat=='0':#se nao tiver lista de diametros definidas
            iface.messageBar().pushMessage("QEsg:", QCoreApplication.translate('QEsg',u'Lista de diâmetros indefinida!'), 
                                           level=QgsMessageBar.WARNING, duration=4)
            return False
        else:
            tubos=eval(tubosMat)
        diam_min,manning=[[d,n] for d,n in tubos if d >= dn_min][0]
        #manning=float(proj.readEntry("QEsg", "MANNING","0.013")[0])
        rec_min=float(proj.readEntry("QEsg", "REC_MIN","0.90")[0])
        lam_max=float(proj.readEntry("QEsg", "LAM_MAX","0.75")[0])
        ProjNode=proj.readEntry("QEsg", "JUNCTIONS")[0]
        PrecSancad=proj.readNumEntry("QEsg", "PREC_SANCAD",0)[0]#diametros progressivos
        NodeCotas={}
        if ProjNode!='':
            vLayerLst=QgsMapLayerRegistry.instance().mapLayersByName(ProjNode)
            if vLayerLst:
                NodeLayer=vLayerLst[0]
                Nodefeats=NodeLayer.getFeatures()
                Fld_id=QEsgModel.COLUMNS['JUNCTIONS'][0]
                Fld_Cota=QEsgModel.COLUMNS['JUNCTIONS'][1]
                #Looping nas junctions
                for Nodefeat in Nodefeats:
                    NodeCotas[Nodefeat[Fld_id]]=Nodefeat[Fld_Cota]
        camposPadroes={'LENGTH':'CALCULA','DIAMETER':diam_min,'MANNING':manning,
                       'Q_CONC_INI':0.0,'Q_CONC_FIM':0.0, 'REC_MIN': rec_min, 'LAM_MAX': lam_max,
                       'CONTR_LADO':2,'ETAPA':1,'PONTA_SECA':'N'}## No futuro usar direto do modelo
        if bool(NodeCotas): #se o dicionario nao estiver nulo
            camposPadroes.update({'CTM':'PREENCHE','CTJ':'PREENCHE'})
        vLayer.startEditing()
        for feicao in feicoes:
            for (campo,valorPad) in camposPadroes.iteritems():
                featVal=feicao[campo]
                if campo=='LENGTH':
                    ext=feicao.geometry().length()
                    if PrecSancad:
                        ext=round(ext,0)
                    feicao[campo]=ext
                elif campo=='CTM':
                    feicao[campo]=NodeCotas[feicao['PVM']]
                elif campo=='CTJ':
                    feicao[campo]=NodeCotas[feicao['PVJ']]
                else:
                    if featVal==NULL:
                        feicao[campo]=valorPad
            vLayer.updateFeature(feicao)
        iface.messageBar().pushMessage("QEsg:", 'Dados preenchidos com sucesso!', level=QgsMessageBar.INFO, duration=4)

    #Substitui o nome dos PVs (campos PVM e PVJ) dos tubos pelo Nome (DC_ID) do layer de nós
    #atraves da posicao espacial 

    def AtualizaNomePVs(self):
        proj = QgsProject.instance()
        Formas=['PIPES','JUNCTIONS']
        msgTxt=''
        vLayer={}
        for aForma in Formas:
            ProjNode=proj.readEntry("QEsg", aForma)[0]
            if ProjNode!='':
                vLayerLst=QgsMapLayerRegistry.instance().mapLayersByName(ProjNode)
                if vLayerLst:
                    vLayer[aForma]=vLayerLst[0]
                else:
                    msgTxt=QCoreApplication.translate('QEsg',u'Layer \'{}\' não encontrado!').format(ProjNode)
                    break
            else:
                msgTxt=QCoreApplication.translate('QEsg','Layer Indefinido: {}').format(aForma)
                break
        if msgTxt!='':
            iface.messageBar().pushMessage("QEsg:", msgTxt, level=QgsMessageBar.WARNING, duration=5)
            return False
        tol=0.5 #tolerancia 0.5 unidades de distancia 
        vLayer['PIPES'].startEditing()
        for ptofeat in vLayer['JUNCTIONS'].getFeatures():
            node = ptofeat.geometry().asPoint()

            rectangle = QgsRectangle(node.x() - tol, node.y() - tol, node.x() + tol, node.y() + tol)
            request = QgsFeatureRequest().setFilterRect(rectangle)
            linefeats = vLayer['PIPES'].getFeatures(request)

            for linefeat in linefeats:
                #get list of nodes
                nodes = linefeat.geometry().asPolyline()
                #get up and end node
                up_node = nodes[0]
                down_node = nodes[-1]
                #setup distance
                distance = QgsDistanceArea()
                #get distance from up_node and down_node to point
                distUp = distance.measureLine(up_node, node)
                distDown = distance.measureLine(down_node, node)
                if distUp < tol:
                    linefeat['PVM']=ptofeat['DC_ID']
                elif distDown < tol:
                    linefeat['PVJ']=ptofeat['DC_ID']
                vLayer['PIPES'].updateFeature(linefeat)
        iface.messageBar().pushMessage("QEsg:", QCoreApplication.translate('QEsg','Nomes dos PVS atualizados com sucesso!'),
                                        level=QgsMessageBar.INFO, duration=5)
    #Rotina sem uso
#     def OnChangeAttribute(self,fid,idx,valor):
#         if valor!=None:
#             campos=self.CarregaCampos()
#             fldName=campos[idx]
#             print 'fid='+str(fid),fldName,'valor='+str(valor)
