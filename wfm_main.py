# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wfm_main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 150, 781, 411))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(250, 50, 301, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.chkAza1 = QtGui.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkAza1.setFont(font)
        self.chkAza1.setObjectName(_fromUtf8("chkAza1"))
        self.horizontalLayout.addWidget(self.chkAza1)
        self.chkAus11 = QtGui.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkAus11.setFont(font)
        self.chkAus11.setObjectName(_fromUtf8("chkAus11"))
        self.horizontalLayout.addWidget(self.chkAus11)
        self.chkPrg10 = QtGui.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkPrg10.setFont(font)
        self.chkPrg10.setObjectName(_fromUtf8("chkPrg10"))
        self.horizontalLayout.addWidget(self.chkPrg10)
        self.chkBlr13 = QtGui.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkBlr13.setFont(font)
        self.chkBlr13.setObjectName(_fromUtf8("chkBlr13"))
        self.horizontalLayout.addWidget(self.chkBlr13)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btnCreateBuckets = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnCreateBuckets.setObjectName(_fromUtf8("btnCreateBuckets"))
        self.verticalLayout.addWidget(self.btnCreateBuckets)
        self.lblInstruct = QtGui.QLabel(self.centralwidget)
        self.lblInstruct.setGeometry(QtCore.QRect(60, 10, 681, 31))
        self.lblInstruct.setObjectName(_fromUtf8("lblInstruct"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "WFM Lite v1.0", None))
        self.chkAza1.setText(_translate("mainWindow", "AZA1", None))
        self.chkAus11.setText(_translate("mainWindow", "AUS11", None))
        self.chkPrg10.setText(_translate("mainWindow", "PRG10", None))
        self.chkBlr13.setText(_translate("mainWindow", "BLR13", None))
        self.btnCreateBuckets.setText(_translate("mainWindow", "Create Buckets!", None))
        self.lblInstruct.setText(_translate("mainWindow", "Select the checkbox for the teams that you would like to create buckets for and click the \"Create Buckets!\" button.", None))

