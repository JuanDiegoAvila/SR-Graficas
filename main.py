from gl import *

# definicion de pantalla con resolucion 1024 x 1024
glCreateWindow(1024, 1024)

# color blanco de fondo
glClearColor(1, 1, 1)
glClear()

# creacion de viewport en el centro 
glViewPort(12, 12, 1000, 1000)

# color de imagen rojo
glColor(1, 0, 0)

# definicion de la casa
glLine(-1, -1, -1, 1)

glFinish()
