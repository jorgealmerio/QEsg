# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QEsg_20ImportaSancad_DXF
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
from QEsg_01Campos import *
from osgeo import ogr
import math
from QEsg_04Estilos import *
#from QEsg_00Model import *


class QEsg_20Sancad:
    def ImportaDXF(self):
        proj = QgsProject.instance()
        #vLayer=iface.activeLayer()
        #vLayer.startEditing()
        baseName=proj.readPath("./")
        nome_arquivo=QFileDialog.getOpenFileName(caption=QCoreApplication.translate('QEsg',u'Abrir o arquivo DXF da rede SANCAD:'),
                                                 directory=baseName,filter="AutoCAD DXF (*.dxf *.DXF)")
        if not nome_arquivo:
            QMessageBox.information(None,'QEsg',QCoreApplication.translate('QEsg',u'Operação cancelada!'))
            return
        else:
            vLayer = QgsVectorLayer(nome_arquivo, "SANCAD DXF", "ogr")
        
        if not vLayer.isValid():
            QMessageBox.warning(None,'QEsg',QCoreApplication.translate('QEsg','Arquivo invalido'))
            return
        #Pega o crs do Projeto atual
#         canvas = iface.mapCanvas()
#         mapRenderer = canvas.mapRenderer()
#         crs=mapRenderer.destinationCrs()
        s=QSettings()
        Userconfig=s.value("/Projections/defaultBehaviour")
        
        Campo='ExtendedEntity'
        RedeEtapa={'SANC_REDE':1,'SANC_REDE2T':2, 'SANC_REDEEXIST':0}
        PVLayer='SANC_PV'
        field_names = [field.name() for field in vLayer.pendingFields()]
        if Campo in field_names:
            # create a memory layer
            vl = QgsVectorLayer("LineString", "Rede Importada", "memory")
            #vl.setCrs(crs) #Configura CRS para o mesmo do projeto atual
            pr = vl.dataProvider()

            
            #Cria os campos padroes sem perguntar
            CamposClasse=QEsg_01Campos()
            CamposClasse.CriaCampos('PIPES',vl, SilentRun=True)
            
            #Filtra os registro com campo Layer like SANC_PV
            requestPVs = QgsFeatureRequest()
            requestPVs.setFilterExpression( '"Layer" like \'%'+PVLayer+'%\'' )
            PViterator=vLayer.getFeatures( requestPVs )
            
            #Cria um layer de pontos temporario e cria um ponto no centro da polilinha que representa um PV
            vPVs = QgsVectorLayer("Point", "PVs", "memory")
            #vPVs.setCrs(crs) #Configura CRS para o mesmo do projeto atual
            prPVs=vPVs.dataProvider()
            feat = QgsFeature()
            fet= QgsFeature()

            while PViterator.nextFeature(feat):
                geom=feat.geometry().centroid()
                fet.setGeometry(geom)
                vPVs.updateFeature(fet)
                prPVs.addFeatures([fet])

            spIndex = QgsSpatialIndex() #create spatial index object
            
            PViterator=vPVs.getFeatures()#            

            # insert features to index
            while PViterator.nextFeature(feat):
                spIndex.insertFeature(feat)

            #filtra os registros com campo ExtendedEntity nao nulos
            request = QgsFeatureRequest()
            request.setFilterExpression( '\"'+Campo+'\" IS NOT NULL')
            iterator=vLayer.getFeatures( request )
            contrlado=2

            #Loop no arquivo DXF onde tiver dados no campo ExtendedEntity            
            for feicao in iterator:
                oValor = feicao[Campo].split()
                dcid=oValor[0]
                strPos1=oValor[0].find('-') # oValor[0] = Coletor-Trecho
                pvm=oValor[1] #PV de montante
                pav=oValor[2] #Pavimento, ex:ASFALTO, TERRENO NATURAL
                Bilateral=oValor[3] #Sim=Bilateral;Uni=Unilateral;Nao=Sem contribuicao
                if Bilateral=='SIM':
                    contrlado=2
                elif Bilateral=='UNI':
                    contrlado=1
                elif Bilateral=='NAO':
                    contrlado=0
                else:
                    contrlado=2
                coletor=int(oValor[0][:strPos1])
                trecho=int(oValor[0][strPos1+1:])
                aGeo=feicao.geometry()
                
                wkb = aGeo.asWkb()
                geom_wkb = ogr.CreateGeometryFromWkb(wkb)
                #aPolilinha = geom_wkb.GetGeometryRef().ExportToWkt()  #wkb.convertToType(QGis.Point, True).exportToWkt()
                pontos3D={}
                pontos3D[0]=str(geom_wkb)[12:-1].split(",")[0].split(" ")
                pontos3D[1]=str(geom_wkb)[12:-1].split(",")[1].split(" ")

                #aPolilinha=aGeo.asLineString25D()#LineString25D  asPolyline
                ctm= float(pontos3D[0][2]) #geom_wkb.GetZ() #aPolilinha[0].x()
                ctj= float(pontos3D[1][2])
                
                #Pega a Etapa de acordo com o layer que se encontra
                oLayer=feicao['Layer']
                etapa=RedeEtapa[oLayer]
                
                # add a feature
                fet = QgsFeature(vl.pendingFields())
                
                pt=aGeo.asPolyline()[0]
                
                # QgsSpatialIndex.nearestNeighbor (QgsPoint point, int neighbors)
                nearestIds = spIndex.nearestNeighbor(pt,1) # we need only one neighbour
                featureId = nearestIds[0]
                #print pt,featureId
                fit2 = vPVs.getFeatures(QgsFeatureRequest().setFilterFid(featureId))
                ftr = QgsFeature()
                fit2.nextFeature(ftr)
                pvProx=ftr.geometry().asPoint() #asPolyline()[0]
                #setup distance
                distance = QgsDistanceArea()
                #get distance
                dist = distance.measureLine(pt, pvProx)
                if dist>3:
                    pontaseca='S'
                    #estende trecho ponta seca para montante
                    aGeo=self.ExtendToMont(aGeo, dist=4)
                else:
                    pontaseca='N'
                #print dcid, pt, featureId, pvProx, dist
#                 fet.setAttributes([coletor, trecho,dcid ,pvm, None, None,ctm, ctj, None,None,None,None,None,None,None,None,None,
#                                    None,None,None,None,None,None,None,None,None,None,None,
#                                    None,None,contrlado])
                fet.setGeometry(aGeo)
                fet['Coletor']=coletor
                fet['Trecho']=trecho
                fet['DC_ID']=dcid
                fet['PVM']=pvm
                fet['CTM']=ctm
                fet['CTJ']=ctj
                fet['CONTR_LADO']=contrlado
                fet['ETAPA']=etapa
                fet['PONTA_SECA']=pontaseca
                vl.updateFeature(fet)
                pr.addFeatures([fet])
#                print coletor,trecho,pvm,pav,contrlado
        else:
            iface.messageBar().clearWidgets()
            QMessageBox.warning(None,'QEsg',QCoreApplication.translate('QEsg',u'Campo \'{}\' não Encontrado').format(campo))
        vl.updateExtents()
        self.PreenchePVJ(vl)
        #vl.setCrs(crs) #Configura CRS para o mesmo do projeto atual
        QgsMapLayerRegistry.instance().addMapLayer(vl)
        EstiloClasse=Estilos()
        EstiloClasse.CarregaEstilo(vl, 'rede_tipo_contribuicao.qml')
        del vPVs
        s.setValue("/Projections/defaultBehaviour", Userconfig)
        iface.messageBar().pushMessage('QEsg',QCoreApplication.translate('QEsg',u'Importação concluída com sucesso!'), 
                                       duration=3)
    def ExtendToMont(self,Geom, dist=4):#Retorna geometria com linha estendida #x1,y1,x2,y2
        poli=Geom.asPolyline()
        pto1=poli[0]
        pto2=poli[1]
        x1=pto1.x()
        y1=pto1.y()
        x2=pto2.x()
        y2=pto2.y()
        Alfa=math.atan2(y2-y1,x2-x1)
        dx=dist*math.cos(Alfa)
        dy=dist*math.sin(Alfa)
        xp=x1-dx
        yp=y1-dy
        pto1_est=QgsPoint(xp,yp)
        newGeo=QgsGeometry.fromPolyline([pto1_est,pto2])
        return newGeo
    def PreenchePVJ(self, vLayer):
        #proj = QgsProject.instance()
        #vLayer=iface.activeLayer()
        tol=0.5 #tolerancia 0.5 unidades de distancia 
        vLayer.startEditing()
        for upfeat in vLayer.getFeatures():
            #get up reach list of nodes
            nodes = upfeat.geometry().asPolyline()
            #get up end node downstream
            up_end_node = nodes[-1]
            rectangle = QgsRectangle(up_end_node.x() - tol, up_end_node.y() - tol, up_end_node.x() + tol, up_end_node.y() + tol)
            request = QgsFeatureRequest().setFilterRect(rectangle)
            downfeats = vLayer.getFeatures(request)
            # start nodes into tolerance        
            n_start_node=0
            for downfeat in downfeats:
                #get list of nodes
                nodes = downfeat.geometry().asPolyline()
                #get start node downstream
                down_start_node = nodes[0]
                #setup distance
                distance = QgsDistanceArea()
                #get distance from up_end_node to down_start_node
                dist = distance.measureLine(up_end_node, down_start_node)
                if dist < tol:
                    n_start_node+=1
                    downPVM=downfeat['PVM']
            if n_start_node>0:
                upfeat['PVJ']=downPVM
                #QMessageBox.warning(None,'QEsg','Mais de uma saida no PV='+downPVM)
            else:
                upfeat['PVJ']='FIM'
            vLayer.updateFeature(upfeat)


