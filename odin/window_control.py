import datetime
import os
import random
import time

import pyautogui

import get_info

import pos

# POS
QUEST_LIST_BTN = (1189, 234)
QUEST_CLEAR_BTN = (1190, 664)
RECEIVE_QUEST_CLEAR_REWARD = (512, 452)

GO_HOME_OK_BTN_S = (643, 429)
GO_HOME_OK_BTN_E = (771, 452)

CHANGE_CHARACTER_BTN_S = (1039, 499)
CHANGE_CHARACTER_BTN_E = (1082, 545)

MAX_POTION_BTN_S = (693, 410)
MAX_POTION_BTN_E = (776, 431)

CHAR_1_BTN_S = (1074, 89)
CHAR_1_BTN_E = (1244, 150)

CHAR_2_BTN_S = (1075, 174)
CHAR_2_BTN_E = (1243, 231)

CHAR_3_BTN_S = (1075, 259)
CHAR_3_BTN_E = (1243, 312)

CHAR_4_BTN_S = (1075, 345)
CHAR_4_BTN_E = (1243, 401)

CHAR_5_BTN_S = (1075, 424)
CHAR_5_BTN_E = (1243, 483)

# 
CHARACTERS = ['',
    { 's': CHAR_1_BTN_S, 'e': CHAR_1_BTN_E },
    { 's': CHAR_2_BTN_S, 'e': CHAR_2_BTN_E },
    { 's': CHAR_3_BTN_S, 'e': CHAR_3_BTN_E },
    { 's': CHAR_4_BTN_S, 'e': CHAR_4_BTN_E },
    { 's': CHAR_5_BTN_S, 'e': CHAR_5_BTN_E }
]

# Control
def click(startXY, endXY):
    # start (x, y) ~ end (x, y)
    x = random.randrange(startXY[0], endXY[0] + 1)
    y = random.randrange(startXY[1], endXY[1] + 1)

    pyautogui.click(x, y)

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
    time.sleep(2)
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

# UI 컨트롤
def openMenu():
    # 메뉴 창 열기
    time.sleep(1)
    pyautogui.press('O')
    time.sleep(1)

def openQuestList():
    openMenu()
    pyautogui.click(QUEST_LIST_BTN[0], QUEST_LIST_BTN[1])
    time.sleep(5)

# 동작
def goHome():
    pyautogui.press('H')
    time.sleep(3)
    click(GO_HOME_OK_BTN_S, GO_HOME_OK_BTN_E)
    time.sleep(10)

def goShop():
    pyautogui.press('4')
    time.sleep(20)

def buyAllPotions():
    click(POSIONS_BTN_S, POSIONS_BTN_E)
    time.sleep(3)
    # 포션 구매 가능 수량 보기
    click(MAX_POTION_BTN_S, MAX_POTION_BTN_E)
    time.sleep(3)
    click(BUY_BTN_S, BUY_BTN_E)
    time.sleep(3)
    pyautogui.press('ESC')
    time.sleep(3)

def goLobby():
    openMenu()
    time.sleep(3)
    click(CHANGE_CHARACTER_BTN_S, CHANGE_CHARACTER_BTN_E)
    time.sleep(3)
    click(ALERT_OK_S, ALERT_OK_E)
    time.sleep(3)

def changeCharacter(chracterNumber):
    character = CHARACTERS[chracterNumber]
    click(character['s'], character['e'])
    time.sleep(20)

def receiveTodayQuest():
    pass

def clearTodayQuest():
    pass


# 리세마라

def checkClearQuestForResetMaraton():
    result = get_info.getImageToText('logs/temp.png', pos.QUEST_CLEAR_AREA_RESET_MARATON)

    print(result)

    if '보상' in result or \
        '터치' in result or \
        '터차' in result or \
        '하어' in result or \
        '수떤' in result or \
        '수정' in result:

        # 퀘스트 완료 클릭
        click(pos.QUEST_CLEAR_BTN_RESET_MARATON_S, pos.QUEST_CLEAR_BTN_RESET_MARATON_E)
        time.sleep(2)
        # ZZZ()

    else:
        print('퀘스트 미완료 or 감지 안됨')

def checkSpeakingForResetMaraton():
    result = get_info.getImageToText('logs/temp2.png', pos.QUEST_SPEAK_AREA_RESET_MARATON)

    if len(result) > 10:
        for _ in range(5):
            click(pos.TEMP_SPEAK_OK_BTN_S, pos.TEMP_SPEAK_OK_BTN_E)
            time.sleep(0.5)


def goQuestForResetMaraton():
    # 퀘스트 완료가 아닐 땐 한번씩 눌러줌
    click(pos.QUEST_CLEAR_BTN_RESET_MARATON_S, pos.QUEST_CLEAR_BTN_RESET_MARATON_E)
    
def checkStories():
    
    # 퀘스트 목록을 눌러서 임무를 자동으로 수행할 수 있어요
    if not pyautogui.locateOnScreen('1.png') == None:
        click(pos.QUEST_CLEAR_BTN_RESET_MARATON_S, pos.QUEST_CLEAR_BTN_RESET_MARATON_E)
        time.sleep(15)
        click(pos.TEMP_POTION_BTN_S, pos.TEMP_POTION_BTN_E) # 물약 클릭
    
    # 아이템 장착
    if not pyautogui.locateOnScreen('2.png') == None:
        click(pos.TEMP_BAG_BTN_S, pos.TEMP_BAG_BTN_E)
        time.sleep(10)
        click(pos.TEMP_CLO_BTN_S, pos.TEMP_CLO_BTN_E)
        time.sleep(3)
        click(pos.TEMP_CLO_BTN_S, pos.TEMP_CLO_BTN_E)
        time.sleep(3)
        click(pos.TEMP_QUIT_BTN_S, pos.TEMP_QUIT_BTN_E)

    if not pyautogui.locateOnScreen('3.png') == None:
        click(pos.POSIONS_BTN_S, pos.POSIONS_BTN_E)
        time.sleep(3)
        click(pos.BUY_BTN_S, pos.BUY_BTN_E)
        time.sleep(3)
        pyautogui.press('ESC')

    if not pyautogui.locateOnScreen('4.png') == None:
        click(pos.TEMP_FAST_SEE_BTN_S, pos.TEMP_FAST_SEE_BTN_E)
        time.sleep(3)
        click(pos.TEMP_FAST_SEE_BTN_S, pos.TEMP_FAST_SEE_BTN_E)
        time.sleep(30)
        click(pos.TEMP_QUIT_BTN_S, pos.TEMP_QUIT_BTN_E)
        time.sleep(3)
        click(pos.TEMP_RIDE_BTN_S, pos.TEMP_RIDE_BTN_E)
        time.sleep(3)
        click(pos.TEMP_RIDE_FIRST_BTN_S, pos.TEMP_RIDE_FIRST_BTN_E)
        time.sleep(3)
        click(pos.TEMP_RIDE_EQUIP_BTN_S, pos.TEMP_RIDE_EQUIP_BTN_E)
        time.sleep(3)
        click(pos.TEMP_QUIT_BTN_S, pos.TEMP_QUIT_BTN_E)

    if not pyautogui.locateOnScreen('5.png') == None:
        click(pos.TEMP_QUIT_BTN_S, pos.TEMP_QUIT_BTN_E)
        time.sleep(3)
        click(pos.TEMP_RIDE_BTN_S, pos.TEMP_RIDE_BTN_E)
        time.sleep(3)
        click(pos.TEMP_RIDE_SECOND_BTN_S, pos.TEMP_RIDE_SECOND_BTN_E)
        time.sleep(3)
        click(pos.TEMP_RIDE_EQUIP_BTN_S, pos.TEMP_RIDE_EQUIP_BTN_E)
        time.sleep(3)
        click(pos.TEMP_QUIT_BTN_S, pos.TEMP_QUIT_BTN_E)

    if not pyautogui.locateOnScreen('6.png') == None:
        click(pos.TEMP_GO_HOME_BTN_S, pos.TEMP_GO_HOME_BTN_E)
        time.sleep(3)
        click(pos.TEMP_ALERT_OK_BTN_S, pos.TEMP_ALERT_OK_BTN_E)
    
    if not pyautogui.locateOnScreen('7.png') == None:
        click(pos.TEMP_BAG_BTN_S, pos.TEMP_BAG_BTN_E)
        time.sleep(5)
        click(pos.TEMP_USE_ITEM_BTN_S, pos.TEMP_USE_ITEM_BTN_E)
        time.sleep(3)
        pyautogui.click(945, 168)
        time.sleep(3)
        pyautogui.click(945, 168)
        time.sleep(3)
        click(pos.TEMP_QUIT_BTN_S, pos.TEMP_QUIT_BTN_E)
        time.sleep(3)
        click(pos.TEMP_QUIT_BTN_S, pos.TEMP_QUIT_BTN_E)
        time.sleep(3)
        pyautogui.click(1059, 158)
        time.sleep(3)
        pyautogui.click(1190, 662)
        time.sleep(3)
        pyautogui.click(1007, 233)
        time.sleep(3)
        pyautogui.click(856, 380)
        time.sleep(3)
        click(pos.TEMP_QUIT_BTN_S, pos.TEMP_QUIT_BTN_E)
        time.sleep(3)
        pyautogui.moveTo(1058, 633)
        pyautogui.dragTo(1059, 682, 1, button='left')
    
    if not pyautogui.locateOnScreen('8.png') == None:
        click(pos.POSIONS_BTN_S, pos.POSIONS_BTN_E)
        time.sleep(3)
        click(pos.BUY_BTN_S, pos.BUY_BTN_E)
        time.sleep(3)
        pyautogui.press('ESC')

    if not pyautogui.locateOnScreen('9.png') == None:
        pyautogui.click(1215, 121)
        time.sleep(3)

    if '정보' in get_info.getImageToText('logs/temp3.png', pos.SELECT_AVATAR_AREA_RESET_MARATON):
        pyautogui.click(368, 509)
        time.sleep(3)
        pyautogui.click(1145, 655)
        time.sleep(3)
        pyautogui.click(1236, 65)
        time.sleep(20)
        pyautogui.click(638, 643)
        time.sleep(10)
        click(pos.TEMP_QUIT_BTN_S, pos.TEMP_QUIT_BTN_E)
        time.sleep(3)
        pyautogui.click(1117, 162)
        time.sleep(3)
        pyautogui.click(972, 185)
        time.sleep(3)
        click(pos.TEMP_RIDE_EQUIP_BTN_S, pos.TEMP_RIDE_EQUIP_BTN_E)
        time.sleep(3)
        click(pos.TEMP_QUIT_BTN_S, pos.TEMP_QUIT_BTN_E)
    
    if not pyautogui.locateOnScreen('12.png') == None:
        click(pos.TEMP_QUIT_BTN_S, pos.TEMP_QUIT_BTN_E)
        time.sleep(3)


def checkEquipBtn():
    # 아이템 자동 장착
    if not pyautogui.locateOnScreen('4.png') == None:
        click(pos.EQUIP_BTN_S, pos.EQUIP_BTN_E)
        time.sleep(3)
        click(pos.TEMP_BAG_BTN_S, pos.TEMP_BAG_BTN_E)
        time.sleep(3)
        pyautogui.click(947, 171)
        time.sleep(3)
        pyautogui.click(444, 598)
        time.sleep(3)
        pyautogui.click(706, 487)
        time.sleep(3)
        pyautogui.click(706, 487)
        time.sleep(3)
        pyautogui.press('ESC')

def ZZZ():
    pyautogui.press('Z')

def temp():
    print(pyautogui.locateOnScreen('12.png'))
    # click(pos.TEMP_ALERT_OK_BTN_S, pos.TEMP_ALERT_OK_BTN_E)
    # checkStories()
    # print(pyautogui.locateOnScreen('11.png'))
    pass