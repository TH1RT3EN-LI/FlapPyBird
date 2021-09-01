import pygame
from pygame.sprite import Sprite


class PillarB(Sprite):
    """设置柱子的属性及功能"""
    def __init__(self, screen, ai_settings):
        super().__init__()
        """初始化"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 载入图像
        self.pillar_b_image = pygame.image.load(r'Flappy Bird\image\pillar\pillar_b.gif')

        # 创建下柱
        self.rect = self.pillar_b_image.get_rect()

        # 得到屏幕的rect参数
        self.screen_rect = self.screen.get_rect()

        # 设置下柱y轴位置
        self.rect.top = self.ai_settings.pillar_factor + self.ai_settings.grap

        # 用小数储存柱子的x轴位置
        self.b_x = float(self.rect.centerx)

    def update(self):
        """自动移动"""
        self.b_x -= self.ai_settings.pillar_speed
        self.rect.centerx = self.b_x

    def blitme(self):
        """在屏幕上绘制"""
        self.screen.blit(self.pillar_b_image, self.rect)
