import sys


from util.datReader import *
from view.mainWindow import MainWindow
from view.view import *
from database.model import TestModel
from controller.delegate import modelEditDelegate


app = QtWidgets.QApplication(sys.argv)
shiftInfo = CreateShiftInfo('data')
view = TestView()
model = TestModel(shiftInfo=shiftInfo)
delegate = modelEditDelegate()

testWindow = MainWindow(view, model, delegate)
testWindow.show()

sys.exit(app.exec_())
