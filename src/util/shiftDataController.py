from util.datReader import DatReader
from util.dataSender import DataSender


class ShiftDataController(DatReader, DataSender):
    def __init__(self, rootPath):
        super().__init__(rootPath)
