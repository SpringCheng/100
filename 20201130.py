# # -*- coding: utf-8 -*-
# # @Time    : 2020/11/30 0030 下午 9:18
# # @Author  : CC1111
#
"""
    根据首字母返回星期几
"""
str1 = input('请输入单词的第一个字母:')
if str1.upper() == 'M':
    print('Monday')
elif str1.upper() == 'W':
    print("Wednesday")
elif str1.upper() == 'F':
    print('Friday')
elif str1.upper() == 'T':
    str2 = input('请输入第二个字母')
    if str2.upper() == 'U':
        print('Tuesday')
    elif str2.upper() == 'H':
        print('Thursday')
elif str1.upper() == 'S':
    str3 = input('请输入第二个字母:')
    if str3.upper() == 'A':
        print('Saturday')
    elif str3.upper() == 'U':
        print('Sunday')

"""
   成绩>=90用A表示，60-89之间的用B表示，60分一下的用C表示
"""
score = int(input('请输入分数：'))
if score >= 90:
    print('A')
elif score >= 60:
    print('B')
else:
    print('C')

"""
    打印星星
"""
for i in range(1,6):
    print('*'*i)

for i in range(5):
    print((5-i)*'*')

"""
    输出1~100内的偶数
"""

number1=1
while number1<101:
    if number1%2==0:
        print(number1)
    else:
        pass
    number1+=1

L1 = []
for i in range(1, 101):
    L1.append(i)
print(L1)
a = L1[1::2]
print(a)
sum = 0
for i in a:
    sum = sum + i
print(sum)

"""
    获取字符串长度
"""
str1=input('请输入字符串长度:')
print(len(str1))

""""
    单词长度判断
    字符串转换为列表
"""
str1 = input("请输入")
l = str1.split(' ')
print(l)
print(len(l))
for i in l:
    if len(i)==2:
        print(i)
    else:
        pass


"""
    字符串拼接
    考察占位符
"""
a='cheng'
b='chun'
print('My name is '+a+',i love '+b+'.')
print('my name is %s,i love %s'%(a,b))

"""
    不可变数据类型
    考察：字符串是不可变的字符类型,列表转化为字符串
"""
info='abc'
info=list(info)
info[2]='d'
print(info)
print(''.join(info))

"""
企业发放的奖金根据利润提成。利润(I)
低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
"""
i=int(input('净利润'))
arr=[1000000,6000000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
r=0
for index in range(0,6):
    if i>arr[index]:
        r+=(i-arr[index])*rat[index]
        print((i-arr[index])*rat[index])
        i=arr[index]
print(r)