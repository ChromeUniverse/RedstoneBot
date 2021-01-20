import os
import csv

cwd = os.getcwd()
dbpath = os.path.join(cwd, 'db.csv')

dbFile = open(dbpath, 'r')
dbReader = csv.reader(dbFile)


for row in dbReader:
    guildID = row[0]
    print('This is the Discord Guild ID: ' + guildID)
    IP = row[1]
    print('This is the PloudOS Server IP address: ' + IP)
    serverID = row[2]
    print('This is the PlousdOS server ID number: ' + serverID + '\n')

dbFile.close()
