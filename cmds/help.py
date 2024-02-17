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
**echo** - send message
**embed** - send embed
**info** - show info about bot
**ping** - show discord bot latency
**wiki** - search things on wiki

***bro who uses help screens in 2024 :skull:***""",

       color=CC_COLOR
    )
    await interaction.response.send_message(embed=embed)