import sys
from PyQt6.QtWidgets import QApplication
import window

app = QApplication(sys.argv)
win = window.MainWindow()
win.show()
app.exec()
