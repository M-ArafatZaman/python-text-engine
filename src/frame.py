import time
from .utils.screen import clearScreen
import os

"""
A frame object that decides how to and what to draw on the screen
"""
class Frame:
    def __init__(self):
        self._objects = []
        self._FPS = 20
        terminalSize = os.get_terminal_size()
        self._width = terminalSize.columns
        self._height = terminalSize.lines

    def addObject(self, obj):
        """
        Add an object to the frame
        """
        self._objects.append(obj)

    def updateFPS(self, fps):
        """
        Update FPS
        """
        self._FPS = fps

    def draw(self):
        """
        This method draws each frame
        """
        print(f"{self._width}x{self._height}")

    def start(self):
        """
        Start rendering objects on the screen
        """
        delta = 1/self._FPS

        while True:
            # Clear screen and update terminal size
            clearScreen()
            terminalSize = os.get_terminal_size()
            self._width = terminalSize.columns
            self._height = terminalSize.lines
            self.draw()

            time.sleep(delta)
            