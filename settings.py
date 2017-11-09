# settings.py - settings for Basketball Scoring
import players
from decimal import getcontext, Decimal


getcontext().prec = 3


class Settings():
	"""A class to store all settings for Basketball Scoring"""

	def __init__(self):
		"""Initialize the scoring's settings."""

		# Screen settings
		self.screen_width = 1500
		self.screen_height = 800

		# Set the original color scheme
		self.orig_colors()

		# Values of scoring
		self.fg = 2
		self.threefg = 3

		# Stats rounding decimal place
		self.rounding = 3

		self.stats_header = [
			'Player',
			'Team',
			'Points',
			'FG',
			'FGAtt',
			'FG%',
			'3Pts',
			'3PtAtt',
			'3Pt%',
			'Assists',
			'0-Rebs',
			'D-Rebs',
			'TotalRebs',
			'Steals',
			'Blocks',
			'Turnovers',
			'Fouls'
		]

		self.stats_sb_header = [
			'Name/#',
			'Team',
			'FG',
			'FGA',
			'FG%',
			'3PT',
			'3PA',
			'3P%',
			'AST',
			'ORB',
			'DRB',
			'TRB',
			'STL',
			'BLK',
			'TOV',
			'PF'
		]

	def orig_colors(self):
		"""Define the original colors"""

		# Colors used
		self.colorHome = (255, 0, 0)			# Home is Red
		self.colorAway = (0, 0, 255)			# Away is Blue
		self.colorPlay = (255, 106, 0)			# Play is Orange
		self.colorText = (255, 255, 255)		# Text is White
		self.bg_color = (230, 230, 230)			# Background is Grey

	def get_playerdict(self, player):
		"""Needs player dict to work"""

		self.stats_values = [
			player.name,
			player.team,
			player.pts,
			player.fg,
			player.fga,
			"{:.{prec}f}".format(player.fgp, prec=self.rounding),
			player.threeP, player.threePa,
			"{:.{prec}f}".format(player.threePp, prec=self.rounding),
			player.ast,
			player.orb,
			player.drb,
			player.totrb,
			player.stl,
			player.blk,
			player.tov,
			player.pf
		]

		return self.stats_values
