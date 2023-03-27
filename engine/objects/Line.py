from .BaseObject import BaseObject
from ..TYPES import FrameInstance
from math import atan

"""
A line object
"""
class LineObject(BaseObject):
    """
    A line object is a static line object that has no physics
    The x1, x2, y1, y2 are the x and y coordinates of each end.
    The char is the character used to print the line into the console
    """
    def __init__(
        self,
        canBeRendered: bool = True,
        x1: int = 0,
        y1: int = 0,
        x2: int = 0,
        y2: int = 0,
        static: bool = True,
        char: str = "-"
    ):
        super().__init__(canBeRendered)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.static = static
        self._char = char

    def requestFrame(self, frame: FrameInstance):
        """
        Draw the line onto the frame
        
        We need to consider that the line can be outside of the screen,
        In which case we ignore any render
        """
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2

        # Check if the x and y is supposed to by dynamic
        if x1 <= 1:
            x1 = int(x1 * self.FRAME_WIDTH)
        
        if y1 <= 1:
            y1 = int(y1 * self.FRAME_HEIGHT)
        
        if x2 <= 1:
            x2 = int(x2 * self.FRAME_WIDTH)
        
        if y2 <= 1:
            y2 = int(y2 * self.FRAME_HEIGHT)

        # Check if the rectangle is still within the bounds of the frame
        if x1 < 0 and x2 < 0:
            return
        if x1 >= self.FRAME_WIDTH and x2 >= self.FRAME_WIDTH:
            return
        if y1 < 0 and y2 < 0:
            return
        if y1 >= self.FRAME_HEIGHT and y2 >= self.FRAME_HEIGHT:
            return
        
        # Some maths
        inverse_gradient = (x2-x1)/(y2-y1)

        START_Y = round(max(min(y1,y2), 0))
        END_Y = round(min(max(y1,y2), self.FRAME_HEIGHT-1))
        START_X = round(max(min(x1,x2), 0))
        END_X = round(min(max(x1,x2), self.FRAME_WIDTH-1))

        last_x = START_X
        _x = -1
        for y in range(START_Y, END_Y):
            for x in range(last_x, END_X):
                _x = round(inverse_gradient * y)

                if _x > x:
                    frame[y][x] = self._char
                else:
                    frame[y][_x] = self._char
                    last_x = x+1
                    break


