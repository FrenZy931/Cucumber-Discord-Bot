import discord
from discord.ext import commands

async def echo(interaction : discord.Interaction, channel, message):
    if channel:
        await interaction.response.send_message('sent  message ***"' + message + '"***  to: ' + channel.mention, ephemeral=True)
        await channel.send(message)
    else:
        default_channel = interaction.channel
        await interaction.response.send_message('sent  message ***"' + message + '"***  to: ' + default_channel.mention, ephemeral=True)
        await default_channel.send(message)