import pygame
from plane_sprite import *

class GameMain(object):
    """创建主游戏类"""
    # 初始化主游戏类
    def __init__(self):
        # 1.建立游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_SIZE.size)
        # 2.设置游戏时钟
        self.clock = pygame.time.Clock()
        # 3.创建游戏精灵
        self.__create_sprite()

        # 4.使用时钟来创建敌机的事件频率
        pygame.time.set_timer(EMENY_CREATE_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,300)

    def __create_sprite(self):
        """创建游戏精灵"""
        # 1.创建背景精灵
        bg1 = BackGround()
        bg2 = BackGround(True)
        # 2.创建背景精灵组
        self.back_group = pygame.sprite.Group(bg1,bg2)

        # 3.创建敌机精灵组
        self.enemy_grop = pygame.sprite.Group()

        # 4.创建英雄精灵和精灵组
        self.hero = HeroPlane()
        self.hero2 = HeroPlane(True)
        self.hero_group = pygame.sprite.Group(self.hero,self.hero2)

    def start_game(self):
        """定义开始游戏的方法"""
        print("游戏开始")
        while True:
            # 1. 设置时钟频率
            self.clock.tick(FRAME_PER_SEC)
            # 2. 事件监听
            self.__event_listen()
            # 3. 碰撞检测
            self.__check_collted()
            # 4. 更新精灵/精灵组
            self.__update_sprite()
            # 5. 绘制到屏幕上
            pygame.display.update()

    def __event_listen(self):
        # 定义退出事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameMain.__game_over()
            # 如果触发敌机创建事件，就创建一个敌机对象，并且加入敌机组
            elif event.type ==  EMENY_CREATE_EVENT:
                enemy = EmenyPlane()
                self.enemy_grop.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero2.fire()
                self.hero.fire()
        # 获取英雄按键事件
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_LEFT]:
            self.hero.speed = -3
            self.hero2.speed = -3
        elif key_press[pygame.K_RIGHT]:
            self.hero.speed = 3
            self.hero2.speed = 3
        else:
            self.hero.speed = 0
            self.hero2.speed = 0

    def __check_collted(self):
        # 1. 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bulltes, self.enemy_grop, True, True)
        pygame.sprite.groupcollide(self.hero2.bulltes, self.enemy_grop, True, True)

        # 2. 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_grop, True)
        enemies2 = pygame.sprite.spritecollide(self.hero2, self.enemy_grop, True)

        # 判断列表时候有内容
        if len(enemies + enemies2) > 0:
            # 让英雄牺牲
            self.hero.kill()
            self.hero2.kill()

            # 结束游戏
            GameMain.__game_over()


    def __update_sprite(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_grop.update()
        self.enemy_grop.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bulltes.update()
        self.hero.bulltes.draw(self.screen)

        self.hero2.bulltes.update()
        self.hero2.bulltes.draw(self.screen)
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == "__main__":

    game = GameMain()

    game.start_game()