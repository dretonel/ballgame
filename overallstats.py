# overallstats.py - Sums together stats created by ball_game.py
# Author:       Dan Retonel
# Date:         18 Nov 2017
# Reads all output*.csv files in current directory,
# Sums together all player stats, each player added to dictionary
# Prints out to .csv file the summation of all stats
# IMPORTANT: Major changes need if summation of FT and FTA

import os
import csv
import players
import teams
from settings import Settings

# Initialize variables needed
bstats_settings = Settings()        # settings for Player class
playerdict = {}                     # dictionary of players

# Designate a file to print out to and open it
writeFile = open('OverallStats.csv', 'w', newline='\n')
csvWriter = csv.writer(writeFile)

# Read output*.csv files in current directory
rName = 'output'
for i in range(1, 25):
    readFName = rName + str(i) + '.csv'

    # The file exists ? open file, finished reading
    if os.path.exists(readFName):
        readFile = open(readFName)
        csvReader = csv.reader(readFile)

        # Change the csvReader into a list, each row is a row on the file
        readData = list(csvReader)

        # Parse through list, each row has multiple items
        for index, item in enumerate(readData):
            # first row of headers ? first iter ? print headers out,
            # else continue
            if index == 0:
                if i == 1:
                    csvWriter.writerow(item)
                continue
            # Empty row ? continue
            if len(item) == 0:
                continue

            # New Player ? add to dictionary, sum stats
            if item[0] not in playerdict:
                if '' in item[0]:
                    playerdict[item[0]] = teams.Team(bstats_settings,
                                                     item[0], index)
                    playerdict[item[0]].win = int(item[-2])
                    playerdict[item[0]].loss = int(item[-1])
                else:
                    playerdict[item[0]] = players.Player(bstats_settings,
                                                         item[0], index)
                playerdict[item[0]].pts = int(item[2])
                playerdict[item[0]].fg = int(item[3])
                playerdict[item[0]].fga = int(item[4])

                playerdict[item[0]].threeP = int(item[6])
                playerdict[item[0]].threePa = int(item[7])

                playerdict[item[0]].ast = int(item[9])
                playerdict[item[0]].orb = int(item[10])
                playerdict[item[0]].drb = int(item[11])
                playerdict[item[0]].totrb = int(item[12])

                playerdict[item[0]].stl = int(item[13])
                playerdict[item[0]].blk = int(item[14])
                playerdict[item[0]].tov = int(item[15])
                playerdict[item[0]].pf = int(item[16])
                playerdict[item[0]].update_fg()

            else:
                if '' in item[0]:
                    playerdict[item[0]].win += int(item[-2])
                    playerdict[item[0]].loss += int(item[-1])

                playerdict[item[0]].pts += int(item[2])
                playerdict[item[0]].fg += int(item[3])
                playerdict[item[0]].fga += int(item[4])

                playerdict[item[0]].threeP += int(item[6])
                playerdict[item[0]].threePa += int(item[7])

                playerdict[item[0]].ast += int(item[9])
                playerdict[item[0]].orb += int(item[10])
                playerdict[item[0]].drb += int(item[11])
                playerdict[item[0]].totrb += int(item[12])

                playerdict[item[0]].stl += int(item[13])
                playerdict[item[0]].blk += int(item[14])
                playerdict[item[0]].tov += int(item[15])
                playerdict[item[0]].pf += int(item[16])
                playerdict[item[0]].update_fg()
    else:
        break

# Write out each player to outfile
for player in playerdict.values():
    statline = bstats_settings.get_playerdict(player)
    if isinstance(player, teams.Team):
        statline += ['', player.win, player.loss]

    csvWriter.writerow(statline)

# Close Read and Write Files
readFile.close()
writeFile.close()
