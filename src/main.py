import sys
# from PyQt5.QtCore import (Qt, QModelIndex, QAbstractTableModel)
from PyQt5 import QtWidgets

from database.datReader import *
from view.kinmuTable import *

app = QtWidgets.QApplication(sys.argv)
shiftInfo = CreateShiftInfo('data')
testWindow = MainWindow(shiftInfo)
testWindow.show()

sys.exit(app.exec_())
