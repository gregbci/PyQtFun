import threading
from PyQt6.QtCore import pyqtSignal, QObject


# Dummy model for view to mess with
class T2SModel(QObject):
    trainingStarted = pyqtSignal()
    trainingCompleted = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self.trainingCount = 0

    def start_training(self):
        # emit a signal when training "starts"
        self.trainingStarted.emit()
        
        # emit a signal when training is "complete" after a delay
        threading.Timer(1, self.training_complete).start()

    def training_complete(self):
        self.trainingCount += 1
        self.trainingCompleted.emit(self.trainingCount)