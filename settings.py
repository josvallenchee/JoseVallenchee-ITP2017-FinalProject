#the setting's class
class Setting():
    # function of the class
    def __init__(self):
        # making the screen's setting
        self.width = 800
        self.height = 600
        self.color = (0,0,0)

        # limit_rabbit = 0
        # self.rabbit_limit = limit_rabbit

        # settings of the bullet
        bullet_size = 10
        self.bullet_width = bullet_size
        self.bullet_height = bullet_size

        self.bullet_color = (255,0,0)
        no_bullet = 100000
        self.bullets_allowed = no_bullet
        drop_speed = 10
        self.drop_speed = drop_speed

        # the scale for the speed up
        scale_speed = 1.1
        self.speedup_scale = scale_speed

        # scale of the score
        scale_score = 1.5
        self.score_scale = scale_score

        self.initialize_dynamic_settings()

    # functions of rabbit, bullet, mouse speed and mouse points
    def initialize_dynamic_settings(self):
        self.rabbit_speed = 1
        self.bullet_speed = 3
        self.mouse_speed = 0.5
        self.mouse_points = 50

    # functions for the increase rate of speed of the mouse, bullet and rabbit
    def increase_speed(self):
        self.rabbit_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.mouse_speed *= self.speedup_scale

        self.mouse_points = int(self.mouse_points*self.score_scale)