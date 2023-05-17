# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1500, 864)
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_start_judge = QtWidgets.QPushButton(self.centralwidget)
        self.button_start_judge.setEnabled(True)
        self.button_start_judge.setGeometry(QtCore.QRect(130, 210, 235, 60))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_start_judge.setFont(font)
        self.button_start_judge.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(190, 184, 171);\n"
"    border-radius: 20px;\n"
"    border: 1px groove gray;\n"
"    border-style:outset;\n"
"}\n"
"QPushButton:disabled {\n"
"    color:#fff;\n"
"    background:#ccc;\n"
"    border-radius: 20px;\n"
"    border: 1px solid gray;\n"
"    border-style:outset;\n"
"}")
        self.button_start_judge.setObjectName("button_start_judge")
        self.button_choose_video = QtWidgets.QPushButton(self.centralwidget)
        self.button_choose_video.setGeometry(QtCore.QRect(130, 130, 235, 60))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_choose_video.setFont(font)
        self.button_choose_video.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(190, 184, 171);\n"
"border-radius: 20px;\n"
"border: 1px groove gray;\n"
"border-style:outset;")
        self.button_choose_video.setObjectName("button_choose_video")
        self.label_video_name = QtWidgets.QLabel(self.centralwidget)
        self.label_video_name.setGeometry(QtCore.QRect(70, 50, 491, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_video_name.setFont(font)
        self.label_video_name.setScaledContents(True)
        self.label_video_name.setWordWrap(True)
        self.label_video_name.setObjectName("label_video_name")
        self.label_interrupt_times = QtWidgets.QLabel(self.centralwidget)
        self.label_interrupt_times.setGeometry(QtCore.QRect(700, 290, 260, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_interrupt_times.setFont(font)
        self.label_interrupt_times.setScaledContents(True)
        self.label_interrupt_times.setWordWrap(True)
        self.label_interrupt_times.setObjectName("label_interrupt_times")
        self.list_widget_interrupt = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget_interrupt.setGeometry(QtCore.QRect(110, 440, 270, 371))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setBold(True)
        font.setWeight(75)
        self.list_widget_interrupt.setFont(font)
        self.list_widget_interrupt.setObjectName("list_widget_interrupt")
        self.button_remove_interrupt = QtWidgets.QPushButton(self.centralwidget)
        self.button_remove_interrupt.setGeometry(QtCore.QRect(410, 770, 170, 35))
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
        self.label_done = QtWidgets.QLabel(self.centralwidget)
        self.label_done.setGeometry(QtCore.QRect(1120, 30, 211, 131))
        self.label_done.setText("")
        self.label_done.setScaledContents(True)
        self.label_done.setObjectName("label_done")
        self.label_performance = QtWidgets.QLabel(self.centralwidget)
        self.label_performance.setEnabled(True)
        self.label_performance.setGeometry(QtCore.QRect(830, 15, 90, 90))
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
        self.label_performance_text.setGeometry(QtCore.QRect(660, 40, 380, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_performance_text.setFont(font)
        self.label_performance_text.setScaledContents(True)
        self.label_performance_text.setWordWrap(True)
        self.label_performance_text.setObjectName("label_performance_text")
        self.comboBox_choose_video = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_choose_video.setGeometry(QtCore.QRect(110, 390, 270, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_choose_video.setFont(font)
        self.comboBox_choose_video.setObjectName("comboBox_choose_video")
        self.plot_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.plot_tabWidget.setGeometry(QtCore.QRect(650, 370, 770, 430))
        self.plot_tabWidget.setStyleSheet("border-top:1px solid;\n"
"border-left:1px solid;\n"
"border-right:1px solid;\n"
"border-bottom:1px  solid;")
        self.plot_tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.plot_tabWidget.setDocumentMode(True)
        self.plot_tabWidget.setTabsClosable(False)
        self.plot_tabWidget.setTabBarAutoHide(False)
        self.plot_tabWidget.setObjectName("plot_tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.plot_label1 = QtWidgets.QLabel(self.tab1)
        self.plot_label1.setGeometry(QtCore.QRect(140, 10, 500, 380))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.plot_label1.setFont(font)
        self.plot_label1.setStyleSheet("border-top:1px ;\n"
"border-left:1px ;\n"
"border-right:1px ;\n"
"border-bottom:1px ;")
        self.plot_label1.setScaledContents(True)
        self.plot_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.plot_label1.setObjectName("plot_label1")
        self.plot_tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.plot_label2 = QtWidgets.QLabel(self.tab2)
        self.plot_label2.setGeometry(QtCore.QRect(140, 10, 500, 380))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.plot_label2.setFont(font)
        self.plot_label2.setStyleSheet("border-top:1px ;\n"
"border-left:1px ;\n"
"border-right:1px ;\n"
"border-bottom:1px ;")
        self.plot_label2.setScaledContents(True)
        self.plot_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.plot_label2.setObjectName("plot_label2")
        self.plot_tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.plot_label3 = QtWidgets.QLabel(self.tab3)
        self.plot_label3.setGeometry(QtCore.QRect(140, 10, 500, 380))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.plot_label3.setFont(font)
        self.plot_label3.setStyleSheet("border-top:1px ;\n"
"border-left:1px ;\n"
"border-right:1px ;\n"
"border-bottom:1px ;")
        self.plot_label3.setScaledContents(True)
        self.plot_label3.setAlignment(QtCore.Qt.AlignCenter)
        self.plot_label3.setObjectName("plot_label3")
        self.plot_tabWidget.addTab(self.tab3, "")
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.plot_label4 = QtWidgets.QLabel(self.tab4)
        self.plot_label4.setGeometry(QtCore.QRect(140, 10, 500, 380))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.plot_label4.setFont(font)
        self.plot_label4.setStyleSheet("border-top:1px ;\n"
"border-left:1px ;\n"
"border-right:1px ;\n"
"border-bottom:1px ;")
        self.plot_label4.setScaledContents(True)
        self.plot_label4.setAlignment(QtCore.Qt.AlignCenter)
        self.plot_label4.setObjectName("plot_label4")
        self.plot_tabWidget.addTab(self.tab4, "")
        self.button_plot_result = QtWidgets.QPushButton(self.centralwidget)
        self.button_plot_result.setGeometry(QtCore.QRect(130, 300, 235, 60))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_plot_result.setFont(font)
        self.button_plot_result.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(190, 184, 171);\n"
"border-radius: 20px;\n"
"border: 1px groove gray;\n"
"border-style:outset;\n"
"")
        self.button_plot_result.setObjectName("button_plot_result")
        self.label_efficeiency_text = QtWidgets.QLabel(self.centralwidget)
        self.label_efficeiency_text.setEnabled(True)
        self.label_efficeiency_text.setGeometry(QtCore.QRect(660, 120, 380, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_efficeiency_text.setFont(font)
        self.label_efficeiency_text.setScaledContents(True)
        self.label_efficeiency_text.setWordWrap(True)
        self.label_efficeiency_text.setObjectName("label_efficeiency_text")
        self.label_surgery_time = QtWidgets.QLabel(self.centralwidget)
        self.label_surgery_time.setGeometry(QtCore.QRect(700, 190, 260, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_surgery_time.setFont(font)
        self.label_surgery_time.setScaledContents(True)
        self.label_surgery_time.setWordWrap(True)
        self.label_surgery_time.setObjectName("label_surgery_time")
        self.label_total_interrupt_time = QtWidgets.QLabel(self.centralwidget)
        self.label_total_interrupt_time.setGeometry(QtCore.QRect(700, 240, 260, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_total_interrupt_time.setFont(font)
        self.label_total_interrupt_time.setScaledContents(True)
        self.label_total_interrupt_time.setWordWrap(True)
        self.label_total_interrupt_time.setObjectName("label_total_interrupt_time")
        self.label_efficiency = QtWidgets.QLabel(self.centralwidget)
        self.label_efficiency.setEnabled(True)
        self.label_efficiency.setGeometry(QtCore.QRect(830, 100, 90, 90))
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
        self.label_ratio.setGeometry(QtCore.QRect(1000, 190, 371, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ratio.setFont(font)
        self.label_ratio.setScaledContents(True)
        self.label_ratio.setWordWrap(True)
        self.label_ratio.setObjectName("label_ratio")
        self.label_unit_interrupt_counts = QtWidgets.QLabel(self.centralwidget)
        self.label_unit_interrupt_counts.setGeometry(QtCore.QRect(1000, 240, 371, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_unit_interrupt_counts.setFont(font)
        self.label_unit_interrupt_counts.setScaledContents(True)
        self.label_unit_interrupt_counts.setWordWrap(True)
        self.label_unit_interrupt_counts.setObjectName("label_unit_interrupt_counts")
        self.button_start_judge.raise_()
        self.button_choose_video.raise_()
        self.label_video_name.raise_()
        self.label_interrupt_times.raise_()
        self.list_widget_interrupt.raise_()
        self.button_remove_interrupt.raise_()
        self.label_done.raise_()
        self.comboBox_choose_video.raise_()
        self.plot_tabWidget.raise_()
        self.button_plot_result.raise_()
        self.label_efficeiency_text.raise_()
        self.label_surgery_time.raise_()
        self.label_total_interrupt_time.raise_()
        self.label_ratio.raise_()
        self.label_unit_interrupt_counts.raise_()
        self.label_performance_text.raise_()
        self.label_performance.raise_()
        self.label_efficiency.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.plot_tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_start_judge.setText(_translate("MainWindow", "❗開始偵測❗"))
        self.button_choose_video.setText(_translate("MainWindow", "👆🏻 選擇資料夾 👆🏻"))
        self.label_video_name.setText(_translate("MainWindow", "資料夾名稱:   尚未選擇資料夾"))
        self.label_interrupt_times.setText(_translate("MainWindow", "總中斷次數:   尚未進行偵測"))
        self.button_remove_interrupt.setText(_translate("MainWindow", "刪除此中斷點 ❌"))
        self.label_performance_text.setText(_translate("MainWindow", "中斷次數評分:   尚未進行偵測"))
        self.plot_label1.setText(_translate("MainWindow", "尚未引入數據!"))
        self.plot_tabWidget.setTabText(self.plot_tabWidget.indexOf(self.tab1), _translate("MainWindow", "總手術時間"))
        self.plot_label2.setText(_translate("MainWindow", "尚未引入數據!"))
        self.plot_tabWidget.setTabText(self.plot_tabWidget.indexOf(self.tab2), _translate("MainWindow", "總中斷時間"))
        self.plot_label3.setText(_translate("MainWindow", "尚未引入數據!"))
        self.plot_tabWidget.setTabText(self.plot_tabWidget.indexOf(self.tab3), _translate("MainWindow", "總中斷次數"))
        self.plot_label4.setText(_translate("MainWindow", "尚未引入數據!"))
        self.plot_tabWidget.setTabText(self.plot_tabWidget.indexOf(self.tab4), _translate("MainWindow", "中斷時間/總手術時間比例 "))
        self.button_plot_result.setText(_translate("MainWindow", "顯示近五次結果圖 📊"))
        self.label_efficeiency_text.setText(_translate("MainWindow", "效率評分:   尚未進行偵測"))
        self.label_surgery_time.setText(_translate("MainWindow", "總手術時間:   尚未進行偵測"))
        self.label_total_interrupt_time.setText(_translate("MainWindow", "總中斷時間:   尚未進行偵測"))
        self.label_ratio.setText(_translate("MainWindow", "中斷時間佔整個手術時間的比例:   尚未進行偵測"))
        self.label_unit_interrupt_counts.setText(_translate("MainWindow", "平均每九分鐘的中斷次數:   尚未進行偵測"))
