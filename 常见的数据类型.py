#常见的数据类型
#整数型：int
print("整数型：int")
vlan_id1 = 10
vlan_id2 = 20
vlan_id3 = 30
print(vlan_id1,type(vlan_id1))
print(vlan_id2,type(vlan_id2))
print(vlan_id3,type(vlan_id3))
#整数可以表示为二进制0b开头的数字，八进制0o开头的数字，十六进制0x开头的数字。
print('十进制', 118)  # 默认为十进制
print('二进制', 0b10101111)  # 0b二进制
print('八进制', 0o176)  # 0o八进制
print('十六进制', 0x1EAF)  # 0x十六进制
#浮点型：float
print("浮点型：float")
a = 3.14
print(a,type(a))
C1 = 1.1
C2 = 2.2
print(C1 + C2)#会出现小数点位不确定的情况，那么我们引入Decimal模块来解决这个问题
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))#使用Decimal模块的加法运算，得到精确的结果
#字符串型：str
print("字符串型：str")
name = "Alice"
age = "25"
print(name,type(name))
print(age,type(age))
#布尔型：bool
print("布尔型：bool")
flag1 = True
flag2 = False
print(flag1,type(flag1))
print(flag1 + 1)#true表示1
print(flag2 + 1)#false表示0
#列表型：list
print("列表型：list")
numbers = ['192.168.10.1','192.168.10.2','192.168.10.3' ]
print(numbers,type(numbers))
#元组型：tuple
print("元组型：tuple")
numbers = (3.14, 0.577, 2.718)
print(numbers,type(numbers))
#字典型：dict
print("字典型：dict")
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
print(person,type(person))
#集合型：set
print("集合型：set")
fruits = {'apple', 'banana', 'orange'}
print(fruits,type(fruits))
#NoneType：None
print("NoneType：None")
nothing = None
print(nothing,type(nothing))
#总结：
#Python中有6种基本数据类型：整数型、浮点型、字符串型、布尔型、列表型、元组型、字典型、集合型、NoneType。