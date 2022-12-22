from PyQt5 import QtCore, QtWidgets

from database.data import *

# dataframeを受け取って表示するようにする
# roleをeditableにして編集してみる


class TableViewTestModel(QtCore.QAbstractTableModel):
    def __init__(self, shiftInfo: CreateShiftInfo, parent=None):
        super().__init__(parent)
        self.shiftInfo = shiftInfo

    def data(self, index: QtCore.QModelIndex, role: int):
        if role == QtCore.Qt.ItemDataRole.EditRole or role == QtCore.Qt.ItemDataRole.DisplayRole:
            # print(str(index.row())+ ':' +str(index.column()))
            return self.shiftInfo.members[index.row()].jobPerDay[self.shiftInfo.day_previous_next[index.column()]]

            # return str(index.row())+ ':' +str(index.column())
        return QtCore.QVariant()

    def rowCount(self, parent=QtCore.QModelIndex()) -> int:
        return len(self.shiftInfo.members)

    def columnCount(self, parent=QtCore.QModelIndex()) -> int:
        return len(self.shiftInfo.day_previous_next)

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.ItemDataRole.DisplayRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return self.shiftInfo.toHeader()[section]


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, shiftInfo: CreateShiftInfo):
        super().__init__()
        rootWidget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()
        self.table = QtWidgets.QTableView()

        layout.addWidget(self.table)
        rootWidget.setLayout(layout)
        self.setCentralWidget(rootWidget)

        self.resize(1500, 800)

        self.table.setModel(TableViewTestModel(shiftInfo))
