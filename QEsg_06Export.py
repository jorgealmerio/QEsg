# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QEsg_06Export
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
from QEsg_03Dimensionamento import *
import math

import qgis
from numpy import insert
from os.path import join
from QEsg_06Export_dialog import dxfExport_Dialog

class QEsg_06Export:
    def __init__(self):
        self.DimensClasse=QEsg_03Dimens()
        try:
            from dxfwrite import DXFEngine as dxf
            QgsMessageLog.logMessage('dxfwrite imported without need of change PATH variable','QEsg_06Export') 
        except ImportError:
            self.dirname, filename = os.path.split(os.path.abspath(__file__))
            sys.path.append(self.dirname)
            from dxfwrite import DXFEngine as dxf
            QgsMessageLog.logMessage('dxfwrite imported, but PATH variable had to be changed','QEsg_06Export')#,level=QgsMessageLog.CRITICAL
        self.dxf=dxf
        self.dirname, filename = os.path.split(os.path.abspath(__file__))
        sys.path.append(self.dirname)

        # Create the dialog and keep reference
        self.dlg = dxfExport_Dialog()
        QObject.connect(self.dlg.btnBrowse, SIGNAL("clicked()"), self.LoadFileName)

    def run(self):
        #dxfPath=os.path.join(self.dirname,'test.dxf')#substituir por filedialog
        noth=['',' ','.dxf']
        if self.dlg.txtFile.text() in noth:
            proj = QgsProject.instance()
            #baseName=proj.readPath("./")
            prjfi = os.path.splitext(QgsProject.instance().fileName())[0]+'.dxf'
            self.dlg.txtFile.setText(prjfi)
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            dxfPath=self.dlg.txtFile.text()
            Invalidos=['',' ',None,NULL]
            if dxfPath in Invalidos:
                aviso=QCoreApplication.translate('QEsg',u'Operação cancelada!')
                iface.messageBar().pushMessage("QEsg:", aviso, level=QgsMessageBar.INFO, duration=4)
                return
            dxf=self.dxf
            drawing = dxf.drawing(dxfPath)
            self.drawing=drawing
            drawing.header['$INSUNITS'] = 6 #set units to meters
            drawing.header['$AUPREC'] = 6 #set angles precision
            self.criaRede()
            drawing.save()
            aviso="Saved to:" + dxfPath
            iface.messageBar().pushMessage("QEsg:", aviso, level=QgsMessageBar.INFO, duration=4)
    def LoadFileName(self):
        prjfi = self.dlg.txtFile.text()
        dxfPath=QFileDialog.getSaveFileName(caption=QCoreApplication.translate('QEsg',u'Exportar DXF como:'),
                                                 directory=prjfi,filter="AutoCAD DXF (*.dxf *.DXF)")
        if dxfPath:
            self.dlg.txtFile.setText(dxfPath)
    def criaRede(self):
        vLayer=self.DimensClasse.PegaQEsgLayer('PIPES')
        if vLayer==False:
            aviso=QCoreApplication.translate('QEsg',u'Layer Tipo \'PIPES\' indefinido ou não encontrado!')
            iface.messageBar().pushMessage("QEsg:", aviso, level=QgsMessageBar.WARNING, duration=4)
            return False
        from dxfwrite.const import CENTER, MIDDLE, TOP, LEFT, RIGHT
        drawing=self.drawing
        dxf=self.dxf
        e=vLayer.extent()
        drawing.header['$EXTMIN'] = (e.xMinimum(),e.yMinimum(),0) #Lower left corner
        drawing.header['$EXTMAX'] = (e.xMaximum(),e.yMaximum(),0) #Upper Right corner

        prefix=self.dlg.txtPrefix.text()#'B'
        self.criaLayers(drawing,prefix)
        drawing.add_style('ROMANS',font='romans.shx')
        #Here I Try to Set vport to initial display extents
        drawing.add_vport('*ACTIVE',height=(e.yMaximum()-e.yMinimum())*1.1, target_point=e.center(),aspect_ratio=3)

        # Get Scale Factor
        fatScale=self.dlg.spinScale.value()
        sc=fatScale/2000.

        # Create block SETA and add to drawing
        lyr=prefix+'SETA'
        solid = dxf.solid([(4*sc, 0), (-4*sc,-1.33*sc), (-4*sc, 1.33*sc)], color=256, layer=lyr)
        # Create a block
        oBlock = dxf.block(name=lyr)
        oBlock.add(solid)
        # add block definition to the drawing
        drawing.blocks.add(oBlock)

        for feat in vLayer.getFeatures():
            polilinha=feat.geometry().asPolyline()
            v1=polilinha[0]
            z1=feat['CCM']
            v2=polilinha[1]
            z2=feat['CCJ']

            lyr=prefix+'REDE'
            if feat['PONTA_SECA']=='S':
                v1d=self.PtoAlong(v1, v2, 4.*sc)
                pto1 = (v1d.x(),v1d.y(),z1)

                ptPerLeft=self.PtoPerp(v1d, v2, -2*sc)
                ptPerRight=self.PtoPerp(v1d, v2, 2*sc)
                ptLeft=(ptPerLeft.x(),ptPerLeft.y(),z1)
                ptRight=(ptPerRight.x(),ptPerRight.y(),z1)
                lyr=prefix+'NO'
                line = dxf.line(ptLeft,ptRight,color=256,layer=lyr)
                drawing.add(line)
            else:
                pto1 = (v1.x(),v1.y(),z1)
            lyr=prefix+'REDE'
            line = dxf.line(pto1,(v2.x(),v2.y(),z2),color=256,layer=lyr)
            drawing.add(line)
            
            pos,rot=self.textIns(v1,v2,-1.25*sc)
            lyr=prefix+'NUMERO'
            texto=feat['DC_ID']
            text = dxf.text(texto,height=2.5*sc,rotation=rot,xscale=.8,style='ROMANS',
                halign=CENTER,alignpoint=pos,color=256,layer=lyr)
            drawing.add(text)

            pos,rot=self.textIns(v1,v2,1.25*sc)
            lyr=prefix+'TEXTO'
            texto='{:.0f}-{:.0f}-{:.5f}'.format(feat["LENGTH"],feat["DIAMETER"],feat["DECL"])
            text = dxf.text(texto,height=2.5*sc,rotation=rot,xscale=.8,style='ROMANS',
                halign=CENTER,valign=TOP,alignpoint=pos,color=256,layer=lyr)
            drawing.add(text)

            # Add Cotas LIDER Polyline
            if feat['PONTA_SECA']=='S':
                aux=QgsPoint(pto1[0],pto1[1])
            else:
                aux=self.PtoAlong(v1, v2, 2.99*sc)
            azim=v1.azimuth(v2)
            if 0<azim<90:
                sign=-1
            else:
                sign=1
            aux2=self.PtoAlong(v1, v2, 3*sign*sc)
            lt1=self.PtoPerp(aux2, v2, 10.0*sc)
            lt2=QgsPoint(lt1.x()-12.*sign*sc,lt1.y())
            lyr=prefix+'LIDER'
            polyline = dxf.polyline(color=256,layer=lyr,polyline_elevation=(0,0,z1))
            polyline.add_vertices([lt2,lt1,aux])
            drawing.add(polyline)
            
            # Add CCM
            pos,rot=self.textIns(lt1,lt2,0.5*sc)
            lyr=prefix+'TEXTOPVS'
            texto='{:.3f}'.format(z1)
            text = dxf.text(texto,height=2.5*sc,rotation=0,xscale=.8,style='ROMANS',
                halign=CENTER,valign=TOP,alignpoint=pos,color=256,layer=lyr)
            drawing.add(text)

            # Add CTM
            pos,rot=self.textIns(lt1,lt2,-0.5*sc)
            texto='{:.3f}'.format(feat['CTM'])
            text = dxf.text(texto,height=2.5*sc,rotation=0,xscale=.8,style='ROMANS',
                halign=CENTER,alignpoint=pos,color=256,layer=lyr)
            drawing.add(text)

            # Add PRFM
            texto='{:.3f}'.format(feat['PRFM'])
            if sign==1:
                halin=RIGHT
            else:
                halin=LEFT
            text = dxf.text(texto,height=2.5*sc,rotation=0,xscale=.8,style='ROMANS',
                halign=halin,valign=MIDDLE,alignpoint=lt2,color=256,layer=lyr)
            drawing.add(text)


            # Add SETA blocks to middle of reaches bigger than 20m
            if feat['LENGTH']>20*sc:
                lyr=prefix+'SETA'
                azim=v1.azimuth(v2)
                if azim<0:
                    azim+=360
                rot=90.-azim
#                 if 180<=azim<360:
#                     rot-=180
                point=((v1.x()+v2.x())/2.,(v1.y()+v2.y())/2.,(z1+z2)/2.)
                drawing.add(dxf.insert2(blockdef=oBlock, insert=point,
                                    layer=lyr, rotation=rot))

        PVLayer=self.DimensClasse.PegaQEsgLayer('JUNCTIONS')
        if PVLayer==False:
            aviso=QCoreApplication.translate('QEsg',u'Layer Tipo \'JUNCTIONS\' indefinido ou não encontrado!\n Os PVs não foram criados!')
            iface.messageBar().pushMessage("QEsg:", aviso, level=QgsMessageBar.WARNING, duration=4)
            return
        
        #Create PV Block
        lyr=prefix+'PV'
        circle=dxf.circle(radius=2.99*sc,center=(0.,0.),color=256,layer=lyr)
        #solid = dxf.solid([(4, 0), (-4,-1.33), (-4, 1.33)], color=256, layer=lyr)
        # Create a block
        oBlock = dxf.block(name=lyr)
        #oBlock.add(solid)
        oBlock.add(circle)
        # add block definition to the drawing
        drawing.blocks.add(oBlock)

        for feat in PVLayer.getFeatures():
            point=feat.geometry().asPoint()
            lyr=prefix+'PV'
            drawing.add(dxf.insert2(blockdef=oBlock, insert=point, layer=lyr))

            lyr=prefix+'NUMPV'
            texto=feat['DC_ID']
            text = dxf.text(texto,height=3*sc,rotation=0.,xscale=.8,style='ROMANS',
                halign=LEFT,insert=(point[0]+3.*sc,point[1]+3.*sc),color=256,layer=lyr)
            drawing.add(text)

    def criaLayers(self,drawing,prefix):
        #[Layer,Color]
        dxfLayers=[['AUX',241],['LIDER',2],['NO',3],['NUMERO',7],['NUMPV',3],['PV',3],['REDE',172],['SETA',172],['TEXTO',7],['TEXTOPVS',7]]
        for lyr,aColor in dxfLayers:
            NomeLyr=prefix+lyr
            drawing.add_layer(NomeLyr, color=aColor)
    def textIns(self,v1,v2,offset):
        azim=v1.azimuth(v2)
        if azim<0:
            azim+=360
        rot=90.-azim
        if 180<=azim<360:
            rot-=180
        pos=self.mid(v1,v2, offset, azim)
        return pos,rot
    def mid(self, pt1, pt2, offset, azim):
       if 180<=azim<360:
            sign=-1*math.copysign(1,offset)
       else:
            sign=1*math.copysign(1,offset)
       mx = (pt1.x() + pt2.x())/2
       my = (pt1.y() + pt2.y())/2
       Len = math.sqrt(pt1.sqrDist(pt2)) 
       x=mx+sign*abs(offset)*(pt2.y()-pt1.y())/Len
       y=my+sign*abs(offset)*(pt1.x()-pt2.x())/Len
       return QgsPoint(x,y)
    def PtoAlong(self,pt1,pt2,Dist):
       Len = math.sqrt(pt1.sqrDist(pt2)) 
       x=pt1.x()+Dist/Len*(pt2.x()-pt1.x())
       y=pt1.y()+Dist/Len*(pt2.y()-pt1.y())
       return QgsPoint(x,y)
    #Cria um ponto perpendicular ao segmento e distante em relacao ao pt1 em offset
    def PtoPerp(self,pt1,pt2,Offset):
       Len = math.sqrt(pt1.sqrDist(pt2)) 
       x=pt1.x()+Offset/Len*(pt2.y()-pt1.y())
       y=pt1.y()+Offset/Len*(pt1.x()-pt2.x())
       return QgsPoint(x,y)
