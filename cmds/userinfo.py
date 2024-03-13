import discord
import os
from config import DATA
import json
from config import CC_COLOR

async def userinfo(server, interaction : discord.Interaction, user):
    server_path = os.path.join(DATA, server)
    user_folder_path = os.path.join(server_path, "users", user.display_name)
    moderate_file_path = os.path.join(user_folder_path, "moderate.json")
    info_file_path = os.path.join(user_folder_path, "info.json")

    with open(moderate_file_path, "r") as moderate_file:
        moderate = json.load(moderate_file)
    with open(info_file_path, "r") as info_file:
        info = json.load(info_file)

    embed = discord.Embed(
        title=(user.mention + "'s stats"),
        description=f"mutes: {moderate['mutes']}\nbans: {moderate['bans']}\nkicks: {moderate['kicks']}\nwarns: {moderate['warns']}\n\ndisplay name: " + info['display_name'] + "\ninfo: " + info['user_id'] + "\ndate of creation: " + info['creation_date'] + "\n ",
        color=CC_COLOR
    )
    avatar = user.display_avatar
    embed.set_image(url=avatar)

    await interaction.response.send_message(embed=embed)