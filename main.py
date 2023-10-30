import sys
from PyQt6.QtWidgets import QApplication
from window import MainWindow

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()
