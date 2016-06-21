# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QEsg_00Settings
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
#from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, QObject, SIGNAL
#from PyQt4.QtGui import QAction, QIcon, QMessageBox
#from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.utils import *
# from qgis.gui import QgsMessageBar
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
import os.path
from QEsg_Settings_dialog import SettingsDialog
from QEsg_00Model import *
from QEsg_00Rename import *
from QEsg_01Campos import *
from QEsg_02Vazao import *
from QEsg_03Dimensionamento import *
from QEsg_05Perfil import *
from QEsg_20Sancad import *

class QEsg:
    """QGIS Plugin Implementation."""
    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'QEsg_en.qm')# 'QEsg_{}.qm'.format(locale) -> mudei para sempre traduzir qdo n for pt

        if os.path.exists(locale_path) and locale!='pt':#se n for pt traduz pra ingles
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = SettingsDialog()

        # Connect to Dialog Buttons
        #self.dlg.pushButton.clicked.connect(self.tableToArray)
        self.dlg.btnDel.clicked.connect(self.btnDel_push)
        self.dlg.btnIns.clicked.connect(self.btnIns_push)
        
        # Declare instance attributes
        self.actions = []
        self.menu = QCoreApplication.translate('QEsg',u"&QEsg")
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(self.tr(u'&QEsg'))
        self.toolbar.setObjectName(self.tr(u'&QEsg'))
        
        #Cria instancias das Classes utilizadas
        self.RenameClasse=Rename_Tools(self.iface)
        self.CamposClasse=QEsg_01Campos()
        self.VazaoClasse=QEsg_02Vazao()
        self.DimensClasse=QEsg_03Dimens()
        self.SancadClasse=QEsg_20Sancad()
        self.PerfilClasse=QEsg_05Perfil()
    # noinspection PyMethodMayBeStatic
    def btnDel_push(self):
        tableWidget=self.dlg.tableWidget
        tableWidget.removeRow(tableWidget.currentRow())
        #tableWidget.setRowCount(tableWidget.rowCount()-1)
    def btnIns_push(self):
        tableWidget=self.dlg.tableWidget
        tableWidget.insertRow(tableWidget.currentRow()+1)
    def carregaTabMats(self,tbMats):
        #tbMats=QEsgModel.TUBOS_MAT
        tableWidget=self.dlg.tableWidget
        tableWidget.setRowCount(0)
        for i, tbMat in enumerate(tbMats):
            currentRowCount = tableWidget.rowCount()
            tableWidget.insertRow(currentRowCount)
            item=QTableWidgetItem("{:7.2f}".format(tbMat[0]))
            item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)
            tableWidget.setItem(currentRowCount , 0, item)
            
            item=QTableWidgetItem("{:5.3f}".format(tbMat[1]))
            item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)
            tableWidget.setItem(currentRowCount , 1, item)
    def tableToArray(self):
        table=self.dlg.tableWidget
        result = []
        num_rows, num_cols = table.rowCount(), table.columnCount()
        for row in range(num_rows):
            rows = []
            for col in range(num_cols):
                item = table.item(row, col)
                rows.append(float(item.text()))#if item else ''
            result.append(rows)
        return result    
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('QEsg', message)


    def add_action(
        self,
        icon_path,
        text,
        callback=None,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None,
        separator=False):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        if not separator:
            action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            if separator:
                menuSep=self.toolbar
                self.separator=menuSep.addSeparator()
                #menuSep.setSeparator(True)
                self.iface.addPluginToMenu(
                    self.menu,
                    self.separator)
#                 menuSep=self.toolbar
#                 self.separator=menuSep.addAction("")
#                 self.separator.setSeparator(True)
#                 self.iface.addPluginToMenu(
#                     self.menu,
#                     self.separator)
            else:
                self.iface.addPluginToMenu(
                    self.menu,
                    action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/QEsg/icons/00config.png'
        self.add_action(
            icon_path,
            text=self.tr(u'00 Configurações'),
            callback=self.run,
            parent=self.iface.mainWindow())

        icon_path = ':/plugins/QEsg/icons/01campos.png'
        self.add_action(
            icon_path,
            text=self.tr('01 Verifica os Campos'),
            callback=self.VerificaCampos,
            parent=self.iface.mainWindow())

        icon_path = ':/plugins/QEsg/icons/00rename.png'
        self.add_action(
            icon_path,
            text=self.tr(u'02 Numerar Rede'),
            callback=self.Rename,
            parent=self.iface.mainWindow())

        icon_path = ':/plugins/QEsg/icons/04crianos.png'
        self.add_action(
            icon_path,
            text=self.tr(u'03 Criar Layer de Nós'),
            callback=self.CriaNodeFile,
            parent=self.iface.mainWindow())

        icon_path = ':/plugins/QEsg/icons/02campos_preenche.png'
        self.add_action(
            icon_path,
            text=self.tr(u'04 Preenche os Campos'),
            callback=self.PreencheCampos,
            parent=self.iface.mainWindow())

        icon_path = ':/plugins/QEsg/icons/03vazao.png'
        self.add_action(
            icon_path,
            text=self.tr(u'05 Calcula Vazão'),
            callback=self.CalculaVazao,
            parent=self.iface.mainWindow())

        icon_path = ':/plugins/QEsg/icons/05dimens.png'
        self.add_action(
            icon_path,
            text=self.tr(u'06 Dimensiona'),
            callback=self.Dimensiona,
            parent=self.iface.mainWindow())

        icon_path = ''
        self.add_action(
            icon_path,
            add_to_menu=True,
            add_to_toolbar=False,
            text='',
#            callback=self.fazNada,
            parent=self.iface.mainWindow(),
            separator=True)

        icon_path = ':/plugins/QEsg/icons/06profile.svg'
        self.add_action(
            icon_path,
            add_to_menu=True,
            add_to_toolbar=True,
            text=self.tr(u'Desenha perfil'),
            callback=self.DesenhaPerfil,
            parent=self.iface.mainWindow())
            
        icon_path = ''
        self.add_action(
            icon_path,
            add_to_menu=True,
            add_to_toolbar=False,
            text=self.tr(u'Atualiza Nome dos PVs a partir dos nós'),
            callback=self.AtualizaPVs,
            parent=self.iface.mainWindow())

        icon_path = ''
        self.add_action(
            icon_path,
            add_to_menu=True,
            add_to_toolbar=False,
            text=self.tr(u'Apaga Nome dos Coletores'),
            callback=self.ClearPipesNames,
            parent=self.iface.mainWindow())

        icon_path = ''
        self.add_action(
            icon_path,
            add_to_menu=True,
            add_to_toolbar=False,
            text=self.tr(u'Importa Sancad DXF'),
            callback=self.ImportaSancadDXF,
            parent=self.iface.mainWindow())


        QObject.connect(self.dlg.btnLimpaSettings, SIGNAL("clicked()"), self.LimpaSettings)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        self.iface.removePluginMenu(
                self.tr(u'&QEsg'),
                self.separator)
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&QEsg'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):
        """Run method that performs all the real work"""
        self.limpaTudo()
        
        layers = self.iface.legendInterface().layers() #self.iface.mapCanvas().layers() 
#         layer_list = []
#         for layer in layers:
#             if layer.type() == QgsMapLayer.VectorLayer:
#                 if layer.wkbType() == QGis.WKBPolygon:
#                     layer_list.append(layer.name())
#         self.dlg.cmbBacia.addItems(layer_list)

        layer_list = ['']
        for layer in layers:
            if layer.type() == QgsMapLayer.VectorLayer:
                if layer.wkbType() == QGis.WKBLineString:
                    layer_list.append(layer.name())
        self.dlg.cmbRede.addItems(layer_list)
        
        layer_list = ['']
        for layer in layers:
            if layer.type() == QgsMapLayer.VectorLayer:
                if layer.wkbType() == QGis.WKBPoint:
                    layer_list.append(layer.name())
        self.dlg.cmbVertices.addItems(layer_list)

        layer_list = ['']
        for layer in layers:
            if layer.type() == QgsMapLayer.VectorLayer:
                if layer.wkbType() == QGis.WKBPoint:
                    layer_list.append(layer.name())
        self.dlg.cmbInterf.addItems(layer_list)
        
        self.leVariaveis()

        #Exibe extensoes da rede
        proj = QgsProject.instance()
        ProjVar=proj.readEntry("QEsg", 'PIPES')[0]
        if ProjVar!='':
            try:
                myLayer=QgsMapLayerRegistry.instance().mapLayersByName(ProjVar)[0]
                tot1a,tot2a,geo1a,geo2a=self.CompRealGeom(myLayer)
    
                msgTxt=self.tr(u'<span style=" color:#0000ff;">Comprimento Geométrico:<br>Etapa 1 = {0:.2f} m<br>Etapa 2 = {1:.2f} m</span>').format(geo1a,geo2a)
                self.dlg.lbl_extGeo.setText(msgTxt)
                msgTxt=''
    
                if tot1a>0 or tot2a>0:
                    msgTxt=self.tr(u'Comprimento Atual:\nEtapa 1 = {} m\nEtapa 2 = {} m').format(tot1a,tot2a)
                self.dlg.lbl_extReal.setText(msgTxt)
                msgTxt=''
    
                Lini,Lfim = self.VazaoClasse.CompVirtualRede(myLayer)
                if Lini>0 or Lfim>0:
                    msgTxt=self.tr(u'Comprimento Virtual:\nEtapa 1 = {} m\nEtapa 2 = {} m').format(Lini,Lfim)
                self.dlg.lbl_extVirtual.setText(msgTxt)
            except: 
                pass

#             conecta o layer da rede ao evento (signal)
#             myLayer.attributeValueChanged.connect(self.CamposClasse.OnChangeAttribute)
#             print 'conectou'

        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            self.gravaVariaveis()

    def CompRealGeom(self,vLayer):
        tot1a=tot2a=0
        geo1a=geo2a=0
        for feat in vLayer.getFeatures():
            ext=feat['LENGTH']
            etapa=feat['ETAPA']
            geo=feat.geometry().length()
            if etapa==1:
                geo1a+=geo
                geo2a+=geo
                if ext!= NULL:
                    tot1a+=ext
                    tot2a+=ext
            elif etapa==2:
                geo2a+=geo
                if ext!= NULL:
                    tot2a+=ext
            else:
                geo1a+=geo
                if ext!= NULL:
                    tot1a+=ext
        return tot1a,tot2a,geo1a,geo2a


    def limpaTudo(self):
        #self.dlg.cmbBacia.clear()
        self.dlg.cmbRede.clear()
        self.dlg.cmbVertices.clear()
        self.dlg.cmbInterf.clear()
    def LimpaSettings(self):
        proj = QgsProject.instance()
        proj.removeEntry("QEsg","")
        MsgTxt=self.tr(u'As configurações do Plugin foram removidas do Projeto')
        #listaEntry = proj.readListEntry()
        self.iface.messageBar().pushMessage("QEsg:", MsgTxt, duration=3)
        self.dlg.close()
    def leVariaveis(self):
        proj = QgsProject.instance()

#         ProjVar=proj.readEntry("QEsg", "BACIAS")[0]
#         oInd=self.EncontraItem(self.dlg.cmbBacia,ProjVar)
#         self.dlg.cmbBacia.setCurrentIndex(oInd)

        ProjVar=proj.readEntry("QEsg", "PIPES")[0]
        oInd=self.EncontraItem(self.dlg.cmbRede,ProjVar)
        self.dlg.cmbRede.setCurrentIndex(oInd)

        ProjVar=proj.readEntry("QEsg", "JUNCTIONS")[0]
        oInd=self.EncontraItem(self.dlg.cmbVertices,ProjVar)
        self.dlg.cmbVertices.setCurrentIndex(oInd)

        ProjVar=proj.readEntry("QEsg", "INTERFERENCES")[0]
        oInd=self.EncontraItem(self.dlg.cmbInterf,ProjVar)
        self.dlg.cmbInterf.setCurrentIndex(oInd)

        self.dlg.Txt_percapita.setText(proj.readEntry("QEsg", "PERCAPTA","150")[0])
        self.dlg.Txt_k1.setText(proj.readEntry("QEsg", "K1_DIA","1.20")[0])
        self.dlg.Txt_k2.setText(proj.readEntry("QEsg", "K2_HORA","1.50")[0])
        self.dlg.Txt_CoefRet.setText(proj.readEntry("QEsg", "COEF_RET","0.80")[0])
        self.dlg.Txt_CoefInf.setText(proj.readEntry("QEsg", "COEF_INF","0.0002")[0])
        self.dlg.Txt_diametro.setText(proj.readEntry("QEsg", "DN_MIN","150")[0])
        self.dlg.Txt_qmin.setText(proj.readEntry("QEsg", "Q_MIN","1.50")[0])
#        self.dlg.Txt_manning.setText(proj.readEntry("QEsg", "MANNING","0.013")[0])
        self.dlg.Txt_rec_min.setText(proj.readEntry("QEsg", "REC_MIN","0.90")[0])
        self.dlg.Txt_y_d_max.setText(proj.readEntry("QEsg", "LAM_MAX","0.75")[0])
        self.dlg.Txt_maxForcar.setText(proj.readEntry("QEsg", "MAX_FORCAR","0.00")[0])
        self.dlg.Txt_deg_ignore.setText(proj.readEntry("QEsg", "DEG_IGNORE","0.02")[0])
        self.dlg.Txt_deg_min.setText(proj.readEntry("QEsg", "DEG_MIN","0.00")[0])

        self.dlg.Txt_popini.setText(proj.readEntry("QEsg", "POPINI","0")[0])
        self.dlg.Txt_popfim.setText(proj.readEntry("QEsg", "POPFIM","0")[0])

        self.dlg.chkDiamProgressivo.setChecked(proj.readNumEntry("QEsg", "DIAM_PROGRESS",1)[0])

        tubosMat=proj.readEntry("QEsg", "TUBOS_MAT","0")[0]
        if tubosMat=='0':#se nao tiver lista de materiais definidas carrega o padrao do modelo
            tubos=QEsgModel.TUBOS_MAT
        else:
            tubos=eval(tubosMat)
        self.carregaTabMats(tubos)
    def EncontraItem(self, Combo, Texto):
        for i in range(Combo.count()):
            if Combo.itemText(i)==Texto:
                return i
        return -1
    def gravaVariaveis(self):
        proj = QgsProject.instance()
        #LyrNameSel=self.dlg.cmbBacia.itemText(self.dlg.cmbBacia.currentIndex())
        #proj.writeEntry("QEsg", "BACIAS", LyrNameSel)
        LyrNameSel=self.dlg.cmbRede.itemText(self.dlg.cmbRede.currentIndex())        
        proj.writeEntry("QEsg", "PIPES", LyrNameSel)
        LyrNameSel=self.dlg.cmbVertices.itemText(self.dlg.cmbVertices.currentIndex())
        proj.writeEntry("QEsg", "JUNCTIONS", LyrNameSel)
        LyrNameSel=self.dlg.cmbInterf.itemText(self.dlg.cmbInterf.currentIndex())
        proj.writeEntry("QEsg", "INTERFERENCES", LyrNameSel)

        proj.writeEntry("QEsg", "PERCAPTA", self.dlg.Txt_percapita.text())
        proj.writeEntry("QEsg", "K1_DIA", self.dlg.Txt_k1.text())
        proj.writeEntry("QEsg", "K2_HORA", self.dlg.Txt_k2.text())
        proj.writeEntry("QEsg", "COEF_RET", self.dlg.Txt_CoefRet.text())
        proj.writeEntry("QEsg", "COEF_INF", self.dlg.Txt_CoefInf.text())
        proj.writeEntry("QEsg", "DN_MIN", self.dlg.Txt_diametro.text())
        proj.writeEntry("QEsg", "Q_MIN", self.dlg.Txt_qmin.text())
#        proj.writeEntry("QEsg", "MANNING", self.dlg.Txt_manning.text())
        proj.writeEntry("QEsg", "REC_MIN", self.dlg.Txt_rec_min.text())
        proj.writeEntry("QEsg", "LAM_MAX", self.dlg.Txt_y_d_max.text())
        proj.writeEntry("QEsg", "MAX_FORCAR", self.dlg.Txt_maxForcar.text())
        proj.writeEntry("QEsg", "DEG_IGNORE", self.dlg.Txt_deg_ignore.text())
        proj.writeEntry("QEsg", "DEG_MIN", self.dlg.Txt_deg_min.text())

        proj.writeEntry("QEsg", "POPINI", self.dlg.Txt_popini.text())
        proj.writeEntry("QEsg", "POPFIM", self.dlg.Txt_popfim.text())

        proj.writeEntry("QEsg", "DIAM_PROGRESS", self.dlg.chkDiamProgressivo.isChecked())

        proj.writeEntry("QEsg", "TUBOS_MAT", str(self.tableToArray()))
    def VerificaCampos(self):
        self.CamposClasse.Verifica('Criar')
    def PreencheCampos(self):
        self.CamposClasse.Verifica('Preencher')
    def CalculaVazao(self):
        self.VazaoClasse.CalcVazao()
    def CriaNodeFile(self):
        self.DimensClasse.CriaNos('',True)
    def Dimensiona(self):
        self.DimensClasse.Dimensiona()  #CalcTheta(1.5,0.013,0.02615,150,0.00000001)
    def AtualizaPVs(self):
        self.CamposClasse.AtualizaNomePVs()
    def ImportaSancadDXF(self):
        self.SancadClasse.ImportaDXF()
    def Rename(self):
        self.RenameClasse.initGui()
    def ClearPipesNames(self):
        self.RenameClasse.LimpaNomesColetores()
    def DesenhaPerfil(self):
        self.PerfilClasse.run()