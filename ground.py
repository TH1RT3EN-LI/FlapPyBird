import pygame
from pygame.sprite import Sprite


class Ground(Sprite):
    """设置地面的属性和功能"""
    def __init__(self, screen, ai_settings):
        super().__init__()
        """初始化"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 载入图像
        self.ground = pygame.image.load(r'Flappy Bird\image\ground\ground.jpg')

        # 创建地面
        self.rect = self.ground.get_rect()

        # 获取屏幕参数
        self.screen_rect = self.screen.get_rect()

        # 确定地面y轴位置
        self.rect.bottom = self.screen_rect.bottom

        # 用小数储存地面的中心x位置
        self.x = float(self.rect.centerx)

    def update(self):
        """自动移动"""
        self.x -= self.ai_settings.ground_speed
        self.rect.centerx = self.x

    def blitme(self):
        """绘制地面"""
        self.screen.blit(self.ground, self.rect)
