#pip3 install pyautogui
#pip install Pillow
import subprocess
import pyautogui
import time
subprocess.call(r'C:\Users\uwu machine\AppData\Roaming\Zoom\bin\Zoom.exe')
time.sleep(1)

#Click on join button
joinCoord = pyautogui.locateOnScreen(r'joinButton.png', grayscale = True)
pyautogui.moveTo(joinCoord)
pyautogui.click()

#Click on join meeting and type the meeting id
joinCoord = pyautogui.locateOnScreen(r'meetingID.png', grayscale = True)
pyautogui.moveTo(joinCoord)
pyautogui.click()
pyautogui.typewrite("hello Geeks !")
