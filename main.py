from src.frame.frame import Frame
from src.objects.Rectangle import RectangleObject
from src.controller.controller import KeyboardController

app = Frame()

Square = RectangleObject(
    x=.2, y=.2,
    width=.5, height=.5, fill=False
)

app.addObject(Square)

controller = KeyboardController()
app.registerExtension(controller)

@Square.update
@controller.on_press("w")
def moveUp(obj: RectangleObject):
    Square.moveUp()

@Square.update
@controller.on_press("s")
def moveDown(obj: RectangleObject):
    Square.moveDown()

@Square.update
@controller.on_press("a")
def moveLeft(obj: RectangleObject):
    Square.moveLeft()

@Square.update
@controller.on_press("d")
def move_right(obj: RectangleObject):
    Square.moveRight()


app.start()