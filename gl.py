import render
import math
from polygon import *
from vertex import Vertex as V

r = None

def glInit():
    pass

def glCreateWindow(width, height):
    global r
 
    w = width % 4
    adjusted_width = width

    if w != 0:
        adjusted_width = width + width % 4

    r = render.Render(adjusted_width, height)

def glViewPort(x, y, width, height):
    global r

    r.viewport = {
        "x" : x,
        "y" : y,
        "width" : width if width < r.width else r.width - x - 1,
        "height" : height if height < r.height else r.height - y - 1
    }

def glClear():
    global r
    r.clear()

def glClearColor(red, green, blue):
    global r
    r.set_clear_color(red, green, blue)

def glVertex(x, y):
    global r

    r.point(* r.convert_coordinates(x, y))

def glLine(x0, y0, x1, y1):
    global r

    r.line(
        * r.convert_coordinates(x0, y0), 
        * r.convert_coordinates(x1, y1)
    )

def glColor(red, green, blue):
    global r
    r.set_current_color(red, green, blue)

def glFinish(name):
    global r
    r.write(name)

def glRawPoint(x, y):
    global r
    r.point(x, y)

def glRenderObject(name, scale_factor, translate_factor):
    global r
    r.generate_object(name, scale_factor, translate_factor)

def glRawLine(x0, y0, x1, y1):
    global r
    r.line(math.floor(x0), math.floor(y0), math.floor(x1), math.floor(y1))
    r.line(math.ceil(x0), math.ceil(y0), math.ceil(x1), math.ceil(y1))

def glScale(c, cord, factor):
    return (((cord - c)* factor) + c)

def glDrawPolygon(points):
    draw_polygon(points)