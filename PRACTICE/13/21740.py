from ipaddress import ip_network

a = ip_network("95.24.16.0/255.255.240.0", 0)
for i in a: pass
a = list(map(int, str((i-1)).split('.')))
print(a[2] + a[3])
#285
