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
from matplotlib.patches import Ellipse
import qgis

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

            tr_id=feat.id()
            #lista as interferencias apenas do trecho
            interfs=[[distMont,cs,ci,tipoInt] for id,distMont,cs,ci,tipoInt in lstTr_inter if id == tr_id]
            for distMont,cs,ci,tipoInt in interfs:
                locX=ext+distMont
                if tipoInt=='TN':
                    lstCTx.append(locX)
                    lstCTy.append(cs)
                else:
                    ellipse = Ellipse(xy=(locX, (cs+ci)/2.), width=5, height=cs-ci, 
                                             edgecolor='r', fc='None', lw=2)
                    ax.add_patch(ellipse)

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
        plt.plot(lstCTx,lstCTy,color='magenta')
        plt.plot(lstCGx,cgs,color='green')
        plt.plot(lstCGx,na,color='cyan')
        plt.plot(lstCGx,cc,color='blue')
        plt.xlabel(QCoreApplication.translate('QEsg',u'Distância (m)'))
        plt.ylabel(QCoreApplication.translate('QEsg','Cota (m)'))
        plt.grid(True)
        plt.legend([QCoreApplication.translate('QEsg','Cota do Terreno'),
                    QCoreApplication.translate('QEsg','Cota da Geratriz Superior'),
                    QCoreApplication.translate('QEsg','Cota do NA'),
                    QCoreApplication.translate('QEsg','Cota da Geratriz Inferior'),
                    QCoreApplication.translate('QEsg',u'Interferências')
                    ])
        plt.title(titulo)
        plt.show()
        plt.draw()
