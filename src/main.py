import sys
from util.dataSender import DataName


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
    return 'str限定です'

ModelDataEditor.callbackFunc = myFunc
delegate = modelEditDelegate()



shiftInfo.getKinmuForm(DataName.kinmu)
shiftInfo.getStaffInfo()
shiftInfo.getYakinForm()
shiftInfo.getDf4Iwasaki()

testWindow = MainWindow(view, model, delegate)
testWindow.show()

sys.exit(app.exec_())
