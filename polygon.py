import gl

def draw_polygon(points):
    temp = None

    minX = min([x for x, y in points])
    maxX = max([x for x, y in points])
    minY = min([y for x, y in points])
    maxY = max([y for x, y in points])
    
    centerX = ((maxX - minX) / 2) + minX
    centerY = ((maxY - minY) / 2) + minY

    ff = 1000
    for j in range(ff):
        factor = (ff - j) /ff
        for i in range(len(points)):
            if temp:
                gl.glRawLine(  
                    gl.glScale(centerX, temp[0], factor),
                    gl.glScale(centerY, temp[1], factor),
                    gl.glScale(centerX, points[i][0], factor),
                    gl.glScale(centerY, points[i][1], factor)
                )
                gl.glRawLine(  
                    gl.glScale(centerX + 1, temp[0], factor),
                    gl.glScale(centerY, temp[1], factor),
                    gl.glScale(centerX + 1, points[i][0], factor),
                    gl.glScale(centerY, points[i][1], factor)
                )
            temp = points[i]
            
            if i == len(points) -1:
                gl.glRawLine(  
                    gl.glScale(centerX + 1, temp[0], factor),
                    gl.glScale(centerY, temp[1], factor),
                    gl.glScale(centerX + 1, points[0][0], factor),
                    gl.glScale(centerY, points[0][1], factor)
                )