from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
import time
# Importing some Windows libraries

desk = GetDC(0) # Get the first monitor and store it in our desk variable
x = GetSystemMetrics(0) # Get screen width and store it in x
y = GetSystemMetrics(1) # Get screen height and store it in y

# Let's try changing it's color! We can do that using SelectObject and CreatSolidBrush!
timeofsleep = int(input('Input time(sec):'))
time.sleep(timeofsleep)
for i in range(0, 9000):
	brush = CreateSolidBrush(RGB(
		randrange(255), # Red value
		randrange(255), # Green value
		randrange(255), # Blue value
		)) # Creates a brush
		
	SelectObject(desk, brush) # Choose that we're drawing with our brush.
	PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT) # Makes a lot of stuff :)
	DeleteObject(brush) # Frees up memory, Pretty necessary to avoid crashes etc.
	Sleep(10) # waits 10 milliseconds
ReleaseDC(desk, GetDesktopWindow()) # Release memory.
DeleteDC(desk) #Deletes our DC.