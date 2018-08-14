import random
import pygame

# 1.设置屏幕常量
SCREEN_SIZE = pygame.Rect(0, 0, 480, 700)
# 2.设置敌机创建事件常量
EMENY_CREATE_EVENT = pygame.USEREVENT
# 3.设置刷新帧率
FRAME_PER_SEC = 60
# 4.设置英雄发射子弹常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """游戏精灵类"""
    def __init__(self, image_name, speed=1):
        super().__init__()
        # 1.定义游戏精灵基本属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 2.重写父类方法
        super().update()
        # 3. 定义游戏精灵移动方法
        self.rect.y += self.speed


class BackGround(GameSprite):
    def __init__(self, is_alt=False):
        # 重写父类初始化方法,传入图像名称
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -SCREEN_SIZE.height

    def update(self):
        # 重写父类方法实现图片的轮播
        super().update()
        # 判断图片是否移出屏幕底端，如果移出，将图片放到屏幕上方
        if self.rect.y >= SCREEN_SIZE.height:
            self.rect.y = -self.rect.height


class EmenyPlane(GameSprite):
    """敌机类"""
    # 初始化,并且调用父类初始化方法
    def __init__(self):
        super().__init__("./images/enemy1.png")
        # 敌机的初始速度
        self.speed = random.randint(2,3)
        # 敌机的初始位置在屏幕上方的随机位置
        self.rect.bottom = 0
        max_x = SCREEN_SIZE.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        # 判断敌机如果飞出屏幕，销毁对象
        if self.rect.y >= SCREEN_SIZE.height:
            self.kill()
        def __del__(self):
            pass


class HeroPlane(GameSprite):
    """定义英雄类"""
    # 初始化
    def __init__(self, is_alt=False):
        super().__init__("./images/me1.png", 0)
        # 英雄的y距离屏幕底部120个像素，x在屏幕的中心
        self.rect.bottom = SCREEN_SIZE.bottom - 120
        self.rect.centerx = SCREEN_SIZE.centerx

        if is_alt:
            self.rect.centerx = self.rect.centerx * 3
        # 创建子弹组
        self.bulltes = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x == -SCREEN_SIZE.width:
            self.rect.x = SCREEN_SIZE.width

        if self.rect.x == SCREEN_SIZE.width * 2 - self.rect.width:
            self.rect.x = -self.rect.width

    def fire(self):
        #print("发射子弹")
        bullte = Bulletd()

        # 子弹位置
        bullte.rect.bottom = self.rect.y - 15
        bullte.rect.centerx = self.rect.centerx
        self.bulltes.add(bullte)


class Bulletd(GameSprite):
    """子弹类"""
    # 初始化
    def __init__(self):
        super().__init__("./images/bullet2.png", -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass

