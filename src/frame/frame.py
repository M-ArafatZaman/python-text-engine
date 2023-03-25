import time
from ..objects.BaseObject import BaseObject
from ..utils.screen import clearScreen
import os
from ..TYPES import FrameInstance
from .FrameExtension import FrameExtension

"""
A frame object that decides how to and what to draw on the screen
"""
class Frame:
    def __init__(self):
        self._objects: list[BaseObject] = []
        self._FPS = 15
        # Frame is simply a 2D list that represents each "pixel" in the screen
        self._frame: FrameInstance = [[]]
        self.updateDimensions()
        self.clearFrame()
        # Some third party components that can be attached to the frame
        self._extensions: list[FrameExtension] = []

    def addObject(self, obj: BaseObject):
        """
        Add an object to the frame
        """
        self._objects.append(obj)

    def updateFPS(self, fps):
        """
        Update FPS
        """
        self._FPS = fps

    def updateDimensions(self):
        """
        Method to update the dimensions
        """
        terminalSize = os.get_terminal_size()
        self._width = terminalSize.columns
        self._height = terminalSize.lines

    @staticmethod
    def getFrame(frame) -> str:
        """
        Converts the frame object to a string
        """
        # Get a copy of the frame
        frame: list[list[str]] = list(frame)
        rows: list[str] = [''.join(row) for row in frame]
        return '\n'.join(rows)

    def clearFrame(self):
        """
        Clears the frame instance
        """
        self._frame: FrameInstance = [[' ' for _ in range(self._width)] for i in range(self._height)]

    def draw(self):
        """
        This method draws each frame
        """
        # Update each object
        for obj in self._objects:
            if obj._canBeRendered:
                obj.performUpdates(self._width, self._height)
                obj.requestFrame(self._frame)

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
            self.updateDimensions()
            self.clearFrame()
            # Update all extensions
            for ext in self._extensions:
                ext.requestUpdate()

            self.draw()

            time.sleep(delta)

    def registerExtension(self, ext: FrameExtension):
        """
        Add an extension to the frame
        """
        self._extensions.append(ext)


            