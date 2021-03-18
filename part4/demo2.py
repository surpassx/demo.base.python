# Author: xujiantong
# 开发时间： 2021/3/18 22:59

# 单分支结构
money = 1000  # 余额
s = int(input('请输入取款金额'))

# 判断余额是否充足
if money >= s:
    money = money - s
    print("取款成功, 余额为", money)


# 双分支结构 if eles 二选一执行
# 判断奇偶
num = int(input("请输入一个整数"))
if num % 2 == 0:
    print("偶数")
else:
    print("奇数")

score = int(input("请输入成绩"))
if 90<=score<=100:
    print("优秀")
elif score >=80 and score <90:
    print("优")
elif score >=60 and score <80:
    print("及格")
elif score<60:
    print("不及格")
else:
    print("非法数据")
