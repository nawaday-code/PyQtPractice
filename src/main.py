import sys


from util.shiftDataController import ShiftDataController
from util.valueEditor import ModelDataEditor
from view.mainWindow import MainWindow
from view.view import *
from database.model import TestModel
from controller.delegate import modelEditDelegate


app = QtWidgets.QApplication(sys.argv)
shiftInfo = ShiftDataController('data')
view = TestView()
model = TestModel(shiftInfo=shiftInfo)

def myFunc()->str:
    print('オリジナル編集有効化')
    return ModelDataEditor.preValue + 'だと思う'

ModelDataEditor.callbackFunc = myFunc
delegate = modelEditDelegate()

shiftInfo.getKinmuDf()

testWindow = MainWindow(view, model, delegate)
testWindow.show()

sys.exit(app.exec_())
