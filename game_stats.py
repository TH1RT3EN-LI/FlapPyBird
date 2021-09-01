class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化"""
        self.ai_settings = ai_settings
        self.game_active = False
        self.died_times = 0
        self.score = -1
        self.angle = 0
