# stats.py - Statistics Class
# Author:    Dan Retonel
# Date:        15 Sept 2017

# Class for stats including:
# Points        Assists        ORebounds    DRebounds    TotRebounds
# FGM/FGA/FPP    3pm/3pa/3PP
# Steals        Blocks        Turnovers
# Personal Fouls


class Stats():
    """Statistics class"""

    def __init__(self):
        """Iniitialize all categories"""
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
