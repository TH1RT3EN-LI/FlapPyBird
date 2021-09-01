class Settings():
    def __init__(self):
        '''设置基本参数'''
        # 屏幕设置
        self.screen_height = 700
        self.screen_width = 450
        self.bg_color = (230, 230, 230)

        # 鸟的设置
        self.bird_drop_speed = 0.2
        self.bird_up_speed = 0.6
        self.moving_direction = -1
        self.rotate_up_speed = 0.4
        self.rotate_down_speed = 0.2
        self.rotate_accelerate = 0

        # 柱子设置
        self.pillar_color = (0, 0, 99)
        self.grap = 180
        self.pillar_width = 80
        self.pillar_speed = 0
        self.pillar_space_para = 4
        self.pillar_factor = 0

        # 地面设置
        self.ground_color = (0, 99, 0)
        self.ground_height = 120
        self.ground_width = 480
        self.ground_speed = 0.15

        # 得分检测集合
        self.p = set()
