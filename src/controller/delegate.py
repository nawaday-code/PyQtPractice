from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class modelEditDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(modelEditDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index) -> QWidget:
        return QLineEdit(parent) #本当はここで編集関数を呼び出したいが、戻り値が必ずQWidgetでないといけない

    def setEditorData(self, editor: QAbstractButton, index:QModelIndex):
        value = index.model().data(index, Qt.ItemDataRole.DisplayRole) #indexを頼りに、編集前データをとる
        editor.setText(value)

    def setModelData(self, editor: QAbstractButton, model, index):
        model.setData(index, editor.text())

        

