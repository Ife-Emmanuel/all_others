import pygame
class ship():
    def __init__(self, a1_settings):
        """Initialize attributes and methods for the ship"""
        image_path = r'C:\Users\User\PycharmProjects\Alien_Invasion\images'
        self.image = pygame.image.load(image_path)
        self.screen = a1_settings.screen
        self.rect = self.image.get_rect()
        self.a1_settings = a1_settings
        self.rect.left = self.a1_settings.screen_rect.right
        self.rect.top = 10
        self.moving_up = False
        self.moving_down = False

    def update(self):
        self.y= float(self.rect.x)
        if self.moving_up and self.rect.top > 0:
            self.y -= self.a1_settings.ship_speed_factor * self.motion_direction
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.a1_settings.ship_speed_factor * self.motion_direction
        self.rect.y = self.y

    def blitme(self):
        """Draw rect object to the screen."""
        self.screen.blit(self.image, self.rect)