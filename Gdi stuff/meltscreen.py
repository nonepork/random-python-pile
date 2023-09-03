import win32gui
import win32con
import random
import ctypes
import time

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
hdc = win32gui.GetDC(0)
for i in range(0, 100): #Change this to while True for trolling :)
    samex = random.randint(0, sw)
    # samex = position start dropping
    #                              fall block width                        fall height
    win32gui.BitBlt(hdc, samex, 0, random.randint(10, 35), sh, hdc, samex, random.randint(-5, -1), win32con.SRCCOPY)
    time.sleep(0.05)
