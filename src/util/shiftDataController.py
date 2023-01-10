

from Event.modelSubjectBase import *
from Event.observer import Observer
from Event.changeLogger import MemberChangeLog
from Event.memberSubject import memberUpdateGenerator
from util.datReader import DatReader
from util.dataSender import DataSender


class ShiftController(DatReader, DataSender, MemberChangeLog):
    def __init__(self, rootPath):
        super().__init__(rootPath)
        generator = memberUpdateGenerator()
        # modelchangeObserver = ModelChangeObserver()
        # generator.addObserber(modelchangeObserver)
    
class MemberChangeObserver(Observer):
    def __init__(self, shiftControllerObj: ShiftController) -> None:
        super().__init__()
        self.shiftCtrlObj = shiftControllerObj
    
    def update(self, generator: memberUpdateGenerator):
        changedMemberElem = generator.getChangedElem()
        
        
        
        

# class ModelChangeObserver(Observer):
#     def update(self, generator: ChangeDataGenerator):
#         if generator.getForm() == DataForm.kinmuDF:
#             print(generator.getIndex())
#             print(generator.getValue())
#         elif generator.getForm() == DataForm.yakinDF:
#             print(generator.getIndex())
#             print(generator.getValue())
