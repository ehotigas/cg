from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from typing import (
    List,
    Tuple
)
from math import (
    sin,
    cos
)


def glHandler(handler):
    def wapper(*args, **kwargs):
        handler(*args, **kwargs)
        glutPostRedisplay()
    return wapper

class OpenGLMouseHandlerInterface:
    @glHandler
    def onClick(
        self,
        button: int,
        state: int,
        x: int,
        y: int
    ) -> None: pass

class OpenGLKeyboardHanderInterface:
    @glHandler
    def onPress(
        self,
        key: bytes,
        x: int,
        y: int
    ) -> None: pass

class OpenGLSpecialKeyboardHandlerInterface:
    @glHandler
    def onPress(
        self,
        key: bytes,
        x: int,
        y: int
    ) -> None: pass

class OpenGLDisplayHandlerInterface:
    def display(self) -> None: pass

class GlPoint:
    _x: float
    _y: float
    def __init__(
        self,
        x: float,
        y: float
    ) -> None:
        self._x = x
        self._y = y
    
    @property
    def x(self) -> float:
        return self._x
    
    @property
    def y(self) -> float:
        return self._y
    
    def toTuple(self) -> Tuple[float]:
        return self._x, self._y

class Point:
    _x: int
    _y: int

    def __init__(
        self,
        x: int,
        y: int
    ) -> None:
        self._x = x
        self._y = y
    
    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y

def pointToGLPoint(
    point: Point
) -> GlPoint:
    x = 2 * point.x / glutGet(GLUT_SCREEN_WIDTH) - 1
    y = (-2 * point.y / glutGet(GLUT_SCREEN_HEIGHT)) + 1
    return GlPoint(x, y)

def vertex2f(point: Point) -> None:
    glVertex2f(*pointToGLPoint(point).toTuple())

class Circle:
    _center: Point
    _radious: int
    def __init__(
        self,
        center: Point,
        radious: int
    ) -> None:
        self._center = center
        self._radious = radious

    @property
    def center(self) -> Point:
        return self._center
    
    @property
    def radious(self) -> int:
        return self._radious
    
    @center.setter
    def center(self, center: Point) -> None:
        self._center = center
    
    @radious.setter
    def radious(self, radious: int) -> None:
        self._radious = radious
    
    def draw(self) -> None:
        glBegin(GL_LINE_LOOP)
        for i in range(360):
            theta = 2 * 3.1415926 * i / 360
            x = self._radious * cos(theta)
            y = self._radious * sin(theta)
            vertex2f(Point(x + self._center.x, y + self._center.y))
        glEnd()

class Flower:
    _center: Point
    _components: List[Circle]
    def __init__(
        self,
        center: Point
    ) -> None:
        self._center = center

    @property
    def center(self) -> Point:
        return self._center
    
    @center.setter
    def center(
        self,
        center: Point
    ) -> None:
        self._center = center

    
    def display(
        self
    ) -> None:
        glMatrixMode(GL_MODELVIEW)
        Circle(self._center, 20).draw()
        glRotatef(10, 0, 0, 1)
        glLoadIdentity()

class Window:
    _width: int
    _height: int
    _startPositionX: int
    _startPositionY: int
    _name: str
    _displayMode: Constant
    _flower: Flower
    def __init__(
        self,
        width: int=400,
        height: int=400,
        startPositionX: int=100,
        startPositionY: int=50,
        name: str='Untitled',
        displayMode: Constant=GLUT_RGBA | GLUT_SINGLE
    ) -> None:
        self._name = name
        self._width = width
        self._height = height
        self._displayMode = displayMode
        self._startPositionX = startPositionX
        self._startPositionY = startPositionY
        self._flower = Flower(Point(self._width/2, self._height/2))

        glutInit()
        glutInitDisplayMode(displayMode)
        glutInitWindowPosition(startPositionX, startPositionY)
        glutInitWindowSize(width, height)
        glutCreateWindow(name)

    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height

    @property
    def startPositionX(self) -> int:
        return self._startPositionX

    @property
    def startPositionY(self) -> int:
        return self._startPositionY
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def displayMode(self) -> int:
        return self._displayMode

    @property
    def flower(self) -> Flower:
        return self._flower
    
    @flower.setter
    def flower(
        self,
        flower: Flower
    ) -> None:
        self._flower = flower
    
    def setMouseHandler(
        self,
        MouseHandler: OpenGLMouseHandlerInterface
    ) -> None:
        instance = MouseHandler(self)
        glutMouseFunc(instance.onClick)
    
    def setKeyboardHandler(
        self,
        KeyboardHandler: OpenGLKeyboardHanderInterface
    ) -> None:
        instance = KeyboardHandler(self)
        glutKeyboardFunc(instance.onPress)
    
    def setSpecialKeyboardHandler(
        self,
        SpecialKeyboardHandler: OpenGLSpecialKeyboardHandlerInterface
    ) -> None:
        instance = SpecialKeyboardHandler(self)
        glutSpecialFunc(instance.onPress)

    def setDisplayHandler(
        self,
        DisplayHandler: OpenGLDisplayHandlerInterface
    ) -> None:
        instance = DisplayHandler(self)
        glutDisplayFunc(instance.display)

    def mainLoop(self) -> None:
        glutMainLoop()


class MouseHandler(OpenGLMouseHandlerInterface):
    _window: Window

    def __init__(
        self,
        window: Window
    ) -> None:
        self._window = window

    @property
    def window(self) -> Window:
        return self._window

    @glHandler
    def onClick(
        self,
        button: int,
        state: int,
        x: int,
        y: int
    ) -> None:
        pass



class KeyboardHandler(OpenGLKeyboardHanderInterface):
    _window: Window

    def __init__(
        self,
        window: Window
    ) -> None:
        self._window = window

    @property
    def window(self) -> Window:
        return self._window

    @glHandler
    def onPress(
        self,
        key: str,
        x: int,
        y: int
    ) -> None:
        pass

class SpecialKeyboardHandler(OpenGLSpecialKeyboardHandlerInterface):
    _window: Window

    def __init__(
        self,
        window: Window
    ) -> None:
        self._window = window
    
    @property
    def window(self) -> Window:
        return self._window
    
    @glHandler
    def onPress(
        self,
        key: bytes,
        x: int,
        y: int
    ) -> None:
        pass



class DisplayHandler(OpenGLDisplayHandlerInterface):
    _window: Window

    def __init__(
        self,
        window: Window
    ) -> None:
        self._window = window

    @property
    def window(self) -> Window:
        return self._window

    def display(self) -> None:
        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        
        glColor(0, 0, 0)
        # glBegin(GL_LINES)
        # glVertex2d(*self.pointToGLPoint(self._window._line.p1).toTuple())
        # glVertex2d(*self.pointToGLPoint(self._window._line.p2).toTuple())
        # glEnd()
        self.window.flower.display()
        Circle(Point(200, 200), 40).draw()
        
        glFlush()


def main() -> None:
    win = Window(name="Ex01")
    win.setKeyboardHandler(KeyboardHandler)
    win.setMouseHandler(MouseHandler)
    win.setSpecialKeyboardHandler(SpecialKeyboardHandler)
    win.setDisplayHandler(DisplayHandler)
    win.mainLoop()


if __name__ == "__main__":
    main()
