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

    if y <= 900 and y > 890:
        return color(clamping(133*i), clamping(112*i), clamping(93*i))
    if y <= 890 and y > 875:
        return color(clamping(150*i), clamping(130*i), clamping(105*i))
    if y <= 875 and y > 840:
        return color(clamping(156*i), clamping(139*i), clamping(100*i))
    if y <= 840 and y > 730:
        return color(clamping(156*i), clamping(139*i), clamping(100*i))
    if y <= 730 and y > 700:
        return color(clamping(170*i), clamping(128*i), clamping(100*i))
    if y <= 700 and y > 650:
        return color(clamping(191*i), clamping(173*i), clamping(143*i))
    if y <= 650 and y > 620:
        return color(clamping(189*i), clamping(169*i), clamping(135*i))
    if y <= 620 and y > 500:
        return color(clamping(197*i), clamping(176*i), clamping(142*i)) # bastante
    if y <= 500 and y > 470:
        return color(clamping(191*i), clamping(172*i), clamping(133*i))
    if y <= 470 and y > 400:
        return color(clamping(203*i), clamping(181*i), clamping(139*i))
    if y <= 400 and y > 280:
        return color(clamping(213*i), clamping(190*i), clamping(155*i)) # bastante
    if y <= 280:
        return color(clamping(159*i), clamping(139*i), clamping(113*i))



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

