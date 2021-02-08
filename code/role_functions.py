def check_user(ctx):
    target_role = 'Redstone User'

    # check if member is Redstone or guild admin - automatic pass
    if check_admin(ctx) == True:
        return True

    # for regular guild members
    for role in ctx.author.roles:
        if target_role == role.name:
            return True

    return False

def check_admin(ctx):
    target_role = 'Redstone Admin'

    # for guild admins
    if ctx.author.guild_permissions.administrator == True:
        return True

    # for regular guild members
    for role in ctx.author.roles:
        if target_role == role.name:
            return True

    return False
