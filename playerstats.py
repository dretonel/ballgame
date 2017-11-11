# playerstats.py - Ball Stats Module to display player stats on Pygame screen
# Author:        Dan Retonel
# Date:            29 Sept 2017
# Contains Playerstats() Class that controls, preps, and draws the player
# stats on the pygame screen.

import pygame.font


# Playerstats class that allows display of player stats. It requires a
# settings, screen, and playerdict object to initialize.
class Playerstats():
    """A class to report player stats."""

    def __init__(self, bstats_settings, screen, playerdict):
        """Initialize player statistic attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bstats_settings = bstats_settings
        self.playerdict = playerdict

        # Font size for player stats
        self.font = pygame.font.SysFont("Courier", 14, bold=True)

        # Prepare the initial player stats
        self.prep_stats()

    def prep_editmode_str(self):
        """Show a string to notify Edit Mode."""
        self.stats_str = 'Edit Mode'
        self.stats_image = self.font.render(
            self.stats_str, True,
            self.bstats_settings.colorText,
            self.bstats_settings.bg_color
        )

        # Set the location of the edit mode str on the bottom right.
        self.stats_rect = self.stats_image.get_rect()
        self.stats_rect.bottomright = self.screen_rect.bottomright

        self.show_stats()

    # --- NOT CURRENLY USED --- #
    def prep_stats_header(self):
        """Turn the stats into a rendered image."""
        stats_str = ''
        for values in self.bstats_settings.stats_sb_header:
            stats_str += str(values)
            stats_str += ' '

        self.stats_image = self.font.render(
            stats_str, True,
            self.bstats_settings.colorHome,
            self.bstats_settings.bg_color
        )

        # Set the location the score on the mid left of the screen.
        self.stats_rect = self.stats_image.get_rect()
        self.stats_rect.midleft = self.screen_rect.midleft

    def show_stats(self):
        """Turn the scores into a rendered image."""
        self.screen.blit(self.stats_image, self.stats_rect)

    def prep_stats(self):
        """Turn the stats from playerdict into a rendered image."""
        self.homecount = 0
        self.awaycount = 0
        self.count = 0

        # In each player, prep each stats line, line-by-line
        for player in self.playerdict.values():

            # Stats buffer string; needs to be cleared for every player
            self.stats_str = ''

            # Player on home team ? prep values for home player then print
            if player.team == 'Home':

                # Parse playerstats list to get which values to print
                # If value is player name, make player name at least 9 chars
                for i, values in \
                        enumerate(self.bstats_settings.get_playerdict(player)):
                    self.stats_str += str(values)
                    while i is 0 and (len(self.stats_str) < 9):
                        self.stats_str += ' '
                    self.stats_str += '  '            # spacing between fields

                self.homecount += 1
                self.count = self.homecount
                offsetx = 0

                # render stats str into a font image with correct settings
                self.stats_image = self.font.render(
                    self.stats_str, True,
                    self.bstats_settings.colorHome,
                    self.bstats_settings.bg_color
                )
            elif player.team == 'Away':

                # Parse playerstats list to get which values to print
                # If value is player name, make player name at least 9 chars
                for i, values in \
                        enumerate(self.bstats_settings.get_playerdict(player)):
                    self.stats_str += str(values)
                    while i is 0 and (len(self.stats_str) < 9):
                        self.stats_str += ' '
                    self.stats_str += '  '            # spacing between fields

                self.awaycount += 1
                self.count = self.awaycount
                offsetx = self.bstats_settings.screen_width / 2

                # render stats str into a font image with correct settings
                self.stats_image = self.font.render(
                    self.stats_str, True,
                    self.bstats_settings.colorAway,
                    self.bstats_settings.bg_color
                )

            # Display the stats on the mid left of the screen.
            self.stats_rect = self.stats_image.get_rect()
            self.stats_rect.midleft = self.screen_rect.left + offsetx,\
                self.screen_rect.centery + 100 + self.count * 25

            self.show_stats()

#    def __get_stats_str(self, team):
