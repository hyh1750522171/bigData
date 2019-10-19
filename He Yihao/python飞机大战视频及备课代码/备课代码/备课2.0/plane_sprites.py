import random
import pygame

# 屏幕尺寸
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)


class GameSprite(pygame.sprite.Sprite):
    """游戏精灵"""

    def __init__(self, image_name, speed=1):
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.top += self.speed

    @staticmethod
    def image_names(prefix, count):
        names = []
        for i in range(1, count + 1):
            names.append("./images/" + prefix + str(i) + ".png")

        return names


class Background(GameSprite):
    """背景精灵"""

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")

        if is_alt:
            self.rect.bottom = 0

    def update(self, *args):
        super().update(args)

        if self.rect.top >= SCREEN_RECT.height:
            self.rect.bottom = 0


class PlaneSprite(GameSprite):
    """飞机精灵，包括敌机和英雄"""

    def __init__(self, image_names, destroy_names, life, speed):

        image_name = image_names[0]
        super().__init__(image_name, speed)

        # 生命值
        self.life = life

        # 正常图像列表
        self.__life_images = []
        for file_name in image_names:
            image = pygame.image.load(file_name)
            self.__life_images.append(image)

        # 被摧毁图像列表
        self.__destroy_images = []
        for file_name in destroy_names:
            image = pygame.image.load(file_name)
            self.__destroy_images.append(image)

        # 默认播放生存图片
        self.images = self.__life_images
        # 显示图像索引
        self.show_image_index = 0
        # 是否循环播放
        self.is_loop_show = True
        # 是否可以被删除
        self.can_destroied = False

    def update(self, *args):
        self.update_images()

        super().update(args)

    def update_images(self):
        """更新图像"""

        pre_index = int(self.show_image_index)
        self.show_image_index += 0.05
        count = len(self.images)

        # 判断是否循环播放
        if self.is_loop_show:
            self.show_image_index %= len(self.images)
        elif self.show_image_index > count - 1:
            self.show_image_index = count - 1
            self.can_destroied = True

        current_index = int(self.show_image_index)

        if pre_index != current_index:
            self.image = self.images[current_index]

    def destroied(self):
        """飞机被摧毁"""

        # 默认播放生存图片
        self.images = self.__destroy_images
        # 显示图像索引
        self.show_image_index = 0
        # 是否循环播放
        self.is_loop_show = False


class Hero(PlaneSprite):
    """英雄精灵"""

    def __init__(self):

        image_names = GameSprite.image_names("me", 2)
        destroy_names = GameSprite.image_names("me_destroy_", 4)

        super().__init__(image_names, destroy_names, 0, 0)

        # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹组
        self.bullets = pygame.sprite.Group()

    def update(self, *args):
        self.update_images()

        # 飞机水平移动
        self.rect.left += self.speed

        # 超出屏幕检测
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        """发射子弹"""

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


class Enemy(PlaneSprite):
    """敌机精灵"""

    def __init__(self):
        image_names = ["./images/enemy1.png"]
        destroy_names = GameSprite.image_names("enemy1_down", 4)
        super().__init__(image_names, destroy_names, 2, 1)

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

        # 判断敌机是否已经被销毁
        if self.can_destroied:
            self.kill()
