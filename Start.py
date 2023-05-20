from PyQt5 import QtWidgets

from MenuController import Menu_controller

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Menu_controller()
    window.show()
    sys.exit(app.exec_())