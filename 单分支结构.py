#单分支结构
priority = 60
a = int(input('请输入链路失效后增加的优先级：'))
if a < priority:
    priority+=a
    print('此时链路的优先级为：',priority)
    