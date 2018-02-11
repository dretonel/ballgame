# player.py - Basketball Player Class which inherits from Stats Class
# Author:       Dan Retonel
# Date:        15 Sept 2017

# Class for stats including:
# Points    Assists     ORebounds   DRebounds    TotRebounds
# FGM/FGA/FPP    3pm/3pa/3PP
# Steals    Blocks  Turnovers
# Personal  Fouls

from stats import Stats


class Player(Stats):
    """Basketball player class"""
    playerCount = 0

    def __init__(self, bstats_settings, name, number, team='none'):
        """Initialize a player with their name and number"""
        super().__init__()
        Player.playerCount += 1
        self.name = name
        self.number = number
        self.team = team
        self.bstats_settings = bstats_settings
        self.stats = [
            self.name + '/' + str(self.number),
            'fg',
            'fga',
            '3pt',
            '3pa',
            # 'ft',
            # 'fta',
            'ast',
            'orb',
            'drb',
            'stl',
            'blk',
            'tov',
            'pf'
        ]

    def describe_player(self):
        """Prints a description of this player"""
        print(
            self.name.title() +
            " is player number " +
            str(self.number) +
            "."
        )

    def fg_made(self, editFlag):
        """Change stats on a field goal made"""
        self.fg += 1 - (2 * int(editFlag))
        self.fga += 1 - (2 * int(editFlag))

        # Field goals are worth value set in settings
        self.pts += self.bstats_settings.fg * (1 - (2 * int(editFlag)))

        self.update_fg()

    def fg_att(self, editFlag):
        """Change stats on a field goal attempted"""
        self.fga += 1 - (2 * int(editFlag))
        self.update_fg()

    def threeP_made(self, editFlag):
        """Change stats on 3-ptr made"""
        self.threeP += 1 - (2 * int(editFlag))
        self.threePa += 1 - (2 * int(editFlag))
        self.fg += 1 - (2 * int(editFlag))
        self.fga += 1 - (2 * int(editFlag))

        # 3s are worth value set in settings
        self.pts += self.bstats_settings.threefg * \
            (1 - (2 * int(editFlag)))

        self.update_fg()

    def threeP_att(self, editFlag):
        """Change stats on 3-ptr attempted"""
        self.threePa += 1 - (2 * int(editFlag))
        self.fga += 1 - (2 * int(editFlag))
        self.update_fg()

    def update_fg(self):
        """Update field goal & 3ptr percentages"""
        if self.fga is not 0:
            self.fgp = self.fg / self.fga
        else:
            self.fgp = 0.000

        if self.threePa is not 0:
            self.threePp = self.threeP / self.threePa
        else:
            self.threePp = 0.000

    def ft_made(self, editFlag):
        """Change stats on a ft made"""
        self.ft += 1 - (2 * int(editFlag))
        self.fta += 1 - (2 * int(editFlag))

        self.pts += 1 - (2 * int(editFlag))

    def update_rb(self):
        """Update the total rebound stat"""
        self.totrb = self.orb + self.drb


# janlie = Player('Janlie', 5)
# janlie.describe_player()
# print(str(janlie.fg))
# janlie.fg = 2
# janlie.fga = 3
# janlie.update_fg()
# print(janlie.fgp)
