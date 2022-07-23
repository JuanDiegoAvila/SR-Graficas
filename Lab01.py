from gl import *

glCreateWindow(800, 800)
glClearColor(1, 1, 1)
glClear()

glColor(0.7, 0, 0)

points1 = [(165, 380),
          (185, 360),
          (180, 330),
          (207, 345),
          (233, 330),
          (230, 360),
          (250, 380),
          (220, 385),
          (205, 410),
          (193, 383)]

glDrawPolygon(points1)

points2 = [(321, 335),
          (288, 286),
          (339, 251),
          (374, 302)]

glDrawPolygon(points2)

points3 = [(377, 249),
          (411, 197),
          (436, 249)]

glDrawPolygon(points3)

points4 = [(413, 177),
          (448, 159),
          (502, 88),
          (553, 53),
          (535, 36),
          (676, 37),
          (660, 52),
          (750, 145),
          (761, 179),
          (672, 192),
          (659, 214),
          (615, 214),
          (632, 230),
          (580, 230),
          (597, 215),
          (552, 214),
          (517, 144),
          (466, 180)]

glDrawPolygon(points4)

glColor(1, 1, 1)
points5 = [(682, 175),
          (708, 120),
          (735, 148),
          (739, 170)]

glDrawPolygon(points5)

# glColor(0, 1, 0)

# temp = None
# for i in range(len(points4)):
#   if temp:
#     glRawLine(temp[0],temp[1], points4[i][0], points4[i][1])
#   temp = points4[i]
  
#   if i == len(points4) -1:
#     glRawLine(  temp[0], temp[1],  points4[0][0], points4[0][1])
      

glFinish('Lab1.bmp')

