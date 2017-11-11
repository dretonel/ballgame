import pygame.font


class Scoreboard():
    """A class to report the team scores."""

    def __init__(self, bstats_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bstats_settings = bstats_settings
        self.stats = stats

        # Font size for scoring information
        self.font = pygame.font.SysFont(None, 56)

        # Prepare the intial score image.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = 'Home: ' + str(self.stats.score['Home']) +\
            '     ' + 'Away: ' + str(self.stats.score['Away'])

        self.score_image = self.font.render(
            score_str,
            True,
            self.bstats_settings.colorText,
            self.bstats_settings.bg_color
        )

        # Display the score the top mid of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.midtop = self.screen_rect.midtop

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)

    def prep_home_score(self):
        """Turn the Home score into a rendered image."""
        score_str = 'Home: ' + str(self.stats.score['Home'])

        self.score_image = self.font.render(
            score_str,
            True,
            self.bstats_settings.colorHome,
            self.bstats_settings.bg_color
        )

        # Display the score 1/4 of screen width, top of screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.midtop = (
            self.bstats_settings.screen_width / 4,
            self.screen_rect.top
        )

        self.show_score()

    def prep_away_score(self):
        """Turn the Away score into a rendered image."""
        score_str = 'Away: ' + str(self.stats.score['Away'])

        self.score_image = self.font.render(
            score_str,
            True,
            self.bstats_settings.colorAway,
            self.bstats_settings.bg_color
        )

        # Display the score 3/4 of screen width, top of screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.midtop = (
            3 * self.bstats_settings.screen_width / 4,
            self.screen_rect.top
        )

        self.show_score()
