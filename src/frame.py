
"""
A frame object that decides how to and what to draw on the screen
"""
class Frame:
    def __init__(self):
        self._objects = []

    def addObject(self, obj):
        """
        Add an object to the frame
        """
        self._objects.append(obj)

    def draw(self):
        pass