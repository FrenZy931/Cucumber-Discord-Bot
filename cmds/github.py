import discord
from config import CC_COLOR

async def github(interaction : discord.Interaction):
    github = discord.Embed(
        title='Github Repo',
        description='https://github.com/FrenZy931/Cucumber-Discord-Bot',
        color=CC_COLOR
    )

    await interaction.response.send_message(embed=github)