L1=[]
L2=[]
L3=[]
s="字符串是字符的有序集合"
print(s)                                       #打印s
for i in range(11):
    L1.append(s[i])                             #把s中的每个字取出放到L1             appden(s[i]):把s中的第i个字符添加到列表的结尾
    L2.append(s[-i-1])                          #把s中的每个字取出，倒序放到L2
print(L1,"\n",L2)
print(s[:len(s):2])                             #把s中的字符，从开始到s的长度结束，偏移为2分片输出          s[a:b] s的第a个数值到第b个数值
print(ord('a')+ord('z'))                        #把a和z通过ord函数转化为ASCII数值，求和输出                 ord("")把字符转化为ASCII数值
for i in range(30):                             #i遍历0-29
    L3.append(chr(i))                           #把0-29用chr函数转化为字符，添加到L3                        chr("")把ASCII数值转化为字符
print(L3)
s=s[:4]+"\n"+s[4:]                               #把s从第4个字符开始打断，换行赋回给s输出
print(s)
print(i for i,x in enumerate(s) if x == "字")

x = "abcdefgfedcba"
print('字符串中字母大写' + x.upper())
print('字符串中字母小写' + x.lower())
print('首字母大写' + x.capitalize())
print('去指定字符' + x.strip('a,b,c'))
a = x.split("f", 2)
tittle = "按指定字符分割字符串："
a.append(tittle)
print(a)

print('判断是否为数字类型',x.isdigit())
print("指定字符串查找返回下标",x.find("f"))
print('字符串替换'+x.replace("a","。"))
'''''
str.replace(old,new[,max])
old  被替换的字符串
new  替换old的字符串
max  可选字符串，替换不超过max次
'''
