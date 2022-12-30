import pyautogui as pt
from time import sleep
from datetime import datetime

datetime.now()
time_stamp = datetime.strftime(datetime.now(), "%d-%m-%y _ %H:%M")
file_name = time_stamp + ".png"

sleep(2)

def start_point():
    start_point = pt.locateCenterOnScreen("start_point.png", confidence=.8)
    pt.moveTo(start_point)
    pt.moveRel(0,250)
    pt.click()

def dl_audio():
    audios = pt.locateAllOnScreen("new_audio.png", confidence=.8)
    options = pt.locateAllOnScreen("options.png", confidence=.5)
    
    sleep(2)
    if audios is not None:
        print('tem audio')
        *_, new_audio = audios
        pt.moveTo(new_audio[0], new_audio[1])
        sleep(2)
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

      
   


# try:
#     #check if new message is an audio message
#     play_button = pt.locateCenterOnScreen("play.png", confidence=.8 )
#     if play_button:
#         print("tem audio")
#         pt.moveTo(play_button)
#         options = pt.locateCenterOnScreen("options.png", confidence=.8 )
#         pt.moveTo(options)
#         pt.click()
#         # pt.moveRel(0, -180)
#         sleep(5)
#                 # pt.click()

#                     # sleep(1)
#                     # pt.moveRel(0, 180)
#                     # sleep(1)
#                     # pt.click()
#                     # sleep(1)

#                     # pt.moveRel(10, -45)
#                     # sleep(1)
#                     # pt.click()

#                     # sleep(1)
#                     # pt.moveRel(0, -50)
#                     # pt.click()
#                     # sleep(1)

#                     # sleep(1)
#                     # pt.moveRel(-400, 0)
#                     # pt.click()
#                     # sleep(1)
#                 else:
#                     start_point()
#             except:
#                 print("no audio sent")
#                 start_point()

#     except:
#         start_point()
#         print("no new messages")


dl_audio()