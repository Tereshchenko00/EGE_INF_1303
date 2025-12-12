import math


with open('c:/Users/student/Desktop/1/HOMEWORKS/27/24562/A.txt') as f:
    clusterA1 = []
    clusterA2 = []
    for i in f:
        x, y = [float(i.replace(',', '.')) for i in f.readline().split()]
        if y > 0:
            clusterA1.append((x, y))
        else:
            clusterA2.append((x, y))

with open('c:/Users/student/Desktop/1/HOMEWORKS/27/24562/B.txt') as f:
    clusterB1 = []
    clusterB2 = []
    clusterB3 = []
    for i in f:
        x, y = [float(i.replace(',', '.')) for i in f.readline().split()]
        if y < -10:
            clusterB1.append((x, y))
        elif y < -3:
            clusterB2.append((x, y))
        elif x>0 and x<10:
            clusterB3.append((x, y))
        
            

def dist(A, B):
    return math.sqrt((A[0] - B[0])**2 + (A[1]-B[1])**2)

def centerOfTheCluster(cluster):
    cent = -1
    minim = 99999999999999999999999999999999999999999999999999999999999999
    for A in cluster:
        total = 0
        for B in cluster:
            total += dist(A, B)
        if minim > total:
            minim = total
            cent = A
    return cent 

cA1 = centerOfTheCluster(clusterA1)
cA2 = centerOfTheCluster(clusterA2)

Sx = cA1[0] + cA2[0]
Sy = cA1[1] + cA2[1]


cB1 = centerOfTheCluster(clusterB1)
cB2 = centerOfTheCluster(clusterB2)
cB3 = centerOfTheCluster(clusterB3)

Bx = cB1[0] + cB2[0] + cB3[0]
By = cB1[1] + cB2[1] + cB3[1]

print(abs(int(Sx * 10000)), abs(int(Sy * 10000)))
print(abs(int(Bx * 10000)), abs(int(By * 10000)))

