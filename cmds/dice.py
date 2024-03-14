import random
import discord

async def dice(interaction : discord.Interaction):
    number = random.randint(1, 6)
    await interaction.response.send_message(number)
