
#設計がおかしいので変更必須
class ValueEditor:
    """
    modelに変更を反映させるもの
    """
    changedValue:str
    
    def __init__(self):
        self.changedValue = None
        pass
    
    def setChangedValue(self, changedValue):
        self.changedValue = changedValue
        
