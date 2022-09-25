from gl import *
from vector import V3
from shaders import * 

glCreateWindow(1024, 1024)

# color negro de fondo
glClearColor(0, 0, 0)
glClear()

# crea un viewport de 1024 x 1024
glViewPort(0, 0, 1024, 1024)

glLookAt((0, 0, 100), (0, 0, 0), (0, 1, 0))

glBackground(Texture('./modelos_prueba/space.bmp'))
#glTexture('./modelos_prueba/earth.bmp')
glShader(planeta)
# renderiza el objeto con su estala, traslación y rotación
glRenderObject('./modelos_prueba/earth.obj', scale = (0.0007, 0.0007, 0.0007), translate = (0, 0, 0), rotate = (0, 0, 0))

# escribe el bmp
glFinish('lab2.bmp')


