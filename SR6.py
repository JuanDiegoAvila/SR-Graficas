from gl import *
from vector import V3

glCreateWindow(1024, 1024)

# color negro de fondo
glClearColor(0, 0, 0)
glClear()

# crea un viewport de 1024 x 1024
glViewPort(0, 0, 1024, 1024)

# color de imagen rojo
glColor(1, 1, 1)

# carga la textura
glTexture('./modelos_prueba/IG.bmp')

'''
# -------------- TOMA 1 MEDIUM SHOT -----------------------
# funcion look at con parametros eye, center y up
glLookAt((0, 0, 2), (0.5, 0, 0), (0, 1, 0))

# renderiza el objeto con su estala, traslación y rotación
glRenderObject('./modelos_prueba/IGCG.obj', scale = (0.35, 0.35, 0.35), translate = (0, -0.9, 0), rotate = (0, 0, 0))

# escribe el bmp
glFinish('SR6_medium.bmp')


# -------------- TOMA 2 LOW ANGLE -----------------------
# funcion look at con parametros eye, center y up
glLookAt((0, -8, 10), (0, 0, 0), (0, 1, 0))

# renderiza el objeto con su estala, traslación y rotación
glRenderObject('./modelos_prueba/IGCG.obj', scale = (0.35, 0.35, 0.35), translate = (-0.5, -0.9, 0), rotate = (0, 0, 0))

# escribe el bmp
glFinish('SR6_low.bmp')

# -------------- TOMA 3 HIGHT ANGLE -----------------------
# funcion look at con parametros eye, center y up
glLookAt((0, 9, 10), (0, 0, 0), (0, 1, 0))

# renderiza el objeto con su estala, traslación y rotación
glRenderObject('./modelos_prueba/IGCG.obj', scale = (0.35, 0.35, 0.35), translate = (-0.5, -0.9, 0), rotate = (0, 0, 0))

# escribe el bmp
glFinish('SR6_high.bmp')

'''
# -------------- TOMA 4 DUTCH ANGLE -----------------------
# funcion look at con parametros eye, center y up
glLookAt((5, 0, 2), (0, 0.1, 0.3), (-0.9, 1, 0))

# renderiza el objeto con su estala, traslación y rotación
glRenderObject('./modelos_prueba/IGCG.obj', scale = (0.35, 0.35, 0.35), translate = (-0.5, -0.9, 0), rotate = (0, 0, 0))

# escribe el bmp
glFinish('SR6_dutch.bmp')
