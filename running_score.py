# running_score.py -  Running score module for Ball Stats
# Author:        Dan Retonel
# Date:          26 Jan 2018
# A class that handles the running score. It contains a list of tuples
# that store the running score for each team. The class also works
# in tandem with pygame to display the running score on a screen.
# When printing on pygame screen, the module aims to print in
# the following manner:
#   Home Player First Letter of Name + Number
#   Home Team Running Score
#   Away Team Running Score
#   Away Player First Letter of Name + Number
#         G34 G34
# Home    1   2   -
# Away    -   -   1
#                 P18

import pygame.font


# RunningScore class that handles the running store. It requires a
# settings, screen, and teams object to initialize.
class RunningScore():
    """ Displays the running score"""

    def __init__(self, bstats_settings, screen, teams):
        """Initialize running score attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bstats_settings = bstats_settings
        self.teams = teams

        # Font size for the running score
        self.width, self.height = (45, 36)

        # List object of running score that contains tuples of each
        # scoring event.
        # Running Score =
        #   [((first letter of name + number, home score),
        #       (away score, first letter of name + number))]
        self.rScore = [(('', 'Home'), ('Away', ''))]

        # The broken down parts of the running score for better printing
        # stored in lists of strings
        self.rsHomeName = ['']      # 1st letter of name + # for home
        self.rsHomePts = ['Home']   # running score of home
        self.rsAwayPts = ['Away']   # running score of away
        self.rsAwayName = ['']      # 1st letter of name + # for away

        # Put the broken down parts into a list for ease of printing
        self.rsLists = [
            self.rsHomeName,
            self.rsHomePts,
            self.rsAwayPts,
            self.rsAwayName
        ]

        # Font size for the running score
        self.font = pygame.font.SysFont('Courier', 14, bold=True)

        # Prepare the initial running score
        self.prep_rs()

    # Update the running score. It requires a player object and an
    # edit flag boolean value to be used.
    # The player object is the one who made a fg, 3p, ft
    def update_rs(self, player, edit_flag):
        """Update the running score."""

        score = 0       # Int value used as a buffer

        # Edit Mode ? delete the last element in the running score,
        #               Check which team the player is on
        #               Update the score for that team
        #               Store the points of that team to the buffer score
        #               Create tuples for Home and Away
        if edit_flag:
            del(self.rScore[-1])
            for rsList in self.rsLists:
                del(rsList[-1])
        else:
            if player.team == 'Home':
                for team in self.teams:
                    if team.team == player.team:
                        team.update_stats()
                        score = team.pts

                scoreH = (player.name[0] + str(player.number), score)
                scoreA = ('-', '')

            elif player.team == 'Away':
                for team in self.teams:
                    if team.team == player.team:
                        team.update_stats()
                        score = team.pts

                scoreH = ('', '-')
                scoreA = (score, player.name[0] + str(player.number))

            # Tuple of the Home and Away Scores
            scoreTup = (scoreH, scoreA)

            # Append the appropriate value to the corresponding list
            self.rScore.append(scoreTup)
            self.rsHomeName.append(scoreH[0])
            self.rsHomePts.append(scoreH[1])
            self.rsAwayPts.append(scoreA[0])
            self.rsAwayName.append(scoreA[1])

    # Prepare the running score as a rendered image to be displayed
    # on a pygame screen object. When called, this method does:
    #   parses through this class' rsLists object
    #       which is a list of various parts of the running score
    #   gets each string ready such that each part lines up
    #   creates a rect object for each part
    #       using pygame.font.render() and pygame.font.get_rect()
    #   defines the coordinates of each rect object on the screen
    #   calls this class' show_rs() method to put the rect object
    #       on the screen
    def prep_rs(self):
        """Prep the rScore into a rendered image."""

        # Parse through rsLists object
        for count, rsList in enumerate(self.rsLists):

            string = ''     # string buf for processing rsList fields

            # Get each string in each rsList field and put in buffer
            # Adds spaces between strings appropriately
            for i, item in enumerate(rsList):

                string += str(item)

                # First element ? make sure string + spaces is 6 chars,
                #                   3 chars --> 1 space
                #                   2 chars --> 2 spaces
                #                   1 chars --> 3 spaces
                #                   0 chars --> 4 spaces
                if i is 0:
                    while len(string) < 6:
                        string += ' '
                else:
                    # The # of chars and spaces maps to the following equation:
                    #   y = -1 * x + 4; x = chars, y = spaces
                    for x in range(-1 * len(str(item)) + 4):
                        string += ' '

            # Change the color of the rect object depending on which
            # rsLists field is being prepared
            if count == 0:
                color = self.bstats_settings.colorHome
                bgcolor = self.bstats_settings.bg_color
            elif count == 1:
                color = self.bstats_settings.colorHome2
                bgcolor = self.bstats_settings.colorHome
            elif count == 2:
                color = self.bstats_settings.colorAway2
                bgcolor = self.bstats_settings.colorAway
            elif count == 3:
                color = self.bstats_settings.colorAway
                bgcolor = self.bstats_settings.bg_color

            # Render string into a font image with appropriate settings
            self.rs_image = self.font.render(
                string, True,
                color, bgcolor
            )

            # Create a rect object & designate position depending on
            # which element of rsLists is prepared
            self.rs_rect = self.rs_image.get_rect()
            self.rs_rect.midleft = (
                self.screen_rect.left,
                self.screen_rect.centery + count * 25 - 100
            )

            self.show_rs()  # Call method to put image on screen

    def show_rs(self):
        """Turn the running score into a rendered image."""
        self.screen.blit(self.rs_image, self.rs_rect)
