# running_score.py
# Running score module for Ball Stats
# Author:        Dan Retonel
# Date:          18 Oct 2017

import pygame.font


class RunningScore():
    """ Displays the running score"""

    def __init__(self, bstats_settings, screen, teams):
        """Initialize running score attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bstats_settings = bstats_settings
        self.teams = teams

        self.width, self.height = (45, 36)

        self.rScore = [(('', 'Home'), ('Away', ''))]

        self.rsHomeName = ['']
        self.rsHomePts = ['Home']
        self.rsAwayPts = ['Away']
        self.rsAwayName = ['']

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

    def update_rs(self, player, edit_flag):
        """Update the running score."""

        score = 0

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

            scoreTup = (scoreH, scoreA)

            self.rScore.append(scoreTup)
            self.rsHomeName.append(scoreH[0])
            self.rsHomePts.append(scoreH[1])
            self.rsAwayPts.append(scoreA[0])
            self.rsAwayName.append(scoreA[1])

    def prep_rs(self):
        """Prep the rScore into a rendered image."""

        count = 0

        for rsList in self.rsLists:
            string = ''
            for i, item in enumerate(rsList):
                string += str(item)
                if i is 0:
                    while len(string) < 6:
                        string += ' '
                elif (len(str(item)) == 3):
                    string += ' '
                elif (len(str(item)) == 2):
                    string += '  '
                elif (len(str(item)) == 1):
                    string += '   '
                elif (str(item) == ''):
                    string += '    '
                else:
                    string += '  '

            if count == 0:
                color = self.bstats_settings.colorHome
                bgcolor = self.bstats_settings.colorHome2
            elif count == 1:
                color = self.bstats_settings.colorHome2
                bgcolor = self.bstats_settings.colorHome
            elif count == 2:
                color = self.bstats_settings.colorAway2
                bgcolor = self.bstats_settings.colorAway
            elif count == 3:
                color = self.bstats_settings.colorAway
                bgcolor = self.bstats_settings.colorAway2

            self.rs_image = self.font.render(
                string, True,
                color, bgcolor
            )

            self.rs_rect = self.rs_image.get_rect()
            self.rs_rect.midleft = (
                self.screen_rect.left,
                self.screen_rect.centery + count * 25 - 100
            )

            self.show_rs()

            count += 1

    def show_rs(self):
        """Turn the running score into a rendered image."""
        self.screen.blit(self.rs_image, self.rs_rect)
