# *-* coding:utf8 *-*

# 引号前面的u告诉解释器这是一个utf8编码格式的字符串
hello_str = u"hello世界"

print(hello_str)

for c in hello_str:
    print(c)
