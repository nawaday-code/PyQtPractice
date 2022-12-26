import datetime
import locale
import logging

import pandas as pd


from database.member import Members


class DataSender(Members):

    def __init__(self):
        super().__init__()
        
    def toHeader(self) -> list[str]:
        locale.setlocale(locale.LC_TIME, 'ja_JP')
        return [datetime.date(*yyyymmddww[:3]).strftime('%x')+datetime.date(*yyyymmddww[:3]).strftime('%a')
                for yyyymmddww in self.day_previous_next]

    
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
    
    def getKinmuDf(self):
        """            
        日付-veriant  日付 (yyyy-mm-dd)  日付+1
        UID 勤務(Not int)
            無いときはNone
        """
        df = pd.DataFrame()
        for person in self.members:
            df[person.uid] = person.jobPerDay
        df.sort_index(axis=0, inplace=True)
        logging.debug(df.T)
        

    def getDf4Iwasaki(self):
        pass