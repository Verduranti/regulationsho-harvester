# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri May 25 17:25:34 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(398, 281)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.cbNasdaq = QtGui.QCheckBox(self.centralWidget)
        self.cbNasdaq.setGeometry(QtCore.QRect(220, 80, 87, 20))
        self.cbNasdaq.setTristate(False)
        self.cbNasdaq.setObjectName(_fromUtf8("cbNasdaq"))
        self.cbNYSE = QtGui.QCheckBox(self.centralWidget)
        self.cbNYSE.setGeometry(QtCore.QRect(220, 110, 87, 20))
        self.cbNYSE.setObjectName(_fromUtf8("cbNYSE"))
        self.cbADF = QtGui.QCheckBox(self.centralWidget)
        self.cbADF.setGeometry(QtCore.QRect(220, 140, 87, 20))
        self.cbADF.setObjectName(_fromUtf8("cbADF"))
        self.cbORF = QtGui.QCheckBox(self.centralWidget)
        self.cbORF.setGeometry(QtCore.QRect(220, 170, 87, 20))
        self.cbORF.setObjectName(_fromUtf8("cbORF"))
        self.cbAllMkts = QtGui.QCheckBox(self.centralWidget)
        self.cbAllMkts.setGeometry(QtCore.QRect(220, 50, 101, 20))
        self.cbAllMkts.setObjectName(_fromUtf8("cbAllMkts"))
        self.startDate = QtGui.QDateEdit(self.centralWidget)
        self.startDate.setGeometry(QtCore.QRect(90, 20, 110, 25))
        self.startDate.setDate(QtCore.QDate(2012, 5, 20))
        self.startDate.setMaximumDate(QtCore.QDate(7999, 12, 31))
        self.startDate.setMinimumDate(QtCore.QDate(2011, 6, 1))
        self.startDate.setCurrentSection(QtGui.QDateTimeEdit.MonthSection)
        self.startDate.setObjectName(_fromUtf8("startDate"))
        self.endDate = QtGui.QDateEdit(self.centralWidget)
        self.endDate.setGeometry(QtCore.QRect(90, 70, 110, 25))
        self.endDate.setDate(QtCore.QDate(2012, 5, 21))
        self.endDate.setMaximumDate(QtCore.QDate(7999, 12, 31))
        self.endDate.setMinimumDate(QtCore.QDate(2011, 6, 1))
        self.endDate.setObjectName(_fromUtf8("endDate"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cbEverything = QtGui.QCheckBox(self.centralWidget)
        self.cbEverything.setGeometry(QtCore.QRect(220, 20, 161, 20))
        self.cbEverything.setObjectName(_fromUtf8("cbEverything"))
        self.harvestButton = QtGui.QPushButton(self.centralWidget)
        self.harvestButton.setGeometry(QtCore.QRect(50, 130, 114, 32))
        self.harvestButton.setObjectName(_fromUtf8("harvestButton"))
        self.cbUseUpdated = QtGui.QCheckBox(self.centralWidget)
        self.cbUseUpdated.setGeometry(QtCore.QRect(220, 200, 141, 20))
        self.cbUseUpdated.setObjectName(_fromUtf8("cbUseUpdated"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 191, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 398, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "FINRA Regulation SHO Data Harvester", None, QtGui.QApplication.UnicodeUTF8))
        self.cbNasdaq.setText(QtGui.QApplication.translate("MainWindow", "NASDAQ", None, QtGui.QApplication.UnicodeUTF8))
        self.cbNYSE.setText(QtGui.QApplication.translate("MainWindow", "NYSE", None, QtGui.QApplication.UnicodeUTF8))
        self.cbADF.setText(QtGui.QApplication.translate("MainWindow", "ADF", None, QtGui.QApplication.UnicodeUTF8))
        self.cbORF.setText(QtGui.QApplication.translate("MainWindow", "ORF", None, QtGui.QApplication.UnicodeUTF8))
        self.cbAllMkts.setText(QtGui.QApplication.translate("MainWindow", "All Markets", None, QtGui.QApplication.UnicodeUTF8))
        self.startDate.setDisplayFormat(QtGui.QApplication.translate("MainWindow", "MM/dd/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.endDate.setDisplayFormat(QtGui.QApplication.translate("MainWindow", "MM/dd/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Start Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "End Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbEverything.setText(QtGui.QApplication.translate("MainWindow", "Just grab everything", None, QtGui.QApplication.UnicodeUTF8))
        self.harvestButton.setText(QtGui.QApplication.translate("MainWindow", "Harvest Data", None, QtGui.QApplication.UnicodeUTF8))
        self.cbUseUpdated.setText(QtGui.QApplication.translate("MainWindow", "Use updated file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "*Earliest date is 06/01/2011", None, QtGui.QApplication.UnicodeUTF8))

