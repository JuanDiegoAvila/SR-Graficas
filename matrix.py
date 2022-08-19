class matriz(object):
  def __init__(self, matriz):
    self.matriz = matriz
  
  def __add__(self, other):
    try:
      for y in range(len(self.matriz)):
        for x in range(len(self.matriz[y])):
          self.matriz[x][y] += other.matriz[x][y]
      return self.matriz

    except:
      print('Error de suma!')

  def __sub__(self, other):
    try:
      for y in range(len(self.matriz)):
        for x in range(len(self.matriz[y])):
          self.matriz[x][y] -= other.matriz[x][y]
      return self.matriz

    except:
      print('Error de suma!')