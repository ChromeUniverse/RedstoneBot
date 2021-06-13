# server webscraper function
from serverlist import serverlist

# database functions
from db_functions import (
    guild_in_db,
    IP_in_db,
    get_serverID,
    link,
)

async def register(ctx, session, guildID, guildName, is_admin, setupIP):

    # check if member is admin
    if is_admin == True:

        # checking for valid argument
        if type(setupIP) == str and '.ploudos.me' in setupIP:

            # check that server isn't already in DB
            if guild_in_db(guildID) == True:
                await ctx.channel.send('**' + guildName + '** is already linked to a PloudOS server.')
                return None, None
            else:
                # check that IP isn't already in DB
                if IP_in_db(setupIP) == True:
                    await ctx.channel.send('This server IP is already linked to another Discord server.')
                    return None, None
                else:
                    # Got valid argument
                    await ctx.channel.send("Running setup... please wait.")

                    # looping through online server list to get serverID
                    return1, return2 = await serverlist(session, setupIP)

                    if return1 != False:
                        # Success!
                        # managed to match input IP to actual IP on server list
                        serverID, serverName = return1, return2

                        # write data to DB
                        link(guildID, setupIP, serverID)

                        title = 'Setup successful!'
                        content = '**' + serverName + '** has been linked to this Discord server.'

                        return title, content

                    else:
                        # couldn't match user input IP and IPs on server list
                        title = '**Incorrect server IP.**'
                        content = ''
                        content += "This IP wasn't found in Redstone's server list.\n\n"
                        content += 'Make sure that Redstone has permissions to open and close this server.\n\n'
                        content += 'Learn more here: https://chromeuniverse.github.io/RedstoneBot/manual.html\n\n'
                        content += '**Please try again.**'

                        return title, content

        else:
            # invalid argument!
            message = ''
            message += 'Invalid IP. The syntax for this command is:\n'
            message += '```!redstone setup [IP address]\n\n[IP address] 🠖 mycoolserver.ploudos.me```'

            await ctx.channel.send(message)
            return None, None
    else:
        # user doesn't have guild admin permission
        await ctx.channel.send('Only members with the `Redstone Admin` role can use this command.')
        return None, None
