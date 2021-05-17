import pygame.font
class Score():
    def __init__(self, game_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 46)

        """Prepeare graphical score"""
        self.prepare_score()

    def prepare_score(self):
        score_str = str(self.stats.score)
        """Convert msg"""
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right
        self.score_image_rect.top = 20

    def draw_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)