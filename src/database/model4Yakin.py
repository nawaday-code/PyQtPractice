
from PyQt5.QtCore import *
from util.dataSender import DataName

from util.shiftDataController import ShiftDataController
from Event.modelSubjectBase import ChangeDataGenerator, DataForm

class Model4Yakin(QAbstractTableModel, ChangeDataGenerator):

    def __init__(self, parent=None, shiftInfo: ShiftDataController = None):
        super().__init__(parent)
        self.yakinDF = shiftInfo.getYakinForm()

    def data(self, index: QModelIndex, role: int):
        if role == Qt.ItemDataRole.EditRole or role == Qt.ItemDataRole.DisplayRole:
            return self.yakinDF.iat[index.row(), index.column()]
        return QVariant()

    def rowCount(self, parent=QModelIndex()) -> int:
        return self.yakinDF.shape[0]

    def columnCount(self, parent=QModelIndex()) -> int:
        return self.yakinDF.shape[1]

    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole:
            self.__changedIndex = index
            self.__changedValue = value
            self.notifyObseber()
            print(
                f'データを編集しました。\n箇所: ({index.row()}, {index.column()})\n変更後: {self.shiftInfo.members[index.row()].jobPerDay[self.shiftInfo.day_previous_next[index.column()]]}')
            
            return True
        return False

    def getIndex(self):
        return self.__changedIndex

    def getValue(self):
        return self.__changedValue

    def getForm(self):
        return DataForm.yakinDF
