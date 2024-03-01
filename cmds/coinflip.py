import random
import discord
from discord.ext import commands

async def coinflip(interaction : discord.Interaction):
    result = random.choice(['head', 'tails'])
    await interaction.response.send_message(result)