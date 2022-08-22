import Obj
from gl import *
from vector import V3
from render import Render
from Obj import Obj

# ----------- dibujar los vertices de la textura -----------------

r = Render(1024, 1024)
t = Texture('./modelos_prueba/IG.bmp')

r.framebuffer = t.pixels

cube = Obj('./modelos_prueba/IGCG.obj')
r.current_color = color(255, 255, 255)

for faceDict in cube.faces:
  face = faceDict['face']

  if len(face) == 4:
    ft1 = face[0][1] - 1
    ft2 = face[1][1] - 1
    ft3 = face[2][1] - 1
    ft4 = face[3][1] - 1

    vt1 = V3(
      cube.tvertices[ft1][0] * t.width,
      cube.tvertices[ft1][1] * t.width
    )
    vt2 = V3(
      cube.tvertices[ft2][0] * t.width,
      cube.tvertices[ft2][1] * t.width
    )
    vt3 = V3(
      cube.tvertices[ft3][0] * t.width,
      cube.tvertices[ft3][1] * t.width
    )
    vt4 = V3(
      cube.tvertices[ft4][0] * t.width,
      cube.tvertices[ft4][1] * t.width
    )
    
    r.lineVector(vt1, vt2)
    r.lineVector(vt2, vt3)
    r.lineVector(vt3, vt4)
    r.lineVector(vt4, vt1)

  if len(face) == 3:

    ft1 = face[0][1] - 1
    ft2 = face[1][1] - 1
    ft3 = face[2][1] - 1

    vt1 = V3(
      cube.tvertices[ft1][0] * t.width,
      cube.tvertices[ft1][1] * t.width
    )
    vt2 = V3(
      cube.tvertices[ft2][0] * t.width,
      cube.tvertices[ft2][1] * t.width
    )
    vt3 = V3(
      cube.tvertices[ft3][0] * t.width,
      cube.tvertices[ft3][1] * t.width
    )
    
    r.lineVector(vt1, vt2)
    r.lineVector(vt2, vt3)
    r.lineVector(vt3, vt1)

r.write("textura_vertices_SR5.bmp")

# ---------- cargar modelo con su textura -------------------

glCreateWindow(1024, 1024)

# color negro de fondo
glClearColor(0, 0, 0)
glClear()

# color de imagen rojo
glColor(0, 0, 0)


#glTexture('./modelos_prueba/model.bmp')
#glTexture('./modelos_prueba/earth.bmp')
#glMaterial('./modelos_prueba/IGCG.mtl')  -- prueba de material .mtl en obj

# --------- se coloca unicamente la direccion del archivo bmp ------------
glTexture('./modelos_prueba/IG.bmp')

# --------- se coloca la direccion del archivo obj, el scale factor y translate factor ------------
glRenderObject('./modelos_prueba/IGCG.obj', (400, 400, 400), (500, 50, 0))
#glRenderObject('batman.obj', (5, 5, 10), (500, 200, 0))
#glRenderObject('./modelos_prueba/earth.obj', (1, 1, 1.5), (500, 500, 0))
#glRenderObject('./modelos_prueba/model.obj', (500, 500, 500), (500, 500, 0))
#glRenderObject('./modelos_prueba/natsuki.obj', (500, 500, 500), (500, 500, 0))


# --------- se coloca el nombre del archivo que se quiere escribir  ------------
glFinish('textura_SR5.bmp')