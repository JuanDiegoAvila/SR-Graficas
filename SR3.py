import Obj
from gl import *

# definicion de pantalla con resolucion 1024 x 1024
glCreateWindow(1024, 1024)

# color blanco de fondo
glClearColor(1, 1, 1)
glClear()

# color de imagen rojo
glColor(0, 0, 0)

glRenderObject('batman.obj', (5, 5, 40), (500, 200, 200))

glFinish('SR3.bmp')
