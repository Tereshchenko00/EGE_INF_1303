from ipaddress import ip_network as ip

a = ip("95.24.20.25/255.255.252.0", 0)

print(a.num_addresses-2-3-4-2-1-1)
#1011
