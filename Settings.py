class Settings:
    """A class to store all setting for example game"""

    def __init__(self):
        """Initialize the game settings"""
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (100,200,255)
        self.ship_speed_factor = 1