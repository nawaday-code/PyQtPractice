import calendar
import datetime
import logging
from enum import Enum

from database.member import *
from decorator.validate import *

logging.basicConfig(filename='log/data.log', level=logging.DEBUG)

# .datファイルを元に職員情報をもったオブジェクトを生成する


class DatNames(Enum):
    configvar = 'configvar.dat'
    staffinfo = 'staffinfo.dat'
    converttable = 'converttable.dat'
    shift = 'shift.dat'
    request = 'request.dat'
    previous = 'previous.dat'


class DatReader(Members):

    def __init__(self, rootPath: str):
        super().__init__()
        self.rootPath = rootPath
        self.readConfigvar()
        self.readStaffInfo()
        self.applyShift2Member()

    def readConfigvar(self, datPath: str = ''):
        if (datPath == ''):
            datPath: str = self.rootPath + "\\" + DatNames.configvar.value
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
        self.previous_month = [datetuple for datetuple in cal.itermonthdays4(
            self.date.year, self.date.month-1) if datetuple[1] == self.date.month - 1]
        self.now_month = [datetuple for datetuple in cal.itermonthdays4(
            self.date.year, self.date.month) if datetuple[1] == self.date.month]
        self.next_month = [datetuple for datetuple in cal.itermonthdays4(
            self.date.year, self.date.month+1) if datetuple[1] == self.date.month + 1]

        self.day_previous_next = self.previous_month + self.now_month + [self.next_month[0]]

    def readStaffInfo(self, datPath: str = ''):

        if (datPath == ''):
            datPath: str = self.rootPath + "\\" + DatNames.staffinfo.value
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

        self.dat2Member(DatNames.shift, self.now_month)
        self.dat2Member(DatNames.previous, self.previous_month)
        self.dat2Member(DatNames.request, self.now_month)

        return self

    def dat2Member(self, readDatName: DatNames, month_calendar: list[tuple[int, int, int, int]], optionPathSetting=''):
        if (optionPathSetting == ''):
            path: str = self.rootPath + "\\" + readDatName.value
        readingDat = open(path, 'r', encoding='utf-8-sig')

        for datRow in readingDat:
            try:
                uid, day, job = datRow.rstrip('\n').split(',')
                # ここで得たdayは(yyyy, mm, dd, ww)に変換
                # dayの'-（マイナス）'データはindex指定として扱えば上手くいくはず
                date = month_calendar[int(day)]
                if not date in self.day_previous_next:
                    raise damagedDataError

            except damagedDataError as ex:
                print(
                    '*.datのdayがカレンダーと一致しませんでした。\n詳細: {ex}\nスキップして次を読み込みます...')
                continue

            except ValueError as ex:
                print(f'異常なデータがありました\n詳細: {ex}\nスキップして次を読み込みます...')
                continue

            # ここforで回さずに検索でマッチングできないか？
            for person in self.members:
                if int(uid) == person.uid:
                    if readDatName == DatNames.shift or readDatName == DatNames.previous:
                        person.jobPerDay[date] = job
                    elif readDatName == DatNames.request:
                        person.requestPerDay[date] = job
        readingDat.close()
