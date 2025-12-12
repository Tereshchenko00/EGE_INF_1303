import math

with open("C:/Users/student/Desktop/1/HOMEWORKS/27/23766/27_A_23766.txt") as f:
    ca1 = []
    ca2 = []
    for i in f:
        x, y = [float(d.replace(',', '.')) for d in i.split()]
        if y < 10:
            ca1.append((x, y)) # нижний
        else:
            ca2.append((x, y)) # верхний

with open('C:/Users/student/Desktop/1/HOMEWORKS/27/23766/27_B_23766.txt') as f:
    cb1 = []
    cb2 = []
    cb3 = []
    for i in f:
        x, y = [float(d.replace(',', '.')) for d in i.split()]
        if ((x > 5) and (x < 30)) and ((y > 10) and (y < 30)):
            if y < 20:
                cb1.append((x, y)) # нижний
            elif x<18:
                cb2.append((x, y)) # левый
            else:
                cb3.append((x, y)) # правый

def d(A: tuple[float, float], B: tuple[float, float])->float:
    return math.sqrt((A[0] -B[0])**2 + (A[1] - B[1])**2)

def center(cluster: list[tuple[float, float]])->tuple[float, float]:
    minim = 99999999999999999999999999999999999999999999999999999999
    rez = -1
    for A in cluster:
        total = 0.0
        for B in cluster:
            total += d(A, B)
        if minim > total:
            minim = total
            rez = A
    return rez

def maxd(cluster: list[tuple[float, float]], center: tuple[float, float])->tuple[float, float]:
    rez = 0.0
    for A in cluster:
        dist = d(center, A)
        if rez < dist:
            rez = dist
    return rez

ca1 = center(ca1)
ca2 = center(ca2)

Px = ca1[0]
Py = ca1[1]

ccb1 = center(cb1)
ccb2 = center(cb2)
ccb3 = center(cb3)

k1 = len(cb1)
k2 = len(cb2)
k3 = len(cb3)

#print(k1, k2, k3)
#      407 113 100
#      cb1 cb2 cb3
#       ^       ^
#      max     min

Q1 = d(ccb1, ccb3)

Q2 = max([maxd(cb1, ccb1),
          maxd(cb2, ccb2), 
          maxd(cb3, ccb3)])

print(int(Px * 10000), int(Py * 10000))
print(int(Q1 * 10000), int(Q2 * 10000))

#38471 61225
#142058 25299