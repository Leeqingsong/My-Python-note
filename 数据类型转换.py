print('str函数')
ipaddress = '192.168.10.1'
vlan = 10
print('vlan'+str(vlan)+'的ip地址是'+ipaddress)#str()函数将其他类型转换为字符串
print('\n')
 
print('int函数')
a = '123'
b =  456
c = True
d = '7.11'
e = 7.22
print(int(a))#前提是字符串一定要是数字串 
print(int(b))
print(int(c))#True转换为1
print(int(d))#会报因为无法转换为整数的错误
print(int(e))#会报因为无法转换为整数的错误
print('\n')

print('float函数')
a = '123.45'
b = 456
c = True
d = '7.11'
e = 7.22
print(float(a))#前提是字符串一定要是数字串 
print(float(b))
print(float(c))#True转换为1.0
print(float(d))#会报因为无法转换为浮点数的错误
print(float(e))#会报因为无法转换为浮点数的错误
print('\n')
