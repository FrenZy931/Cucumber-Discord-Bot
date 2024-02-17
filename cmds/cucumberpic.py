from discord.ext import commands
import discord
import os
import random
from config import IMG_DIR

async def cucumberpic(interaction : discord.Interaction):
    images_folder = IMG_DIR
    images = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]
        
    if images:
         chosen_image = random.choice(images)
         image_path = os.path.join(images_folder, chosen_image)
         await interaction.response.send_message(file=discord.File(image_path))