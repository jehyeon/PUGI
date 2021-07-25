from window_control import *

class Character:
    def __init__(self, nickName):
        self._nickName = nickName
    
    def setInitHp(self, nowHp, maxHp):
        self._maxHp = maxHp
        self._nowHp = nowHp

    def setHp(self, nowHp):
        pass

    def checkNowHp(self):
        if self._nowHp < int(self._maxHp / 2):
            message = '체력 50% 이하 {0} / {1}'.format(self._nowHp, self._maxHp)

            saveLog(self._nickName, message)
            goHome()
            goShop()
            buyAllPotions()

            return False

        else:
            message = '체력 {0} / {1}'.format(self._nowHp, self._maxHp)

            saveLog(self._nickName, message)

            return True
    '''
    def initStatus(self, level, exp, nowHp):
        self._level = level
        self._exp = exp

        # temp
        self._nowHp = nowHp

        message = 'nickName:{0} init'.format(self._nickName)
        saveLog(self._nickName, message)
    
    def updateStatus(self, level, exp, nowHp):
        # Status 업데이트 and 로그 저장
        self._level = level
        self._exp = exp
        self._nowHp = nowHp

        self.saveStatusToLog()

        # temp
        return self._nickName + ' (' + self._level + '.' + self._exp + ') - hp: ' + self._nowHp

    '''


    def getlog(self):
        return getLogData(self._nickName)

    def saveStatusToLog(self):
        message = 'nickName:{0}|lv:{1}|exp:{2}|nowHp:{3}'.format(
            self._nickName,
            self._level,
            self._exp,
            self._nowHp
        )
        saveLog(self._nickName, message)

    # def saveNowHpToLog(self):
    #     message = 'nowHp:{0}'.format(self._nowHp)
    #     saveLog(self._nickName, message)