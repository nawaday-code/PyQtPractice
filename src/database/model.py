# QTableViewモデルで構築　モデルに入れるDataはPandas DataFrame
# 清水さんのプログラムもQTableViewを使用している

# data.pyは保存しておく。後々やっぱりpandasが使えない状況のために。
import logging

from PyQt5.QtCore import *


from util.datReader import CreateShiftInfo


class TestModel(QAbstractTableModel):
    shiftInfo: CreateShiftInfo

    def __init__(self, parent=None, shiftInfo=None):
        super().__init__(parent)
        self.shiftInfo = shiftInfo

    def data(self, index: QModelIndex, role: int):
        if role == Qt.ItemDataRole.EditRole or role == Qt.ItemDataRole.DisplayRole:
            return self.shiftInfo.members[index.row()].jobPerDay[self.shiftInfo.day_previous_next[index.column()]]
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
            self.shiftInfo.members[index.row(
            )].jobPerDay[self.shiftInfo.day_previous_next[index.column()]] = value
            print(
                f'データを編集しました。箇所：({index.row()}, {index.column()}) 変更後：{self.shiftInfo.members[index.row()].jobPerDay[self.shiftInfo.day_previous_next[index.column()]]}')
            return True
        return False
