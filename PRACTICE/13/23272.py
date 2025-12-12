from ipaddress import ip_network

a = ip_network("205.99.68.249/255.255.248.0", 0)

for i in a: pass

print(''.join(str(i-1).split('.')))

# объяснение - смотри 23372.py
#2059971254
