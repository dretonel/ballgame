# csvfunc.py - Module to handle the export of Ball Game Stats to a .csv
# Author:       Dan Retonel
# Date:         7 Oct 2017
# This module contains funcions to read from and write to .csv files
# for the operation of Ball Game Stats.

import os
import csv
import players
from teams import Team


# Read Player List CSV file, get players from file and make a
# dictionary of players
# Currently, it reads from a folder where this module is located called:
# ./PlayerLists/
def read_playersCSV(bstats_settings, playerdict, teams):
    teamsFile = open('PlayerLists/playerlist.csv')
    teamsReader = csv.reader(teamsFile)
    teamsData = list(teamsReader)
    for index, info in enumerate(teamsData):
        if int(info[1]) < 0:
            teams.append(Team(bstats_settings, info[0], info[1], info[2]))
        else:
            playerdict['player{0}'.format(index)] = \
                players.Player(bstats_settings, info[0], info[1], info[2])


# Write to stats to CSV File and close the file
def write_CSV(bstats_settings, teams, runScore):

    fName = ''

    # Format the file name such to be:
    # HOMEvsAWAY-#.csv
    # Where HOME is Home team name, AWAY is away team name
    # and # is the iterations if this game in this folder
    for index, team in enumerate(teams):
        fName += team.name
        if index is 0:
            fName += 'vs'

    i = 1
    filename = fName + '-' + str(i) + '.csv'

    while os.path.exists(filename):
        filename = fName + '-' + str(i) + '.csv'
        i += 1

    # Open a file with the correct filename and make the
    # CSV Writer for that file
    csvOutfile = open(filename, 'w', newline='\n')
    csvWriter = csv.writer(csvOutfile)

    # Write the header before players
    csvWriter.writerow(bstats_settings.stats_header)

    # Write the stats for each player, Home then Away
    for team in teams:
        for player in sorted(team.teamlist, key=lambda player: player.name):
            csvWriter.writerow(bstats_settings.get_playerdict(player))

    # Write 11 blank lines
    for counter in range(11):
        csvWriter.writerow([])

    # Write out the team stats
    for team in teams:
        csvWriter.writerow(bstats_settings.get_playerdict(team) +
                           ['', team.win, team.loss])

    # Write 4 blank lines
    for counter in range(4):
        csvWriter.writerow([])

    # Write the title for Running Score
    csvWriter.writerow(['Running Score'])

    # Write out the Running Score
    for rlist in runScore.rsLists:
        csvWriter.writerow(rlist)

    # Close the file
    csvOutfile.close()

    # Prompt to terminal the name of the .csv file written
    print('The stats were written in:\t' + filename)
