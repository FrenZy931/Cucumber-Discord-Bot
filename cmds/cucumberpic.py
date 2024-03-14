import discord
import serpapi
import random

# List to store URLs of images already fetched
fetched_thumbnails = []

async def update_pictures():
    fetch_thumbnails("cucumber")

async def cucumberpic(interaction: discord.Interaction):
    # Select a random thumbnail from fetched thumbnails
    if fetched_thumbnails:
        chosen_url = random.choice(fetched_thumbnails)
        await interaction.response.send_message(chosen_url)
    else:
        await interaction.response.send_message("No images found")

def fetch_thumbnails(query):
    # Generate a random offset between 0 and 99 to request different sets of images
    for _ in range(100):  # Fetch 10 sets of images (100 images in total)
        params = {
            "engine": "google_images",
            "q": query,
            "hl": "en",
            "gl": "us",
            "tbs": "il:cl",
            "api_key": "227b49ad03b660906d3299571b1e9bfcb2621d99e0c58b76d2d78025cf61b489",
            "num": 1,
        }

        search = serpapi.search(params)
        if "images_results" in search:
            images = search["images_results"]
            for image in images:
                thumbnail_url = image.get("thumbnail")
                if thumbnail_url:
                    fetched_thumbnails.append(thumbnail_url)