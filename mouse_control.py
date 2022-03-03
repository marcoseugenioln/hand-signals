from pynput.mouse import Controller
import screeninfo

class MouseControl:

    def __init__(self):
        self.mouse = Controller()

        monitor = screeninfo.get_monitors()

        self.screenHeight = monitor[0].height
        self.screenWidth = monitor[0].width

    def moveMouse(self, x, y):
        self.mouse.position = (x, y)
        