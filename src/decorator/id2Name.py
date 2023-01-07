from enum import Enum


class JobName(Enum):
    AngioNight = '4'
    MRINight = '5'
    CTNight = '6'
    AngioDay = '0'
    MRIDay = '1'
    CTDay = '2'
    Free1 = '3'
    Free2 = '30'

class ID2Name():
    """
    jobのidなどをstrの名前に変換するデコレータ
    """
    