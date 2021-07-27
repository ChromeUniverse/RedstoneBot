# database function import
from db_functions import deleteEntry

async def unregister(guildID, guildName, is_admin):

    if is_admin == True:

        # deleting this guild's entry in the DB
        deleteEntry(guildID)

        message = ''
        message += 'Successfully unlinked **' + guildName + '** from PloudOS. '
        message += '\nUse `!redstone setup` to link to a new PloudOS server.'

    else:

        message = 'Only members with the `Redstone Admin` role can use this command.'
        # user doesn't have admin permissions.

    return message
