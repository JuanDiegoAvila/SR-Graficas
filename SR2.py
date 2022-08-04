from gl import *
import vector

# definicion de pantalla con resolucion 1024 x 1024
glCreateWindow(400, 400)

# color blanco de fondo
glClearColor(1, 1, 1)
glClear()

# creacion de viewport en el centro 
glViewPort(12, 12, 1000, 1000)

# color de imagen rojo
glColor(0.7, 0, 0)

# definicion de la casa

# chimenea pared izquierda

glColor(0.7, 0, 0)


x0 = 0
y0 = 0.335
x1 = 0
y1 = 0.5

temp = None
for i in range(500):
  x0 += 0.0001
  x1 += 0.0001  
  y0 -= 0.0001
  y1 -= 0.0001
  glLine(x0, y0, x1, y1)

  temp = [x0, y0, x1, y1]

# chimenea pared frontal

glColor(0.86, 0, 0)

for i in range(800):
  x0 += 0.0001
  x1 += 0.0001  
  y0 -= 0.0001

  glLine(x0, y0, x1, y1)

# chimenea parte de arriba
glColor(0.96, 0, 0)

x0 = 0
y0 = 0.5
x1 = 0.08
y1 = 0.5

for i in range(500):
  x0 += 0.0001
  x1 += 0.0001  
  y0 -= 0.0001
  y1 -= 0.0001
  glLine(x0, y0, x1, y1)

# pared izquierda

glColor(0.7, 0, 0)

x0 = -0.1
y0 = -0.9
x1 = -0.1
y1 = -0.3

for i in range(4000):
  x0 -= 0.0001
  x1 -= 0.0001  
  y0 += 0.0001
  y1 += 0.0001
  glLine(x0, y0, x1, y1)

# pared frontal

glColor(0.86, 0, 0)

x0 = -0.1
y0 = -0.9
x1 = -0.1
y1 = -0.3

for i in range(5500):
  x0 += 0.0001
  x1 += 0.0001  
  y0 += 0.00005
  y1 += 0.00005
  glLine(x0, y0, x1, y1)

# puerta blanca

glColor(1, 1, 1)

x0 = 0.15
y0 = -0.775
x1 = 0.15
y1 = -0.5

for i in range(1000):
  x0 += 0.0001
  x1 += 0.0001  
  y0 += 0.00005
  y1 += 0.00005
  glLine(x0, y0, x1, y1)

# techo lado izquierdo

glColor(0.96, 0, 0)

x0 = -0.5
y0 = 0.105
x1 = -0.2
y1 = 0.505

temp = None

for i in range(4000):
  x0 += 0.0001
  x1 += 0.0001  
  y0 -= 0.0001
  y1 -= 0.00009
  glLine(x0, y0, x1, y1)

  temp = x0

# pared triangular

glColor(0.86, 0, 0)

x0 = -0.1
y0 = -0.3
x1 = -0.1
y1 = -0.3

temp = None

for i in range(3050):
  glLine(x0, y0, x1, y1)
  x0 += 0.0001
  x1 += 0.0001  
  y0 += 0.000145
  y1 += 0.00005

  temp = [x0, x1, y0, y1]

x0 = temp[0]
x1 = temp[1]
y0 = temp[2]
y1 = temp[3]

for i in range(2380):
  glLine(x0, y0, x1, y1)
  x0 += 0.0001
  x1 += 0.0001
  y0 -= 0.00007
  y1 += 0.00005




glFinish('casa.bmp')
