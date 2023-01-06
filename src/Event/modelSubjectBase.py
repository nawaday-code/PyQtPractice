

from abc import ABCMeta, abstractmethod
from enum import Enum, auto

from Event.observer import Observer

class DataForm(Enum):
    kinmuDF = auto()
    yakinDF = auto()
    member = auto()

class ChangeDataGenerator(metaclass=ABCMeta):
    """
    docstring
    """

    def __init__(self) -> None:
        self.__observers:list[Observer] = []  # __を付けることでprivate変数にできる

    def addObserber(self, observer) -> None:
        self.__observers.append(observer)

    def removeObserber(self, observer) -> None:
        self.__observers.remove(observer)

    def notifyObseber(self):
        for observer in self.__observers:
            observer.update(self)

    @abstractmethod
    def getIndex(self):
        pass

    @abstractmethod
    def getValue(self):
        pass
    
    @abstractmethod
    def getForm(self):
        pass
