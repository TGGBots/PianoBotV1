import sys
import subprocess
exceptions = 0
try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', 'numpy'])
except:
    print("uninstall failed command: pip uninstall numpy")
    exceptions += 1
try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', 'keyboard'])
except:
    print("uninstall failed command: pip uninstall keyboard")
    exceptions += 1
try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', 'pyautogui'])
except:
    print("uninstall failed command: pip uninstall pyautogui")
    exceptions += 1
if exceptions >= 1:
    print("Uninstall failed\n to manually uninstall follow the following steps:\n Step 1. type cmd\n Step 2. Press Enter.\n Step 3. type: pip uninstall numpy and press enter\n Step 4. when that's finished type: pip uninstall keyboard and press enter.\n Step 5. when that's finished type: pip uninstall pyautogui and press enter.\n Step 6. type in a browser tab: https://www.youtube.com/watch?v=dQw4w9WgXcQ\n if any of the previous fails throw your computer in the trash")
else: 
    print('congrats you have gotten rid of PianoBot and its associated packages.')