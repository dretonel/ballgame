# teamstats.py - Team Class which inherits from Player Class
# Author:       Dan Retonel
# Date:         20 Nov 2017
# Class for teams which includes a list of all players on that team,
# and a win and a loss integer value.

from players import Player


class Team(Player):
    """Basketball team class"""

    def __init__(self, bstats_settings, name, number, team='none'):
        """Initialize a team with their team direction"""
        super().__init__(bstats_settings, name, number, team)
        self.teamlist = []
        self.win = 0
        self.loss = 0

    def update_stats(self):
        """Update team stats"""

        self.__reset_stats()

        for player in self.teamlist:
            self.pts += player.pts
            self.ast += player.ast

            self.orb += player.orb
            self.drb += player.drb
            self.totrb += player.totrb

            self.fg += player.fg
            self.fga += player.fga

            self.threeP += player.threeP
            self.threePa += player.threePa

            self.update_fg()

            self.ft += player.ft
            self.fta += player.fta

            self.stl += player.stl
            self.blk += player.blk
            self.tov += player.tov

            self.pf += player.pf

#           self.().format(pattr) += pvalue
#           self.pts += player.pts

    def __reset_stats(self):
        """Zero all team stats"""
        self.pts = 0
        self.ast = 0

        self.orb = 0
        self.drb = 0
        self.totrb = 0

        self.fg = 0
        self.fga = 0
        self.fgp = 0.0

        self.threeP = 0
        self.threePa = 0
        self.threePp = 0.0

        self.ft = 0
        self.fta = 0
        self.ftp = 0.0

        self.stl = 0
        self.blk = 0
        self.tov = 0

        self.pf = 0
