import datetime

class damagedDataError(Exception):
    pass

#独自の型
class PersonType:
    # 個人の情報
    uid: int
    staffid: str
    name: str
    jobPerDay: dict

class MemberType(PersonType):
    members: list[PersonType]

    # 全職員で共通な情報
    date: datetime

    day_previous_next: list[tuple[int, int, int, int]]


    # a_month_calendar: list[list[int]]
    # a_month_days: list[int]
    

class Validater:
    # デコレータとして検証

    # データの欠損を検証
    # 汎用性がなく、いい書き方ではない
    @staticmethod
    def validJobPerDay(func, logger:bool=False):
        def wrapper(*args, **kwargs):
            membersInfo: MemberType= func(*args, **kwargs)
            for person in membersInfo.members:
                    for day in membersInfo.day_previous_next:
                        try:
                            person.jobPerDay[day]
                            # if len(person.jobPerDay) != len(membersInfo.a_month_days):
                            #     raise damagedDataError()
                        except KeyError as _ex:
                            # データ穴埋め
                            person.jobPerDay[day] = None
                            # person.jobPerDay = {
                            #     day: None for day in membersInfo.a_month_days}
                            if(logger):
                                print('欠損データはNoneで埋められました')
                                print(f'対象名: {person.name} 職員ID: {person.staffid}')
                                print(f'日時: {day}')

            return membersInfo
        return wrapper

    # 使い道ないかも↓
    @staticmethod
    def validListlen(func, wantLen: int):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                if len(result) != wantLen:
                    raise damagedDataError()
            except damagedDataError as _ex:
                print('データが望まない長さになっています')
                print('データ長: '+len(result))
            return result
        return wrapper
