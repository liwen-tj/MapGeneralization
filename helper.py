def checkSC1(lines):
    # two lines have the same starting and ending points
    se = []
    id = []
    for k in lines:
        id.append(k)
        se.append((lines[k][0], lines[k][-1]))

    repeated_id = []
    for i, n in enumerate(se):
        if se.count(n) > 1:
            repeated_id.append(id[i])
    
    return repeated_id

def checkSC2(lines):
    # starting and ending points are the same(a circle)
    circle_line_id = []

    for k in lines:
        if lines[k][0] == lines[k][-1]:
            circle_line_id.append(k)
    
    return circle_line_id

def getBoundingBox(points):
    #[(), (), ()]
    x_min, x_max = points[0][0], points[0][0]
    y_min, y_max = points[0][1], points[0][1]

    for p in points[1:]:
        if p[0] > x_max: x_max = p[0]
        elif p[0] < x_min: x_min = p[0]
        if p[1] > y_max: y_max = p[1]
        elif p[1] < y_min: y_min = p[1]
    
    return (x_min, x_max, y_min, y_max)

def getCPNumInBox(cps, x_min, x_max, y_min, y_max):
    # cps:[(), (), ()]
    cou = 0
    inside_cps = []
    for cp in cps:
        if cp[0] < x_min or cp[0] > x_max:
            continue
        elif cp[1] < y_min or cp[1] > y_max:
            continue
        else:
            inside_cps.append(cp)
            cou +=  1

    return (cou, inside_cps)
        