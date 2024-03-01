import discord
from PIL import Image, ImageDraw
import random
import io
import requests

async def randomcolor(interaction : discord.Interaction):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    image = generate_color_image(color)
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    imgur_url = upload_to_imgur(image_bytes, 'bd876d2a4f8175e')

    embed = discord.Embed(
        title='Random Color',
        description=f'RGB: {color[0]}, {color[1]}, {color[2]}',
        color=discord.Color.from_rgb(*color)
    )

    embed.set_image(url=imgur_url)

    await interaction.response.send_message(embed=embed)

def generate_color_image(color):
    image = Image.new("RGB", (200, 200), color)
    return image

def upload_to_imgur(image_bytes, client_id):
    url = 'https://api.imgur.com/3/image'

    headers = {
        'Authorization': f'Client-ID {client_id}'
    }

    files = {'image': image_bytes.getvalue()}

    response = requests.post(url, headers=headers, files=files)
    imgur_url = response.json()['data']['link']

    return imgur_url
