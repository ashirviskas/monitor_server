import pyautogui
import time


class ScreenShotter():
    def __init__(self, interval=1):
        self.interval = interval

    def do_screenshot(self):
        screenshot = pyautogui.screenshot(region=(0, 0, 600, 720))
        screenshot.save('./static/screenshot.png')

    def make_screenshots(self):
        while True:
            self.do_screenshot()
            time.sleep(self.interval)
