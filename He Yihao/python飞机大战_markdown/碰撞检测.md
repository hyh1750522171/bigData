# 碰撞检测

## 目标

* 了解碰撞检测方法
* 碰撞实现

## 01. 了解碰撞检测方法

* `pygame` 提供了 **两个非常方便** 的方法可以实现碰撞检测：

### pygame.sprite.groupcollide()

* **两个精灵组** 中 **所有的精灵** 的碰撞检测

```python
groupcollide(group1, group2, dokill1, dokill2, collided = None) -> Sprite_dict
```

* 如果将 `dokill` 设置为 `True`，则 **发生碰撞的精灵将被自动移除**
* `collided` 参数是用于 **计算碰撞的回调函数**
    * 如果没有指定，则每个精灵必须有一个 `rect` 属性

### pygame.sprite.spritecollide()

* 判断 **某个精灵** 和 **指定精灵组** 中的精灵的碰撞

```python
spritecollide(sprite, group, dokill, collided = None) -> Sprite_list
```

* 如果将 `dokill` 设置为 `True`，则 **指定精灵组** 中 **发生碰撞的精灵将被自动移除**
* `collided` 参数是用于 **计算碰撞的回调函数**
    * 如果没有指定，则每个精灵必须有一个 `rect` 属性
* 返回 **精灵组** 中跟 **精灵** 发生碰撞的 **精灵列表**

## 02. 碰撞实现

```python
def __check_collide(self):

    # 1. 子弹摧毁敌机
    pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
    
    # 2. 敌机撞毁英雄
    enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
    
    # 判断列表时候有内容
    if len(enemies) > 0:
    
        # 让英雄牺牲
        self.hero.kill()
        
        # 结束游戏
        PlaneGame.__game_over()
```


