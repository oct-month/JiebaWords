# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from config import TRASH_ICON
from .label import MyLabel, CliLabel
from .listwidget import MyQListWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 623)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(270, 50, 204, 231))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("font: 12pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.analy_set = QtWidgets.QComboBox(self.formLayoutWidget)
        self.analy_set.setObjectName("analy_set")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.analy_set)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("font: 12pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.num_set = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.num_set.setProperty("value", 20)
        self.num_set.setObjectName("num_set")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.num_set)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setStyleSheet("font: 12pt \"黑体\";")
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.pros_cons = QtWidgets.QComboBox(self.formLayoutWidget)
        self.pros_cons.setObjectName("pros_cons")
        self.pros_cons.addItem("")
        self.pros_cons.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pros_cons)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 4, 111, 31))
        self.label_4.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 10, 111, 31))
        self.label_5.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(510, 10, 111, 31))
        self.label_6.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 420, 191, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.export_txt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.export_txt.setObjectName("export_txt")
        self.verticalLayout.addWidget(self.export_txt)
        self.export_png = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.export_png.setObjectName("export_png")
        self.verticalLayout.addWidget(self.export_png)
        self.export_html = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.export_html.setObjectName("export_html")
        self.verticalLayout.addWidget(self.export_html)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(270, 370, 111, 31))
        self.label_7.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 370, 141, 31))
        self.label_8.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(250, 20, 20, 541))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(480, 20, 20, 541))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.source_list = MyQListWidget(self.centralwidget)
        self.source_list.setGeometry(QtCore.QRect(10, 50, 231, 311))
        self.source_list.setObjectName("source_list")
        self.stop_list = MyQListWidget(self.centralwidget)
        self.stop_list.setGeometry(QtCore.QRect(10, 410, 231, 161))
        self.stop_list.setObjectName("stop_list")
        self.action_btn = QtWidgets.QPushButton(self.centralwidget)
        self.action_btn.setGeometry(QtCore.QRect(270, 300, 201, 61))
        self.action_btn.setStyleSheet("font: 20pt \"微软雅黑\";")
        self.action_btn.setObjectName("action_btn")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(270, 280, 211, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(270, 365, 211, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.graphics_view = CliLabel(self.centralwidget)
        self.graphics_view.setGeometry(QtCore.QRect(510, 60, 591, 511))
        self.graphics_view.setText("")
        self.graphics_view.setObjectName("graphics_view")
        self.add_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_file_btn.setGeometry(QtCore.QRect(200, 10, 35, 35))
        self.add_file_btn.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.add_file_btn.setObjectName("add_file_btn")
        self.label = MyLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 4, 35, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(TRASH_ICON))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "词频探探"))
        self.label_2.setText(_translate("MainWindow", "分析引擎"))
        self.label_3.setText(_translate("MainWindow", "析词数量"))
        self.label_9.setText(_translate("MainWindow", "正/反序"))
        self.pros_cons.setItemText(0, _translate("MainWindow", "正序"))
        self.pros_cons.setItemText(1, _translate("MainWindow", "反序"))
        self.label_4.setText(_translate("MainWindow", "source"))
        self.label_5.setText(_translate("MainWindow", "options"))
        self.label_6.setText(_translate("MainWindow", "graphics"))
        self.export_txt.setText(_translate("MainWindow", "导出文本"))
        self.export_png.setText(_translate("MainWindow", "导出图像"))
        self.export_html.setText(_translate("MainWindow", "导出HTML"))
        self.label_7.setText(_translate("MainWindow", "operator"))
        self.label_8.setText(_translate("MainWindow", "stopwords"))
        self.action_btn.setText(_translate("MainWindow", "Action"))
        self.add_file_btn.setText(_translate("MainWindow", "+"))
