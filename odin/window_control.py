import datetime
import os
import pyautogui
import time

from get_info import *

# POS
QUEST_LIST_BTN = (1189, 234)
QUEST_CLEAR_BTN = (1190, 664)
RECEIVE_QUEST_CLEAR_REWARD = (512, 452)

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
def workQuest():
    # 퀘스트 받기 
    # 일정시간 기다리기? 5분 간격으로 퀘스트 확인?

    openQuestList()

    if checkQuestClear():
        # 보상 받기
        pyautogui.click(QUEST_CLEAR_BTN[0], QUEST_CLEAR_BTN[1])
        time.sleep(3)

        # 보상 선택하기
        pyautogui.click(RECEIVE_QUEST_CLEAR_REWARD[0], RECEIVE_QUEST_CLEAR_REWARD[1])
        time.sleep(2)

    else:
        print('퀘스트 미 클리어')     # 현재 시간 표기

def openMenu():
    # 메뉴 창 열기
    activateGameWindow()
    time.sleep(1)
    pyautogui.press('O')
    time.sleep(1)

def openQuestList():
    openMenu()
    pyautogui.click(QUEST_LIST_BTN[0], QUEST_LIST_BTN[1])
    time.sleep(1)

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