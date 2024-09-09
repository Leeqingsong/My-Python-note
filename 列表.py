#列表
my_list = [1, 2, 3, 4, 5]
print(my_list)
 #输出列表中的元素
print(my_list[0],my_list[-1])#0表示从右往左第一个，-1表示从右往左最后一个

#创建列表有两种方式
#第一种方式：使用方括号[]创建列表
my_list = [1, 2, 3, 4, 5]
print(my_list)

#第二种方式：使用list()函数创建列表
my_list = list([1, 2, 3, 4, 5])
print(my_list)

print('''列表的特点：
1.列表元素按照顺序有序排序
2.索引映射唯一一个数据
3.列表可以存储重复数据
4.任意数据类型混存
5.根据需要动态分配和回收内存''')

#使用index()方法查找元素的索引
my_list = [1, 2, 3, 4, 5]
print(my_list.index(3))#输出3的索引

#使用append()方法在列表末尾添加元素 】
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)

#使用insert()方法在指定位置插入元素
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 10)# 在索引2位置添加10
print(my_list)


#使用pop()方法删除列表末尾元素
my_list = [1, 2, 3, 4, 5]
my_list.pop()
print(my_list)


#使用remove()方法删除指定元素       
my_list = [1, 2, 3, 4, 5]       
my_list.remove(3)       
print(my_list)       

#使用extend()方法在列表末尾添加另一个列表
my_list = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8, 9, 10]
my_list.extend(my_list2)
print(my_list)


#使用sort()方法对列表进行排序
my_list = [5, 2, 9, 1, 7]
my_list.sort()
print(my_list)


#使用reverse()方法对列表进行反转    

my_list = [5, 2, 9, 1, 7]       
my_list.reverse()       
print(my_list)       


#使用count()方法统计列表中某个元素出现的次数
my_list = [1, 2, 3, 4, 5, 3, 2, 1]
print(my_list.count(2))#输出2出现的次数


#使用clear()方法清空列表
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list) 

#使用del语句删除列表
my_list = [1, 2, 3, 4, 5]
del my_list
print(my_list)#输出错误，因为my_list已经被删除  


#使用列表切片
my_list = [1, 2, 3, 4, 5]
print(my_list[1:3])#输出列表中索引为1和2的元素
print(my_list[:3])#输出列表中索引为0到2的元素
print(my_list[2:])#输出列表中索引为2到末尾的元素
print(my_list[::2])#输出列表中索引为0、2、4的元素
print(my_list[::-1])#输出列表中索引为5、4、3、2、1的元素
