from ..TYPES import FrameInstance

"""
An abstract base object that defines each component on the screen
"""
class BaseObject:
    def __init__(
            self,
            canBeRendered = True,
    ):
        self._canBeRendered = canBeRendered

    def update(self, delta: int):
        """
        A method to update the object
        """
        raise NotImplementedError("update() is not implemented. Either this is an abstract class or it has not been implemented yet.")

    def requestFrame(self, frame: FrameInstance, frameWidth: int, frameHeight: int):
        """
        A method to request a frame instance of an object.
        The frame instance will allow the frame to draw the element
        """
        raise NotImplementedError("update() is not implemented. Either this is an abstract class or it has not been implemented yet.")
    
    