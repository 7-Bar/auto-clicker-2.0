import pyautogui
import time


print("|*| OP AUTO CLICKER 2.0 |*|")
print()
print("BEAST MODE or normal mode")
mode = str(input("CHOOSE: ")).lower()

print()

if mode == "beast":
    print("WARNING IT'S VERY HARD TO CONTROL BEAST MODE")
    pyautogui.PAUSE = 0
    time.sleep(1)
    print("STARTING BEAST MODE...")
elif mode == "normal":
    print("STARTING NORMAL MODE...")
    pyautogui.PAUSE = 0.01
else:
    print("choose a REAL option next time")
    print()
    quit()

time.sleep(2)

while True:
    pyautogui.click()