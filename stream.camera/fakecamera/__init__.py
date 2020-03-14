import os
import shutil


class PiCamera:
    def __init__(self):
        self.test_pic = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.png")

    def resolution(self, res):
        return

    def start_preview(self):
        return

    def capture(self, filename):
        shutil.copyfile(self.test_pic, filename)
