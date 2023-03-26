from src.frame.frame import Frame
from src.objects.Rectangle import RectangleObject
from src.objects.Line import LineObject
from src.controller.controller import KeyboardController

app = Frame()

controller = KeyboardController()
app.registerExtension(controller)

line = LineObject(
    x1=.05, x2=.8,
    y1=.05, y2=.5
)

app.addObject(line)

app.start()