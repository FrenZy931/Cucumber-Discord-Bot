import discord
from discord.ext import commands
import datetime

async def unmute(interaction : discord.Interaction, member):
    try:
       delta = datetime.timedelta(seconds=0)
       await member.timeout(delta)
    except Exception as e:
        await interaction.response.send_message('you dont have permissions to mute this user')
        return
    await interaction.response.send_message('user ' + member.mention + ' has been unmuted')
