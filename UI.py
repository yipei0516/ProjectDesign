# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
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
        MainWindow.resize(1500, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_start_judge = QtWidgets.QPushButton(self.centralwidget)
        self.button_start_judge.setGeometry(QtCore.QRect(150, 140, 220, 60))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_start_judge.setFont(font)
        self.button_start_judge.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(190, 184, 171);\n"
"border-radius: 20px;\n"
"border: 1px groove gray;\n"
"border-style:outset;")
        self.button_start_judge.setObjectName("button_start_judge")
        self.button_choose_video = QtWidgets.QPushButton(self.centralwidget)
        self.button_choose_video.setGeometry(QtCore.QRect(150, 60, 220, 60))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
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
        self.label_video_name.setGeometry(QtCore.QRect(60, 309, 380, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_video_name.setFont(font)
        self.label_video_name.setScaledContents(True)
        self.label_video_name.setWordWrap(True)
        self.label_video_name.setObjectName("label_video_name")
        self.label_interrupt_times = QtWidgets.QLabel(self.centralwidget)
        self.label_interrupt_times.setGeometry(QtCore.QRect(60, 370, 380, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_interrupt_times.setFont(font)
        self.label_interrupt_times.setScaledContents(True)
        self.label_interrupt_times.setWordWrap(True)
        self.label_interrupt_times.setObjectName("label_interrupt_times")
        self.list_widget_interrupt = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget_interrupt.setGeometry(QtCore.QRect(70, 450, 241, 351))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.list_widget_interrupt.setFont(font)
        self.list_widget_interrupt.setObjectName("list_widget_interrupt")
        self.button_play = QtWidgets.QPushButton(self.centralwidget)
        self.button_play.setGeometry(QtCore.QRect(920, 670, 60, 60))
        self.button_play.setStyleSheet("QPushButton {\n"
"        border: 0px solid;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: rgb(223, 223, 223);\n"
"    }\n"
"")
        self.button_play.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_play.setIcon(icon)
        self.button_play.setIconSize(QtCore.QSize(60, 60))
        self.button_play.setObjectName("button_play")
        self.button_pause = QtWidgets.QPushButton(self.centralwidget)
        self.button_pause.setGeometry(QtCore.QRect(1050, 670, 60, 60))
        self.button_pause.setStyleSheet("QPushButton {\n"
"        border: 0px solid;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: rgb(223, 223, 223);\n"
"    }\n"
"")
        self.button_pause.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_pause.setIcon(icon1)
        self.button_pause.setIconSize(QtCore.QSize(60, 60))
        self.button_pause.setObjectName("button_pause")
        self.label_videoplayer = QtWidgets.QLabel(self.centralwidget)
        self.label_videoplayer.setGeometry(QtCore.QRect(610, 110, 800, 450))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_videoplayer.setFont(font)
        self.label_videoplayer.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_videoplayer.setTextFormat(QtCore.Qt.AutoText)
        self.label_videoplayer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_videoplayer.setWordWrap(True)
        self.label_videoplayer.setObjectName("label_videoplayer")
        self.slider_videoframe = QtWidgets.QSlider(self.centralwidget)
        self.slider_videoframe.setGeometry(QtCore.QRect(580, 630, 651, 22))
        self.slider_videoframe.setOrientation(QtCore.Qt.Horizontal)
        self.slider_videoframe.setObjectName("slider_videoframe")
        self.label_frameinfo = QtWidgets.QLabel(self.centralwidget)
        self.label_frameinfo.setGeometry(QtCore.QRect(1250, 630, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.label_frameinfo.setFont(font)
        self.label_frameinfo.setObjectName("label_frameinfo")
        self.button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_stop.setGeometry(QtCore.QRect(780, 670, 60, 60))
        self.button_stop.setStyleSheet("QPushButton {\n"
"        border: 0px solid;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgb(223, 223, 223);\n"
"    }\n"
"")
        self.button_stop.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_stop.setIcon(icon2)
        self.button_stop.setIconSize(QtCore.QSize(60, 60))
        self.button_stop.setObjectName("button_stop")
        self.button_check_result = QtWidgets.QPushButton(self.centralwidget)
        self.button_check_result.setGeometry(QtCore.QRect(150, 230, 220, 60))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_check_result.setFont(font)
        self.button_check_result.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(190, 184, 171);\n"
"border-radius: 20px;\n"
"border: 1px groove gray;\n"
"border-style:outset;\n"
"")
        self.button_check_result.setObjectName("button_check_result")
        self.button_rewind = QtWidgets.QPushButton(self.centralwidget)
        self.button_rewind.setGeometry(QtCore.QRect(620, 670, 60, 60))
        self.button_rewind.setStyleSheet("QPushButton {\n"
"        border: 0px solid;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: rgb(223, 223, 223);\n"
"    }\n"
"")
        self.button_rewind.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/rewind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_rewind.setIcon(icon3)
        self.button_rewind.setIconSize(QtCore.QSize(60, 60))
        self.button_rewind.setObjectName("button_rewind")
        self.button_forward = QtWidgets.QPushButton(self.centralwidget)
        self.button_forward.setGeometry(QtCore.QRect(1190, 670, 60, 60))
        self.button_forward.setStyleSheet("QPushButton {\n"
"        border: 0px solid;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: rgb(223, 223, 223);\n"
"    }\n"
"")
        self.button_forward.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_forward.setIcon(icon4)
        self.button_forward.setIconSize(QtCore.QSize(60, 60))
        self.button_forward.setObjectName("button_forward")
        self.button_remove_interrupt = QtWidgets.QPushButton(self.centralwidget)
        self.button_remove_interrupt.setGeometry(QtCore.QRect(330, 750, 170, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_remove_interrupt.setFont(font)
        self.button_remove_interrupt.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius: 10px;\n"
"border: 1px groove gray;\n"
"border-style:outset;")
        self.button_remove_interrupt.setObjectName("button_remove_interrupt")
        self.button_import_result = QtWidgets.QPushButton(self.centralwidget)
        self.button_import_result.setGeometry(QtCore.QRect(370, 360, 220, 60))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_import_result.setFont(font)
        self.button_import_result.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(190, 184, 171);\n"
"border-radius: 20px;\n"
"border: 1px groove gray;\n"
"border-style:outset;\n"
"")
        self.button_import_result.setObjectName("button_import_result")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_start_judge.setText(_translate("MainWindow", "❗Start Judge❗"))
        self.button_choose_video.setText(_translate("MainWindow", "👆🏻 Choose Video 👆🏻"))
        self.label_video_name.setText(_translate("MainWindow", "Video Name: "))
        self.label_interrupt_times.setText(_translate("MainWindow", "Interrupt Times:"))
        self.label_videoplayer.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#908b81;\">📸</span><span style=\" font-size:20pt; text-decoration: underline; color:#908b81;\">Video Player</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#cf341c;\">Please choose a video first</span></p></body></html>"))
        self.label_frameinfo.setText(_translate("MainWindow", "current frame/total frame"))
        self.button_check_result.setText(_translate("MainWindow", "✅Check result✅"))
        self.button_remove_interrupt.setText(_translate("MainWindow", "remove interrupt ❌"))
        self.button_import_result.setText(_translate("MainWindow", "Import Result"))
