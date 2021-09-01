import pygame
import random
from pygame.sprite import Sprite


class PillarA(Sprite):
    """设置柱子的属性及功能"""
    def __init__(self, screen, ai_settings):
        super().__init__()
        """初始化"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 载入图像
        self.pillar_a_image = pygame.image.load(r'Flappy Bird\image\pillar\pillar_a.gif')

        # 计算随机的柱子间的空隙位置
        self.pillar_a_height = random.randint(30, self.ai_settings.screen_height -
                                              self.ai_settings.grap - self.ai_settings.ground_height - 30)

        # 把计算结果暂时保存到settings 方便传递给B柱
        self.ai_settings.pillar_factor = self.pillar_a_height

        # 创建上柱
        self.rect = self.pillar_a_image.get_rect()

        # 得到屏幕的rect参数
        self.screen_rect = self.screen.get_rect()

        # 设置上柱y轴位置
        self.rect.bottom = self.pillar_a_height

        # 用小数储存柱子的x轴位置
        self.a_x = float(self.rect.centerx)

    def update(self):
        """自动移动"""
        self.a_x -= self.ai_settings.pillar_speed
        self.rect.centerx = self.a_x

    def blitme(self):
        """在屏幕上绘制"""
        self.screen.blit(self.pillar_a_image, self.rect)
