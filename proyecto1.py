from gl import *
from shaders import * 

glCreateWindow(1024, 1024)

# color negro de fondo
glClearColor(0, 0, 0)
glClear()

# crea un viewport de 1024 x 1024
glViewPort(0, 0, 1024, 1024)

glLookAt((0, 0, 100), (0, 0, 0), (0, 1, 0))

glShader()

glBackground(Texture('./modelos_prueba/proyecto/fondo.bmp'))

#glTexture('./modelos_prueba/proyecto/DeLorean.bmp')
#glRenderObject('./modelos_prueba/proyecto/delorean.obj', scale = (0.07, 0.07, 0.07), translate = (0, 0, 0), rotate = (0, 0, 0))

# ya quedo
glTexture('./modelos_prueba/proyecto/hydrant_BaseColor.bmp')
glRenderObject('./modelos_prueba/proyecto/hydrant_low.obj', scale = (0.002, 0.002, 0.002), translate = (0, -0.235, 0), rotate = (0, 0, 0))

# ya quedo
glTexture('./modelos_prueba/proyecto/Street_lamp_7_BaseColor.bmp')
glRenderObject('./modelos_prueba/proyecto/Street_lamp_7.obj', scale = (0.2, 0.2, 0.2), translate = (-0.2, -0.23, 0), rotate = (0, 0, 0))

# escribe el bmp
glFinish('proyecto1.bmp')
