import pyautogui as pt
from time import sleep
import pyperclip
from datetime import datetime

datetime.now()
time_stamp = datetime.strftime(datetime.now(), "%d-%m-%y _ %H:%M")
file_name = time_stamp + ".png"

sleep(2)


def check_new_messages():
    green_button = pt.locateOnScreen("new.png", confidence=.8)
    while True:
        try: 
            pt.moveTo(green_button)
            pt.moveRel(-100,0)
            pt.click()
            sleep(1)
            pt.screenshot(time_stamp)
            pt.moveRel(-100, 200)
            pt.click()
            
                        
        
            play_button = pt.locateOnScreen("play.png", confidence=.8 )
        
            print("tem audio")
            pt.moveTo(play_button)
            pt.moveRel(265, -30)
            pt.click()
            pt.moveRel(0, -180)
            sleep(1)
            pt.click()

            sleep(1)
            pt.moveRel(0, 180)
            sleep(1)
            pt.click()
            sleep(1)

            pt.moveRel(10, -45)
            sleep(1)
            pt.click()

            sleep(1)
            pt.moveRel(0, -50)
            pt.click()
            sleep(1)

            sleep(1)
            pt.moveRel(-400, 0)
            pt.click()
            sleep(1)

        except:
            print("no new messages")


check_new_messages()