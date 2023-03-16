import time

"""
A frame object that decides how to and what to draw on the screen
"""
class Frame:
    def __init__(self):
        self._objects = []
        self._FPS = 20

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

    def draw(self):
        """
        This method draws each frame
        """
        pass

    def start(self):
        """
        Start rendering objects on the screen
        """
        delta = 1/self._FPS
        self._i = 0
        while True:
            self.draw()

            time.sleep(delta)
            