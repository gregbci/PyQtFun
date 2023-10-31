import sys
from PyQt6.QtWidgets import QApplication
from .MainView import MainView
from .TrainingController import TrainingController


def start():
    app = QApplication(sys.argv)

    # inject model into view
    view = MainView()
    controller = TrainingController(view)

    # start application
    controller.showView()
    app.exec()
