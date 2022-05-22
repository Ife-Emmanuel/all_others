import pygame
class Settings():
    """Represents settings for the game."""
    def __init__(self):
        """Initialize attributes and methods of the game."""
        self.screen = pygame.display.set_mode((1280, 700))
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height
        self.bg_colour = 230, 230, 230

        #Speed settings
        self.target_speed_factor = 10
        self.ship_speed_factor = 5


