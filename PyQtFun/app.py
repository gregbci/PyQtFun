import sys
from PyQt6.QtWidgets import QApplication
from PyQtFun.MainWindow import MainWindow


def start():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
