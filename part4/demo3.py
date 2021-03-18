# Author: xujiantong
# 开发时间： 2021/3/18 23:38


# 嵌套结构

age = int(input("请输入年龄"))

if age > 18:
    if age > 60:
        print("你是个老年人了")
    else:
        print("你是个青年")
else:
    print("你还未成年")

answer = input("你是会员么?y/n")
money = float(input("请输入金额"))

if answer=='y':
    if money>=200:
        print("打八折,付款金额为", money*0.8)
    elif money >= 100:
        print("打九折 付款金额为",money * 0.9)
    else:
        print("不打折,付款金额为", money)
else:
    print("非会员不打折, 付款金额为",money)