import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Alien class"""
    def __init__(self, game_setting, screen):
        super().__init__()
        self.screen = screen
        self.game_settings = game_setting
        self.image = pygame.image.load("Images/vaenlane.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw ship at this position"""
        self.screen.blit(self.image, self.rect)