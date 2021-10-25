import keyboard
import sys
import time

interval = int(sys.argv[1] if len(sys.argv) == 2 else 5)
while(True):
	keyboard.press_and_release(keyboard.KEY_DOWN)
	time.sleep(interval)
