# the class of the game's stats
class GameStats():
    def __init__(self, setting):
        self.setting = setting
        self.reset_stats()
        # activating the game for the first time making the high score 0
        self.game_active = False
        self.high_score = 0

    # resetting the score when main character dies
    def reset_stats(self):
        self.rabbit_left = self.setting.rabbit_limit
        self.score = 0
