# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 0029 下午 3:40
# @Author  : CC1111

"""
    有四个数字：1,2,3,4，能组成多个个互不相同且不重复的三位数？各是多少？
"""
import math

for i in range(1, 5):  # 百位
    for j in range(1, 5):  # 十位
        for k in range(1, 5):  # 个位
            if (i != k) and (j != k) and (i != j):
                print(i, j, k)

"""
    输入a b c d 4个整数，计算a+b-c*d的结果
"""
a=int(input("请输入第一个数字:"))
b=int(input("请输入第一个数字:"))
c=int(input("请输入第一个数字:"))
d=int(input("请输入第一个数字:"))

print(a+b-c*d)

"""
    计算矩形的面积和周长
"""
a = 12.5
b = 16.7

print("矩形的面积:", a * b)
print("矩形的面积:", 2 * (a + b))

"""
    计算圆的面积
"""
r = 1
circle = math.pi ** r
print("圆的面积:", circle)

"""
    幂函数
"""
# pow()幂函数
print(7 * 7 * 7 * 7)
print(7 ** 4)
print(pow(7, 4))

"""
    类型转换
"""
a = '1'
b = 2
print(int(a) + b)

"""
    输入1-127的ASCII码
"""
chr()将整数转换为字符
number = int(input("请输入数字:"))
print(chr(number))

"""
    3个人吃饭总共花费35.27美元，给15%的小费，每个人应该付多少
"""
# round为浮点数四舍五入值
print(round((35.27 * (1 + 0.15) / 3), 2))

"""
    交换两个数
"""
a = 23
b = 41
a, b = b, a
print(a)
print(b)

"""
    打印100~999水仙花数
    水仙花数=各位数字立方和等于该数本身
"""
for i in range(100, 1000):
    a = i // 100
    b = (i % 100) // 10
    c = i % 10
    if i == a ** 3 + b ** 3 + c ** 3:
        print(i)
"""
    九九乘法表
"""
# 外层for循环控制函数，内层for循环控制列数

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d " % (i, j, j * i), end='')
    print()

"""
    1~100的和
"""
res = 0
i = 1
while i < 101:
    res += i
    i = i + 1
print(res)
result = 0
for i in range(1, 101):
    result += i
    i = i + 1
print(result)

"""
    判断是否是闰年(被400整除或能被4整除但不能被100整除）
"""
a = int(input('请输入年份:'))
if ((a % 400 == 0) or (a % 4 == 0 and a % 100 != 0)):
    print("%d是闰年" % a)
else:
    print("%d是平年" % a)

"""
    邮箱 验证
"""

email=input("请输入邮箱号:")
if len(email.split('@'))==2 and email.endswith('.com'):
    print('邮箱的格式正确:')
else:
    print('邮箱格式错误:')

