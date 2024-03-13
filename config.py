import pathlib
import discord

TOKEN = 'YOUR_TOKEN_HERE'
BASE_DIR = pathlib.Path(__file__).parent
CMDS_DIR = BASE_DIR / "cmds"
IMG_DIR = BASE_DIR / "images"
CC_COLOR = discord.Color.from_rgb(64, 121, 32)
DATA = BASE_DIR / "data"