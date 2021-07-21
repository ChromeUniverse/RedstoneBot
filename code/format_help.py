def format_help():

    title = 'Help Page'
    content = ''

    content += "\n\n**About**\n\n"
    content += 'RedstoneBot is a Discord bot for interacting with Minecraft servers hosted by PloudOS.\n'

    content += "\n\n**RedstoneBot's Commands**\n\n"
    content += '_Please note: running most of these commands requires the **Redstone User** role._\n\n'

    content += '`!redstone help`\n\n'
    content += 'Shows this page.\n\n'

    content += '`!redstone ping`\n\n'
    content += 'Replies with "Pong!" and shows connection latency in miliseconds.\n\n'

    content += '`!redstone status`\n\n'
    content += 'Displays current server status: "Online", "In queue", "Starting up", etc.\n\n'
    content += 'Also shows additional info about server resources, number of online players, and more.\n\n'

    content += '`!redstone list`\n\n'
    content += 'Shows a list of online players.\n\n'

    content += '`!redstone time`\n\n'
    content += 'Shows server locations and queue waiting times.\n\n'

    content += '`!redstone start [location]`\n\n'
    content += 'Puts your server in the activation queue.\n\n'
    content += 'Specify the server location with `[1]` (Nuremberg).\n\n'
    content += 'You only need to run this once: RedstoneBot automatically sends user confirmation when you reach the top spot of the queue.\n\n'

    content += '`!redstone exit`\n\n'
    content += 'Exits the activation queue.\n\n'
    content += '**NOTE:** only members with the **Redstone Admin** role can use this command.\n\n'

    content += '`!redstone stop`\n\n'
    content += 'If the server is "Online", this will deactivate the server.\n\n'
    content += '**NOTE:** only members with the **Redstone Admin** role can use this command.\n\n'

    content += '`!redstone restart`\n\n'
    content += 'If the server is "Stopped", this will reactivate the server.\n\n'

    content += '`!redstone setup [IP]`\n\n'
    content += 'A configuration command - this will link your Discord server to the PloudOS server with the specified IP address.\n\n'
    content += 'Specify your server address with the following format:\n\n'
    content += '`[IP] -> myverycoolserver.ploudos.me`\n\n'
    content += '**NOTE:** only members with the **Redstone Admin** role can use this command.\n\n'

    content += '`!redstone reset`\n\n'
    content += 'Resets the setup process.\n\n'
    content += 'Can come in handy if you ever change the IP of your PloudOS server.\n\n'
    content += '**NOTE:** only members with the **Redstone Admin** role can use this command.\n\n'


    content += "\n**Additional Resources**"

    content += "\n\nFor more information, visit RedstoneBot's official webpage:\n"
    content += 'http://34.200.98.64/redstone'

    content += "\n\nIf you need help setting up RedstoneBot, please refer to the quickstart guide:\n"
    content += 'http://34.200.98.64/redstone-quickstart'

    content += "\n\nIf you're having trouble with RedstoneBot, please create a new issue on GitHub:\n"
    content += 'https://github.com/ChromeUniverse/RedstoneBot/issues/'


    return title, content
