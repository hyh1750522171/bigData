import pygame

# 游戏屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 800, 600)

pygame.init()

# 游戏代码...
# 1. 创建游戏主窗口
screen = pygame.display.set_mode(SCREEN_RECT.size)

# 2. 绘制英雄
# 1> 加载图像
hero = pygame.image.load("./images/me1.png")
# 2> 绘制图像
screen.blit(hero, (400, 300))
# 3> 更新屏幕
pygame.display.update()

# 3. 创建游戏时钟对象
clock = pygame.time.Clock()

# 4. 定义英雄的初始位置
hero_rect = pygame.Rect(400, 300, 102, 126)

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

    # 更新英雄的位置
    hero_rect.top -= 1

    # 判断是否移出屏幕
    if hero_rect.top <= 0:
        hero_rect.top = SCREEN_RECT.height

    # 填充背景颜色
    screen.fill((255, 255, 255))

    # 绘制英雄
    screen.blit(hero, hero_rect)

    # 更新屏幕显示
    pygame.display.update()
