from engine.frame.frame import Frame
from engine.objects.Rectangle import RectangleObject
from engine.objects.Line import LineObject
from engine.controller.controller import KeyboardController

app = Frame()

controller = KeyboardController()
app.registerExtension(controller)

obj = RectangleObject(
    x=.1, y=.2,
    width=5, height=10, fill=False
)

@obj.update
@controller.on_press("w")
def moveUp():
    obj.moveUp(1)

@obj.update
@controller.on_press("s")
def moveDown():
    obj.moveDown(1)

@obj.update
@controller.on_press("a")
def moveLeft():
    obj.moveLeft(1)

@obj.update
@controller.on_press("d")
def moveRight():
    obj.moveRight(1)

app.addObject(obj)

app.start()