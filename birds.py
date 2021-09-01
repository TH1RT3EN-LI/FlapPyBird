import pygame
from pygame.sprite import Sprite


class Bird(Sprite):
    """设置鸟的属性及功能"""
    def __init__(self, screen, ai_settings, stats):
        super().__init__()
        """初始化"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.stats = stats

        # 载入图像
        self.bird = pygame.image.load(r'Flappy Bird\image\bird\bird_location.jpg')

        # 创建鸟
        self.rect = self.bird.get_rect()

        # 设置位置
        self.screen_rect = self.screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.x = 100

        # 用小数存储鸟的位置
        self.bird_y = self.rect.centery

        # 设置移动参数 默认为False
        self.moving = False

        # 设置移动距离参数
        self.moving_distance = 0

    def update(self):
        """更新鸟的位置"""
        # 鸟时刻下坠
        self.bird_y += self.ai_settings.bird_drop_speed
        self.ai_settings.bird_drop_speed += 0.0001
        # 响应向上移动一段距离(减速)
        if self.moving:
            self.bird_y -= self.ai_settings.bird_up_speed
            self.ai_settings.bird_up_speed -= 0.0009
            self.moving_distance += 1
        self.rect.centery = self.bird_y
        if self.ai_settings.bird_up_speed <= 0:
            self.moving = False
            self.ai_settings.bird_up_speed = 0.6

    def get_location(self):
        """取得鸟的左上坐标"""
        return (self.rect.x, self.rect.y)

    def update_angle(self):
        """更新角度"""
        if not self.moving and self.stats.angle >= -90:
            self.stats.angle -= self.ai_settings.rotate_down_speed
        elif self.moving and self.stats.angle <= 45:
            self.stats.angle += self.ai_settings.rotate_up_speed + self.ai_settings.rotate_accelerate
            self.ai_settings.rotate_accelerate += 0.003
