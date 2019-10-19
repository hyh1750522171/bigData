#! /usr/bin/python3

import pygame
from plane_sprites import *

# 敌机出现事件
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class PlaneGame(object):
    """飞机大战游戏类"""

    def __init__(self):

        # 1. pygame 初始化
        pygame.init()

        # 2. 创建游戏屏幕
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 3. 创建游戏时钟
        self.clock = pygame.time.Clock()

        # 4. 创建精灵组
        self.__create_sprites()

        # 5. 创建用户事件
        PlaneGame.__create_user_events()

    def __create_sprites(self):
        """创建精灵组"""

        # 背景组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 敌机组
        enemy = Enemy()
        self.enemy_group = pygame.sprite.Group(enemy)

        # 英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    @staticmethod
    def __create_user_events():
        """创建用户事件"""

        # 每秒添加一架敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1 * 1000)

        # 每秒发射两次子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def start_game(self):
        """开始游戏"""
        while True:
            # 1. 设置刷新帧率
            self.clock.tick(60)
            # 2. 事件监听
            self.__event_handler()
            # 3. 更新精灵组
            self.__update_sprites()
            # 碰撞检测
            self.__check_collide()
            # 4. 更新屏幕显示
            pygame.display.update()

    def __event_handler(self):
        """事件监听"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                print("退出游戏...")
                pygame.quit()
                exit()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机，并且添加到敌机组
                self.enemy_group.add(Enemy())

                # 测试敌机精灵数量
                # enemy_count = len(self.enemy_group.sprites())
                # print("敌机精灵数量 %d" % enemy_count)
            elif event.type == HERO_FIRE_EVENT:
                # 英雄发射子弹
                self.hero.fire()

        # 通过 pygame.key 获取用户按键
        keys_pressed = pygame.key.get_pressed()
        dir = keys_pressed[pygame.K_RIGHT] - keys_pressed[pygame.K_LEFT]

        # 根据移动方向设置英雄的速度
        self.hero.speed = dir * 2

    def __update_sprites(self):
        """更新精灵组"""

        for group in [self.back_group, self.enemy_group,
                      self.hero_group, self.hero.bullets]:

            group.update()
            group.draw(self.screen)

    def __check_collide(self):
        """碰撞检测"""

        # 1. 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 2. 英雄被撞毁
        collide_list = pygame.sprite.spritecollide(self.hero, self.enemy_group, False)

        if len(collide_list) > 0:
            self.hero.is_alive = False

            print("英雄牺牲...")

            pygame.quit()
            exit()

if __name__ == '__main__':
    # 1. 创建游戏对象
    game = PlaneGame()

    # 2. 开始游戏
    game.start_game()
