def cyclic(num1, num2):
    s1 = str(num1)
    s2 = str(num2)
    if s1[2:] == s2[:2]:
        return True
    return False


triangles = list()
squares = list()
pentagons = list()
hexagons = list()
heptagons = list()
octagons = list()
polygons = list()

for n in range(45, 142):
    t = (n*(n + 1)/2)
    triangles.append(t)

for n1 in range(32, 100):
    squares.append(n1**2)

for n2 in range(26, 81):
    pentagons.append((n2*(3*n2 - 1))/2)

for n3 in range(23, 71):
    hexagons.append(n3*(2*n3 - 1))

for n4 in range(21, 64):
    heptagons.append((n4*(5*n4 - 3))/2)

for n5 in range(19, 60):
    octagons.append(n5*(3*n5 - 2))

polygons = {'3' : triangles,
 '4' : squares,
 '5' : pentagons,
 '6' : hexagons,
 '7' : heptagons,
 '8' : octagons}


temp = []
for k in polygons.keys():
    for v in polygons[k]:
        temp.append((k,v))


for k1,v1 in temp:
    for k2,v2 in temp:
        if k1 != k2 and cyclic(v1,v2):
            for k3,v3 in temp:
                if k1 != k3 and k2 != k3:
                    if cyclic(v2, v3):
                        for k4,v4 in temp:
                            if k1 != k4 and k2 != k4 and k3 != k4:
                                if cyclic(v3,v4):
                                    for k5,v5 in temp:
                                        if k1 != k5 and k2 != k5 and k3 != k5 and k4 != k5:
                                            if cyclic(v4, v5):
                                                for k6,v6 in temp:
                                                    if k1 != k6 and k2 != k6 and k3 != k6 and k4 != k6 and k5 != k6:
                                                        if cyclic(v5,v6) and cyclic(v6,v1):
                                                            print v1+v2+v3+v4+v5+v6
                                                            exit()

