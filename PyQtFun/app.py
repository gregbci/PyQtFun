import sys
from PyQt6.QtWidgets import QApplication
from PyQtFun.MainWindow import MainWindow
from PyQtFun.T2SModel import T2SModel


def start():
    app = QApplication(sys.argv)

    # inject model into view
    model = T2SModel()
    win = MainWindow(model)

    # start application
    win.show()
    app.exec()
