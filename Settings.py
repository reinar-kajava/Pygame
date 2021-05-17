class Settings:
    """A class to store all setting for example game"""

    def __init__(self):
        """Initialize the game settings"""
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (150,150,128)
        # ship settings


        self.ship_limit = 3
        # bullet settings

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 6
        # aliens settings


        self.fleet_drop_speed = 5
        self.init_dynamics()

        #speed up factor
        self.speedup_scale = 1.1
    def init_dynamics(self):
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 0.5
        self.alien_speed_factor = 0.5

        # fleet derection right = 1, left = -1
        self.fleet_direction = 1

        self.alien_points = 50


    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        # fleet derection right = 1, left = -1
        self.fleet_direction = 1
