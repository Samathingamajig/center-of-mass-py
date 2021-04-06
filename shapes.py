"""
Global Constants
"""
# Directions
# all are powers of 2 so that combinations can be used
UP = 1
DOWN = 2
LEFT = 4
RIGHT = 8

# PI mathematical constant (change for more precision)
PI = 3.14

"""
Shapes Container
"""

shapes = []


def reset_shapes():
    shapes.clear()


"""
Parent Class
"""


class Shape:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError

    def x(self) -> float:
        raise NotImplementedError

    def y(self) -> float:
        raise NotImplementedError


"""
Derived Shape Classes
"""


class Rect(Shape):
    def __init__(
        self, x: float, y: float, width: float, height: float, inverted: bool = False
    ):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mInverted = -1 if inverted else 1

    def area(self) -> float:
        return self.mWidth * self.mHeight * self.mInverted

    def x(self) -> float:
        return self.mX + (self.mWidth / 2)

    def y(self) -> float:
        return self.mY + (self.mHeight / 2)


class RightTriangle(Shape):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        direction: int,
        inverted: bool = False,
    ):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mDir = direction
        self.mInverted = -1 if inverted else 1

    def area(self) -> float:
        return 1 / 2 * self.mWidth * self.mHeight * self.mInverted

    def x(self) -> float:
        return self.mX + (self.mWidth / 3) * (-1 if self.mDir & LEFT else 1)

    def y(self) -> float:
        return self.mY + (self.mHeight / 3) * (-1 if self.mDir & DOWN else 1)


class SemiCircle(Shape):
    def __init__(
        self, x: float, y: float, radius: float, direction: int, inverted: bool = False
    ):
        self.mX = x
        self.mY = y
        self.mRadius = radius
        self.mDir = direction
        self.mInverted = -1 if inverted else 1

    def area(self) -> float:
        return PI * self.mRadius ** 2 / 2 * self.mInverted

    def x(self) -> float:
        if self.mDir in (UP, DOWN):
            return self.mX
        return self.mX + (4 * self.mRadius / 3 / PI) * (-1 if self.mDir == RIGHT else 1)

    def y(self) -> float:
        if self.mDir in (LEFT, RIGHT):
            return self.mY
        return self.mY + (4 * self.mRadius / 3 / PI) * (-1 if self.mDir == DOWN else 1)


"""
Simple Function Versions
"""


def rect(x: float, y: float, width: float, height: float):
    shapes.append(Rect(x, y, width, height))


def irect(x: float, y: float, width: float, height: float):
    shapes.append(Rect(x, y, width, height, inverted=True))


def tri(x: float, y: float, width: float, height: float, direction: float):
    shapes.append(RightTriangle(x, y, width, height, direction))


def itri(x: float, y: float, width: float, height: float, direction: float):
    shapes.append(RightTriangle(x, y, width, height, direction, inverted=True))


def semi(x: float, y: float, radius: float, direction: int):
    shapes.append(SemiCircle(x, y, radius, direction))


def isemi(x: float, y: float, radius: float, direction: int):
    shapes.append(SemiCircle(x, y, radius, direction, inverted=True))


"""
Overall Calculations
"""


def calculateX() -> float:
    top = sum(shape.x() * shape.area() for shape in shapes)
    bottom = sum(shape.area() for shape in shapes)
    return top / bottom


def calculateY() -> float:
    top = sum(shape.y() * shape.area() for shape in shapes)
    bottom = sum(shape.area() for shape in shapes)
    return top / bottom


def calculate():
    return calculateX(), calculateY()
