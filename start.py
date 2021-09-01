import pygame
from birds import Bird
from settings import Settings
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats
from button import Button
from bird_motion import BirdMotion


def run_game():
    # 初始化游戏 创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    pygame.display.set_caption('Flappy Birds')

    # 创建游戏数据实例
    stats = GameStats(ai_settings)

    # 用Group存储分数
    score_board = Group()

    # 创建鸟实例
    bird = Bird(screen, ai_settings, stats)

    # 创建鸟动作实例
    bm = BirdMotion(screen, (17, 12), stats)

    bird_motion = Group()
    bird_motion.add(bm)

    # 用编组存储pillar
    pillars_a = Group()
    pillars_b = Group()

    bg = pygame.image.load(r'Flappy Bird\image\bg\bg.jpg')

    # 用编组存储ground
    grounds = Group()

    # 创建按钮实例
    play_button = Button(screen, r'Flappy Bird\image\button\button_play.png')
    restart_button = Button(screen, r'Flappy Bird\image\button\button_restart.png')
    quit_button = Button(screen, r'Flappy Bird\image\button\quit_button.png')
    quit_button.rect.y += 30

    while True:
        gf.check_event(bird, play_button, restart_button, stats, pillars_a, pillars_b, score_board,
                       ai_settings, quit_button)
        if stats.game_active:
            ai_settings.ground_speed = 0.15
            ai_settings.pillar_speed = 0.15
            bird.update()
            bird.update_angle()
            gf.check_pillar_collide(bird, pillars_a, pillars_b, stats, ai_settings, restart_button)
        gf.update_screen(screen, ai_settings, bird, pillars_a, pillars_b, grounds, bg, play_button,
                         stats, restart_button, bird_motion, score_board, quit_button)


run_game()
