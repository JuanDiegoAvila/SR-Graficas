from gl import *
from vector import V3
from shaders import * 

glCreateWindow(1024, 1024)

# color negro de fondo
glClearColor(1, 1, 1)
glClear()

# crea un viewport de 1024 x 1024
glViewPort(0, 0, 1024, 1024)

glLookAt((0, 0, 100), (0, 0, 0), (0, 1, 0))

#glTexture('./modelos_prueba/earth.bmp')
glShader(planeta)
# renderiza el objeto con su estala, traslación y rotación
glRenderObject('./modelos_prueba/earth.obj', scale = (0.001, 0.001, 0.009), translate = (0, 0, 0), rotate = (0, 0, 0))

# escribe el bmp
glFinish('lab2.bmp')


