import pyautogui
import time

class ScreenShotter():
    def __init__(self, interval=1):
        self.interval = interval

    def make_screenshots(self):
        while True:
            screenshot = pyautogui.screenshot
            screenshot.save('./imgs/screenshot.png')
            time.sleep(self.interval)
