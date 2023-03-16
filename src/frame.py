import time
from .objects.BaseObject import BaseObject
from .utils.screen import clearScreen
import os

"""
A frame object that decides how to and what to draw on the screen
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"
class Frame:
    def __init__(self):
        self._objects: list[BaseObject] = []
        self._FPS = 15
        terminalSize = os.get_terminal_size()
        self._width = terminalSize.columns
        self._height = terminalSize.lines
        # Frame is simply a 2D list that represents each "pixel" in the screen
        self._frame = [[' ' for _ in range(self._width)] for i in range(self._height)]

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

    @staticmethod
    def getFrame(frame) -> str:
        """
        Converts the frame object to a string
        """
        # Get a copy of the frame
        frame: list[list[str]] = list(frame)
        rows: list[str] = [''.join(row) for row in frame]
        return '\n'.join(rows)

    def draw(self):
        """
        This method draws each frame
        """
        # Get a copy of the frame
        frameScreen = self.getFrame(self._frame)
        print(frameScreen)

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
            