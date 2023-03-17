from src.frame import Frame
from src.objects.Rectangle import RectangleObject

app = Frame()

Square = RectangleObject(
    x=10, y=10,
    width=10, height=10
)

app.addObject(Square)

app.start()