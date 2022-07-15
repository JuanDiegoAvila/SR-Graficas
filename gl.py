from lib2to3.pytree import convert
import render

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
        "width" : width,
        "height" : height
    }

def glClear():
    global r
    r.clear()

def glClearColor(red, green, blue):
    global r
    r.set_clear_color(red, green, blue)

def glVertex(x, y):
    global r

    if x < -1 or x > 1 or y < -1 or y > 1:
        return
    
    adjusted_x = x + 1
    adjusted_y = y + 1

    converted_x = (adjusted_x * r.viewport["width"])/2
    converted_y = (adjusted_y * r.viewport["height"])/2

    final_x = int(converted_x + r.viewport["x"])
    final_y = int(converted_y + r.viewport["y"])

    r.point(final_x, final_y)

def glColor(red, green, blue):
    global r
    r.set_current_color(red, green, blue)

def glFinish():
    global r
    r.write('a.bmp')
