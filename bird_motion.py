import pygame
from pygame.sprite import Sprite


class BirdMotion(Sprite):
    def __init__(self, screen, originPos, stats):
        """初始化"""
        super().__init__()
        self.screen = screen
        self.stats = stats
        self.main_image = pygame.image.load(r'Flappy Bird\image\bird\birds.png')
        self.image_rect = self.main_image.get_rect()
        self.frame_width = self.image_rect.width / 3
        self.frame_height = self.image_rect.height
        self.columns = 3
        self.last_frame = 2
        self.last_time = 0
        self.frame = 0
        self.old_frame = -1
        self.first_frame = 0
        self.originPos = originPos

    def update(self, current_time, pos, rate=120):
        """更新图像动画"""
        # 扇动翅膀
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            part_rect = (frame_x, frame_y, self.frame_width, self.frame_height)
            self.image_r = self.main_image.subsurface(part_rect)
            self.old_frame = self.frame

        # 旋转图像
        self.pos = pos
        self.angle = self.stats.angle

        self.w = 34
        self.h = 24
        self.box = [pygame.math.Vector2(p) for p in [(0, 0), (self.w, 0), (self.w, -self.h), (0, -self.h)]]
        self.box_rotate = [p.rotate(self.angle) for p in self.box]
        self.min_box = (min(self.box_rotate, key=lambda p: p[0])[0], min(self.box_rotate, key=lambda p: p[1])[1])
        self.max_box = (max(self.box_rotate, key=lambda p: p[0])[0], max(self.box_rotate, key=lambda p: p[1])[1])

        self.pivot = pygame.math.Vector2(self.originPos[0], - self.originPos[1])
        self.pivot_rotate = self.pivot.rotate(self.angle)
        self.pivot_move = self.pivot_rotate - self.pivot

        self.origin = (self.pos[0] - self.originPos[0] - self.pivot_move[0] + self.min_box[0],
                       self.pos[1] - self.max_box[1] - self.originPos[1] + self.pivot_move[1])
        self.origin = (self.pos[0], self.pos[1])
        self.rect = self.origin
        self.image = pygame.transform.rotate(self.image_r, self.angle)
