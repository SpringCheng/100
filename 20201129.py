# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 0029 下午 3:40
# @Author  : CC1111
"""
    有四个数字：1,2,3,4，能组成多个个互不相同且不重复的三位数？各是多少？
"""

for i in range(1, 5):  # 百位
    for j in range(1, 5):  # 十位
        for k in range(1, 5):  # 个位
            if (i != k) and (j != k) and (i != j):
                print(i, j, k)
# result
"""
1 2 3
1 2 4
1 3 2
1 3 4
1 4 2
1 4 3
2 1 3
2 1 4
2 3 1
2 3 4
2 4 1
2 4 3
3 1 2
3 1 4
3 2 1
3 2 4
3 4 1
3 4 2
4 1 2
4 1 3
4 2 1
4 2 3
4 3 1
4 3 2
"""


# 输入abcd4个整数，计算a+b-c*d的结果
# a=int(input("请输入第一个数字:"))
# b=int(input("请输入第一个数字:"))
# c=int(input("请输入第一个数字:"))
# d=int(input("请输入第一个数字:"))
#
# print(a+b-c*d)

