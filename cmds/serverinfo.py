import discord
import os
from config import DATA
import json
from config import CC_COLOR

async def serverinfo(server, interaction : discord.Interaction):
    server_path = os.path.join(DATA, server)
    info_file_path = os.path.join(server_path, "info.txt")

    with open(info_file_path, "r") as info_file:
        info = json.load(info_file)
    
    embed=discord.Embed(
        title=server + " stats",
        description=f"users: {info['member_count']}\nserver id: " + info["server_id"] + "\ndisplay name: " + info["display_name"],
        color=CC_COLOR
    )
    await interaction.response.send_message(embed=embed)