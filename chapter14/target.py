import pygame
class Target():
    """A shape that can move up and down the the right side of a screen."""
    def __init__(self, a1_settings):
        """Initialize the attributes and methods of the class."""
        self.a1_settings = a1_settings
        self.screen_rect = self.a1_settings.screen_rect
        self.width = 50
        self.height = 40
        self.rect = pygame.Rect(self.a1_settings.screen_width - 60, 10, 50, 40)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.right = self.screen_rect.right
        self.colour = 60, 60, 60
        self.moving_direction = 1

    def update(self):
        self.y= float(self.rect.x)
        self.y += self.a1_settings.target_speed_factor * self.moving_direction
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)


