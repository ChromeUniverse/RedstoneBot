import discord

# format online player list rich embed

from server_name import server_name

async def format_list(players, ctx, session, serverID):

  name = await server_name(session, serverID)

  title = 'Online players'
  content = 'There are **' + str(len(players)) + '** players online on **' + name + '** right now.\n\n'

  if len(players) != 0:
    for player in players:
      new_entry = ":arrow_forward:  **" + player + '**\n\n'
      content += new_entry

  content += '\n'

  page=discord.Embed(
      title=title,
      description=content,
      colour=discord.Colour.from_rgb(221,55,55)
  )
  await ctx.send(embed=page)

  return page