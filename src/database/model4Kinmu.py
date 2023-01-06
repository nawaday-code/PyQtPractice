
from PyQt5.QtCore import *
from lib.noMetaClassConfrict import classmaker
from util.dataSender import DataName

from util.shiftDataController import ShiftDataController
from Event.modelSubjectBase import ChangeDataGenerator, DataForm


class Model4Kinmu(QAbstractTableModel, ChangeDataGenerator):
    
    __metaclass__ = classmaker()

    def __init__(self, parent=None, shiftInfo: ShiftDataController = None):
        super().__init__(parent)
        self.kinmuDF = shiftInfo.getKinmuForm(DataName.kinmu)

    def data(self, index: QModelIndex, role: int):
        if role == Qt.ItemDataRole.EditRole or role == Qt.ItemDataRole.DisplayRole:
            return self.kinmuDF.iat[index.row(), index.column()]
        return QVariant()

    def rowCount(self, parent=QModelIndex()) -> int:
        return self.kinmuDF.shape[0]

    def columnCount(self, parent=QModelIndex()) -> int:
        return self.kinmuDF.shape[1]

    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole:
            self.__changedIndex = index
            self.__changedValue = value
            self.notifyObseber()
            #変更後のデータをモデルDFに入れる
            self.kinmuDF.iat[index.row(), index.column()] = value #ここMemberDatabaseから引っ張ってくる
            print(
                f'データを編集しました。\n箇所: ({index.row()}, {index.column()})\n変更後: {value}')
            return True
        return False

    def getIndex(self):
        return self.__changedIndex

    def getValue(self):
        return self.__changedValue

    def getForm(self):
        return DataForm.kinmuDF