from dataclasses import dataclass
import datetime
import locale

@dataclass(slots=True)
class Person:

    # 個人の情報
    uid: int
    staffid: str
    name: str
    jobPerDay: dict

    def __init__(self, uid: int, staffid: str, name: str) -> None:
        self.uid = uid
        self.staffid = staffid
        self.name = name
        self.jobPerDay = {}


@dataclass(slots=True)
class Members:
    members: list[Person]

    # 全職員で共通な情報
    # (year, month, day, dayofweek) のtupleにする
    date: datetime
    previous_month: list[tuple[int, int, int, int]]
    now_month: list[tuple[int, int, int, int]]
    next_month: list[tuple[int, int, int, int]]
    #                           [( 年,  月,  日, 曜日)]
    day_previous_next: list[tuple[int, int, int, int]]

    def __init__(self):
        self.members = []

    def addMember(self, person: Person):
        self.members.append(person)

    def getDf4Shimizu(self):

        pass

    def getDf4Honda(self):
        """
            日付-veriant  日付 (yyyy-mm-dd)  日付+1
        UID 勤務(Not int)
            無いときはNone

            日付-veriant  日付               日付+1
        UID request(Not int)  request
            無いときはNone

            UID 職員ID name depf(モダリティ)
        UID
        """
        pass

    def getDf4Iwasaki(self):
        pass

    def toHeader(self) -> list[str]:
        locale.setlocale(locale.LC_TIME, 'ja_JP')
        return [datetime.date(*yyyymmddww[:3]).strftime('%x')+datetime.date(*yyyymmddww[:3]).strftime('%a')
                for yyyymmddww in self.day_previous_next]
