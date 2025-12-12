import math

with open("C:/Users/student/Desktop/1/HOMEWORKS/27/23571/27_A_23571.txt") as f:
    f.readline()
    ca1 = [] # верхний
    ca2 = [] # нижний
    for i in f:
        x, y = [float(d.replace(',', '.')) for d in i.split()]
        if y > 15:
            ca1.append((x, y))
        else:
            ca2.append((x, y))

with open('C:/Users/student/Desktop/1/HOMEWORKS/27/23571/27_B_23571.txt') as f:
    f.readline()
    cb1 = [] # правый
    cb2 = [] # верхний
    cb3 = [] # нижний

    for i in f:
        x, y = [float(d.replace(',', '.')) for d in i.split()]

        if ((x > 10.0) and (x < 30.0)) and ((y > 0.0) and (y < 25.0)):

            if x > 20:
                cb1.append((x, y))
            elif y > 14:
                cb2.append((x, y))
            else: 
                cb3.append((x, y))

def d(A: tuple[float, float], B: tuple[float, float])-> float:
    return math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)

def center(cluster: list[tuple[float, float]]) -> tuple[float, float]:
    minim = float('inf')
    rez = -1
    for A in cluster:
        total = 0.0
        for B in cluster:
            total += d(A, B)
        if minim > total:
            minim = total
            rez = A
    return rez

def maxd(cluster1: list[tuple[float, float]], cluster2: list[tuple[float, float]]) -> list[float, float]:
    minim = float('inf')
    maxim = 0.0
    for A in cluster1:     
        for B in cluster2:
            dis = d(A, B)
    
            if minim > dis:
                minim = dis
            if maxim < dis:
                maxim = dis
    return [minim, maxim]

a1 = center(ca1)
a2 = center(ca2)

Px = a1[0] + a2[0] 
Py = a1[1] + a2[1] 

Q1 = maxd(cb2, cb3)[0]
Q2 = max([maxd(cb1, cb2)[1], maxd(cb1, cb3)[1]])

print(int(Px * 10000), int(Py * 10000))
print(int(Q1 * 10000), int(Q2 * 10000))
#92256 258611
#33863 170816