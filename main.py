from engine.frame.frame import Frame
from engine.objects.Rectangle import RectangleObject
from engine.objects.Line import LineObject
from engine.controller.controller import KeyboardController

app = Frame()

controller = KeyboardController()
app.registerExtension(controller)

line = LineObject(
    x1=.05, x2=.8,
    y1=.05, y2=.8
)

app.addObject(line)

app.start()