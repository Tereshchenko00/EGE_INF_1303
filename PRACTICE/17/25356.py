f = open('17_25356.txt')
a = f.readlines()
maxk=0
for k in a:
    k=int(k)
    if k%100==30:
        maxk = max(maxk,k)
        
print(maxk)
k=0
maxs = 0
for i in range (len(a)-2):
    x,y,z = a[i:i+3]
    lst = [x,y,z]
    flag=0
    for t in lst:
        if len(str(abs(int(t))))==4:
            flag=1
            
    summ = int(x)+int(y)+int(z)

    if flag==0 and summ>maxk:       
        k+=1
        maxs = max(maxs,summ)
print(k)
print(maxs)
