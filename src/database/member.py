from dataclasses import dataclass
import datetime

@dataclass(slots=True)
class Person:

    # 個人の情報
    uid: int
    staffid: str
    name: str
    jobPerDay: dict
    requestPerDay : dict

    def __init__(self, uid: int, staffid: str, name: str) -> None:
        self.uid = uid
        self.staffid = staffid
        self.name = name
        self.jobPerDay = {}
        self.requestPerDay = {}


@dataclass(slots=True)
class Members:
    members: list[Person]

    # 全職員で共通な情報
    # (year, month, day, dayofweek) のtupleにする
    date: datetime
    #                        [( 年,  月,  日, 曜日)]
    previous_month: list[tuple[int, int, int, int]]
    now_month: list[tuple[int, int, int, int]]
    next_month: list[tuple[int, int, int, int]]
    day_previous_next: list[tuple[int, int, int, int]]

    def __init__(self):
        self.members = []

    def addMember(self, person: Person):
        self.members.append(person)
        




