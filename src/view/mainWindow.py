import logging
from Event.observer import Observer
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from database.model4Kinmu import Model4Kinmu
from database.model4Yakin import Model4Yakin
from Event.memberSubject import memberUpdateGenerator

from util.shiftController import ShiftChannel


class MainWindow(QMainWindow):
    def __init__(self, view: QTableView, shiftChannel: ShiftChannel, delegate: QStyledItemDelegate):
        super().__init__()

        self.memberElemObserver = MemberElemObserver(
            Model4Kinmu(shiftCtrlChannel=shiftChannel), Model4Yakin(shiftCtrlChannel=shiftChannel))

        shiftChannel.addObserber(self.memberElemObserver)

        self.view = view
        self.delegate = delegate

        self.view.setModel(self.memberElemObserver.kinmuModel)  # とりあえず
        self.view.setItemDelegate(self.delegate)
        self.setCentralWidget(self.view)

        self.resize(1500, 800)


class MemberElemObserver(Observer):
    def __init__(self, kinmuModel: Model4Kinmu, yakinModel: Model4Yakin) -> None:
        super().__init__()
        self.kinmuModel = kinmuModel
        self.yakinModel = yakinModel

    def update(self, generator: memberUpdateGenerator):
        self.kinmuModel.updateDF(generator.getKinmuDF())
        self.yakinModel.updateDF(generator.getYakinDF())
