import discord

async def avatar(interaction : discord.Interaction, member):

   await interaction.response.send_message(f"{member.display_avatar}")