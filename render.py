from writeUtils import *
from color import *

class Render(object):

  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.current_color = color(0, 0, 0)
    self.clear()
  
  def clear(self):
    self.framebuffer = [
      [self.current_color for x in range(self.width)]
      for y in range(self.height)
    ]

  def clear_color(self, r, g, b):
    self.current_color = color(r, g, b)
    self.clear()

  def write(self, filename):
    f = open(filename, 'bw')

    # pixel header
    f.write(char('B'))
    f.write(char('M'))
    f.write(dword(14 + 40 + self.width * self.height * 3))
    f.write(word(0))
    f.write(word(0))
    f.write(dword(14 + 40))

    # info header
    f.write(dword(40))
    f.write(dword(self.width))
    f.write(dword(self.height))
    f.write(word(1))
    f.write(word(24))
    f.write(dword(0))
    f.write(dword(self.width * self.height * 3))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))

    # pixel data
    for x in range(self.width):
      for y in range(self.height):
        f.write(self.framebuffer[x][y])

    f.close()

  def point(self, x, y):
    self.framebuffer[x][y] = self.current_color

  def line(self, x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    # Si es empinado, poco movimiento en x y mucho en y.
    steep = dy > dx 

    # Se invierte si es empinado
    if steep: 
      x0, y0 = y0, x1
      x1, y1 = y1, x1 

    # Si la linea tiene direccion contraria, invertir
    if x0 > x1: 
      x0, x1 = x1, x0
      y0, y1 = y1, y0

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    offset = 0 
    threshold= dx
    y = y0

    for x in range(x0, x1):
      offset += dy * 2

      if offset >= threshold:
        y += 1 if y0 < y1 else -1
      
        threshold += dx * 2

      if steep:
        r.point(y, x)
      else:
        r.point(x, y)

r = Render(100, 100)

r.current_color = color(0, 250, 250)
  
#linea(20, 13, 40, 80)
#linea(80, 40, 13, 20)
r.line(20, 40, 4, 50)
#linea(13, 20, 80, 40)

r.write('a.bmp')