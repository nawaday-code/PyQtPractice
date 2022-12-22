from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import logging
from database.datReader import *

logging.basicConfig(filename='log/pyqt.log', level=logging.DEBUG)


# dataframeを受け取って表示するようにする
# roleをeditableにして編集してみる


class TestModel(QtCore.QAbstractTableModel):
    shiftInfo: CreateShiftInfo

    def __init__(self, parent=None, shiftInfo=None):
        super().__init__(parent)
        self.shiftInfo = shiftInfo

    def data(self, index: QtCore.QModelIndex, role: int):
        if role == QtCore.Qt.ItemDataRole.EditRole or role == QtCore.Qt.ItemDataRole.DisplayRole:
            return self.shiftInfo.members[index.row()].jobPerDay[self.shiftInfo.day_previous_next[index.column()]]
        return QtCore.QVariant()

    def rowCount(self, parent=QtCore.QModelIndex()) -> int:
        return len(self.shiftInfo.members)

    def columnCount(self, parent=QtCore.QModelIndex()) -> int:
        return len(self.shiftInfo.day_previous_next)

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.ItemDataRole.DisplayRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return self.shiftInfo.toHeader()[section]

    def flags(self, index):
        return QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsEditable


class TestView(QtWidgets.QTableView):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, shiftInfo: CreateShiftInfo):
        super().__init__()

        self.view = TestView(self)
        self.model = TestModel(self, shiftInfo=shiftInfo)
        self.view.setModel(self.model)
        self.setCentralWidget(self.view)

        self.resize(1500, 800)
        
        delButton = QPushButton('取得')
        


    def selectedCell(self):
        logging.debug(self.view.selectedIndexes())
