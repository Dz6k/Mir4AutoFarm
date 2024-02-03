# lib   
import random
import pyautogui
import os
from mousekey import MouseKey
from time import sleep
from pywinauto import Application
from datetime import datetime
import threading

def farm_die_on():
    # check resolution
    RESOLUTION = 1920,1080
    check_resolution = pyautogui.resolution()
    if check_resolution != RESOLUTION:
        return print('Essa aplicacao é somente para monitores 1920x1080')
    
    app = Application().connect(title='Mir4G[1]')   
    app.window().set_focus()
    mkey = MouseKey()
    possibilities = 1.75,2,2.25,2.5,2.75,3

    # for stop execution: press CTRL + E 
    mkey.enable_failsafekill('ctrl+e')
    
    # variables
    ultimate = True # use ultimate set to True // don't use ultimate set to False
    im_live = "yes"
    counter2 = 0

    # start auto atack
    pyautogui.press('b')
    while im_live == "yes":
        # detect if you die    
        try:
            #find the revive button  in especific area on your monitor
            death = pyautogui.locateOnScreen('AutoFarm\imagens\morto.png', region=(1621,858,300,170),confidence=0.7)

            # ok, now you're dead and we'll take you for some air
            os.system('cls')
            print('Voce morreu, em 10 segundos levaremos voce para farmar energia.')
            sleep(10)
            pyautogui.click(death)
            os.system('cls')
            print('A caminho do farm de energia, aguarde.')
            sleep(7)
            
            # open map
            pyautogui.press('f10')
            sleep(1)
            
            # open favorites places
            look_map_x,look_map_y = pyautogui.locateCenterOnScreen('AutoFarm\imagens\map.png',confidence=0.7)
            pyautogui.click(x=look_map_x,y=look_map_y, duration=0.5)
            sleep(0.5)
            
            # select de energy
            energia_x,energia_y = pyautogui.locateCenterOnScreen('AutoFarm\imagens\energia.png',confidence=0.7)
            pyautogui.click(x=energia_x,y=energia_y, duration=0.5)
            
            # teleport to and keep mining
            tp_x,tp_y = pyautogui.locateCenterOnScreen('AutoFarm\imagens\\tp.png',confidence=0.7)
            pyautogui.click(x=tp_x,y=tp_y, duration=0.5)
            sleep(10)
            pyautogui.press('n')
            os.system('cls')
            
            # print good bye 
            print(f'Você morreu as {datetime.now().strftime("%H:%M")}')
            im_live = "not"
            
        # if not die, execute this
        except pyautogui.ImageNotFoundException:
            os.system('cls')
            counter2 += 1
            print('ainda vivo', counter2)
            # open battle menu
            sleep(0.2)
            pyautogui.press('tab')
            
            # select mob on battle menu(random selection, not AI or other thing)
            pyautogui.press('pageUP',presses=(random.randint(2,4)))
            pyautogui.press('f')
            sleep(random.choice(possibilities))
            if ultimate:
                pyautogui.press('r')

def start_simple():
    farm = threading.Thread(target=farm_die_on)
    farm.start()
