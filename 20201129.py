# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 0029 下午 3:40
# @Author  : CC1111
"""
    有四个数字：1,2,3,4，能组成多个个互不相同且不重复的三位数？各是多少？
"""
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=k) and (j!=k) and (i!=j):
                print(i,j,k)