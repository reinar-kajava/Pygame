
class Stats():
    """This file is responsible for the statistics of the game"""

    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.game_active = False

        self.resetstats()

    """Restarts stats"""

    def resetstats(self):
        self.ships_left = self.game_settings.ship_limit
        self.score = 0


