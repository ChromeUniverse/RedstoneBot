def format_help():

    title = 'Help Page'

    content = ''
    content = 'RedstoneBot is a Discord bot made for interacting with Minecraft servers hosted by PloudOS, originally built for the SMP BR community.'

    content += '\n\n**Commands**\n\n'
    content += '`!redstone help`\n'
    content += 'Shows this page.\n\n'

    content += '`!redstone ping`\n'
    content += 'Replies with "Pong!" and shows connection latency in miliseconds.\n\n'

    content += '`!redstone status`\n'
    content += 'Shows current server status: "Online", "In queue", "Starting up", etc.\n'
    content += 'Shows additional info about server resources, number of online players, and more.\n\n'

    content += '`!redstone queueTime`\n'
    content += 'Shows server locations and queue waiting times.\n\n'

    content += '`!redstone start [location]`\n'
    content += 'Puts your server in the activation queue.\n'
    content += 'Specify the server location with `[1]` (Nuremberg) or `[2]` (St. Louis).\n'
    content += 'You only need to run this once: it automatically sends user confirmation when you reach the top spot of the queue.\n\n'

    content += '`!redstone stop`\n'
    content += 'If the server is "Online", this will deactivate the server.\n\n'

    content += '`!redstone restart`\n'
    content += 'If the server is "Stopped", this will reactivate the server.\n\n'

    content += "For more information, visit RedstoneBot's GitHub:\n"
    content += 'https://github.com/ChromeUniverse/RedstoneBot'

    return title, content
