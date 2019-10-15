def demo1():
    return int(input("输入整数："))


def demo2():
    return demo1()

# 利用异常的传递性，在主程序捕获异常
try:
    print(demo2())
except Exception as result:
    print("未知错误 %s" % result)
