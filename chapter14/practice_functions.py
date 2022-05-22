import pygame
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = True
        ship.update()
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
        ship.update()

def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def change_target_direction(target):
    """changes the direction of the target as it hits the top and bottom of the screen."""
    target.moving_direction *= -1