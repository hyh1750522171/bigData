import pygame
from plane_sprites import *

pygame.init()

# 游戏代码...
# 1. 创建游戏主窗口
screen = pygame.display.set_mode(SCREEN_RECT.size)

# 2. 创建英雄精灵组
hero = Hero("./images/me1.png")
hero_group = pygame.sprite.Group(hero)

# 3. 创建游戏时钟对象
clock = pygame.time.Clock()

# 游戏循环
while True:

    # 设置屏幕刷新帧率
    clock.tick(60)

    # 事件监听
    for event in pygame.event.get():

        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏...")

            pygame.quit()

            # 直接退出系统
            exit()

    # 填充背景颜色
    screen.fill((255, 255, 255))

    # 让精灵组更新位置并且绘制精灵
    hero_group.update()
    hero_group.draw(screen)

    # 更新屏幕显示
    pygame.display.update()
