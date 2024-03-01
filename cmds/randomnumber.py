import random
import discord
from discord.ext import commands

async def randomnumber(interaction : discord.Interaction, minimum, maximum):
    if minimum < maximum:
       random_num = random.randint(minimum, maximum)
       await interaction.response.send_message(random_num)
    else:
       random_num = random.randint(maximum, minimum)
       await interaction.response.send_message(random_num)