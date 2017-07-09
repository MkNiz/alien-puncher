import pygame

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from pygame.sprite import Group

import game_logic as gl

def run_game():
    # Initialization of game and screen
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )
    pygame.display.set_caption("Alien Puncher")

    # Create a play button
    play_button = Button(game_settings, screen, "Play Game")

    # Create a game statistics and scoreboard instance
    stats = GameStats(game_settings)
    sb = Scoreboard(game_settings, screen, stats)

    # Create the player ship
    ship = Ship(game_settings, screen)

    # Store bullets in a group
    bullets = Group()

    # Store aliens in a group
    aliens = Group()

    # Create a fleet of aliens
    gl.create_fleet(game_settings, screen, ship, aliens)

    # Primary loop
    while True:
        gl.check_events(game_settings, stats, screen, ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            gl.update_bullets(game_settings, screen, ship, aliens, bullets)
            gl.update_aliens(game_settings, stats, screen, ship, aliens, bullets)

        gl.update(game_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
