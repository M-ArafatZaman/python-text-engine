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

    def update(self, fn: Callable):
        """
        A decorator to add a function that is executed whenever the Frame requests an update
        
        The decorated function will also have access to instance context
        """
        def decoratedFn(self, *args, **kwargs):
            fn(self, *args, **kwargs)
        self._updateFn.append(decoratedFn)
        return decoratedFn
    
    def performUpdates(self):
        """
        The function that is called to perform all the updates attached to this base object
        """
        [update(self) for update in self._updateFn]

    def requestFrame(self, frame: FrameInstance, frameWidth: int, frameHeight: int):
        """
        A method to request a frame instance of an object.
        The frame instance will allow the frame to draw the element
        """
        raise NotImplementedError("update() is not implemented. Either this is an abstract class or it has not been implemented yet.")
    
    