#整数类型         type(a)判断类型
"""""
(ox,OX开头表示16进制)
(ob,OB开头表示2进制)
(0o,oO开头表示8进制)
"""""
#浮点数类型
""""
科学计数法：<a>e<b>=a*10^b
"""

#数字运算
''''
abs(x)        x的绝对值
x//y          商的整数部分
divmod(x,y)   同时返回x/y的整数和小数部分（x//y,x%y）
pow(x,y)      x的y次幂

<string>.upper( )             字符串中字母大写
<string>.lower( )             字符串中字母小写
<string>.capitalize( )        首字母大写
<string>.strip("str")             去首尾空格及指定字符
<string>.split("str",int)             按str分割字符串为int条数组
<string>.isdigit( )           判断是否是数字类型
<string>.find("str")              搜索指定字符串
str.replace(old,new[,max])           字符串替换，不超过max次
'''


#转义符#
"""
print("\"hello\"")
"hello"
print("\\hello\\")
\hello\
"""
#平闰年
"""
def Year(year,A):

    if year % 4 == 0 and year % 100 != 0:
        A="年为闰年"
        return A
    else:
        A="年为平年"
        return A
if __name__ == '__main__':
    year = int(input("请输入年份:\n"))
    A=""
    A=Year(year,A)
    print(year,A,sep='')
"""

#99乘法表
"""""
row=1
while row<=9:
    col=1
    while col<=row:
        print("%d * %d = %d"%(col,row,row*col),end="\t")
        col+=1
    print("")
    row+=1
"""
"""
firstName = input("Enter your first name")
lastName = input("Enter your last name")
print("firstname:"+firstName+"Last name:"+lastName)
print(firstName+"\n"+"\t"+lastName)
print(firstName,lastName,sep="*****",end="-----")

s1="hello,how are you"
print(format(s1,'40s'))
print(format(s1,'>40s'))
print(format(s1,'<40s'))


a=float(1234.1234567)
print(a)
print ("2位：",format(a,'.2f'))
print ("3位：",format(a,'.3f'))
print ("4位：",format(a,'.4f'))
print ("5位：",format(a,'.5f'),"\n\n\n")
print ("1位：",format(a,'1.5f'))
print ("2位：",format(a,'10.1f'))
print ("3位：",format(a,'3.5f'))

for num in [0,1,2,3,'a','b']:
   print(num)
for num in range(5):
 print(num)
import math
print(math.pi)
#shift + enter 当前行结尾快速换行
"""

#格式化输出
"""
day=1
month=3
hour=2.333
print("今天是第%d天,第%d月，第%.2f小时"%(day,month,hour))
"""

#函数嵌套调用
"""
def miXiangcheng(a,b,c):
    res = pow(xiangcheng(a,b),c)       pow(x,y)函数：计算x^y
    return res

def xiangcheng(a,b):
    res = a * b
    return res

if __name__ == '__main__':
    print(miXiangcheng(2,8,2))
"""
#函数库引用
"""""
from 库名 import 函数名
from 库名 import *
>>>from turtle import *
>>>fd(100)

import 库名
库名.函数名（）
>>>import turtle
>>>turtle.fd(100）
"""

#list检索字符返回下标
"""
s="字符串是字符的有序集合字符串字符串"
print([i for i,x in enumerate(s) if x == "字"])
"""
