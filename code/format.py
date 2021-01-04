# format Rich Embed message

def format(data):

    status = ''
    message = '\n'
    message += 'Server name: **' + str(data["serverName"]) + '**'
    message += '\nCurrently running **' + str(data["serverVersion"]) + '**'

    if data["status"] == 'READY':

        message += '\n\n**Server Resources**\n'
        message += '\nCPU: **' + str(data["serverUsedCPU"]) + '%** in use'
        message += '\nMemory: **' + str(data["serverUsedRAM"]) + ' MB** in use out of **' + str(data["serverMaxRam"]) + ' MB** max'
        message += '\nSSD storage: **' + str(data["serverUsedSpace"]/1000) + ' GB** used out of **' + str(data["serverTotalSpace"]/1000) + ' GB** max'
        message += '\n\n**Extra Info**\n'


        if data["isRunning"] == False:

            message = '\n'
            message += 'Server name: **' + str(data["serverName"]) + '**'
            message += '\nCurrently running **' + str(data["serverVersion"]) + '**'

            if data["isEditorMode"] == True:
                # actually means that the Server is offline!
                status = 'Server is offline.'

            if data["isEditorMode"] == False:
                status = 'Server stopped.'
                message += '\nTimeout is **' + str(data["serverTimeout"]) + '** seconds or **' + str(data["serverTimeoutFormatted"]) + '**'


        if data["isRunning"] == True:
            if data["isStarted"] == True:
                status = 'Server is up and running!'
                message += '\nPlayers online: **' + str(data["onlineCount"]) + '** out of **' + str(data["onlineMax"]) + '** max'
                message += '\nTimeout is **' + str(data["serverTimeout"]) + '** seconds or **' + str(data["serverTimeoutFormatted"]) + '**'

            if data["isStarted"] == False:
                status = 'Server is starting up!'



    elif data["status"] == "SETUP":

        status = 'Server is running setup!'


    elif data["status"] == "CLOSING":

        status = 'Server is closing'


    elif data["status"] == "OFFLINE":

        status = 'Server is offline.'


    elif data["status"] == "QUEUE":

        status = 'Server is in the queue!'

        message += '\n\n**Queue Info**\n'
        message += '\nQueue position: **' + str(data["queuePos"]) +'** out of **'+ str(data["queueSize"]) + '**'
        message += '\nApproximate waiting time: **' + str(data["queueTimeFormatted"]) + ' minute(s)**'

    elif data["status"] == "WAITING_FOR_ACCEPT":

        status = 'Waiting for user confirmation on admin page.'

        message += '\n\n**Use the `!redstone accept` command!**\n'

    return status, message
