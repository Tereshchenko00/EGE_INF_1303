from ipaddress import ip_network

a = ip_network("98.71.254.171/255.248.0.0", 0)

for x in a:
    s = '.'.join([bin(int(i))[2:].zfill(8) for i in str(x).split('.')])
    if s.count('1')%7==0:
        print(''.join([str(int(i, 2)) for i in s.split('.')]))
        break
#986407
