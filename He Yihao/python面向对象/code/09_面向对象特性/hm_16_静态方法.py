class Dog(object):

    @staticmethod
    def run():
        
        # 不访问实例属性/类属性
        print("小狗要跑...")

# 通过类名.调用静态方法 - 不需要创建对象
Dog.run()
