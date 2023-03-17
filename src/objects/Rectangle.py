from .BaseObject import BaseObject
from ..TYPES import FrameInstance

"""
A rectangle object
"""
class RectangleObject(BaseObject):
    """
    A rectangle object is a static rectangle object that does has no physics
    The x and y coordinates are the top left corner of the rectangle.
    The width and height are measured in terms of columns and lines.
    The char is the character used to print the rectangle into the console
    """
    def __init__(
        self,
        canBeRendered: bool = True,
        x: int = 0,
        y: int = 0,
        width: int = 5,
        height: int = 5,
        static: bool = True,
        char: str = "#"
    ):
        super().__init__(canBeRendered)
        self.x = x
        self.y = y
        self._width = width
        self._height = height
        self.static = static
        self._char = char

    def update(self, delta: int):
        pass

    def requestFrame(self, frame: FrameInstance, frameWidth: int, frameHeight: int):
        """
        Draw the rectangle onto the frame
        
        We need to consider that x and y can be outside of the screen,
        In which case we ignore any render
        """
        if self.x > frameWidth or (self.x + self._width) < 0:
            return
        if self.y > frameHeight or (self.y + self._height) < 0:
            return
        

        
