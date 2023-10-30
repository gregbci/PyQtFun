from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout

from PyQtFun.T2SModel import T2SModel


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self, model: T2SModel):
        super().__init__()

        self.model = model
        self.model.trainingStarted.connect(self.display_training_start)
        self.model.trainingCompleted.connect(self.display_training_count)

        self.setWindowTitle("PyQtFun")

        button = QPushButton("Train")
        button.clicked.connect(self.model.start_training)

        self.label = QLabel("Press Train!")

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.label)

        main = QWidget()
        main.setLayout(layout)

        self.setCentralWidget(main)

    @QtCore.pyqtSlot()
    def display_training_start(self):
        self.label.setText("training...")

    @QtCore.pyqtSlot(int)
    def display_training_count(self, count):
        self.label.setText(str(count))
