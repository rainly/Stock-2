# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MinDataUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(802, 614)
        self.gpdm = QtWidgets.QLabel(Dialog)
        self.gpdm.setGeometry(QtCore.QRect(10, 30, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gpdm.setFont(font)
        self.gpdm.setObjectName("gpdm")
        self.gpdmEdit = QtWidgets.QLineEdit(Dialog)
        self.gpdmEdit.setGeometry(QtCore.QRect(100, 30, 311, 31))
        self.gpdmEdit.setObjectName("gpdmEdit")
        self.xzsj = QtWidgets.QLabel(Dialog)
        self.xzsj.setGeometry(QtCore.QRect(10, 100, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.xzsj.setFont(font)
        self.xzsj.setObjectName("xzsj")
        self.zhi = QtWidgets.QLabel(Dialog)
        self.zhi.setGeometry(QtCore.QRect(250, 100, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.zhi.setFont(font)
        self.zhi.setObjectName("zhi")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(110, 110, 130, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.bclj = QtWidgets.QLabel(Dialog)
        self.bclj.setGeometry(QtCore.QRect(10, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bclj.setFont(font)
        self.bclj.setObjectName("bclj")
        self.bclj_2 = QtWidgets.QLineEdit(Dialog)
        self.bclj_2.setGeometry(QtCore.QRect(100, 70, 211, 31))
        self.bclj_2.setReadOnly(True)
        self.bclj_2.setObjectName("bclj_2")
        self.ljxz = QtWidgets.QPushButton(Dialog)
        self.ljxz.setGeometry(QtCore.QRect(320, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ljxz.setFont(font)
        self.ljxz.setObjectName("ljxz")
        self.xzlsFs = QtWidgets.QPushButton(Dialog)
        self.xzlsFs.setGeometry(QtCore.QRect(10, 140, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.xzlsFs.setFont(font)
        self.xzlsFs.setObjectName("xzlsFs")
        self.xzdtfs = QtWidgets.QPushButton(Dialog)
        self.xzdtfs.setGeometry(QtCore.QRect(10, 170, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.xzdtfs.setFont(font)
        self.xzdtfs.setObjectName("xzdtfs")
        self.xzlsFs_2 = QtWidgets.QPushButton(Dialog)
        self.xzlsFs_2.setGeometry(QtCore.QRect(10, 200, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.xzlsFs_2.setFont(font)
        self.xzlsFs_2.setObjectName("xzlsFs_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 421, 591))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.listView_2 = QtWidgets.QListView(self.groupBox)
        self.listView_2.setGeometry(QtCore.QRect(10, 230, 401, 351))
        self.listView_2.setObjectName("listView_2")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit_2.setGeometry(QtCore.QRect(280, 100, 130, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(440, 10, 351, 591))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.listView = QtWidgets.QListView(self.groupBox_2)
        self.listView.setGeometry(QtCore.QRect(10, 80, 331, 451))
        self.listView.setObjectName("listView")
        self.dqlj = QtWidgets.QLineEdit(self.groupBox_2)
        self.dqlj.setGeometry(QtCore.QRect(10, 20, 201, 31))
        self.dqlj.setReadOnly(True)
        self.dqlj.setObjectName("dqlj")
        self.dqljwj = QtWidgets.QPushButton(self.groupBox_2)
        self.dqljwj.setGeometry(QtCore.QRect(220, 20, 121, 31))
        self.dqljwj.setObjectName("dqljwj")
        self.hbgpCode = QtWidgets.QLabel(self.groupBox_2)
        self.hbgpCode.setGeometry(QtCore.QRect(20, 540, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.hbgpCode.setFont(font)
        self.hbgpCode.setObjectName("hbgpCode")
        self.gpdmHb = QtWidgets.QLineEdit(self.groupBox_2)
        self.gpdmHb.setGeometry(QtCore.QRect(120, 540, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.gpdmHb.setFont(font)
        self.gpdmHb.setObjectName("gpdmHb")
        self.hbbb = QtWidgets.QPushButton(self.groupBox_2)
        self.hbbb.setGeometry(QtCore.QRect(240, 540, 101, 31))
        self.hbbb.setObjectName("hbbb")
        self.dqljwj_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.dqljwj_2.setGeometry(QtCore.QRect(10, 50, 331, 31))
        self.dqljwj_2.setObjectName("dqljwj_2")
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.gpdm.raise_()
        self.gpdmEdit.raise_()
        self.xzsj.raise_()
        self.zhi.raise_()
        self.dateEdit.raise_()
        self.bclj.raise_()
        self.bclj_2.raise_()
        self.ljxz.raise_()
        self.xzlsFs.raise_()
        self.xzdtfs.raise_()
        self.xzlsFs_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.gpdm.setText(_translate("Dialog", "股票代码："))
        self.xzsj.setText(_translate("Dialog", "下载时间："))
        self.zhi.setText(_translate("Dialog", "至"))
        self.bclj.setText(_translate("Dialog", "保存路径："))
        self.ljxz.setText(_translate("Dialog", "路径选择"))
        self.xzlsFs.setText(_translate("Dialog", "下载历史分时"))
        self.xzdtfs.setText(_translate("Dialog", "下载当天分时"))
        self.xzlsFs_2.setText(_translate("Dialog", "多个股票下载历史分时"))
        self.groupBox.setTitle(_translate("Dialog", "下载数据"))
        self.groupBox_2.setTitle(_translate("Dialog", "合并数据"))
        self.dqljwj.setText(_translate("Dialog", "选择路径"))
        self.hbgpCode.setText(_translate("Dialog", "股票代码："))
        self.hbbb.setText(_translate("Dialog", "合并表格"))
        self.dqljwj_2.setText(_translate("Dialog", "查询"))

