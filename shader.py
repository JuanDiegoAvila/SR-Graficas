from gl import *
from vector import V3

glCreateWindow(2024, 2024)

# color negro de fondo
glClearColor(1, 1, 1)
glClear()

# crea un viewport de 1024 x 1024
glViewPort(0, 0, 1024, 1024)

# carga la textura
glTexture('./modelos_prueba/model.bmp')

glLookAt((0, 0, 10), (0, 0, 0), (0, 1, 0))

#glShader()
# renderiza el objeto con su estala, traslación y rotación
glRenderObject('./modelos_prueba/model.obj', scale = (0.8, 0.8, 0.8), translate = (0, 0, 0), rotate = (0, 0.7, 0))

# escribe el bmp
glFinish('shader.bmp')
