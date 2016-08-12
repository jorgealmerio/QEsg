# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QEsg_05Perfil
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
from QEsg_05ProfileDialog import ProfileDialog
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle

from matplotlib.legend_handler import HandlerPatch
import matplotlib.patches as mpatches

import qgis

class HandlerEllipse(HandlerPatch):
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        center = 0.5 * width - 0.5 * xdescent, 0.5 * height - 0.5 * ydescent
        p = mpatches.Ellipse(xy=center, width=width + xdescent,
                             height=height + ydescent)
        self.update_prop(p, orig_handle, legend)
        p.set_transform(trans)
        return [p]


class QEsg_05Perfil:
    def __init__(self):
        self.dlg=ProfileDialog()
        self.DimensClasse=QEsg_03Dimens()

    def run(self):
#        self.DimensClasse=QEsg_03Dimens()
        vLayer=self.DimensClasse.PegaQEsgLayer('PIPES')
        if vLayer==False:
            aviso=QCoreApplication.translate('QEsg',u'Layer Tipo \'PIPES\' indefinido ou não encontrado!')
            iface.messageBar().pushMessage("QEsg:", aviso, level=QgsMessageBar.WARNING, duration=4)
            return False
            
        valores=[]
        idx = vLayer.fieldNameIndex('Coletor')
        valInts = vLayer.uniqueValues( idx )
        valores=[str(i) for i in valInts]
        self.dlg.cmbColetores.clear()
        self.dlg.cmbColetores.addItems(valores)
        
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            Coletor=self.dlg.cmbColetores.itemText(self.dlg.cmbColetores.currentIndex())
            self.Desenha_Perfil(vLayer,Coletor)

    def Desenha_Perfil(self,vLayer,Coletor=1):
        campo='Coletor'
        coletor=Coletor
        request = QgsFeatureRequest()
        expres='\"'+campo+'\"='+coletor
        request.setFilterExpression(expres)
        lstCTx=[]
        lstCGx=[]
        lstCTy=[]
        cc=[]
        cgs=[]
        na=[]
        ext=0
        titulo=QCoreApplication.translate('QEsg','Coletor ')+Coletor
        plt.figure(num=titulo)
        ax = plt.gca()
        #Lista as interfencias de todos os trechos apenas uma vez
        lstIds,lstTr_inter=self.DimensClasse.Lista_Interferencias(vLayer)
        HasInter=False
        for feat in vLayer.getFeatures(request):
            ident=feat['DC_ID']
            lstCTx.append(ext)
            lstCGx.append(ext)

            ctm=feat['CTM']
            ccm=feat['CCM']
            namon=feat['NA_MON']
            diam=feat['DIAMETER']/1000.

            lstCTy.append(ctm)
            cc.append(ccm)
            na.append(namon)
            cgs.append(ccm+diam)

            self.Desenha_PV(ax, ext, ctm, ccm, .8, .1)

            tr_id=feat.id()
            #lista as interferencias apenas do trecho
            interfs=[[distMont,cs,ci,tipoInt] for id,distMont,cs,ci,tipoInt in lstTr_inter if id == tr_id]
            for distMont,cs,ci,tipoInt in interfs:
                locX=ext+distMont
                if tipoInt=='TN':
                    lstCTx.append(locX)
                    lstCTy.append(cs)
                else:
                    ellipse = Ellipse(xy=(locX, (cs+ci)/2.), width=cs-ci, height=cs-ci, 
                                             edgecolor='r', fc='None', lw=2)
                    intLine=ax.add_patch(ellipse)
                    HasInter=True

            ctj=feat['CTJ']
            ccj=feat['CCJ']
            najus=feat['NA_JUS']

            plt.annotate(ident,(ext,ctm))
            ext+=feat['LENGTH']

            lstCTx.append(ext)
            lstCGx.append(ext)

            lstCTy.append(ctj)
            cc.append(ccj)
            na.append(najus)
            cgs.append(ccj+diam)
        #end for Trechos
        
        #Draw last PV
        self.Desenha_PV(ax, ext, ctj, ccj, .8, .1)
        
        ctLine,=plt.plot(lstCTx,lstCTy,color='magenta')
        cgsLine,=plt.plot(lstCGx,cgs,color='green')
        naLine,=plt.plot(lstCGx,na,color='cyan')
        cgiLine,=plt.plot(lstCGx,cc,color='blue')
        plt.xlabel(QCoreApplication.translate('QEsg',u'Distância (m)'))
        plt.ylabel(QCoreApplication.translate('QEsg','Cota (m)'))
        plt.grid(True)
        LegLines=[ctLine,cgsLine,naLine,cgiLine]
        subs=[QCoreApplication.translate('QEsg','Cota do Terreno'),
                    QCoreApplication.translate('QEsg','Cota da Geratriz Superior'),
                    QCoreApplication.translate('QEsg','Cota do NA'),
                    QCoreApplication.translate('QEsg','Cota da Geratriz Inferior')
                    ]
        #QCoreApplication.translate('QEsg','PV\'s')
        
        if HasInter:
            LegLines.append(intLine)
            subs.append(QCoreApplication.translate('QEsg',u'Interferências'))
            hndMap={intLine: HandlerEllipse()}
        else:
            hndMap={}
        plt.legend(LegLines,subs,handler_map=hndMap)
        plt.title(titulo)
        plt.show()
        plt.draw()
    def Desenha_PV(self,ax,ext,ctm,ccm,pvDiam,thick):
        #Add PV wall
        thick=.1 #espessura da parede
        pvDiam=.8+2.*thick #PV diam
        pvBLx=(ext-pvDiam/2.) #PV Bottom Left X
        pvBLy=ccm-thick #PV Bottom Left Y
        pvH=ctm-ccm+thick #PV Height
        rect = plt.Rectangle((pvBLx, pvBLy), pvDiam, pvH, facecolor="#aaaaaa",alpha=.70)
        ax.add_patch(rect)

        #Add PV
        pvDiam=.8 #PV diam
        pvBLx=ext-pvDiam/2. #PV Bottom Left X
        pvBLy=ccm #PV Bottom Left Y
        pvH=ctm-ccm-thick/2. #PV Height
        rect = plt.Rectangle((pvBLx, pvBLy), pvDiam, pvH, facecolor="white")
        ax.add_patch(rect)

        #Linha vertical no eixo do PV
        plt.plot([ext,ext],[ctm,ccm],color='black',linestyle='--')