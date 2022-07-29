class Vertex(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return "(%s, %s)" % (self.x, self.y)

  def __mul__(self, other):
    return Vertex(self.x * other.x,  self.y * other.y)

vertex = Vertex(3, 3)
vertex2 = Vertex(1, 1)
print(vertex * vertex2)