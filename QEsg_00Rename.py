# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name		     : QEsg Rename Tools
Description          : 
Date                 : 28/Jan/2016/ 
copyright            : (C) 2016 by Jorge Almerio
email                : jorgealmerio@gmail.com 
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
# Import the PyQt and QGIS libraries
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import qgis.utils
from QEsg_01Campos import *
import os
from QEsg_04Estilos import *

class Rename_Tools:
    
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.EstiloClasse=Estilos()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/network_tools/icon.png"), "Renomeia Rede", self.iface.mainWindow())
        #Add toolbar button and menu item
        #self.iface.addPluginToMenu("&Renomeia Rede", self.action)
        #self.iface.addToolBarIcon(self.action)
        
        proj = QgsProject.instance()
        aForma='PIPES'
        ProjVar=proj.readEntry("QEsg", aForma)[0]
        if ProjVar=='':
            msgTxt=QCoreApplication.translate('QEsg','Layer Indefinido: ') +aForma+ '\n'
            iface.messageBar().pushMessage('QEsg', msgTxt, level=QgsMessageBar.WARNING, duration=4)
            return False
        else:
            vLayerLst=QgsMapLayerRegistry.instance().mapLayersByName(ProjVar)
            if vLayerLst:
                vl=vLayerLst[0]
                #Cria os campos padroes sem perguntar
                CamposClasse=QEsg_01Campos()
                CamposClasse.CriaCampos(aForma,vl, SilentRun=True)
                #Chama a rotina que Verifica se existem multipartes ou polilinhas
                self.CheckPolylines(vl,SilentRun=True)
            else:
                msgTxt=aForma+'='+ProjVar+QCoreApplication.translate('QEsg',u' (Layer não encontrado)')
                iface.messageBar().pushMessage('QEsg', msgTxt, level=QgsMessageBar.WARNING, duration=4)
                return False
        
        #load the form
        path = os.path.dirname(os.path.abspath(__file__))
        self.dock = uic.loadUi(os.path.join(path, "QEsg_Rename_dialog.ui"))
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock)#Qt.RightDockWidgetArea
        
        self.sourceIdEmitPoint = QgsMapToolEmitPoint(self.iface.mapCanvas())
        
        #connect the action to each method
        QObject.connect(self.action, SIGNAL("triggered()"), self.show)
        QObject.connect(self.dock.buttonSelectSourceId, SIGNAL("clicked(bool)"), self.selectSourceId)
        QObject.connect(self.sourceIdEmitPoint, SIGNAL("canvasClicked(const QgsPoint&, Qt::MouseButton)"), self.setSourceId)
        QObject.connect(self.dock.buttonRun, SIGNAL("clicked()"), self.run)
        QObject.connect(self.dock.buttonClear, SIGNAL("clicked()"), self.clear)
        QObject.connect(self.dock.buttonVerifica, SIGNAL("clicked()"), self.call_Verifica)

        self.sourceFeatID = None
        self.TrechosChained=[]
        self.PVfim='FIM'

    def show(self):
        self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.dock)
       
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Renomeia Rede", self.action)
        self.iface.removeDockWidget(self.dock)

    def selectSourceId(self, checked):
        if checked:
            self.toggleSelectButton(self.dock.buttonSelectSourceId)
            self.iface.mapCanvas().setMapTool(self.sourceIdEmitPoint)
        else:
            self.iface.mapCanvas().unsetMapTool(self.sourceIdEmitPoint)

    def PegaPipeLayer(self):
        proj = QgsProject.instance()
        aForma='PIPES'
        ProjVar=proj.readEntry("QEsg", aForma)[0]
        if ProjVar=='':
            msgTxt=QCoreApplication.translate('QEsg','Layer Indefinido: ') +aForma
            QMessageBox.warning(None,'QEsg',msgTxt)
            return False
        LayerLst=QgsMapLayerRegistry.instance().mapLayersByName(ProjVar)
        if LayerLst:
            layer = QgsMapLayerRegistry.instance().mapLayersByName(ProjVar)[0]
            return layer
        else:
            msgTxt=aForma+'='+ProjVar+QCoreApplication.translate('QEsg',u' (Layer não encontrado)')
            QMessageBox.warning(None,'QEsg',msgTxt)
            return False

    def setSourceId(self, pt):
        proj = QgsProject.instance()
        aForma='PIPES'
        ProjVar=proj.readEntry("QEsg", aForma)[0]
        if ProjVar=='':
            msgTxt=QCoreApplication.translate('QEsg','Layer Indefinido: ') +aForma
            QMessageBox.warning(None,'QEsg',msgTxt)
            return
        layer = QgsMapLayerRegistry.instance().mapLayersByName(ProjVar)[0]
        layer.removeSelection()
        width = self.iface.mapCanvas().mapUnitsPerPixel() * 4
        rect = QgsRectangle(pt.x() - width,
                                  pt.y() - width,
                                pt.x() + width,
                                pt.y() + width)
        layer.select(rect,True)
        selected_features = layer.selectedFeatures()
        if layer.selectedFeatureCount()>1:
            QMessageBox.warning(self.dock, self.dock.windowTitle(),
                    'WARNING: more than one feature selected!\n')
            return
        if layer.selectedFeatureCount()==0:
            return
        for feat in selected_features:
            sourceID='1-1'#feat['DC_ID']
            self.sourceFeatID=feat.id()
            self.selectDownstream(layer)

    def getLength(self,layer):
        totalLen = 0
        count = 0
        for feature in layer.selectedFeatures():
            geom = feature.geometry()
#            idtxt = feature[str(self.dock.comboFields.currentText())]
#            self.dock.textEditLog.append(idtxt)
            totalLen = totalLen + geom.length()
            count = count + 1
        return totalLen, count

    def run(self):
#        QMessageBox.warning(self.dock, self.dock.windowTitle(),
#                'WARNING: run action, renomear')
        proj = QgsProject.instance()
        aForma='PIPES'
        ProjVar=proj.readEntry("QEsg", aForma)[0]
        if ProjVar=='':
            msgTxt='Layer Indefinido: ' +aForma+ '\n'
            QMessageBox.warning(None,'QEsg',msgTxt)
            return
        layer = QgsMapLayerRegistry.instance().mapLayersByName(ProjVar)[0]
        
        campoID='DC_ID'
        Coletor=self.dock.spinColetor.value()
        Trecho=1
        NroDigitos = self.dock.spinColetorDigitos.value()
        NroDigitosPV = self.dock.spinPVDigitos.value()
        PVpref =self.dock.lineEditPV_pref.text()
        OrdCresc=self.dock.radioCrescente.isChecked()
        NroElems=len(self.TrechosChained)
        PVini=self.dock.spinPV_ini.value()
        if OrdCresc:
            PVnro = PVini
            Dir=1
        else:
            PVnro =PVini+NroElems-1
            Dir=-1
        layer.startEditing()
        for index, elem in enumerate(self.TrechosChained):
#            print(index, elem)
            request = QgsFeatureRequest().setFilterFid(elem)
            feat=layer.getFeatures(request).next()
            feat['Coletor']=Coletor
            feat['Trecho']=Trecho
            feat['DC_ID']=str(Coletor).rjust(NroDigitos,'0')+'-'+str(Trecho).rjust(NroDigitos,'0')
            Trecho += 1
            if index==0:#No primeiro trecho Verifica se tem algum trecho saindo do mesmo PV de montante
                Tem, NomePVM = self.VerificaPVMont_comun_comID(layer, feat)
                if Tem:
                    feat['PVM']=NomePVM
                else:
                    feat['PVM']=PVpref+str(PVnro).rjust(NroDigitosPV,'0')
            else:
                feat['PVM']=PVpref+str(PVnro).rjust(NroDigitosPV,'0')
            PVnro += Dir
            if index<NroElems-1:#Numera o PVJ final do coletor
                feat['PVJ']=PVpref+str(PVnro).rjust(NroDigitosPV,'0')
            else:
                feat['PVJ']=self.PVfim
            layer.updateFeature(feat)
        self.dock.textEditLog.append("N. of Renamed: "+str(len(self.TrechosChained)))
        self.EstiloClasse.CarregaEstilo(layer, 'rede_nomes.qml')
        self.iface.mapCanvas().refresh()
        if self.dock.buttonSelectSourceId.isChecked():
            self.dock.buttonSelectSourceId.click()

    def VerificaPVMont_comun_comID(self, layer, feat):
        tol = self.dock.spinBoxTol.value()
        # get list of nodes
        nodes = feat.geometry().asPolyline()
        # get end node upstream 
        up_end_node = nodes[0]
        # select all features around upstream coordinate using a bounding box
        rectangle = QgsRectangle(up_end_node.x() - tol, up_end_node.y() - tol, up_end_node.x() + tol, up_end_node.y() + tol)
        request = QgsFeatureRequest().setFilterRect(rectangle)
        features = layer.getFeatures(request)
        # start nodes into tolerance        
        n_start_node=0
        features = layer.getFeatures(request)
        #iterate thru requested features
        for feature in features:
            if feat.id()!=feature.id():
                #get list of nodes
                nodes = feature.geometry().asPolyline()
                #get start node upstream
                outro_up_node = nodes[0]
                #setup distance
                distance = QgsDistanceArea()
                #get distance from up_end_node to outro_up_node
                dist = distance.measureLine(up_end_node, outro_up_node)
                if dist < tol:
                    n_start_node=n_start_node+1
                    #add feature to selection list to iterate over it (if it not is the target)
                    pvm=feature['PVM']
                    if pvm!=NULL:
                        return True, pvm
        return False, 0
    def selectDownstream(self,layer):
        self.dock.textEditLog.clear()
        campo='DC_ID' 
        #QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
    
        final_list = self.TrechosChained
        selection_list = []
        tol = self.dock.spinBoxTol.value()
        self.dock.textEditLog.append("Starting...")

        layer.removeSelection()
        
        layer.select(self.sourceFeatID)
        provider = layer.dataProvider()
        selection_list.append(self.sourceFeatID)
        final_list.append(self.sourceFeatID)
        self.PVfim='FIM'
        # this part partially based on flowTrace by "Ed B"
        while selection_list:
            request = QgsFeatureRequest().setFilterFid(selection_list[0])
            feature = layer.getFeatures(request).next()
            # get list of nodes
            nodes = feature.geometry().asPolyline()
            # get end node upstream 
            up_end_node = nodes[-1]
            # select all features around upstream coordinate using a bounding box
            rectangle = QgsRectangle(up_end_node.x() - tol, up_end_node.y() - tol, up_end_node.x() + tol, up_end_node.y() + tol)
            request = QgsFeatureRequest().setFilterRect(rectangle)
            features = layer.getFeatures(request)
            # start nodes into tolerance        
            n_start_node=0
            features = layer.getFeatures(request)
            #iterate thru requested features
            for feature in features:
                #get list of nodes
                nodes = feature.geometry().asPolyline()
                #get start node downstream
                down_start_node = nodes[0]
                #setup distance
                distance = QgsDistanceArea()
                #get distance from up_end_node to down_start_node
                dist = distance.measureLine(up_end_node, down_start_node)
                if dist < tol and feature['PONTA_SECA']!='S':
                    n_start_node=n_start_node+1
                    #add feature to final list
                    final_list.append(feature.id())
                    #add feature to selection list to iterate over it (if it not is the target)
                    pvm=feature['PVM']
                    if self.dock.checkBifurcat.isChecked() and (pvm != NULL):
                        final_list[len(final_list)-n_start_node:len(final_list)] = []
                        self.dock.textEditLog.append("Stop at PVM="+pvm)
                        self.PVfim=pvm
                        self.dock.lineEditPV_pref.setText(pvm+'.')
                        break
                    if feature.id() not in selection_list:
                        selection_list.append(feature.id())
            if n_start_node > 1:
                self.dock.textEditLog.append("Bifurcation at end of: ")#+    feature[campo])
            if n_start_node > 1 and self.dock.checkBifurcat.isChecked():
                #remove last n_start_node items from final_list                
                final_list[len(final_list)-n_start_node:len(final_list)] = []
                self.dock.textEditLog.append("Stop at bifurcation!")
                break            
            #remove feature "0" from selection list
            selection_list.pop(0)
        #select features using final_list            
        layer.setSelectedFeatures(final_list)
        self.TrechosChained=final_list
        tot = self.getLength(layer)
        self.dock.textEditLog.append("")
        self.dock.textEditLog.append("N. of selected feature(s): " + str(tot[1]))
        self.dock.textEditLog.append("Length of selected feature(s): " + str(round(tot[0],3)))
        #zoom to selected feature if requested by ui
        if self.dock.checkZoomToSel.isChecked():
            mapCanvas = self.iface.mapCanvas()
            mapCanvas.zoomToSelected(layer)
        QApplication.restoreOverrideCursor()
            
    def call_Verifica(self):
#        qgis.utils.showPluginHelp()
        proj = QgsProject.instance()
        aForma='PIPES'
        ProjVar=proj.readEntry("QEsg", aForma)[0]
        if ProjVar=='':
            msgTxt=QCoreApplication.translate('QEsg','Layer Indefinido: {}').format(aForma)
            QMessageBox.warning(None,'QEsg',msgTxt)
            return
        layer = QgsMapLayerRegistry.instance().mapLayersByName(ProjVar)[0]
        self.CheckPolylines(layer)

    def CheckPolylines(self, layer,SilentRun=False):
        for feature in layer.getFeatures():
            geom=feature.geometry()
            if geom.isMultipart():
                vertices = geom.asMultiPolyline()
                NroVertices=len(vertices)
                msgTxt=QCoreApplication.translate('QEsg',u'Existem elementos multipartes com {:d} vértices.').format(NroVertices)
                resp=QMessageBox.question(None,'QEsg',msgTxt+QCoreApplication.translate('QEsg',u' Deseja convertê-los para partes simples?'),QMessageBox.Yes, QMessageBox.No)
#                self.iface.messageBar().pushMessage("QEsg:", "Existem elementos multipartes com "+
#                                                    str(NroVertices)+ " vertices", duration=0)
#                QgsMessageLog.logMessage(msgTxt, 'QEsg', QgsMessageLog.INFO)
                if resp==QMessageBox.Yes:
                    self.run_segmenter(layer)
                    return True
                return False
                #print 'Multipolilinha', [len(v) for v in vertices]
            else:
                vertices = geom.asPolyline()
                NroVertices=len(vertices)
                if NroVertices>2:
                    msgTxt=QCoreApplication.translate('QEsg',u'Existem elementos com {:d} vértices.').format(NroVertices)
                    resp=QMessageBox.question(None,'QEsg',msgTxt+QCoreApplication.translate('QEsg',u' Deseja convertê-los para linhas simples?'),QMessageBox.Yes, QMessageBox.No)
    #                self.iface.messageBar().pushMessage("QEsg:", "Existem elementos multipartes com "+
    #                                                    str(NroVertices)+ " vertices", duration=0)
#                    QgsMessageLog.logMessage(msgTxt, 'QEsg', QgsMessageLog.INFO)
                    if resp==QMessageBox.Yes:
                        self.run_segmenter(layer)
                        return True
                    return False
        if not SilentRun:
            QMessageBox.information(None,'QEsg','Os elementos foram verificados com sucesso!')
            return True
    def run_segmenter(self, layer):
        #Routine from Networks Plugin from CEREMA Nord-Picardie
        #layer = self.iface.activeLayer()
        if not layer==None:
            if layer.featureCount()>0 and layer.geometryType()==1:
                layer.startEditing()
                layer.beginEditCommand("Split polylines into lines")
                for feature in layer.getFeatures():
                    geom = feature.geometry()
                    nodes = geom.convertToType(QGis.Line,True).asMultiPolyline()
                    att=feature.attributes()
                    id=feature.id()
                    for poly in nodes:
                        for pt in range(len(poly)-1):
                            segment=QgsFeature()
                            segment.setGeometry(QgsGeometry.fromPolyline([poly[pt],poly[pt+1]]))
                            segment.setAttributes(att)
                            layer.addFeature(segment)
                    layer.deleteFeature(id)
                layer.endEditCommand()
            elif not layer.geometryType()==1:
                QMessageBox().information(None,"Split",u'O layer não é de linhas')
            else:
                QMessageBox().information(None,"Split","Layer vazio")
        else:
            QMessageBox().information(None,"Split","Layer indefinido")

    def clear(self):
        self.dock.spinColetor.setValue(self.dock.spinColetor.value()+1)
        self.TrechosChained=[]
        self.dock.textEditLog.clear()
        #self.dock.buttonSelectSourceId.click()
        layer=self.PegaPipeLayer()
        if layer!=False:
            layer.removeSelection()
        self.iface.mapCanvas().unsetMapTool(self.sourceIdEmitPoint)
        self.iface.mapCanvas().setMapTool(self.sourceIdEmitPoint)
        if not self.dock.buttonSelectSourceId.isChecked():
            self.dock.buttonSelectSourceId.click()
        QApplication.restoreOverrideCursor()

    def LimpaNomesColetores(self):
        vLayer=self.PegaPipeLayer()
        if vLayer==False:
            return
        if vLayer.selectedFeatureCount()==0:
            feicoes=vLayer.getFeatures()
        else:
            resp=QMessageBox.question(None,'QEsg',QCoreApplication.translate('QEsg','Apagar os nomes apenas dos coletores selecionados?'),
                                      QMessageBox.Yes, QMessageBox.No)
            if resp==QMessageBox.Yes:
                feicoes=vLayer.selectedFeatures()
            else:
                feicoes=vLayer.getFeatures()
        vLayer.startEditing()
        campos=['DC_ID','Coletor','Trecho','PVM','PVJ']
        for feicao in feicoes:
            for campo in campos:
                feicao[campo]=NULL
            vLayer.updateFeature(feicao)
        self.iface.mapCanvas().refresh()

    def toggleSelectButton(self, button):
        selectButtons = [
            self.dock.buttonSelectSourceId
        ]
        for selectButton in selectButtons:
            if selectButton != button:
                if selectButton.isChecked():
                    selectButton.click()
        

