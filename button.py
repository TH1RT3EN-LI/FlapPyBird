import pygame


class Button():

    def __init__(self, screen, path):
        """初始化"""
        self.screen = screen

        self.button = pygame.image.load(path)
        self.rect = self.button.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.button, self.rect)
