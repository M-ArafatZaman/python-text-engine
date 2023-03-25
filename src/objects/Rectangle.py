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
        char: str = "#",
        fill: bool = True
    ):
        super().__init__(canBeRendered)
        self.x = x
        self.y = y
        self._width = width
        self._height = height
        self.static = static
        self._char = char
        self._fill = fill

    def requestFrame(self, frame: FrameInstance):
        """
        Draw the rectangle onto the frame
        
        We need to consider that x and y can be outside of the screen,
        In which case we ignore any render
        """
        width = self._width
        height = self._height

        x = self.x
        y = self.y

        # Check if the x and y is supposed to by dynamic
        if x <= 1:
            x = int(self.x * self.FRAME_WIDTH)
        
        if y <= 1:
            y = int(self.y * self.FRAME_HEIGHT)

        # Check if the width is supposed to be dynamic
        if width <= 1:
            width = int(width * self.FRAME_WIDTH)
        
        if height <= 1:
            height = int(height * self.FRAME_HEIGHT)

        # Check if the rectangle is still within the bounds of the frame
        if x >= self.FRAME_WIDTH or (x + width) < 0:
            return
        if y >= self.FRAME_HEIGHT or (y + height) < 0:
            return
        
        START_Y = max(y, 0)
        END_Y = min(y + height, self.FRAME_HEIGHT-1)
        START_X = max(x, 0)
        END_X = min(x + width, self.FRAME_WIDTH - 1)
        
        if self._fill:
            # Print the entire grid
            for y in range(START_Y, END_Y):
                for x in range(START_X, END_X):
                    frame[y][x] = self._char

        else:
            # Print the borders
            # Vertifcal borders
            for y in range(START_Y, END_Y):
                frame[y][START_X] = self._char
                frame[y][END_X-1] = self._char
            
            # Horizontal borders
            for x in range(START_X, END_X):
                frame[START_Y][x] = self._char
                frame[END_Y-1][x] = self._char

    # Methods to move the rectangle
    def moveUp(self, length=1):
        if self.y < 1: self.y -= length/self.FRAME_HEIGHT
        else: self.y -= length

    def moveDown(self, length=1):
        if self.y < 1: self.y += length/self.FRAME_HEIGHT
        else: self.y += length

    def moveLeft(self, length=1):
        if self.x < 1: self.x -= length/self.FRAME_WIDTH 
        else: self.x -= length
    
    def moveRight(self, length=1):
        if self.x < 1: self.x += length/self.FRAME_WIDTH
        else: self.x += length

