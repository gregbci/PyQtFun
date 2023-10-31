import threading
from PyQt6.QtCore import pyqtSignal, QObject

from .MainView import MainView


# Controller (or presenter if you prefer) that connects the view to a model.
# The model doesn't really exist in this example, see _train() which pretends to
# do some training before emitting an event when done.
#
# More info here: https://wiki.qt.io/Model-View-Presenter(MVP)_Design_Pattern_in_Qt_Application
#
class TrainingController(QObject):
    trainingStarted = pyqtSignal()
    trainingCountChanged = pyqtSignal(int)

    def __init__(self, mainView: MainView):
        super().__init__()

        self.mainView = mainView
        self.trainingCount = 0
        self.initializeView()

    def initializeView(self):
        self.trainingStarted.connect(self.mainView.display_training_start)
        self.trainingCountChanged.connect(self.mainView.display_training_count)
        self.mainView.button.clicked.connect(self._start_training)

    def showView(self):
        self.mainView.show()

    def _start_training(self):
        # emit a signal when training "starts"
        self.trainingStarted.emit()
        self._train()

    def _training_complete(self):
        self.trainingCount += 1
        self.trainingCountChanged.emit(self.trainingCount)

    def _train(self):
        # This is the "model", in reality, this would be another object or set of objects
        # that are coordinated by TrainingController.

        # Pretend to "train", then emit a signal when complete
        threading.Timer(1, self._training_complete).start()
