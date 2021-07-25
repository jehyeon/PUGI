import schedule
from game_manager import *

def main():
    # a = Character('치즈오리', 35, 23.6122, '')
    # a.saveStatusToLog()
    # print(a.getlog())
    # capture()
    # print(imageToText('logs/remain_potion.png'))
    # print(imageToText('logs/exp.png'))
    # print(imageToText('logs/hp.png'))
    #print(imageToText('logs/buff1.png'))
    # print(imageToText('logs/buff2.png'))
    # print(imageToText('logs/buff3.png'))
    # print(imageToText('logs/buff4.png'))
    # print(imageToText('logs/portion.png'))
    # print(imageToText('logs/quest.png'))
    # print(imageToText('logs/quest_clear.png'))


    # schedule.every(5).seconds.do(workQuest)

    
    # goHome()
    # goShop()
    activateGameWindow()
    # buyAllPotions()
    goLobby()

    # selectCharacter()
    # schedule.every(5).seconds.do(checkStatus)
    
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

if __name__ == '__main__':
    main()