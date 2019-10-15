class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()

tom.eat()
tom.drink()

print(tom)

# 再创建一个猫对象
lazy_cat = Cat()

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

lazy_cat2 = lazy_cat

print(lazy_cat2)
