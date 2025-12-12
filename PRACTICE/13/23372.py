import ipaddress
ip = ipaddress.ip_network('73.148.145.65/255.224.0.0', 0)
for i in ip:
    pass #  пролистываем список адресов, чтобы дойти до последнего
print(''.join(str(i-1).split('.'))) #  выводим предпоследний

