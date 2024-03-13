import discord
from discord.ext import commands
import datetime
import os
import json
from config import DATA
from unidecode import unidecode

def update_mute_info(server_name, user_display_name, category):
    server_path = os.path.join(DATA, server_name)
    user_folder_path = os.path.join(server_path, "users", user_display_name)
    mute_file_path = os.path.join(user_folder_path, "moderate.json")

    if os.path.exists(mute_file_path):
        with open(mute_file_path, "r") as mute_file:
            mute_info = json.load(mute_file)
    else:
        mute_info = {}

    mute_info[category] += 1

    with open(mute_file_path, "w") as mute_file:
        json.dump(mute_info, mute_file)

async def mute(interaction : discord.Interaction, member, weeks, days, hours, minutes, guild):
    sanitized_guild = unidecode(guild)
    if not weeks and not days and not hours and not minutes:
        await interaction.response.send_message('please enter for how much should the user be muted.')
        return
       
    if not weeks:
        weeks = 0
    if not days:
        days = 0
    if not hours:
        hours = 0
    if not minutes:
        minutes = 0
    
    delta_duration = datetime.timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes)
    try:
        await member.timeout(delta_duration)
    except Exception as e:
        await interaction.response.send_message('you dont have permissions to mute this user')
        return

    await interaction.response.send_message('user ' + member.mention + f' has been muted for {weeks}w {days}d {hours}h {minutes}m')
    update_mute_info(user_display_name=member.display_name, server_name=sanitized_guild, category="mutes")


