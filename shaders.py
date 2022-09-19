from color import * 

def planeta(**kwargs):
    w, u, v = kwargs['bar']
    A, B, C = kwargs['vertices']
    L = kwargs['light']
    nA, nB, nC = kwargs['normals']
    y = kwargs['height']


    iA = nA.normalize() @ L.normalize()
    iB = nB.normalize() @ L.normalize()
    iC = nC.normalize() @ L.normalize()

    i = iA * w + iB * u + iC * v
    i *= -1
    if y <= 800 and y > 750:
        return color(clamping(103 * i), clamping(92 * i), clamping(77 * i))
    if y <= 750 and y > 760:
        return color(clamping(154 * i), clamping(139 * i), clamping(114 * i))
    if y <= 700 and y > 620:
        return color(clamping(190 * i), clamping(174 * i), clamping(147 * i))
    if y <= 620 and y > 615:
        return color(clamping(200 * i), clamping(180* i), clamping(148 * i))
    if y <= 615 and y > 590:
        return color(clamping(119 * i), clamping(106* i), clamping(87 * i))
    if y <= 590:
        return color(clamping(154 * i), clamping(139 * i), clamping(114 * i))
    else:
        return color(clamping(95* i), clamping(85 * i), clamping(70 * i))


def default(**kwargs):
    
    w, u, v = kwargs['bar']
    texture = kwargs['texture']

    if texture:
        tA, tB, tC = kwargs['texture_coords']
    
    A, B, C = kwargs['vertices']
    L = kwargs['light']
    nA, nB, nC = kwargs['normals'] 
           
    iA = nA.normalize() @ L.normalize()
    iB = nB.normalize() @ L.normalize()
    iC = nC.normalize() @ L.normalize()
    
    i = iA * w + iB * u + iC * v
    i *= -1

    if texture:
        tx = tA.x * w + tB.x * u + tC.x * v
        ty = tA.y * w + tB.y * u + tC.y * v
        
        return texture.get_color_with_intensity(tx, ty, i)
    else:
        return color(clamping(250*i), clamping(1*i), clamping(1*i))

