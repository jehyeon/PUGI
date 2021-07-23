from window_control import getLogData, saveLog

class Character:
    def __init__(self, nickName, level, exp, startTime):
        self._nickName = nickName
        self._level = level
        self._exp = exp
        self._startTime = startTime
    
    def getlog(self):
        return getLogData(self._nickName)
    
    def setInitHp(self, nowHp, maxHp):
        self._maxHp = maxHp
        self._nowHp = nowHp

    def saveStatusToLog(self):
        message = 'nickName:{0}|lv:{1}|exp:{2}'.format(
            self._nickName,
            self._level,
            self._exp
        )
        saveLog(self._nickName, message)