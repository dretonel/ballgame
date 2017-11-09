class ScoreStats():
	"""Track statistics for the Scoreboard."""

	def __init__(self, bstats_settings):
		"""Initialize statistics."""
		self.bstats_settings = bstats_settings
		self.edit_flag = False
		self.stat_change = False

		self.reset_stats()


		# Start Ball Stats in an inactive state.
		self.game_active = False

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		# Things the need to be reset
		self.game_active = False
		self.score = {'Home': 0, 'Away': 0}

	def update_score(self, teams):
		"""Sum up all the scores per team and update"""
		#self.score = {'Home': 0, 'Away': 0}
		#for player in playerdict.values():
		#	if player.team == 'Home':
				#self.score['Home'] += player.pts
			#elif player.team == 'Away':
			#	self.score['Away'] += player.pts

		for team in teams:
			if team.team == 'Home':
				self.score['Home'] = team.pts
			elif team.team == 'Away':
				self.score['Away'] = team.pts

	def edit_stats(self):
		"""Toggle edit stat flag"""
		self.edit_flag = not self.edit_flag

		if self.edit_flag:
			self.__edit_mode()
		else:
			self.bstats_settings.orig_colors()

	def __edit_mode(self):
		"""Change settings to know that you're in edit mode"""

		# Change color palettes
		self.bstats_settings.bg_color = (32, 32, 32)
		self.bstats_settings.colorHome = (255, 128, 128)
		self.bstats_settings.colorAway = (128, 128, 255)
		self.bstats_settings.colorText = (255, 255, 0)
