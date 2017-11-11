# running.py
# Running score module for Ball Stats
# Author:        Dan Retonel
# Date:            18 Oct 2017

import pygame


class RunningScore():
    """ Displays the running score"""

    def __init__(self, bstats_settings, screen, playerdict):
        """Initialize running score attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bstats_settings = bstats_settings
        self.playerdict = playerdict

        self.width, self.height = 45, 36
