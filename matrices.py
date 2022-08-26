from gl import *

glCreateWindow(1024, 1024)

# color negro de fondo
glClearColor(0, 0, 0)
glClear()

# color de imagen rojo
glColor(1, 1, 1)

# --------- se coloca unicamente la direccion del archivo bmp ------------
glTexture('./modelos_prueba/IG.bmp')

# --------- se coloca la direccion del archivo obj, el scale factor y translate factor ------------
glRenderObject('./modelos_prueba/IGCG.obj', (400, 400, 400), (500, 20, 0), (0, 0, 0))

# --------- se coloca el nombre del archivo que se quiere escribir  ------------
glFinish('matrices.bmp')