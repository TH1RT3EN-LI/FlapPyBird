import pygame
import sys
from pillar_a import PillarA
from pillar_b import PillarB
from ground import Ground
from score_number import ScoreNumber


def check_keydown_event(event, bird, ai_settings):
    """响应按键按下的事件"""
    if event.key == pygame.K_SPACE:
        bird.moving = True
        ai_settings.rotate_accelerate = 0
        ai_settings.bird_up_speed = 0.6
        ai_settings.bird_drop_speed = 0.2


def check_event(bird, play_button, restart_button, stats, pillars_a, pillars_b, score_board,
                ai_settings, quit_button):
    """捕获事件"""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_event(event, bird, ai_settings)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if not stats.game_active:
                check_play_button(play_button, stats, mouse_x, mouse_y, bird)
                check_restart_button(restart_button, stats, mouse_x, mouse_y, pillars_a,
                                     pillars_b, bird, score_board, ai_settings)
                check_quit_button(quit_button, mouse_x, mouse_y, stats)
        elif event.type == pygame.QUIT:
            sys.exit()


def creat_pillar(pillars_a, pillars_b, screen, ai_settings):
    """创建柱子并添加到Group中"""
    len_p = len(pillars_a)
    for i in range(3 - len_p):
        pillar_a = PillarA(screen, ai_settings)
        pillar_b = PillarB(screen, ai_settings)
        if len(pillars_a) > 0:
            # 用  pygame.sprite.Group.sprites()  获取pillars列表 是可进行迭代的对象
            last_x = pillars_a.sprites()[-1].a_x
            pillar_a.a_x = last_x + ai_settings.pillar_space_para * ai_settings.pillar_width
        else:
            pillar_a.a_x = ai_settings.screen_width + 0.5*ai_settings.pillar_width + 999
        pillar_b.b_x = pillar_a.a_x
        pillars_a.add(pillar_a)
        pillars_b.add(pillar_b)


def update_pillar(pillars_a, pillars_b, screen, ai_settings, bird, stats):
    """维持柱子数量， 在屏幕上打印柱子并更新其位置"""
    if len(pillars_a) < 3:
        creat_pillar(pillars_a, pillars_b, screen, ai_settings)
    for pillar in pillars_a:
        pillar.update()
        pillar.blitme()
        if bird.rect.left == pillar.rect.right:
            ai_settings.p.add(pillar)
        check_pillar(pillars_a, pillar, ai_settings)
    for pillar in pillars_b:
        pillar.update()
        pillar.blitme()
        check_pillar(pillars_b, pillar, ai_settings)
    check_up_border(bird, stats, ai_settings)


def check_pillar(pillars, pillar, ai_settings):
    """检测出界的柱子并删除"""
    if pillar.rect.right < 0:
        pillars.remove(pillar)


def creat_ground(grounds, screen, ai_settings):
    """创建地面"""
    len_g = len(grounds)
    for i in range(2 - len_g):
        ground = Ground(screen, ai_settings)
        if len(grounds) > 0:
            ground.x = ai_settings.screen_width * 1.5
        grounds.add(ground)


def update_ground(grounds, screen, ai_settings, bird, stats):
    """保持地面循环移动"""
    if len(grounds) < 2:
        creat_ground(grounds, screen, ai_settings)
    for ground in grounds:
        ground.update()
        ground.blitme()
        check_ground(grounds, ground, ai_settings)
    check_ground_collide(bird, grounds, stats, ai_settings)


def check_ground(grounds, ground, ai_settings):
    """移除出界的地面"""
    if ground.rect.right <= 0:
        grounds.remove(ground)


def check_pillar_collide(bird, pillars_a, pillars_b, stats, ai_settings, restart_button):
    """检测柱子和鸟的碰撞并响应"""
    if pygame.sprite.spritecollideany(bird, pillars_a) or pygame.sprite.spritecollideany(bird, pillars_b):
        stats.game_active = False
        stats.died_times += 1
        ai_settings.pillar_speed = 0
        ai_settings.ground_speed = 0


def check_ground_collide(bird, grounds, stats, ai_settings):
    """检测地面和鸟的碰撞并响应"""
    if pygame.sprite.spritecollideany(bird, grounds):
        stats.game_active = False
        stats.died_times += 1
        ai_settings.pillar_speed = 0
        ai_settings.ground_speed = 0


def check_play_button(play_button, stats, mouse_x, mouse_y, bird):
    """响应开始按钮"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
        bird.moving = True


def check_restart_button(restart_button, stats, mouse_x, mouse_y, pillars_a, pillars_b,
                         bird, score_board, ai_settings):
    """响应重新开始按钮"""
    if restart_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
        pillars_a.empty()
        pillars_b.empty()
        bird.bird_y = 300
        ai_settings.p.clear()
        stats.score = -1
        score_board.empty()
        bird.moving = True


def bird_float(bird, ai_settings):
    """未开始时鸟上下浮动"""
    float_range = bird.rect.height * 0.3
    bird.bird_y += 0.03 * ai_settings.moving_direction
    bird.rect.centery = bird.bird_y
    if bird.bird_y <= bird.screen_rect.centery - float_range:
        ai_settings.moving_direction *= -1
    elif bird.bird_y >= bird.screen_rect.centery + float_range:
        ai_settings.moving_direction *= -1


def update_score(ai_settings, stats, score_board, screen):
    """绘制分数，更新得分"""
    if stats.score != len(ai_settings.p):
        stats.score += 1
        score_board.empty()
        update_score_board(stats, score_board, screen)
    for num in score_board:
        num.blitme()


def update_score_board(stats, score_board, screen):
    """用得分板显示分数，设置其位置"""
    score = str(stats.score)
    for s in score:
        sn = ScoreNumber(screen, s)
        score_board.add(sn)
    n = len(score_board)
    score_board.sprites()[0].rect.centerx -= (n-1) * 0.5 * 20
    for x in range(n):
        if x != 0:
            score_board.sprites()[x].rect.left = score_board.sprites()[x-1].rect.right


def check_up_border(bird, stats, ai_settings):
    """检测鸟是否接触上边界"""
    if bird.rect.top <= 0:
        stats.game_active = False
        stats.died_times += 1
        ai_settings.pillar_speed = 0
        ai_settings.ground_speed = 0


def check_quit_button(quit_button, mouse_x, mouse_y, stats):
    if quit_button.rect.collidepoint(mouse_x, mouse_y):
        sys.exit()


def update_screen(screen, ai_settings, bird, pillars_a, pillars_b, grounds, bg, play_button, stats,
                  restart_button, bird_motion, score_board, quit_button):
    """更新屏幕上的元素"""
    # 填充背景
    screen.blit(bg, (0, 0))

    # 更新柱子
    update_pillar(pillars_a, pillars_b, screen, ai_settings, bird, stats)

    # 绘制鸟
    ticks = pygame.time.get_ticks()
    bird_motion.update(ticks, bird.get_location())
    bird_motion.draw(screen)

    # 更新地面
    update_ground(grounds, screen, ai_settings, bird, stats)

    # 更新分数
    update_score(ai_settings, stats, score_board, screen)

    # 显示按键
    if not stats.game_active and stats.died_times == 0:
        play_button.blitme()
        bird_float(bird, ai_settings)
    elif not stats.game_active and stats.died_times > 0:
        restart_button.blitme()
        quit_button.blitme()

    # 绘制所有元素
    pygame.display.flip()
