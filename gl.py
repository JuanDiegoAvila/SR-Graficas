import render
import math

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

def glRawLine(x0, y0, x1, y1):
    global r
    r.line(math.floor(x0), math.floor(y0), math.floor(x1), math.floor(y1))
    r.line(math.ceil(x0), math.ceil(y0), math.ceil(x1), math.ceil(y1))

def glScale(c, cord, factor):
    return (((cord - c)* factor) + c)

def glDrawPolygon(points):
    temp = None

    minX = min([x for x, y in points])
    maxX = max([x for x, y in points])
    minY = min([y for x, y in points])
    maxY = max([y for x, y in points])
    
    centerX = ((maxX - minX) / 2) + minX
    centerY = ((maxY - minY) / 2) + minY

    ff = 1000
    for j in range(ff):
        factor = (ff - j) /ff
        for i in range(len(points)):
            if temp:
                glRawLine(  
                    glScale(centerX, temp[0], factor),
                    glScale(centerY, temp[1], factor),
                    glScale(centerX, points[i][0], factor),
                    glScale(centerY, points[i][1], factor)
                )
                glRawLine(  
                    glScale(centerX + 1, temp[0], factor),
                    glScale(centerY, temp[1], factor),
                    glScale(centerX + 1, points[i][0], factor),
                    glScale(centerY, points[i][1], factor)
                )
            temp = points[i]
            
            if i == len(points) -1:
                glRawLine(  
                    glScale(centerX + 1, temp[0], factor),
                    glScale(centerY, temp[1], factor),
                    glScale(centerX + 1, points[0][0], factor),
                    glScale(centerY, points[0][1], factor)
                )