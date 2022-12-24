import logging
from PyQt5 import QtWidgets

from view.view import TestView
from database.model import TestModel
from controller.delegate import modelEditDelegate


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, view: TestView, model: TestModel, delegate: modelEditDelegate):
        super().__init__()

        self.view = view
        self.model = model
        self.delegate = delegate

        self.view.setModel(self.model)
        self.view.setItemDelegate(self.delegate)
        self.setCentralWidget(self.view)

        self.resize(1500, 800)

    def selectedCell(self):
        logging.debug(self.view.selectedIndexes())
