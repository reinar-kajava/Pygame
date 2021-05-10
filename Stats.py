class Stats():
    # This file is responsible for stats
    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.game_active = False

        self.resetstats()

    def resetstats(self):
        self.ships_left = self.game_settings.ship_limit
        """Restarts stats"""
#This file is responsible for stats
