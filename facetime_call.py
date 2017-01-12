# _*_ coding:utf-8 _*_
import subprocess
import time


class FaceTimeDriver(object):
    def __init__(self):
        self.window = [0] * 8
        self.last_call = time.time()

    def action(self, result):
        self.window.pop(0)
        self.window.append(result)
        if time.time() - self.last_call > 10 and sum(self.window) >= 6:
            subprocess.call(["osascript", "/Users/gavin/Desktop/FaceHer.scpt"])
            print("Start FaceTime!")
            self.last_call = time.time()
