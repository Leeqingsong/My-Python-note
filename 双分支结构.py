addrss = [10, 20, 30, 40, 50]
vlan_id=int(input("请输入vlan: "))
if vlan_id in addrss:
    print('交换机有这个vlan')
else:
    print('交换机没有这个vlan  ')
    