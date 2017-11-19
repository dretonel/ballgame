import csv
import players
from stats import Stats
from settings import Settings


bstats_settings = Settings()
playerdict = {}
writeFile = open('overallstats.csv', 'w', newline='\n')
csvWriter = csv.writer(writeFile)

rName = 'output'
for i in range(1, 15):
    readFile = open(rName + str(i) + '.csv')

# readFile = open('output1.csv')

    csvReader = csv.reader(readFile)
    readData = list(csvReader)
#print(readData)

    for index, item in enumerate(readData):
        if index == 0:
            if i == 13:
                csvWriter.writerow(item)
            continue
        if len(item) == 0:
            continue
#    print(item)

        if item[0] not in playerdict:
            playerdict[item[0]] = players.Player(bstats_settings, item[0], index)
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

for player in playerdict.values():
    csvWriter.writerow(bstats_settings.get_playerdict(player))

print(playerdict['Janlie'].pts)

readFile.close()
writeFile.close()
