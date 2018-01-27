# timer.py - Timer module for Ball Stats

import pygame.font

class Timer():
    """A class to display the timer."""

    def __init__(self, bstats_settings, screen):
        """Initialize timer attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bstats_settings = bstats_settings

        self.font = pygame.font.SysFont("Courier", 56)

