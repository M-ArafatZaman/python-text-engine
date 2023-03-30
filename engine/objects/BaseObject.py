from ..TYPES import FrameInstance
from typing import Callable

"""
An abstract base object that defines each component on the screen
"""
class BaseObject:
    def __init__(
            self,
            canBeRendered = True,
    ):
        self._canBeRendered = canBeRendered
        self._updateFn: list[ Callable[[BaseObject, int]] ] = []
        self.FRAME_WIDTH: int | None = None
        self.FRAME_HEIGHT: int | None = None

    def update(self, fn: Callable):
        """
        A decorator to add a function that is executed whenever the Frame requests an update
        
        The decorated function will also have access to instance context
        """
        def decoratedFn(*args, **kwargs):
            fn(*args, **kwargs)
        self._updateFn.append(decoratedFn)
        return decoratedFn
    
    def performUpdates(self, frameWidth: int, frameHeight: int):
        """
        The function that is called to perform all the updates attached to this base object
        """
        self.FRAME_WIDTH = frameWidth
        self.FRAME_HEIGHT = frameHeight
        [update(self) for update in self._updateFn]

    def requestFrame(self, frame: FrameInstance):
        """
        A method to request a frame instance of an object.
        The frame instance will allow the frame to draw the element
        """
        raise NotImplementedError("update() is not implemented. Either this is an abstract class or it has not been implemented yet.")
    
    