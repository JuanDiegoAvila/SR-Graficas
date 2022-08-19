import Obj
from gl import *


# definicion de pantalla con resolucion 1024 x 1024
glCreateWindow(1024, 1024)

# color blanco de fondo
glClearColor(0, 0, 0)
glClear()

# color de imagen rojo
glColor(0, 0, 0)

glRenderObject('batman.obj', (5, 5, 25), (500, 200, 0))
#glRenderObject('3d-model.obj', (2, 2, 5), (500, 200, 200))
#glRenderObject('model.obj', (500, 500, 500), (500, 500, 500))

glFinish('SR4.bmp')
glFinishZ('zBuffer-SR4.bmp')

