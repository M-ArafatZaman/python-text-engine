"""
An abstract base object that defines each component on the screen
"""
class BaseObject:
    def __init__(
            self,
            canBeRendered = True,
    ):
        self._canBeRendered = canBeRendered

    def update(self):
        """
        A method to update the object
        """
        pass

    def requestFrame(self):
        """
        A method to request a frame instance of an object.
        The frame instance will allow the frame to draw the element
        """
        pass
    
    