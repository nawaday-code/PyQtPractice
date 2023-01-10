import logging
import sys
from database.model4Kinmu import Model4Kinmu


from util.shiftDataController import ShiftController
from view.mainWindow import MainWindow
from view.view import *
from controller.delegate import modelEditDelegate


app = QtWidgets.QApplication(sys.argv)
shiftInfo = ShiftController('data')
view = TestView()
# model = TestModel(shiftInfo=shiftInfo)


# def myFunc()->str:
#     print('オリジナル編集有効化')
#     return ModelDataEditor.preValue + 'だと思う'

# ModelDataEditor.callbackFunc = myFunc

model = Model4Kinmu(shiftInfo=shiftInfo)
delegate = modelEditDelegate()

testWindow = MainWindow(view, model, delegate)
testWindow.show()

sys.exit(app.exec_())
