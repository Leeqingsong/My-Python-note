print(1+1)  # 加法运算
print(1-1)  # 减法运算
print(2*4)  # 乘法运算
print(1/2)  # 除法运算
print(11/2)  # 5.5，除法运算
print(11// 2)  # 5，整除运算
print(11%2)  # 取余运算
print(2**2)  # 表示的是2的2次方
print(2**3)  # 表示的是2的3次方
# 存在正负数的情况
print(9//4)  # 2
print(-9//-4)  # 2
# 一正一负整除，向下取整
print(9//-4)  # -3
print(-9//4)  # -3
# 一正一负取余，公式：余数=被除数-除数*商
print(9%-4)  # -3
print(-9%4)  # 3
print("\n")
# 赋值运算符，执行顺序：从右到左
i = 3 + 4
print(i)
# 链式赋值
a = b = c = 20
print(a, id(a))  # id为内存地址，三个变量指向相同的地址
print(b, id(b))
print(c, id(c))
# 参数赋值
a = 20
a += 30  # a=a+30
print(a)
a -= 10
print(a)  # a=a-10
a *= 2
print(a)  # a=a*2
print(type(a))  # int
a /= 3
print(a)
print(type(a))  # float
a //= 2
print(a)  # float
a %= 3
print(a)
# 系列解包赋值，要求等号左右数量相同，注意顺序不能错
a, b, c = 20, 30, 40
print(a, b, c)
# 解包赋值应用在交换两个变量的值，不需要中间变量
a, b = 10, 20
print('交换之前：', a, b)
a, b = b, a  # 交换
print('交换之后：', a, b)
print("\n")

a, b = 1, 2
print(a == 1 and b == 2)  # True and True ---> True
print(a == b and b == 2)  # True and True ---> True
print(a == 1 and b < 2)  # False
print(a != 1 and b == 2)  # False
print(a !=1 and b != 2)  # False

# or 或者   
print(a == 1 or b == 2)  # T
print(a == 1 or b < 2)  # T
print(a != 1 or b == 2)  # T
print(a != 1 or b != 2)  # F

# not 取反，    针对bool类型操作数
f = True
ff = False
print(not f)  # F
print(not ff)  # T

# in    
# not in    
s = 'helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)
# 按位与&，同为1时为1
print(4 & 8)

# 按位或|，有1时为1
print(4 | 8)

# <<左移运算符，高位溢出舍弃，低位补0
# 4左移1位
print(4 << 1)

# >>右移运算符，低位溢出舍弃，高位补0
# 4右移1位
print(4 >> 1)
# 算术运算 > 位运算 > 比较运算 > 布尔运算
# 有括号先括号