from Character import *
from window_control import *
from get_info import *

CHARACTERS = {}

def selectCharacter():
    # temp
    CHARACTERS['치즈개'] = Character('치즈개')
    level, exp, nowHp = getStatus()
    CHARACTERS['치즈개'].initStatus(level, exp, nowHp)
    # level, exp, nowHp

def checkStatus():
    # temp
    level, exp, nowHp = getStatus()
    print(CHARACTERS['치즈개'].updateStatus(level, exp, nowHp))

def checkHp():
    # 5초마다 현재 체력 확인
    # 체력이 없으면 집 가서 물약 사옴
    pass