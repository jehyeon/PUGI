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
        time.sleep(5)

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
    time.sleep(5)
    click(GO_HOME_OK_BTN_S, GO_HOME_OK_BTN_E)
    time.sleep(10)

def goShop():
    pyautogui.press('4')
    time.sleep(20)

def buyAllPotions():
    click(POSIONS_BTN_S, POSIONS_BTN_E)
    time.sleep(5)
    # 포션 구매 가능 수량 보기
    click(MAX_POTION_BTN_S, MAX_POTION_BTN_E)
    time.sleep(5)
    click(BUY_BTN_S, BUY_BTN_E)
    time.sleep(5)
    pyautogui.press('ESC')
    time.sleep(5)

def goLobby():
    openMenu()
    time.sleep(5)
    click(CHANGE_CHARACTER_BTN_S, CHANGE_CHARACTER_BTN_E)
    time.sleep(5)
    click(ALERT_OK_S, ALERT_OK_E)
    time.sleep(5)

def changeCharacter(chracterNumber):
    character = CHARACTERS[chracterNumber]
    click(character['s'], character['e'])
    time.sleep(20)

def receiveTodayQuest():
    pass

def clearTodayQuest():
    pass


# 리세마라
def resetMaraton():
    # Z 계속 눌러줌
    pyautogui.press('Z')

    # 퀘스트가 있을 경우
    result = get_info.getImageToText('logs/temp.png', (1073, 111, 1165, 130))
    if '터처' in result or \
        '터차' in result or \
        '터치' in result:
        click(pos.QUEST_CLEAR_BTN_RESET_MARATON_S, pos.QUEST_CLEAR_BTN_RESET_MARATON_E)

    # 퀘스트를 클리어 한 경우
    result = get_info.getImageToText('logs/temp.png', pos.QUEST_CLEAR_AREA_RESET_MARATON)
    if '보상' in result or \
        '터치' in result or \
        '터차' in result or \
        '하어' in result or \
        '수떤' in result or \
        '수정' in result:
        click(pos.QUEST_CLEAR_BTN_RESET_MARATON_S, pos.QUEST_CLEAR_BTN_RESET_MARATON_E)

    # NPC가 말하고 있으면 SKIP 클릭
    if len(get_info.getImageToText('logs/temp.png', (412, 586, 863, 669))) > 15:
        pyautogui.click(1228, 64)
    
    # NPC가 말하고 있으면 대화창 연속 클릭
    if len(get_info.getImageToText('logs/temp.png', pos.QUEST_SPEAK_AREA_RESET_MARATON)) > 15:
        for _ in range(8):
            click(pos.TEMP_SPEAK_OK_BTN_S, pos.TEMP_SPEAK_OK_BTN_E)
            time.sleep(0.5)

    # 아이템 자동 장착
    if not pyautogui.locateOnScreen('equip.png') == None:
        print('아이템 먹음')
        click(pos.EQUIP_BTN_S, pos.EQUIP_BTN_E)

    # 튜토리얼 진행 중인지
    if get_info.compareImage('logs/temp.png', (1060, 382, 1261, 424), '0.png'):
        # HP 회복 물약을 사용해보세요!
        pyautogui.click(1159, 500)

    if get_info.compareImage('logs/temp.png', (973, 613, 1131, 656), '1.png'):
        # 마물들을 쓰러뜨리게
        pyautogui.click(1220, 638)
        time.sleep(15)
        pyautogui.click(990, 638)
        time.sleep(15)
        pyautogui.click(1220, 638)
        time.sleep(15)
        pyautogui.moveTo(990, 638)
        pyautogui.dragTo(990, 648, 1, button='left')
        time.sleep(5)
        pyautogui.click(1220, 638)
        time.sleep(15)
        pyautogui.click(1220, 638)
        time.sleep(15)
        pyautogui.click(1220, 638)
        time.sleep(15)
        pyautogui.click(753, 413)
        time.sleep(5)
        pyautogui.click(1220, 638)

    if get_info.compareImage('logs/temp.png', (996, 204, 1219, 247), '2.png'):
        # 임무를 자동으로 수행할 수 있어요!
        pyautogui.click(1090, 127)

    if get_info.compareImage('logs/temp.png', (951, 142, 1269, 185), '3.png'):
        # 획득한 장비는 가방 버튼을 눌러 확인할 수 있네.
        pyautogui.click(1179, 55)
        time.sleep(5)
        pyautogui.click(945, 171)
        time.sleep(5)
        pyautogui.click(945, 171)
        time.sleep(5)
        pyautogui.click(1246, 56)

def clickQuest():
    # 한번씩 퀘스트 클릭 해주기
    # 감지가 안될 경우 스토리 진행을 막기 위함
    click(pos.QUEST_CLEAR_BTN_RESET_MARATON_S, pos.QUEST_CLEAR_BTN_RESET_MARATON_E)

def temp():
    # get_info.captureT((951, 142, 1269, 185))
    print(get_info.compareImage('logs/temp.png', (951, 142, 1269, 185), '3.png'))
    # print(get_info.compareImage('logs/temp.png', (996, 204, 1219, 247), '2.png'))
    # print(get_info.getImageToText('logs/temp.png', (1029, 131, 1146, 147)))
    pass