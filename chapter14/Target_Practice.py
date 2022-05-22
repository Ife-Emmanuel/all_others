import pygame
class Rectangle():
    """A shape that can move up and down the the right side of a screen."""
    def __init__(self, a1_settings):
        """Initialize the attributes and methods of the class."""
        self.a1_settings = a1_settings
        self.width = 50
        self.height = 40
        self.rect = pygame.Rect(self.a1_settings.screen_width - 60, 10, 50, 40)
        self.colour = 60, 60, 60


    def draw(self):
        """Draw rect object to the screen."""
        pygame.draw.rect(self.screen, self.colour, self.rect)