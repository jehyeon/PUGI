from Character import *
from window_control import *
from get_info import *

def main():
    while True:
        inp = input('')
        if inp == 'quit' or inp == 'Quit':
            break

if __name__ == '__main__':
    # a = Character('치즈오리', 35, 23.6122, '')
    # a.saveStatusToLog()
    # print(a.getlog())
    # activateGameWindow()
    capture()
    # print(imageToText('logs/level.png'))
    # print(imageToText('logs/exp.png'))
    print(imageToText('logs/hp.png'))
    #print(imageToText('logs/buff1.png'))
    # print(imageToText('logs/buff2.png'))
    # print(imageToText('logs/buff3.png'))
    # print(imageToText('logs/buff4.png'))
    # print(imageToText('logs/portion.png'))
