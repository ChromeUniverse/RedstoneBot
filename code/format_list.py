import discord

# format online player list rich embed

async def format_list(players, ctx):

  title = 'Online players'
  content = 'There are **' + str(len(players)) + '** players online on **' + str(ctx.guild.name) + '** right now.\n\n'

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