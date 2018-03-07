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
from formatter import NullWriter

ClassName='QEsg_06Export'
UsrAppId='NUMEROTRE' #appid for DXF extended data
TemCTNula=False
class QEsg_06Export:
    def __init__(self):
        global ClassName
        self.DimensClasse=QEsg_03Dimens()

        # Create the dialog and keep reference
        self.dlg = dxfExport_Dialog()
        QObject.connect(self.dlg.btnBrowse, SIGNAL("clicked()"), self.LoadFileName)
        QObject.connect(self.dlg.chkSancad, SIGNAL("clicked()"), self.chkSancad_toggle)
    def ImportDxf_Lib(self):
        try:
            import ezdxf as dxf
            QgsMessageLog.logMessage('ezdxf imported without need of change PATH variable',ClassName) 
        except ImportError:
            self.dirname, filename = os.path.split(os.path.abspath(__file__))
            sys.path.append(self.dirname)
            import ezdxf as dxf
            QgsMessageLog.logMessage('ezdxf imported, but PATH variable had to be changed',ClassName)#,level=QgsMessageLog.CRITICAL
        # self.dirname, filename = os.path.split(os.path.abspath(__file__))
        # sys.path.append(self.dirname)

        self.dxf=dxf
    def tr(self, Texto):
        return QCoreApplication.translate(ClassName,Texto)
    def nz(self, Valor):
        global TemCTNula
        #function to treat Null values
        if Valor==NULL:
            TemCTNula=True
            return 0
        else:
            return Valor
    def run(self):
        global UsrAppId, TemCTNula
        #dxfPath=os.path.join(self.dirname,'test.dxf')#substituir por filedialog
        self.ImportDxf_Lib()
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
                aviso=self.tr(u'Operação cancelada!')
                iface.messageBar().pushMessage(ClassName, aviso, level=QgsMessageBar.INFO, duration=4)
                return
            dxf=self.dxf
            # Create a new drawing in the DXF format of AutoCAD 2010
            drawing = dxf.new('ac1024')
            self.drawing=drawing
            drawing.header['$INSUNITS'] = 6 #set units to meters
            drawing.header['$AUNITS'] = 0 #set angle unit to decimal degrees
            drawing.header['$AUPREC'] = 6 #set angles precision
            drawing.appids.new(UsrAppId) #Create AppId entry to xdata
            self.criaRede()

            # Save the drawing.
            drawing.saveas(dxfPath)

            aviso=self.tr("Salvo em:") + dxfPath
            if TemCTNula:
                aviso=self.tr("Valores nulos foram substituidos por Zeros. ")+aviso
                iface.messageBar().pushMessage(ClassName, aviso, level=QgsMessageBar.WARNING, duration=4)
            else:
                iface.messageBar().pushMessage(ClassName, aviso, level=QgsMessageBar.INFO, duration=4)
    def chkSancad_toggle(self):
        chk=self.dlg.chkSancad.isChecked()
        if chk:
            self.dlg.txtPrefix.setText('SANC_')
        #self.dlg.txtPrefix.setEnabled(not chk)
    def LoadFileName(self):
        prjfi = self.dlg.txtFile.text()
        dxfPath=QFileDialog.getSaveFileName(caption=self.tr(u'Exportar DXF como:'),
                                                 directory=prjfi,filter="AutoCAD DXF (*.dxf *.DXF)")
        if dxfPath:
            self.dlg.txtFile.setText(dxfPath)
    def criaRede(self):
        global UsrAppId, ClassName, TemCTNula
        vLayer=self.DimensClasse.PegaQEsgLayer('PIPES')
        if vLayer==False:
            aviso=self.tr(u'Layer Tipo \'PIPES\' indefinido ou não encontrado!')
            iface.messageBar().pushMessage(ClassName, aviso, level=QgsMessageBar.WARNING, duration=4)
            return False
        #from dxfwrite.const import CENTER, MIDDLE, TOP, LEFT, RIGHT
        drawing=self.drawing
        dxf=self.dxf
        e=vLayer.extent()
        drawing.header['$EXTMIN'] = (e.xMinimum(),e.yMinimum(),0) #Lower left corner
        drawing.header['$EXTMAX'] = (e.xMaximum(),e.yMaximum(),0) #Upper Right corner

        prefix=self.dlg.txtPrefix.text()#'B'
        self.criaLayers(drawing,prefix)
        drawing.styles.new('ROMANS',{'font':'romans.shx'})

        #Here I Try to Set vport to initial display extents
        #print e.center().x(),e.center().y()
        #drawing.viewports.new('*ACTIVE',{'target_point':(e.center().x(),e.center().y(),0)})
        active_viewport = drawing.viewports.new('*ACTIVE')
        #drawing.viewports.new('*ACTIVE',{'height':(e.yMaximum()-e.yMinimum())*1.1, 'target_point':(e.center().x(),e.center().y(),0),'aspect_ratio':3})
        active_viewport.dxf.center_point = (e.center().x(),e.center().y()) #(40, 30)  # center of viewport, this parameter works
        active_viewport.dxf.height = (e.yMaximum()-e.yMinimum())*1.5# 15 height of viewport, this parameter works
        active_viewport.dxf.aspect_ratio = 2.5  #1.5 aspect ratio of viewport (x/y)
        # Get Scale Factor
        fatScale=self.dlg.spinScale.value()
        sc=fatScale/2000.

        # Create block SETA and add to drawing
        blkSeta=prefix+'SETA'
        oBlock = drawing.blocks.new(name=blkSeta)
        oBlock.add_solid([(4*sc, 0), (-4*sc,-1.33*sc), (-4*sc, 1.33*sc)], dxfattribs={'color':256, 'layer':blkSeta})
        
        # Get the modelspace of the drawing.
        msp = drawing.modelspace()
        
        #Array of Lateral contribution to covert from QEsg to Sancad
        contLad_lst=[[0,'NAO'],[1,'UNI'],[2,'SIM']]
        
        #for add extended data to entities, here to be read in Sancad
        from ezdxf.lldxf.types import DXFTag
        SancadPad=self.dlg.chkSancad.isChecked()
        TemCTNula=False
        for feat in vLayer.getFeatures():
            polilinha=feat.geometry().asPolyline()
            v1=polilinha[0]
            z1=self.nz(feat['CTM'])
            v2=polilinha[1]
            z2=self.nz(feat['CTJ'])

            lyr=prefix+'REDE'
            if feat['PONTA_SECA']=='S':
                v1d=self.PtoAlong(v1, v2, 4.*sc)
                pto1 = (v1d.x(),v1d.y(),z1)
                if not SancadPad:
                    ptPerLeft=self.PtoPerp(v1d, v2, -2*sc)
                    ptPerRight=self.PtoPerp(v1d, v2, 2*sc)
                    ptLeft=(ptPerLeft.x(),ptPerLeft.y(),z1)
                    ptRight=(ptPerRight.x(),ptPerRight.y(),z1)
                    lyr=prefix+'NO'
                    msp.add_line(ptLeft,ptRight,dxfattribs={'color':256, 'layer':lyr})#add perpendicular line
            else:
                pto1 = (v1.x(),v1.y(),z1)
            lyr=prefix+'REDE'
            line = msp.add_line(pto1,(v2.x(),v2.y(),z2),dxfattribs={'color':256, 'layer':lyr})

            #add extended data to the entity for sancad reading
            txtID=feat['DC_ID']
            txtPVM=feat['PVM']
            txtPAV='ASFALTO' #no futuro adaptar para compatibilizar com o Sancad que 
                                #considera a prof de recobrimento a partir do tipo de pavimento
            txtLADOS=contLad_lst[feat['CONTR_LADO']][1]
            line.set_xdata(appid=UsrAppId,xdata_tags=[DXFTag(1000,txtID),
                                                      DXFTag(1000,txtPVM),
                                                      DXFTag(1000,txtPAV),
                                                      DXFTag(1000,txtLADOS)])

            if not SancadPad:
                pos,rot=self.textIns(v1,v2,-1.25*sc)
                lyr=prefix+'NUMERO'
                texto=feat['DC_ID']
                msp.add_text(texto,{'height':2.5*sc,'rotation':rot,'width':.8,'style':'ROMANS','color':256, 'layer':lyr}).set_pos(pos,align='BOTTOM_CENTER')
    
                pos,rot=self.textIns(v1,v2,1.25*sc)
                lyr=prefix+'TEXTO'
                ext=self.nz(feat["LENGTH"])
                dn=self.nz(feat["DIAMETER"])
                i=self.nz(feat["DECL"])
                texto='{:.0f}-{:.0f}-{:.5f}'.format(ext,dn,i)
                msp.add_text(texto,{'height':2.5*sc,'rotation':rot,'width':.8,'style':'ROMANS','color':256, 'layer':lyr}).set_pos(pos,align='TOP_CENTER')
    
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
                
                vertices=[lt2,lt1,aux]
                msp.add_polyline2d(vertices,{'color':256,'layer':lyr,'elevation':(0,0,z1)})
    
                
                # Add CCM
                pos,rot=self.textIns(lt1,lt2,0.5*sc)
                lyr=prefix+'TEXTOPVS'
                texto='{:.3f}'.format(self.nz(feat['CCM']))
                msp.add_text(texto,{'height':2.5*sc,'rotation':0,'width':.8,'style':'ROMANS','color':256, 'layer':lyr}).set_pos(pos,align='TOP_CENTER')
    
                # Add CTM
                pos,rot=self.textIns(lt1,lt2,-0.5*sc)
                texto='{:.3f}'.format(self.nz(feat['CTM']))
                msp.add_text(texto,{'height':2.5*sc,'rotation':0,'width':.8,'style':'ROMANS','color':256, 'layer':lyr}).set_pos(pos,align='BOTTOM_CENTER')
    
                # Add PRFM
                texto='{:.3f}'.format(self.nz(feat['PRFM']))
                if sign==1:
                    alin='MIDDLE_RIGHT'
                else:
                    alin='MIDDLE_LEFT'
                msp.add_text(texto,{'height':2.5*sc,'rotation':0,'width':.8,'style':'ROMANS','color':256, 'layer':lyr}).set_pos(lt2,align=alin)
    
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
                    msp.add_blockref(blkSeta, point, dxfattribs={
                        'xscale': 1,
                        'yscale': 1,
                        'rotation': rot,
                        'layer':lyr
                    })
                #end if
            #endif SancadPad

        PVLayer=self.DimensClasse.PegaQEsgLayer('JUNCTIONS')
        if PVLayer==False:
            aviso=self.tr(u'Layer Tipo \'JUNCTIONS\' indefinido ou não encontrado! Os PVs não foram criados!')
            iface.messageBar().pushMessage("QEsg:", aviso, level=QgsMessageBar.WARNING, duration=4)
            return
        
        #Name PV Block
        lyr=prefix+'PV'
        # Create a block
        oBlock = drawing.blocks.new(name=lyr)
        oBlock.add_circle(center=(0.,0.),radius=2.99*sc,dxfattribs={'color':256, 'layer':lyr})

        for feat in PVLayer.getFeatures():
            point=feat.geometry().asPoint()
            lyr=prefix+'PV'
            msp.add_blockref(lyr,point,dxfattribs={'layer':lyr})
            if not SancadPad:
                lyr=prefix+'NUMPV'
                texto=feat['DC_ID']
                pos=(point[0]+3.*sc,point[1]+3.*sc)
                msp.add_text(texto,{'height':3*sc,'rotation':0,'width':.8,'style':'ROMANS','color':256, 'layer':lyr}).set_pos(pos,align='BOTTOM_LEFT')

    def criaLayers(self,drawing,prefix):
        #[Layer,Color]
        dxfLayers=[['AUX',241],['LIDER',2],['NO',3],['NUMERO',7],['NUMPV',3],['PV',3],['REDE',172],['SETA',172],['TEXTO',7],['TEXTOPVS',7]]
        for lyr,aColor in dxfLayers:
            NomeLyr=prefix+lyr
            drawing.layers.new(NomeLyr, dxfattribs={'color': aColor})
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
