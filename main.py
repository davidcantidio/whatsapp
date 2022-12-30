import pyautogui as pt
from time import sleep
from datetime import datetime

datetime.now()
time_stamp = datetime.strftime(datetime.now(), "%d-%m-%y _ %H:%M")
file_name = time_stamp + ".png"

sleep(2)
def start_point():
    start_point = pt.locateCenterOnScreen("start_point.png", confidence=.8)
    pt.moveTo(0, 650)
    pt.click()


def dl_audio():
    
    audios = pt.locateAllOnScreen("new_audio.png", confidence=.8)
    if audios is not None:
        print('tem audio')
        *_, new_audio = audios
        pt.moveTo(new_audio[0], new_audio[1])
        sleep(1)
        pt.moveRel(230, 0)
        pt.click()
        sleep(1)
        dl = pt.locateCenterOnScreen("download.png", confidence=.8)
        if dl is not None:
            pt.moveTo(dl[0], dl[1])
            pt.click()
            start_point()
        else:
            print("não achei botão de download")
            start_point()


def check_new_messages():    
    while True:
        green_button = pt.locateOnScreen("new.png", confidence=.8)
        try: 
            #detect the green circle indicating new message on screen
            if green_button is not None:
            #click on new message
                pt.moveTo(green_button)
                pt.moveRel(-100,0)
                pt.click()
                pt.screenshot(file_name)
                sleep(.5)
                try:
                    dl_audio()
                except:
                    start_point()
                    print("no audio sent")
        except:
            start_point()
            print("no new messages")


check_new_messages()