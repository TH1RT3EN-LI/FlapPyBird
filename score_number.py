import pygame

from pygame.sprite import Sprite


class ScoreNumber(Sprite):
    '''显示得分信息的类'''
    def __init__(self, screen, s):
        super().__init__()
        number_dict = {}

        self.zero = pygame.image.load(r'Flappy Bird\image\number\font_048.png')
        self.one = pygame.image.load(r'Flappy Bird\image\number\font_049.png')
        self.two = pygame.image.load(r'Flappy Bird\image\number\font_050.png')
        self.three = pygame.image.load(r'Flappy Bird\image\number\font_051.png')
        self.four = pygame.image.load(r'Flappy Bird\image\number\font_052.png')
        self.five = pygame.image.load(r'Flappy Bird\image\number\font_053.png')
        self.six = pygame.image.load(r'Flappy Bird\image\number\font_054.png')
        self.seven = pygame.image.load(r'Flappy Bird\image\number\font_055.png')
        self.eight = pygame.image.load(r'Flappy Bird\image\number\font_056.png')
        self.nine = pygame.image.load(r'Flappy Bird\image\number\font_057.png')

        number_list = [self.zero, self.one, self.two, self.three, self.four, self.five,
                       self.six, self.seven, self.eight, self.nine]

        for num in range(10):
            number_dict[str(num)] = number_list[num]

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.num = number_dict[s]
        self.rect = self.num.get_rect()
        self.rect.centery = self.screen_rect.centery / 8
        self.rect.centerx = self.screen_rect.centerx

    def blitme(self):
        """在屏幕上绘制"""
        self.screen.blit(self.num, self.rect)
