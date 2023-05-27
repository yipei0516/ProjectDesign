# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\VSCode_JuniorSubject\nasal_surgery\05272030_ProjectDesign\Result.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_interrupt_times = QtWidgets.QLabel(self.centralwidget)
        self.label_interrupt_times.setGeometry(QtCore.QRect(130, 411, 260, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_interrupt_times.setFont(font)
        self.label_interrupt_times.setStyleSheet("")
        self.label_interrupt_times.setScaledContents(True)
        self.label_interrupt_times.setWordWrap(True)
        self.label_interrupt_times.setObjectName("label_interrupt_times")
        self.list_widget_interrupt = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget_interrupt.setGeometry(QtCore.QRect(740, 170, 321, 431))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setBold(True)
        font.setWeight(75)
        self.list_widget_interrupt.setFont(font)
        self.list_widget_interrupt.setObjectName("list_widget_interrupt")
        self.button_remove_interrupt = QtWidgets.QPushButton(self.centralwidget)
        self.button_remove_interrupt.setGeometry(QtCore.QRect(890, 620, 170, 35))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.button_remove_interrupt.setFont(font)
        self.button_remove_interrupt.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius: 10px;\n"
"border: 1px groove gray;\n"
"border-style:outset;")
        self.button_remove_interrupt.setObjectName("button_remove_interrupt")
        self.label_performance = QtWidgets.QLabel(self.centralwidget)
        self.label_performance.setEnabled(True)
        self.label_performance.setGeometry(QtCore.QRect(340, 116, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_performance.setFont(font)
        self.label_performance.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_performance.setText("")
        self.label_performance.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_performance.setObjectName("label_performance")
        self.label_performance_text = QtWidgets.QLabel(self.centralwidget)
        self.label_performance_text.setEnabled(True)
        self.label_performance_text.setGeometry(QtCore.QRect(130, 146, 380, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_performance_text.setFont(font)
        self.label_performance_text.setStyleSheet("")
        self.label_performance_text.setScaledContents(True)
        self.label_performance_text.setWordWrap(True)
        self.label_performance_text.setObjectName("label_performance_text")
        self.comboBox_choose_video = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_choose_video.setGeometry(QtCore.QRect(740, 110, 321, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_choose_video.setFont(font)
        self.comboBox_choose_video.setObjectName("comboBox_choose_video")
        self.label_efficeiency_text = QtWidgets.QLabel(self.centralwidget)
        self.label_efficeiency_text.setEnabled(True)
        self.label_efficeiency_text.setGeometry(QtCore.QRect(130, 226, 380, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_efficeiency_text.setFont(font)
        self.label_efficeiency_text.setStyleSheet("")
        self.label_efficeiency_text.setScaledContents(True)
        self.label_efficeiency_text.setWordWrap(True)
        self.label_efficeiency_text.setObjectName("label_efficeiency_text")
        self.label_surgery_time = QtWidgets.QLabel(self.centralwidget)
        self.label_surgery_time.setGeometry(QtCore.QRect(130, 311, 260, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_surgery_time.setFont(font)
        self.label_surgery_time.setStyleSheet("")
        self.label_surgery_time.setScaledContents(True)
        self.label_surgery_time.setWordWrap(True)
        self.label_surgery_time.setObjectName("label_surgery_time")
        self.label_total_interrupt_time = QtWidgets.QLabel(self.centralwidget)
        self.label_total_interrupt_time.setGeometry(QtCore.QRect(130, 361, 260, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_total_interrupt_time.setFont(font)
        self.label_total_interrupt_time.setStyleSheet("")
        self.label_total_interrupt_time.setScaledContents(True)
        self.label_total_interrupt_time.setWordWrap(True)
        self.label_total_interrupt_time.setObjectName("label_total_interrupt_time")
        self.label_efficiency = QtWidgets.QLabel(self.centralwidget)
        self.label_efficiency.setEnabled(True)
        self.label_efficiency.setGeometry(QtCore.QRect(340, 201, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_efficiency.setFont(font)
        self.label_efficiency.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_efficiency.setText("")
        self.label_efficiency.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_efficiency.setObjectName("label_efficiency")
        self.label_ratio = QtWidgets.QLabel(self.centralwidget)
        self.label_ratio.setGeometry(QtCore.QRect(130, 511, 371, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ratio.setFont(font)
        self.label_ratio.setStyleSheet("")
        self.label_ratio.setScaledContents(True)
        self.label_ratio.setWordWrap(True)
        self.label_ratio.setObjectName("label_ratio")
        self.label_unit_interrupt_counts = QtWidgets.QLabel(self.centralwidget)
        self.label_unit_interrupt_counts.setGeometry(QtCore.QRect(130, 461, 371, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_unit_interrupt_counts.setFont(font)
        self.label_unit_interrupt_counts.setStyleSheet("")
        self.label_unit_interrupt_counts.setScaledContents(True)
        self.label_unit_interrupt_counts.setWordWrap(True)
        self.label_unit_interrupt_counts.setObjectName("label_unit_interrupt_counts")
        self.button_back_menu = QtWidgets.QPushButton(self.centralwidget)
        self.button_back_menu.setGeometry(QtCore.QRect(1130, 630, 60, 60))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.button_back_menu.setFont(font)
        self.button_back_menu.setStyleSheet("QPushButton {\n"
"        border: 0px solid;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgb(223, 223, 223);\n"
"    }\n"
"")
        self.button_back_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./image/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back_menu.setIcon(icon)
        self.button_back_menu.setIconSize(QtCore.QSize(60, 60))
        self.button_back_menu.setObjectName("button_back_menu")
        self.label_frame = QtWidgets.QLabel(self.centralwidget)
        self.label_frame.setGeometry(QtCore.QRect(90, 101, 531, 501))
        self.label_frame.setStyleSheet("border-color: rgb(84, 84, 84);\n"
"border-radius: 30px;\n"
"border: 2px groove black;\n"
"border-style:outset;")
        self.label_frame.setText("")
        self.label_frame.setScaledContents(True)
        self.label_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.label_frame.setObjectName("label_frame")
        self.label_cute_image = QtWidgets.QLabel(self.centralwidget)
        self.label_cute_image.setGeometry(QtCore.QRect(440, 140, 150, 150))
        self.label_cute_image.setText("")
        self.label_cute_image.setScaledContents(True)
        self.label_cute_image.setObjectName("label_cute_image")
        self.label_background = QtWidgets.QLabel(self.centralwidget)
        self.label_background.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.label_background.setText("")
        self.label_background.setScaledContents(True)
        self.label_background.setObjectName("label_background")
        self.label_frame.raise_()
        self.label_interrupt_times.raise_()
        self.list_widget_interrupt.raise_()
        self.button_remove_interrupt.raise_()
        self.comboBox_choose_video.raise_()
        self.label_efficeiency_text.raise_()
        self.label_surgery_time.raise_()
        self.label_total_interrupt_time.raise_()
        self.label_ratio.raise_()
        self.label_unit_interrupt_counts.raise_()
        self.label_performance_text.raise_()
        self.label_performance.raise_()
        self.label_efficiency.raise_()
        self.button_back_menu.raise_()
        self.label_cute_image.raise_()
        self.label_background.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_interrupt_times.setText(_translate("MainWindow", "總中斷次數:   尚未進行偵測"))
        self.button_remove_interrupt.setText(_translate("MainWindow", "刪除此中斷點 ❌"))
        self.label_performance_text.setText(_translate("MainWindow", "中斷次數評分:   尚未進行偵測"))
        self.label_efficeiency_text.setText(_translate("MainWindow", "效率評分:   尚未進行偵測"))
        self.label_surgery_time.setText(_translate("MainWindow", "總手術時間:   尚未進行偵測"))
        self.label_total_interrupt_time.setText(_translate("MainWindow", "總中斷時間:   尚未進行偵測"))
        self.label_ratio.setText(_translate("MainWindow", "中斷時間佔整個手術時間的比例:   尚未進行偵測"))
        self.label_unit_interrupt_counts.setText(_translate("MainWindow", "平均每九分鐘的中斷次數:   尚未進行偵測"))
