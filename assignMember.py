import calendar
import datetime
from dataclasses import dataclass

import pandas as pd



# from pathlib import Path

# .datファイルを元に職員情報をもったオブジェクトを生成する

# rootDataPath = Path('radschedule/勤務表/data')
# C:/Users/pelu0/Desktop/ShiftManager/configvar.dat
# "C:/Users/pelu0/Desktop/ShiftManager/staffinfo.dat"
# "C:/Users/pelu0/Desktop/ShiftManager/converttable.dat"
# "C:/Users/pelu0/Desktop/ShiftManager/shift.dat"
# "C:/Users/pelu0/Desktop/ShiftManager/request.dat"
# "C:/Users/pelu0/Desktop/ShiftManager/previous.dat"



#dataclassでslots機能を使って若干早くなった？デザインパターン的には変わっていない
@dataclass(slots=True)
class Person:
    # 全職員で共通な情報
    date: datetime
    a_month_calendar : list[list[int]]
    a_month_days : list[int]

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

    # 今は要らなそうだけど、後々ヘッダー用に簡単に編集できるように
    def toHeader():
        return Person.a_month_days

    def getData4Shimizu():
        #夜勤表表示用
        #openFile.py を見て
        pass

    def getData4Iwasaki():
        #勤務表カウント用
        #
        pass

    def getData4Honda():
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


# person = Person()



class ShiftDataReader:
    @staticmethod
    def readConfigvar(datPath: str):
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
        Person.date = datetime.datetime.strptime(*data['date'], '%Y/%m/%d')
        Person.a_month_calendar = calendar.monthcalendar(
            Person.date.year, Person.date.month)
        Person.a_month_days = [
            day for week in Person.a_month_calendar for day in week if day > 0]

    @staticmethod
    def readStaffInfo(datPath: str) -> list:
        inputData = open(datPath, 'r', encoding='utf-8-sig')
        members = []
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
            uid, staffid, name = rows.rstrip('\n').split(',')
            members.append(Person(int(uid), staffid, name))
        return members

    @staticmethod
    def applyShift2Member(datPath: str, members: list[Person]):
        inputData = open(datPath, 'r', encoding='utf-8-sig')
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
        for rows in inputData:
            uid, day, job = rows.rstrip('\n').split(',')
            for person in members:
                if int(uid) is person.uid:
                    person.jobPerDay[person.a_month_days[int(day)]] = int(
                        job)
        print(person.jobPerDay.keys())

    @staticmethod
    def applyShift2Member(datPath: str, members: list[Person]):
        inputData = open(datPath, 'r', encoding='utf-8-sig')
        df = pd.read_csv(datPath,sep=',')
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
        for rows in inputData:
            uid, day, job = rows.rstrip('\n').split(',')
            for person in members:
                if int(uid) is person.uid:
                    person.jobPerDay[person.a_month_days[int(day)]] = int(
                        job)

    # @staticmethod
    # def member2PandasDataFrame(members: list[Person]):
    #     df = pd.DataFrame()
    #     for person in members:
    #         pd.DataFrame(person.jobPerDay)
    #     print(df)

ShiftDataReader.readConfigvar('radschedule\勤務表\data\configvar.dat')
members = ShiftDataReader.readStaffInfo('radschedule\勤務表\data\staffinfo.dat')
ShiftDataReader.applyShift2Member('radschedule\勤務表\data\shift.dat', members)

# ShiftDataReader.member2PandasDataFrame(members)
