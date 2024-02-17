import discord
import time

async def ping(interaction : discord.Interaction, bot):
    latency = round(bot.latency*1000)
    latency_value = str(latency)
    await interaction.response.send_message('pong!... ' + latency_value + ' ms')