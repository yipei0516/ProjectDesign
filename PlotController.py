from PyQt5 import QtWidgets, QtGui, QtCore
from Ui_Plot import Ui_Form
import MenuController
from Plot import Plot


class Plot_controller(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # qimage = image.show_image_on_label("./image/surgery1.png")
        # self.ui.label_background.setPixmap(qimage)
        # self.ui.label_background.lower()
        # op = QtWidgets.QGraphicsOpacityEffect()
        # op.setOpacity(0.5)
        # self.ui.label_background.setGraphicsEffect(op)

        self.plotObject = Plot(ui=self.ui)
        has_FiveDaysData = self.plotObject.judge_fiveDays()
        if(has_FiveDaysData == True):
            self.plotObject.load_currentFiveDaysData()
        else:
            self.ui.plot_label1.setText("尚未集滿5天手術資料!")
            self.ui.plot_label2.setText("尚未集滿5天手術資料!")
            self.ui.plot_label3.setText("尚未集滿5天手術資料!")
            self.ui.plot_label4.setText("尚未集滿5天手術資料!")

        self.setup_control()

    def setup_control(self):
        self.ui.button_back_menu.clicked.connect(self.back_menu)


    def back_menu(self):
        self.hide()
        self.result_window = MenuController.Menu_controller()
        self.result_window.show()