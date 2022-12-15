import sys
# from PyQt5.QtCore import (Qt, QModelIndex, QAbstractTableModel)
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *

from assignMember import *




class TableViewTestModel(QtCore.QAbstractTableModel):
    def __init__(self, members: list[Person], parent=None):
        super().__init__(parent)
        self.members = members

    def data(self, index: QtCore.QModelIndex, role: int):
        if role == QtCore.Qt.EditRole or role == QtCore.Qt.ItemDataRole.DisplayRole:
            return self.members[index.row()].jobPerDay[index.column()+1]
            # return str(index.row())+ ':' +str(index.column())
        return QtCore.QVariant()

    def rowCount(self, parent=QtCore.QModelIndex()) -> int:
        return len(self.members)

    def columnCount(self, parent=QtCore.QModelIndex()) -> int:
        return len(self.members[0].jobPerDay)

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.ItemDataRole.DisplayRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return Person.toHeader()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, members: list[Person]):
        super().__init__()
        rootWidget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()
        self.table = QtWidgets.QTableView()

        layout.addWidget(self.table)
        rootWidget.setLayout(layout)
        self.setCentralWidget(rootWidget)
        
        self.resize(1500, 800)

        self.table.setModel(TableViewTestModel(members))



ShiftDataReader.readConfigvar('radschedule\勤務表\data\configvar.dat')
members = ShiftDataReader.readStaffInfo('radschedule\勤務表\data\staffinfo.dat')
ShiftDataReader.applyShift2Member('radschedule\勤務表\data\shift.dat', members)




app = QtWidgets.QApplication(sys.argv)

testWindow = MainWindow(members)
testWindow.show()

sys.exit(app.exec_())





