with open('C:/Users/student/Desktop/1/HOMEWORKS/27/24670/27A_24670.txt') as f:
    f.readline()
    clusterA1 = []
    clusterA2 = []
    for point in f:
        x, y = [float(i.replace(',','.')) for i in point.split()]
        if x<10:
            clusterA1.append((x, y))
        else:
            clusterA2.append((x, y))

with open('C:/Users/student/Desktop/1/HOMEWORKS/27/24670/27B_24670.txt') as f:
    f.readline()
    clusterB1 = []
    clusterB2 = []
    clusterB3 = []
    for point in f:
        x, y = [float(i.replace(',','.')) for i in point.split()]
        if x<10:
            clusterB1.append((x, y))
        elif y<20:
            clusterB2.append((x, y))
        else:
            clusterB3.append((x, y))


def dist(A, B):
    return abs(A[0]-B[0]) + abs(A[1]-B[1])

def center(cluster):
    m = 9999999999999999999999999999999999999999999999
    A_rez = -1
    for A in cluster:
        total = 0
        for B in cluster:
            total += dist(A, B)
        if m>total:
            m = total
            A_rez = A
    return A_rez

a1 = center(clusterA1)
a2 = center(clusterA2)
b1 = center(clusterB1)
b2 = center(clusterB2)
b3 = center(clusterB3)

print(int((a1[0] + a2[0])/2 *10000) , int((a1[1] + a2[1])/2*10000))
print(int((b1[0] + b2[0] + b3[0])/3 *10000), int((b1[1] + b2[1] + b3[1])/3*10000))
#101666 39433
#131555 134793