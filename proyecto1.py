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

# se renderiza sin textura con escala de grises
glRenderObject('./modelos_prueba/proyecto/mouse-droid.obj', scale = (0.05, 0.05, 0.05), translate = (0.1, -0.235, 1), rotate = (0.2, 1.4, 0))

# se renderiza con textura y un mapa normal
glTexture('./modelos_prueba/proyecto/Camtono_Base_color.bmp')
glNormalMap('./modelos_prueba/proyecto/Camtono_Normal.bmp')
glRenderObject('./modelos_prueba/proyecto/camtomo.obj', scale = (0.0039, 0.0039, 0.0039), translate = (0.1, -0.135, -4), rotate = (0.1, 0, 0))

# se renderiza con textura
glTexture('./modelos_prueba/IG.bmp')
glRenderObject('./modelos_prueba/proyecto/IG_CG.obj', scale = (0.18, 0.18, 0.18), translate = (-0.17, -0.235, 0), rotate = (0, 0.4, 0))

# se renderiza con textura
glTexture('./modelos_prueba/proyecto/GNK_BaseColor.bmp')
glRenderObject('./modelos_prueba/proyecto/GNK.obj', scale = (0.0007, 0.0007, 0.0007), translate = (-0.29, -0.435, 0), rotate = (0.44, 0.8, 0.05))

# se renderiza con textura
glTexture('./modelos_prueba/proyecto/R2-D2.bmp')
glRenderObject('./modelos_prueba/proyecto/R2-D2.obj', scale = (0.05, 0.05, 0.05), translate = (0.34, -0.015, 2.5), rotate = (0.1, 1, 0))


# escribe el bmp
glFinish('proyecto1.bmp')
