import logging
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, view: QTableView, model: QAbstractTableModel, delegate: QStyledItemDelegate):
        super().__init__()

        self.view = view
        self.model = model
        self.delegate = delegate

        self.view.setModel(self.model)
        self.view.setItemDelegate(self.delegate)
        self.setCentralWidget(self.view)

        self.resize(1500, 800)

