# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TdxAudTool.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1216, 688)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(1040, 660, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1191, 651))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_data = QtWidgets.QWidget()
        self.tab_data.setObjectName("tab_data")
        self.groupBox = QtWidgets.QGroupBox(self.tab_data)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 981, 291))
        self.groupBox.setObjectName("groupBox")
        self.tv_lhb = QtWidgets.QTableView(self.groupBox)
        self.tv_lhb.setGeometry(QtCore.QRect(10, 43, 961, 241))
        self.tv_lhb.setObjectName("tv_lhb")
        self.rb_5day = QtWidgets.QRadioButton(self.groupBox)
        self.rb_5day.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.rb_5day.setObjectName("rb_5day")
        self.rb_10day = QtWidgets.QRadioButton(self.groupBox)
        self.rb_10day.setGeometry(QtCore.QRect(60, 20, 47, 16))
        self.rb_10day.setObjectName("rb_10day")
        self.rb_30day = QtWidgets.QRadioButton(self.groupBox)
        self.rb_30day.setGeometry(QtCore.QRect(110, 20, 47, 16))
        self.rb_30day.setObjectName("rb_30day")
        self.rb_60day = QtWidgets.QRadioButton(self.groupBox)
        self.rb_60day.setGeometry(QtCore.QRect(160, 20, 47, 16))
        self.rb_60day.setObjectName("rb_60day")
        self.btn_lhb = QtWidgets.QPushButton(self.groupBox)
        self.btn_lhb.setGeometry(QtCore.QRect(214, 17, 75, 23))
        self.btn_lhb.setObjectName("btn_lhb")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_data)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 310, 981, 281))
        self.groupBox_2.setObjectName("groupBox_2")
        self.rb_lhb = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_lhb.setGeometry(QtCore.QRect(20, 50, 89, 16))
        self.rb_lhb.setObjectName("rb_lhb")
        self.rb_all = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_all.setGeometry(QtCore.QRect(120, 50, 111, 16))
        self.rb_all.setObjectName("rb_all")
        self.btn_read_stock = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_read_stock.setGeometry(QtCore.QRect(260, 50, 101, 23))
        self.btn_read_stock.setObjectName("btn_read_stock")
        self.lv_msg = QtWidgets.QListView(self.groupBox_2)
        self.lv_msg.setGeometry(QtCore.QRect(10, 80, 961, 192))
        self.lv_msg.setObjectName("lv_msg")
        self.le_tdx_path = QtWidgets.QLineEdit(self.groupBox_2)
        self.le_tdx_path.setGeometry(QtCore.QRect(110, 20, 141, 20))
        self.le_tdx_path.setObjectName("le_tdx_path")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label.setObjectName("label")
        self.btn_tdx_path = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_tdx_path.setGeometry(QtCore.QRect(260, 20, 101, 23))
        self.btn_tdx_path.setObjectName("btn_tdx_path")
        self.le_read_path = QtWidgets.QLineEdit(self.groupBox_2)
        self.le_read_path.setGeometry(QtCore.QRect(460, 20, 171, 20))
        self.le_read_path.setObjectName("le_read_path")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(380, 20, 81, 16))
        self.label_2.setObjectName("label_2")
        self.btn_clearMsg = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_clearMsg.setGeometry(QtCore.QRect(640, 50, 75, 23))
        self.btn_clearMsg.setObjectName("btn_clearMsg")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(380, 50, 261, 16))
        self.label_4.setObjectName("label_4")
        self.btn_stop_readTdx = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_stop_readTdx.setGeometry(QtCore.QRect(730, 50, 101, 23))
        self.btn_stop_readTdx.setObjectName("btn_stop_readTdx")
        self.progressBar = QtWidgets.QProgressBar(self.tab_data)
        self.progressBar.setGeometry(QtCore.QRect(340, 600, 261, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.le_outpath = QtWidgets.QLineEdit(self.tab_data)
        self.le_outpath.setGeometry(QtCore.QRect(100, 600, 231, 20))
        self.le_outpath.setObjectName("le_outpath")
        self.label_3 = QtWidgets.QLabel(self.tab_data)
        self.label_3.setGeometry(QtCore.QRect(20, 600, 81, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_data, "")
        self.tab_view = QtWidgets.QWidget()
        self.tab_view.setObjectName("tab_view")
        self.groupBox_pic = QtWidgets.QGroupBox(self.tab_view)
        self.groupBox_pic.setGeometry(QtCore.QRect(210, 10, 971, 611))
        self.groupBox_pic.setObjectName("groupBox_pic")
        self.dateEdit_Start = QtWidgets.QDateEdit(self.tab_view)
        self.dateEdit_Start.setGeometry(QtCore.QRect(72, 10, 131, 20))
        self.dateEdit_Start.setObjectName("dateEdit_Start")
        self.dateEdit_End = QtWidgets.QDateEdit(self.tab_view)
        self.dateEdit_End.setGeometry(QtCore.QRect(72, 31, 131, 20))
        self.dateEdit_End.setObjectName("dateEdit_End")
        self.lineEdit_CodeUp = QtWidgets.QLineEdit(self.tab_view)
        self.lineEdit_CodeUp.setGeometry(QtCore.QRect(102, 52, 101, 20))
        self.lineEdit_CodeUp.setObjectName("lineEdit_CodeUp")
        self.lineEdit_CodeDn = QtWidgets.QLineEdit(self.tab_view)
        self.lineEdit_CodeDn.setGeometry(QtCore.QRect(102, 73, 101, 20))
        self.lineEdit_CodeDn.setObjectName("lineEdit_CodeDn")
        self.label_7 = QtWidgets.QLabel(self.tab_view)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 84, 16))
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.tab_view)
        self.label_12.setGeometry(QtCore.QRect(10, 33, 84, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_view)
        self.label_13.setGeometry(QtCore.QRect(10, 50, 84, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_view)
        self.label_14.setGeometry(QtCore.QRect(10, 70, 84, 16))
        self.label_14.setObjectName("label_14")
        self.comboBox = QtWidgets.QComboBox(self.tab_view)
        self.comboBox.setGeometry(QtCore.QRect(80, 94, 121, 22))
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setObjectName("comboBox")
        self.label_15 = QtWidgets.QLabel(self.tab_view)
        self.label_15.setGeometry(QtCore.QRect(10, 95, 51, 16))
        self.label_15.setObjectName("label_15")
        self.btn_getValue = QtWidgets.QPushButton(self.tab_view)
        self.btn_getValue.setGeometry(QtCore.QRect(10, 116, 191, 31))
        self.btn_getValue.setObjectName("btn_getValue")
        self.groupBox_drawPic = QtWidgets.QGroupBox(self.tab_view)
        self.groupBox_drawPic.setGeometry(QtCore.QRect(0, 210, 191, 281))
        self.groupBox_drawPic.setObjectName("groupBox_drawPic")
        self.btn_drawPic = QtWidgets.QPushButton(self.groupBox_drawPic)
        self.btn_drawPic.setGeometry(QtCore.QRect(10, 220, 161, 31))
        self.btn_drawPic.setObjectName("btn_drawPic")
        self.cb_kLine = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_kLine.setGeometry(QtCore.QRect(10, 26, 51, 16))
        self.cb_kLine.setObjectName("cb_kLine")
        self.cb_volume = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_volume.setGeometry(QtCore.QRect(80, 26, 61, 16))
        self.cb_volume.setObjectName("cb_volume")
        self.cb_nhd31_60_120 = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_nhd31_60_120.setGeometry(QtCore.QRect(10, 86, 113, 16))
        self.cb_nhd31_60_120.setObjectName("cb_nhd31_60_120")
        self.cb_MA10 = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_MA10.setGeometry(QtCore.QRect(10, 133, 53, 16))
        self.cb_MA10.setObjectName("cb_MA10")
        self.cb_MA31 = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_MA31.setGeometry(QtCore.QRect(10, 166, 53, 16))
        self.cb_MA31.setObjectName("cb_MA31")
        self.cb_MA120 = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_MA120.setGeometry(QtCore.QRect(10, 200, 53, 16))
        self.cb_MA120.setObjectName("cb_MA120")
        self.cb_slopeMA20 = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_slopeMA20.setGeometry(QtCore.QRect(80, 150, 71, 16))
        self.cb_slopeMA20.setObjectName("cb_slopeMA20")
        self.cb_slopeMA60 = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_slopeMA60.setGeometry(QtCore.QRect(80, 183, 71, 16))
        self.cb_slopeMA60.setObjectName("cb_slopeMA60")
        self.cb_slopeMA5 = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_slopeMA5.setGeometry(QtCore.QRect(80, 116, 71, 16))
        self.cb_slopeMA5.setObjectName("cb_slopeMA5")
        self.cb_MA60 = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_MA60.setGeometry(QtCore.QRect(10, 183, 53, 16))
        self.cb_MA60.setObjectName("cb_MA60")
        self.cb_MACD = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_MACD.setGeometry(QtCore.QRect(10, 46, 44, 16))
        self.cb_MACD.setObjectName("cb_MACD")
        self.cb_MA20 = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_MA20.setGeometry(QtCore.QRect(10, 150, 53, 16))
        self.cb_MA20.setObjectName("cb_MA20")
        self.cb_BOLL = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_BOLL.setGeometry(QtCore.QRect(79, 46, 44, 16))
        self.cb_BOLL.setObjectName("cb_BOLL")
        self.cb_MA5 = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_MA5.setGeometry(QtCore.QRect(10, 116, 53, 16))
        self.cb_MA5.setObjectName("cb_MA5")
        self.cb_slopeMA10 = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_slopeMA10.setGeometry(QtCore.QRect(80, 133, 71, 16))
        self.cb_slopeMA10.setObjectName("cb_slopeMA10")
        self.cb_slopeMA31 = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_slopeMA31.setGeometry(QtCore.QRect(80, 166, 71, 16))
        self.cb_slopeMA31.setObjectName("cb_slopeMA31")
        self.cb_slopeMA120 = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_slopeMA120.setGeometry(QtCore.QRect(80, 200, 71, 16))
        self.cb_slopeMA120.setObjectName("cb_slopeMA120")
        self.cb_nhd_20_31_60 = QtWidgets.QCheckBox(self.groupBox_drawPic)
        self.cb_nhd_20_31_60.setGeometry(QtCore.QRect(10, 68, 113, 16))
        self.cb_nhd_20_31_60.setObjectName("cb_nhd_20_31_60")
        self.le_drawPic = QtWidgets.QLineEdit(self.groupBox_drawPic)
        self.le_drawPic.setEnabled(False)
        self.le_drawPic.setGeometry(QtCore.QRect(10, 251, 161, 20))
        self.le_drawPic.setObjectName("le_drawPic")
        self.le_dbStatus = QtWidgets.QLineEdit(self.tab_view)
        self.le_dbStatus.setEnabled(False)
        self.le_dbStatus.setGeometry(QtCore.QRect(10, 148, 191, 20))
        self.le_dbStatus.setObjectName("le_dbStatus")
        self.groupBox_drawPic.raise_()
        self.groupBox_pic.raise_()
        self.dateEdit_Start.raise_()
        self.dateEdit_End.raise_()
        self.lineEdit_CodeUp.raise_()
        self.lineEdit_CodeDn.raise_()
        self.label_7.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.comboBox.raise_()
        self.label_15.raise_()
        self.btn_getValue.raise_()
        self.le_dbStatus.raise_()
        self.tabWidget.addTab(self.tab_view, "")
        self.tab_hyfx = QtWidgets.QWidget()
        self.tab_hyfx.setObjectName("tab_hyfx")
        self.le_hyfxCode = QtWidgets.QLineEdit(self.tab_hyfx)
        self.le_hyfxCode.setGeometry(QtCore.QRect(75, 10, 113, 20))
        self.le_hyfxCode.setObjectName("le_hyfxCode")
        self.lb_hycode = QtWidgets.QLabel(self.tab_hyfx)
        self.lb_hycode.setGeometry(QtCore.QRect(11, 14, 54, 12))
        self.lb_hycode.setObjectName("lb_hycode")
        self.btn_tqHyfx = QtWidgets.QPushButton(self.tab_hyfx)
        self.btn_tqHyfx.setGeometry(QtCore.QRect(191, 8, 75, 23))
        self.btn_tqHyfx.setObjectName("btn_tqHyfx")
        self.tbl_hyfx = QtWidgets.QTableView(self.tab_hyfx)
        self.tbl_hyfx.setGeometry(QtCore.QRect(10, 33, 981, 451))
        self.tbl_hyfx.setObjectName("tbl_hyfx")
        self.le_hyfxStatus = QtWidgets.QLineEdit(self.tab_hyfx)
        self.le_hyfxStatus.setEnabled(False)
        self.le_hyfxStatus.setGeometry(QtCore.QRect(268, 9, 301, 20))
        self.le_hyfxStatus.setObjectName("le_hyfxStatus")
        self.tabWidget.addTab(self.tab_hyfx, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "股票"))
        self.groupBox.setTitle(_translate("Dialog", "龙虎榜"))
        self.rb_5day.setText(_translate("Dialog", "5日"))
        self.rb_10day.setText(_translate("Dialog", "10日"))
        self.rb_30day.setText(_translate("Dialog", "30日"))
        self.rb_60day.setText(_translate("Dialog", "60日"))
        self.btn_lhb.setText(_translate("Dialog", "获取龙虎榜"))
        self.groupBox_2.setTitle(_translate("Dialog", "获取通达信数据"))
        self.rb_lhb.setText(_translate("Dialog", "路径龙虎榜股票"))
        self.rb_all.setText(_translate("Dialog", "路径下所有股票"))
        self.btn_read_stock.setText(_translate("Dialog", "读取通达信股票"))
        self.label.setText(_translate("Dialog", "通达信安装路径"))
        self.btn_tdx_path.setText(_translate("Dialog", "查找"))
        self.label_2.setText(_translate("Dialog", "数据读取路径"))
        self.btn_clearMsg.setText(_translate("Dialog", "清除信息"))
        self.label_4.setText(_translate("Dialog", "深证:/vipdoc/sz/lday 上证：/vipdoc/sh/lday"))
        self.btn_stop_readTdx.setText(_translate("Dialog", "停止读取"))
        self.label_3.setText(_translate("Dialog", "数据输出路径"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), _translate("Dialog", "提取数据"))
        self.groupBox_pic.setTitle(_translate("Dialog", "绘图区"))
        self.label_7.setText(_translate("Dialog", "开始时间："))
        self.label_12.setText(_translate("Dialog", "结束时间："))
        self.label_13.setText(_translate("Dialog", "股票代码(上)："))
        self.label_14.setText(_translate("Dialog", "股票代码(下)："))
        self.label_15.setText(_translate("Dialog", "类型："))
        self.btn_getValue.setText(_translate("Dialog", "读取数据库数据"))
        self.groupBox_drawPic.setTitle(_translate("Dialog", "选择绘图"))
        self.btn_drawPic.setText(_translate("Dialog", "绘制选择的图像"))
        self.cb_kLine.setText(_translate("Dialog", "日K线"))
        self.cb_volume.setText(_translate("Dialog", "交易量"))
        self.cb_nhd31_60_120.setText(_translate("Dialog", "粘合度31_60_120"))
        self.cb_MA10.setText(_translate("Dialog", "MA10"))
        self.cb_MA31.setText(_translate("Dialog", "MA31"))
        self.cb_MA120.setText(_translate("Dialog", "MA120"))
        self.cb_slopeMA20.setText(_translate("Dialog", "斜率M20"))
        self.cb_slopeMA60.setText(_translate("Dialog", "斜率M60"))
        self.cb_slopeMA5.setText(_translate("Dialog", "斜率M5"))
        self.cb_MA60.setText(_translate("Dialog", "MA60"))
        self.cb_MACD.setText(_translate("Dialog", "MACD"))
        self.cb_MA20.setText(_translate("Dialog", "MA20"))
        self.cb_BOLL.setText(_translate("Dialog", "BOLL"))
        self.cb_MA5.setText(_translate("Dialog", "MA5"))
        self.cb_slopeMA10.setText(_translate("Dialog", "斜率M10"))
        self.cb_slopeMA31.setText(_translate("Dialog", "斜率M31"))
        self.cb_slopeMA120.setText(_translate("Dialog", "斜率M120"))
        self.cb_nhd_20_31_60.setText(_translate("Dialog", "粘合度20_31_60"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_view), _translate("Dialog", "查看图形"))
        self.lb_hycode.setText(_translate("Dialog", "股票代码："))
        self.btn_tqHyfx.setText(_translate("Dialog", "提取数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hyfx), _translate("Dialog", "查看行业排名"))

