import discord
from discord.ext import commands
import os
import pathlib
from config import TOKEN
from cmds import cucumber as Cucumber
from cmds import help as Help
from cmds import credits as Credits
from cmds import cucumberpic as Cucumberpic
from cmds import ping as Ping
from cmds import info as Info
from cmds import avatar as Avatar
from cmds import echo as Echo
from cmds import embed as Embed
from cmds import wiki as Wiki
from cmds import reddit as Reddit
from cmds import randomnumber as RandomNumber
from cmds import coinflip as CoinFlip
from cmds import clear as Clear

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='cc!', intents=intents)
bot.help_command = None
activity = discord.Game(name="/help")
bot.activity = activity

@bot.tree.command(name="coinflip", description="flip a coin")
async def coinflip(interaction : discord.Interaction):
    await CoinFlip.coinflip(interaction)

@bot.tree.command(name="reddit", description="search subreddits")
async def reddit(interaction : discord.Interaction, redditname : str, posts : int):
    await Reddit.reddit(interaction, redditname, posts)

@bot.tree.command(name="randomnumber", description="generate random number")
async def randomnumber(interaction : discord.Interaction, minimum : int, maximum : int):
    await RandomNumber.randomnumber(interaction, minimum, maximum)

@bot.tree.command(name="wiki", description="find things on wiki")
async def wiki(interaction : discord.Interaction, query : str):
    await Wiki.wiki(interaction, query)

@bot.tree.command(name="embed", description="send embed")
async def embed(interaction : discord.Interaction, title : str, description : str, imageurl : str = None, channel : discord.TextChannel = None):
    await Embed.embed(interaction, title, description, imageurl, channel)

@bot.tree.command(name="avatar", description="sends a avatar of an user")
async def avatar(interaction : discord.Interaction, member : discord.Member):
    await Avatar.avatar(interaction, member)

@bot.tree.command(name="echo", description="say a message")
async def echo(interaction : discord.Interaction, message : str, channel : discord.TextChannel = None):
    await Echo.echo(interaction, channel, message)

@bot.tree.command(name="ping", description="shows cucumber's latency")
async def ping(interaction : discord.Interaction,):
    await Ping.ping(interaction, bot)

@bot.tree.command(name="info", description="shows bot info")
async def ping(interaction : discord.Interaction,):
    await Info.info(interaction, bot)

@bot.tree.command(name="cucumber", description="says the most shocking thing ever")
async def cucumber(interaction : discord.Interaction):
    await Cucumber.cucumber(interaction)

@bot.tree.command(name="help", description="shows help screen")
async def help(interaction : discord.Interaction):
    await Help.help(interaction)

@bot.tree.command(name="credits", description="shows credits")
async def help(interaction : discord.Interaction):
    await Credits.credits(interaction)

@bot.tree.command(name="cucumberpic", description="sends random cucumber picture from our cucumber database")
async def help(interaction : discord.Interaction):
    await Cucumberpic.cucumberpic(interaction)

@bot.event
async def on_ready():
    await bot.tree.sync()

if __name__ == "__main__":
     bot.run(TOKEN)