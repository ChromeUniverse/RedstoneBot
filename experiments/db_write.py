import os
import csv

def update_db(guildID, setupIP, serverID):
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
