from PyQt5 import QtCore, QtGui, QtWidgets

def ui_show(UI):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
   # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())