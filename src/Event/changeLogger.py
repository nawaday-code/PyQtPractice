from PyQt5.QtCore import QModelIndex


from Event.memberSubject import memberUpdateGenerator
from database.member import Members


class MemberChangeLog(Members, memberUpdateGenerator):

    changeLog: list[dict[str:QModelIndex, str:str, str:str]]

    def __init__(self):
        super(MemberChangeLog, self).__init__()
        self.changeLog = []

    def updateMember(self, index: QModelIndex, value, fromClass):
        print(f'row:{index.row()}, column:{index.column()}, value:{value}, from:{fromClass}')
        """
        <<fromClass: Model4Kinmu>>
        index.column() -> uid
        index.row() -> day
        value -> job
        """
        if fromClass == "Model4Kinmu":
            self.changeLog.append(
                {'uid': index.column(), 'day': index.row(), 'job': value})
            self.members[self.changeLog[-1]['uid']
                         ].jobPerDay[self.day_previous_next[int(self.changeLog[-1]['day'])]] = self.changeLog[-1]['job']

    def getChangedElem(self) -> dict[str:QModelIndex, str:str, str:str]:
        return self.changeLog[-1]
    
    def getIndex(self):
        row = 0
        column = 0
        return (row, column)
