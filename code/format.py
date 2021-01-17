# format Rich Embed message

def format(data):

    status = ''

    # status cheat sheet
    #
    # 0 -> offline
    # 1 -> stopped execution
    # 2 -> up and running
    # 3 -> starting up
    # 4 -> running setup
    # 5 -> closing
    # 6 -> in queue
    # 7 -> waiting for accept
    # 8 -> preparing server reallocation


    title = ''
    message = '\n'
    message += 'Server name: **' + str(data["serverName"]) + '**'
    message += '\nCurrently running **' + str(data["serverVersion"]) + '**'

    if data["status"] == 'READY':

        message += '\n\n**Server Resources**\n'
        message += '\nCPU: **' + str(data["serverUsedCPU"]) + '%** in use'
        message += '\nMemory: **' + str(data["serverUsedRAM"]) + ' MB** in use out of **' + str(data["serverMaxRam"]) + ' MB** max'
        message += '\nSSD storage: **' + str(data["serverUsedSpace"]/1000) + ' GB** used out of **' + str(data["serverTotalSpace"]/1000) + ' GB** max'


        if data["isRunning"] == False:

            message = '\n'
            message += 'Server name: **' + str(data["serverName"]) + '**'
            message += '\nCurrently running **' + str(data["serverVersion"]) + '**'

            if data["isEditorMode"] == True:
                # actually means that the Server is offline!
                status = 0

                title = 'Server is offline.'

            if data["isEditorMode"] == False:
                status = 1

                title = 'Server stopped.'
                message += '\n\n**Extra Info**\n'
                message += '\nTimeout is **' + str(data["serverTimeout"]) + '** seconds or **' + str(data["serverTimeoutFormatted"]) + '**'
                message += '\nTo restart server, use `!redstone restart`'


        if data["isRunning"] == True:
            if data["isStarted"] == True:
                status = 2

                title = 'Server is up and running!'
                message += '\n\n**Extra Info**\n'
                message += '\nPlayers online: **' + str(data["onlineCount"]) + '** out of **' + str(data["onlineMax"]) + '** max'
                message += '\nTimeout is **' + str(data["serverTimeout"]) + '** seconds or **' + str(data["serverTimeoutFormatted"]) + '**'

            if data["isStarted"] == False:
                status = 3

                title = 'Server is starting up!'



    elif data["status"] == "SETUP":
        status = 4
        title = 'Server is running setup!'


    elif data["status"] == "CLOSING":
        status = 5
        title = 'Server is closing'


    elif data["status"] == "OFFLINE":
        status = 0
        title = 'Server is offline.'


    elif data["status"] == "QUEUE":
        status = 6

        title = 'Server is in the queue!'

        message += '\n\n**Queue Info**\n'
        message += '\nQueue position: **' + str(data["queuePos"]) +'** out of **'+ str(data["queueSize"]) + '**'
        message += '\nApproximate waiting time: **' + str(data["queueTimeFormatted"]) + ' minute(s)**'

    elif data["status"] == "WAITING_FOR_ACCEPT":
        status = 7

        title = 'Waiting for user confirmation on admin page.'

        message += '\n\n**Use the `!redstone accept` command!**\n'

    elif data["status"] == "PREPARE_SERVER_REALLOCATION":
        status = 8

        title = 'Preparing server for reallocation.'

        message += '\n\nPlease wait while PloudOS does its thing.\n'
        message += 'Use `!redstone status` to check server status'

    return status, title, message
