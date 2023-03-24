from ..frame.FrameExtension import FrameExtension
from pynput import keyboard

class KeyboardController(FrameExtension):
    def __init__(self):
        self.pressed: dict[str, bool] = {}

        def on_press(key: keyboard.Key | keyboard.KeyCode | None):
            try:
                self.pressed[key.char] = True
            except AttributeError:
                pass

        def on_release(key: keyboard.Key | keyboard.KeyCode | None):
            self.pressed[key.char] = False
            
        listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release
        )
        listener.start()

    def requestUpdate(self):
        """
        Every frame updates what character is currently active
        """
        pass

    def on_press(self, key: str):
        if len(key) != 1:
            raise Exception("Can only listen for one character updates.")
        
        def wrapper(fn):

            def decorated(*args, **kwargs):
                if key in self.pressed and self.pressed[key] == True:
                    fn(*args, **kwargs)
            return decorated
        return wrapper