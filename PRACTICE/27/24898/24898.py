import math 
print('ok')
with open('C:/Users/student/Desktop/1/HOMEWORKS/27/24898/27_A_24898.txt') as f:
    f.readline()
    clA1 = []
    clA2 = []
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        if x > 40:
            clA1.append((x, y))
        else:
            clA2.append((x, y))

with open('C:/Users/student/Desktop/1/HOMEWORKS/27/24898/27_B_24898.txt') as f:
    f.readline()
    clB1 = []
    clB2 = []
    clB3 = []
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        if (x > 10) and (y > 20):
            if y < 32:
                clB1.append((x, y))
                #print('1') # нижний
            elif y < 42:
                clB2.append((x, y))
                #print('2') # средний
            else:
                clB3.append((x, y))
                #print('3') # верхний

def d(A, B):
    return math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)

def cent(cluster: list[tuple[float]]) -> tuple[float]:
    center = (0, 0)
    minim = 999999999999999999999999999999999999999999999999999
    for a in cluster:
        total = 0
        for b in cluster:
            total+= d(a, b)
        if minim > total:
            minim = total
            center = a
    return center

print(cent(clB3))

if len(clA1) > len(clA2):
    p2 = int(sum(cent(clA1)) * 10000)
    p1 = int(sum(cent(clA2)) * 10000)

Qx = int((cent(clB3)[0] * 10000))
Qy = int((cent(clB1)[1] * 10000))

print(p1, p2, '\n', Qx, Qy)
#1171117 1532167 
#222238 280837