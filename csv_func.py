import csv
import players


# Read Player List CSV file, get players from file and make a
# dictionary of players
def read_playersCSV(bstats_settings):
	playerdict = {}
	teamsFile = open('PlayerLists/playerlist.csv')
	teamsReader = csv.reader(teamsFile)
	teamsData = list(teamsReader)
	for index, info in enumerate(teamsData):
		playerdict['player{0}'.format(index)] = \
			players.Player(bstats_settings, info[0], info[1], info[2])

	return playerdict


# Write to stats to CSV File and close the file
def write_CSV(playerdict, bstats_settings, teams):
	csvOutfile = open('output.csv', 'w', newline='\n')
	csvWriter = csv.writer(csvOutfile)

	# Write the header before players
	csvWriter.writerow(bstats_settings.stats_header)

	for player in playerdict.values():
		csvWriter.writerow(bstats_settings.get_playerdict(player))

	for counter in range(11):
		csvWriter.writerow([])

	for team in teams:
		csvWriter.writerow(bstats_settings.get_playerdict(team))

	# Close the file
	csvOutfile.close()
