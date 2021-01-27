def format_help():

    title = 'Help Page'

    content = ''
    content = 'RedstoneBot is a Discord bot for interacting with Minecraft servers hosted by PloudOS, originally built for the SMP BR Discord community.'

    content += "\n\n**Redstone's Commands**\n\n"
    content += '`!redstone help`\n\n'
    content += 'Shows this page.\n\n'

    content += '`!redstone ping`\n\n'
    content += 'Replies with "Pong!" and shows connection latency in miliseconds.\n\n'

    content += '`!redstone status`\n\n'
    content += 'Displays current server status: "Online", "In queue", "Starting up", etc.\n\n'
    content += 'Also shows additional info about server resources, number of online players, and more.\n\n'

    content += '`!redstone queueTime`\n\n'
    content += 'Shows server locations and queue waiting times.\n\n'

    content += '`!redstone start [location]`\n\n'
    content += 'Puts your server in the activation queue.\n\n'
    content += 'Specify the server location with `[1]` (Nuremberg) or `[2]` (St. Louis).\n\n'
    content += 'You only need to run this once: it automatically sends user confirmation when you reach the top spot of the queue.\n\n'

    content += '`!redstone exit`\n\n'
    content += 'Exits the activation queue.\n\n'

    content += '`!redstone stop`\n\n'
    content += 'If the server is "Online", this will deactivate the server.\n\n'

    content += '`!redstone restart`\n\n'
    content += 'If the server is "Stopped", this will reactivate the server.\n\n'

    content += '`!redstone setup [IP]`\n\n'
    content += 'Configuration command.\n\n'
    content += 'Links your Discord server to the PloudOS server with the specified IP address.\n\n'
    content += '_**NOTE:** user must have admin permissions to run this command._\n\n'

    content += '`!redstone reset`\n\n'
    content += 'Resets the setup process.\n\n'
    content += 'Can come in handy if you ever change the IP of your PloudOS server.\n\n'
    content += '_**NOTE:** user must have admin permissions to run this command._\n\n'



    content += "\n\nFor more information, visit RedstoneBot's GitHub repo:\n"
    content += 'https://github.com/ChromeUniverse/RedstoneBot'

    return title, content
