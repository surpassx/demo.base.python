# Author: xujiantong
# 开发时间： 2021/3/17 23:48
# 打印关键字
# import keyword
# print(keyword.kwlist)

# 定义变量
name = "赛利亚" #标识 表示对象所存储的内存地址,使用内置函数id(obj)来获取
# 类型 表示的是对象的数据类型 使用内置函数 type(obj) 来获取
# 值 表示对象所存储的具体数据 使用print(obj) 可以将值进行打印输出
#     age = 100
#     print(id(name))
#     print(type(name))
#     print(type(age))
#     print(name)
# -----------------------------
# int 整数类型
# float 浮点类型
# bool 布尔类型 -> True False
# str
i = 3.141592658539999999
print(i ,type(i))
print(1.1+2.2)
from decimal import Decimal
print(Decimal("1.1")+Decimal("2.2"))

f1 = True
f2 = False
print(f1+1, type(f1))
print(f2, type(f2))
names = "xujiantong"
age = 20

print("我叫"+names+",我今年"+str(age)+"岁")
# 类型转换 int(xxx) str(xxx) float(xxx)

f1 = "98.7"
print(Decimal(f1),type(Decimal(f1)))
# """
# 你好呀赛利亚
# """