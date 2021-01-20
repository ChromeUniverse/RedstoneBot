import os
import csv

def guild_in_db(inputGuildID):
    cwd = os.getcwd()
    dbpath = os.path.join(cwd, 'db.csv')

    dbFile = open(dbpath, 'r')
    dbReader = csv.reader(dbFile)

    for row in dbReader:
        # if guildID is already in DB
        if inputGuildID == row[0]:
            return True
    return False

    dbFile.close()

def IP_in_db(inputIP):
    cwd = os.getcwd()
    dbpath = os.path.join(cwd, 'db.csv')

    dbFile = open(dbpath, 'r')
    dbReader = csv.reader(dbFile)

    for row in dbReader:
        # if guildID is already in DB
        if inputIP == row[1]:
            return True
    return False

    dbFile.close()

def get_serverID(inputGuildID):
    cwd = os.getcwd()
    dbpath = os.path.join(cwd, 'db.csv')

    dbFile = open(dbpath, 'r')
    dbReader = csv.reader(dbFile)

    for row in dbReader:
        # if guildID is already in DB
        if inputGuildID == row[0]:
            serverID = row[2]
            return serverID
    return False


def link(guildID, setupIP, serverID):
    cwd = os.getcwd()
    dbpath = os.path.join(cwd, 'db.csv')

    # creating a new DB entry
    newEntry = []
    # add Discord server/guild ID
    newEntry.append(guildID)
    # add PloudOS server address
    newEntry.append(setupIP)
    # add PloudOS server ID
    newEntry.append(serverID)
    print(newEntry)

    # opening log file in append mode
    dbFile = open(dbpath, 'a', newline='')
    dbWriter = csv.writer(dbFile)
    # updating log.txt
    dbWriter.writerow(newEntry)
    #closing log file
    dbFile.close()
