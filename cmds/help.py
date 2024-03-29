import discord
from config import CC_COLOR

async def help(interaction : discord.Interaction):
    embed = discord.Embed(
       title='Help Menu',

       description="""
hello thank you for using cucumber, the best bot ever made.

**help** - shows this bad screen
**credits** - shows credits
**cucumber** - says cucumber
**cucumberpic** - posts random cucumber pic from our big cucumber database
**avatar** - show user avatar
**echo** - send message (admin only)
**embed** - send embed (admin only)
**info** - show info about bot
**ping** - show discord bot latency
**wiki** - search things on wiki
**reddit** - search subreddits on reddit
**randomnumber** - generate random number
**github** - sends link to our github repo
**coinflip** - flip a coin
**randomcolor** - generate random color
**meme** - posts random meme
**mute** - mute users (admin only)
**unmute** - unmute users (admin only)
**userinfo** - send information about an user
**serverinfo** - send information about this server
**meme** - send random meme
**server** - send invite to cucumber community official
**dice** - throw a dice

***bro who uses help screens in 2024 :skull:***""",

       color=CC_COLOR
    )
    await interaction.response.send_message(embed=embed)