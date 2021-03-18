# Author: xujiantong
# 开发时间： 2021/3/16 23:50

print("Hello world")
print(520)
print("1" == "2")
print(False)
print(True)
print(3+1)

# 将数据输出到文件中 a+追加
fp = open('E:/pywork/level1/text.txt','a+')
print("hello world", file=fp)
fp.close()

## 不进行换行输入
print('hello','world', 'python')

# 转义字符
print('hello \n nihao')
print('老师说‘大家好’')
print('http:\\\\hello.world')
print(r'http:\\baidu.com\0')
















