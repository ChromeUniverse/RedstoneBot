import os
import csv

def guild_in_db(guildID):
    cwd = os.getcwd()
    dbPath = os.path.join(cwd, 'db.csv')

    dbFile = open(dbPath, 'r')
    dbReader = csv.reader(dbFile)

    for row in dbReader:
        # if guildID is already in DB
        if guildID == row[0]:
            return True
    return False

    dbFile.close()

def IP_in_db(IP):
    cwd = os.getcwd()
    dbPath = os.path.join(cwd, 'db.csv')

    dbFile = open(dbPath, 'r')
    dbReader = csv.reader(dbFile)

    for row in dbReader:
        # if guildID is already in DB
        if IP == row[1]:
            return True
    return False

    dbFile.close()

def serverID_in_db(serverID):
    cwd = os.getcwd()
    dbPath = os.path.join(cwd, 'db.csv')

    dbFile = open(dbPath, 'r')
    dbReader = csv.reader(dbFile)

    for row in dbReader:
        # if guildID is already in DB
        if serverID == row[2]:
            return True
    return False

    dbFile.close()

def get_IP(serverID):
    cwd = os.getcwd()
    dbPath = os.path.join(cwd, 'db.csv')

    dbFile = open(dbPath, 'r')
    dbReader = csv.reader(dbFile)

    for row in dbReader:
        # if guildID is already in DB
        if serverID == row[2]:
            IP = row[1]
            return IP
    return False


def get_serverID(GuildID):
    cwd = os.getcwd()
    dbPath = os.path.join(cwd, 'db.csv')

    dbFile = open(dbPath, 'r')
    dbReader = csv.reader(dbFile)

    for row in dbReader:
        # if guildID is already in DB
        if GuildID == row[0]:
            serverID = row[2]
            return serverID
    return False


def link(guildID, setupIP, serverID):
    cwd = os.getcwd()
    dbPath = os.path.join(cwd, 'db.csv')

    # creating a new DB entry
    newEntry = []
    # add Discord server/guild ID
    newEntry.append(guildID)
    # add PloudOS server address
    newEntry.append(setupIP)
    # add PloudOS server ID
    newEntry.append(serverID)
    # by default, looping is False
    newEntry.append(str(False))
    print(newEntry)

    # opening log file in append mode
    dbFile = open(dbPath, 'a', newline='')
    dbWriter = csv.writer(dbFile)
    # updating log.txt
    dbWriter.writerow(newEntry)
    #closing log file
    dbFile.close()

def get_looping(guildID):
    cwd = os.getcwd()
    dbPath = os.path.join(cwd, 'db.csv')

    # opening database and spliting it into lines
    dbFile = open(dbPath)
    dbReader = csv.reader(dbFile)

    for row in dbReader:
        if row[0] == guildID:
            # found the guild in DB
            # get looping
            looping = row[3]
            print("Got looping! It's..." + str(looping))
            return str(looping)
    return False




def update_looping(guildID, looping):
    cwd = os.getcwd()
    dbPath = os.path.join(cwd, 'db.csv')

    # opening database and spliting it into lines
    dbFile = open(dbPath)
    dbReader = csv.reader(dbFile)

    # creating a copy of the DB
    dbCopy = []

    for row in dbReader:
        # found the guild's entry in database
        if row[0] == guildID:
            # change the looping variable
            row[3] = str(looping)
        # add this row to the DB copy
        dbCopy.append(row)
    dbFile.close()

    dbFile = open(dbPath, 'w', newline='')
    dbWriter = csv.writer(dbFile)

    for row in dbCopy:
        # paste dbCopy into DB file
        dbWriter.writerow(row)

    dbFile.close()
