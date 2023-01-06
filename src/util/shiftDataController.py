from Event.modelSubjectBase import *
from Event.observer import Observer
from util.datReader import DatReader
from util.dataSender import DataSender


class ShiftDataController(DatReader, DataSender):
    def __init__(self, rootPath):
        super().__init__(rootPath)
        generator = ChangeDataGenerator()
        modelchangeObserver = ModelChangeObserver()
        generator.addObserber(modelchangeObserver)
        

class ModelChangeObserver(Observer):
    def update(self, generator: ChangeDataGenerator):
        if generator.getForm() == DataForm.kinmuDF:
            print(generator.getIndex())
            print(generator.getValue())
        elif generator.getForm() == DataForm.yakinDF:
            print(generator.getIndex())
            print(generator.getValue())
