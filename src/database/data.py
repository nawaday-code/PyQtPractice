import calendar
import datetime
from dataclasses import dataclass
from enum import Enum

import pandas as pd

from decorator.validate import *

# .datファイルを元に職員情報をもったオブジェクトを生成する


class datNames(Enum):
    configvar = 'configvar.dat'
    staffinfo = 'staffinfo.dat'
    converttable = 'converttable.dat'
    shift = 'shift.dat'
    request = 'request.dat'
    previous = 'previous.dat'


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
    # 先月分データなどがあるため、a_month_daysは変更するべき。
    # (year, month, day, dayofweek) のtupleにする
    date: datetime
    #                           [( 年,  月,  日, 曜日)]
    day_previous_next: list[tuple[int, int, int, int]]

    # a_month_calendar: list[list[int]] #つかわない
    # a_month_days: list[int]

    def __init__(self):
        self.members = []
        self.date = None
        self.day_previous_next = None

        # self.a_month_calendar = None
        # self.a_month_days = None

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

    # 今は要らなそうだけど、後々ヘッダー用に簡単に編集できるように
    def toHeader(self):
        return self.day_previous_next


class CreateShiftInfo(Members):
    rootPath: str

    def __init__(self, rootPath: str):
        super().__init__()
        self.rootPath = rootPath
        self.readConfigvar()
        self.readStaffInfo()
        self.applyShift2Member()

    def readConfigvar(self, datPath: str = ''):
        if (datPath == ''):
            datPath: str = self.rootPath + "\\" + datNames.configvar.value
        inputData = open(datPath, 'r', encoding='utf-8-sig')
        data = {}
        # 次のようなデータ構造を想定しています
        """
        date,2023/04/01
        kappa,150
        iota,12
        myu,8
        nyu,3,0,0
        rho,3
        epsilon,5
        lambda,0.1,0.01,0.01,0.001,0.1
        """
        for rows in inputData:
            elem = rows.rstrip('\n').split(',')
            data[elem[0]] = elem[1:]

        inputData.close()

        # 日付データを設定
        self.date: datetime.datetime = datetime.datetime.strptime(
            *data['date'], '%Y/%m/%d')
        cal = calendar.Calendar()
        previous = [datetuple for datetuple in cal.itermonthdays4(self.date.year, self.date.month-1)]
        now = [datetuple for datetuple in cal.itermonthdays4(self.date.year, self.date.month)]
        next = [datetuple for datetuple in cal.itermonthdays4(self.date.year, self.date.month+1)]

        self.day_previous_next = previous + now + next
        # self.day_previous_next = list(set(
        #     [datetuple for datetuple in cal.itermonthdays4(self.date.year, self.date.month-1)].extend(
        #         [datetuple for datetuple in cal.itermonthdays4(self.date.year, self.date.month)].extend(
        #             [datetuple for datetuple in cal.itermonthdays4(self.date.year, self.date.month+1)]))))

        # self.a_month_calendar = calendar.monthcalendar(
        #     self.date.year, self.date.month)
        # self.a_month_days = [
        #     day for week in self.a_month_calendar for day in week if day > 0]

    def readStaffInfo(self, datPath: str = ''):

        if (datPath == ''):
            datPath: str = self.rootPath + "\\" + datNames.staffinfo.value
        inputData = open(datPath, 'r', encoding='utf-8-sig')
        # 次のようなデータ構造を想定しています
        """
        uid, staffid, name
        2,R04793,小川智
        4,055236,戸高秀晴
        5,059247,福井浩
        6,067607,佐藤雄喜
        7,076610,川嶋康裕
        8,078321,池田秀
        9,090668,笠原賢治
        10,090670,高橋直紀
        11,109876,平田聡
        """

        for rows in inputData:
            if (len(rows.rstrip('\n').split(',')) == 3):
                uid, staffid, name = rows.rstrip('\n').split(',')
                self.addMember(Person(int(uid), staffid, name))

        inputData.close()

    # 先月分とrequestは一括読み込みして、一部分だけほしいときは切り取るやり方にします
    @Validater.validJobPerDay
    def applyShift2Member(self, shiftPath: str = '', previousPath: str = '', requestPath: str = ''):
        # 次のようなデータ構造を想定しています
        """
        uid, day, job
        2,0,63
        2,1,10
        2,2,8
        2,3,8
        2,4,8
        2,5,8
        2,6,8
        """

        if (shiftPath == ''):
            shiftPath: str = self.rootPath + "\\" + datNames.shift.value
        if (previousPath == ''):
            previousPath: str = self.rootPath + "\\" + datNames.previous.value
        if (requestPath == ''):
            requestPath: str = self.rootPath + "\\" + datNames.request.value
        
        self.dat2Member(shiftPath)
        self.dat2Member(previousPath)
        self.dat2Member(requestPath)

        return self

    def dat2Member(self, path:str):
        readDat = open(path, 'r', encoding='utf-8-sig')
        for datRow in readDat:
            uid, day, job = datRow.rstrip('\n').split(',')
            # ここで得たdayは(yyyy, mm, dd, ww)に変換
            try:
                date = self.day2yyyymmddww(day)
                if not date in self.day_previous_next:
                    raise damagedDataError
            except damagedDataError as _ex:
                print('*.batのday部分に異常値がある恐れがあります。')
                print(f'day部分変換後: {date}')
                print('勤務データの格納に失敗しました。')

            # ここforで回さずに検索でマッチングできないか？
            for person in self.members:
                if int(uid) == person.uid:
                    person.jobPerDay[date] = int(job)
        readDat.close()

    def day2yyyymmddww(self, day) -> tuple[int, int, int, int]:
        print(day)
        yyyymmdd = (self.date.year, self.date.month, int(day)+1)
        return (*yyyymmdd, datetime.date(*yyyymmdd).weekday())
