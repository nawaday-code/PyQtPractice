import logging

from PyQt5.QtCore import *

from util.shiftDataController import ShiftDataController
from util.valueEditor import ModelDataEditor


class TestModel(QAbstractTableModel):
    shiftInfo: ShiftDataController

    def __init__(self, parent=None, shiftInfo=None):
        super().__init__(parent)
        self.shiftInfo = shiftInfo

    def data(self, index: QModelIndex, role: int):
        if role == Qt.ItemDataRole.EditRole or role == Qt.ItemDataRole.DisplayRole:
            
            return self.shiftInfo.members[list(self.shiftInfo.members.keys())[index.row()]].jobPerDay[self.shiftInfo.day_previous_next[index.column()]]
        return QVariant()

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.shiftInfo.members)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self.shiftInfo.day_previous_next)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self.shiftInfo.toHeader()[section]

    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole:
            ModelDataEditor.preValue = value
            self.shiftInfo.members[list(self.shiftInfo.members.keys())[index.row(
            )]].jobPerDay[self.shiftInfo.day_previous_next[index.column()]] = ModelDataEditor.getPostValue()
            print(
                f'データを編集しました。\n箇所: ({index.row()}, {index.column()})\n変更後: {self.shiftInfo.members[index.row()].jobPerDay[self.shiftInfo.day_previous_next[index.column()]]}')
            return True
        return False
