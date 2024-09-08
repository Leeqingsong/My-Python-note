user = input("请输入用户名：  ")
a=int(input("请输入第一个数字：  "))
b=int(input("请输入第二个数字：  "))
print(type(a))
print(type(b))
print(a+b)# 简单拼接str
print(int(a)+int(b))# 默认为str，需要转类型，或者用a=int(a)，转后输出a+b即可，或者用a=int(input('请输入一个加数：'))，提前转换