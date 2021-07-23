import datetime
import os
import pyautogui

# 현재 시간
# YYYY-MM-DD-HH-MM-SS
def now():
    return datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

# 로그 관련
def getLogData(nickName):
    if not 'logs' in os.listdir('./'):
        # logs 폴더가 없는 경우
        os.system('mkdir logs')
        
    try:
        with open('logs/' + nickName + '_log.txt', 'r') as f:
            return f.readlines()
            
    except:
        # log.txt가 없는 경우
        with open('logs/' + nickName + '_log.txt', 'w') as f:
            f.write('{0} 로그 파일 생성\n'.format(now()))
            return getLogData(nickName)

def saveLog(nickName, message):
    if not 'logs' in os.listdir('./'):
        # logs 폴더가 없는 경우
        os.system('mkdir logs')

    with open('logs/' + nickName + '_log.txt', 'a') as f:
        f.write('{0} {1}\n'.format(now(), message))

# window 조작
# 프로세스를 활성화
# 윈도우 + left + up 으로 왼쪽 위 모서리에 위치하도록 함
# 임시로 사용
def activateGameWindow():
    pyautogui.moveTo(30, 10)    # temporary
    pyautogui.click()
    # pyautogui.press('enter')

# 게임 컨트롤
def goHome():
    # H
    pass

def goShop():
    pass

def buyAllPotions():
    pass

def goLobby():
    pass

def changeCharacter():
    pass

def receiveTodayQuest():
    pass

def clearTodayQuest():
    pass