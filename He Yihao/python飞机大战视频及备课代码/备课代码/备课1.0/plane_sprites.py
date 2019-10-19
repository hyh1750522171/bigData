import random
import pygame


# 游戏屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)


class GameSprite(pygame.sprite.Sprite):
    """游戏精灵基类"""

    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 加载图像
        self.image = pygame.image.load(image_name)
        # 设置尺寸
        self.rect = self.image.get_rect()
        # 记录速度
        self.speed = speed

    def update(self, *args):

        # 默认在垂直方向移动
        self.rect.top += self.speed


class Background(GameSprite):
    """背景精灵"""

    def __init__(self, is_alt=False):

        image_name = "./images/background.png"
        super().__init__(image_name)

        # 判断是否交替图片，如果是，将图片设置到屏幕顶部
        if is_alt:
            self.rect.bottom = 0

    def update(self, *args):

        # 调用父类方法
        super().update(args)

        # 判断是否超出屏幕
        if self.rect.top >= SCREEN_RECT.height:
            self.rect.bottom = 0


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):

        image_name = "./images/enemy1.png"
        super().__init__(image_name)

        # 随机敌机出现位置
        width = SCREEN_RECT.width - self.rect.width
        self.rect.left = random.randint(0, width)
        self.rect.bottom = 0

        # 随机速度
        self.speed = random.randint(1, 3)

    def update(self, *args):
        super().update(args)

        # 判断敌机是否移出屏幕
        if self.rect.top >= SCREEN_RECT.height:
            # 将精灵从所有组中删除
            self.kill()


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):

        image_name = "./images/me1.png"
        super().__init__(image_name, 0)

        # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹组
        self.bullets = pygame.sprite.Group()

    def update(self, *args):

        # 飞机水平移动
        self.rect.left += self.speed

        # 超出屏幕检测
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):

        # bullet_count = len(self.bullets.sprites())
        # print("子弹数量 %d" % bullet_count)

        for i in range(0, 3):
            # 创建子弹精灵
            bullet = Bullet()

            # 设置子弹位置
            bullet.rect.bottom = self.rect.top - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 将子弹添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):

        image_name = "./images/bullet1.png"
        super().__init__(image_name, -2)

    def update(self, *args):

        super().update(args)

        # 判断是否超出屏幕
        if self.rect.bottom < 0:
            self.kill()
