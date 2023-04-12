print("PianoBot V. Beta (c) Michael")
try:
    import sys
    import subprocess
except:
    print("congrats your computer can't import an INTEGRATED package. idk try reinstalling the package I have no clue what you expect me to do...")
print("mporting packages:")
try:
    import pyautogui
except:
    # installs pyautogui
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])
        import pyautogui
    except:
        print("Failed to install neccesary package")
        breakpoint
print(str(round(1/6*100)) + "%")
try:
    import numpy as np
except:
    # installs numpy
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
        import numpy as np
    except:
        print("Failed to install neccesary package")
        breakpoint
print(str(round(1/3*100)) + "%")
try:
    from PIL import ImageGrab
except:
    # installs Pillow
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
        from PIL import ImageGrab
        print("WARNING: ImageGrab is broken. as such custom code was inserted please visit help document for details")
    except:
        print("Failed to install neccesary package")
        breakpoint
print(str(round(1/2*100)) + "%")
try:
    import keyboard
except:
    # installs keyboard
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'keyboard'])
        import keyboard
    except:
        print("Failed to install neccesary package")
        breakpoint
print(str(round(4/6*100)) + "%")
import time
print(str(round(5/6*100)) + "%")
try:
    import cv2
except:
    # installs opencv
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opencv-python'])
        import cv2
    except:
        print("Failed to install neccesary package")
        breakpoint
print("100%\n Completed hold enter to run program (stops when let go for safety reasons)")
width, height = pyautogui.size()
dis = np.array([round(width/3.0188679245), round(height/3), round(width/1.4930015552), round(height/1.3646055437)]) #Hopefully compatible with more devices
#screen = np.array(ImageGrab.grab(bbox=dis)) #captures screen
#RGB = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB) #-\('~')/-
#mask = cv2.inRange(RGB, np.array([0, 0, 0]), np.array([54, 159, 198])) #Masks out the Tiles.
while 1:
    avg = None
    if(keyboard.is_pressed('enter')):
        screen = np.array(ImageGrab.grab(bbox=dis)) #captures screen
        RGB = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB) #-\('~')/-
        mask = cv2.inRange(RGB, np.array([0, 0, 0]), np.array([54, 159, 198])) #Masks out the Tiles.
        positives = cv2.findNonZero(mask)
        try:
            avg = np.average(positives, axis=0)
            pyautogui.mouseDown(avg[0][0] + round(width/3.0188679245), avg[0][1] + round(height/3))
            pyautogui.mouseUp()
        except:
            None
        if(keyboard.is_pressed('l')):
            cv2.imshow('mask', mask)