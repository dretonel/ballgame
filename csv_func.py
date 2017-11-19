import os
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
def write_CSV(bstats_settings, teams):
    fName = 'output'
    filename = fName + '.csv'

    i = 1
    while os.path.exists(filename):
        filename = fName + str(i) + '.csv'
        i = i + 1

    csvOutfile = open(filename, 'w', newline='\n')
    csvWriter = csv.writer(csvOutfile)

    # Write the header before players
    csvWriter.writerow(bstats_settings.stats_header)

    for team in teams:
        for player in sorted(team.teamlist, key=lambda player:player.name):
            csvWriter.writerow(bstats_settings.get_playerdict(player))

    for counter in range(11):
        csvWriter.writerow([])

    for team in teams:
        csvWriter.writerow(bstats_settings.get_playerdict(team))

    # Close the file
    csvOutfile.close()

    print('The stats were written in:\t' + filename)
