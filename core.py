import datetime
import discord
from discord.ext import commands
import os
import pathlib
import database
import asyncio
import subprocess
import typing
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
from cmds import github as GitHub
from cmds import randomcolor as RandomColor
from cmds import meme as Meme
from cmds import mute as Mute
from cmds import unmute as Unmute
from cmds import userinfo as Userinfo
from cmds import serverinfo as Serverinfo
from cmds import server as Server

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='cucumber!!!!!!', intents=intents)
bot.help_command = None
activity = discord.Game(name="/help")
bot.activity = activity

@discord.app_commands.checks.has_permissions(mute_members=True)
@discord.app_commands.AppCommandError
async def error(interaction : discord.Interaction):
    await interaction.response.send_message('you dont have permissions to use this command')
@bot.tree.command(name="mute", description="mute an user")
async def mute(interaction : discord.Interaction, member : discord.Member, weeks : int = None, days : int = None, hours : int = None, minutes : int = None):
    guild = interaction.guild.name
    await Mute.mute(interaction, member, weeks, days, hours, minutes, guild)

@discord.app_commands.checks.has_permissions(mute_members=True)
@discord.app_commands.AppCommandError
async def error(interaction : discord.Interaction):
    await interaction.response.send_message('you dont have permissions to use this command')
@bot.tree.command(name="unmute", description="unmute an user")
async def unmute(interaction : discord.Interaction, member : discord.Member):
    await Unmute.unmute(interaction, member)

@bot.tree.command(name="serverinfo", description="obtain info about server")
async def serverinfo(interaction : discord.Interaction):
    guild = interaction.guild.name
    await Serverinfo.serverinfo(guild, interaction)

@bot.tree.command(name="userinfo", description="obtain info about user")
async def userinfo(interaction : discord.Interaction, user : discord.Member):
    guild = interaction.guild.name
    await Userinfo.userinfo(guild, interaction, user)

@bot.tree.command(name="meme", description="get a random meme")
async def meme(interaction : discord.Interaction, query : str = None):
    await Meme.meme(interaction, query)

@bot.tree.command(name="randomcolor", description="generate random color")
async def randomcolor(interaction : discord.Interaction, color_code: typing.Literal['HSV', 'RGB', 'HEX']):
    await RandomColor.randomcolor(interaction, color_code)

@bot.tree.command(name="coinflip", description="flip a coin")
async def coinflip(interaction : discord.Interaction):
    await CoinFlip.coinflip(interaction)

@bot.tree.command(name="github", description="sends link to github repo")
async def github(interaction : discord.Interaction):
    await GitHub.github(interaction)

@bot.tree.command(name="reddit", description="search subreddits")
async def reddit(interaction : discord.Interaction, redditname : str, posts : int):
    await Reddit.reddit(interaction, redditname, posts)

@bot.tree.command(name="randomnumber", description="generate random number")
async def randomnumber(interaction : discord.Interaction, minimum : int, maximum : int):
    await RandomNumber.randomnumber(interaction, minimum, maximum)

@bot.tree.command(name="wiki", description="find things on wiki")
async def wiki(interaction : discord.Interaction, query : str):
    await Wiki.wiki(interaction, query)

@discord.app_commands.checks.has_permissions(administrator=True)
@discord.app_commands.AppCommandError
async def error(interaction : discord.Interaction):
    await interaction.response.send_message('you dont have permissions to use this command')
@bot.tree.command(name="embed", description="send embed")
async def embed(interaction : discord.Interaction, title : str, description : str, imageurl : str = None, channel : discord.TextChannel = None):
    await Embed.embed(interaction, title, description, imageurl, channel)

@bot.tree.command(name="avatar", description="sends a avatar of an user")
async def avatar(interaction : discord.Interaction, member : discord.Member):
    await Avatar.avatar(interaction, member)

@discord.app_commands.checks.has_permissions(administrator=True)
@discord.app_commands.AppCommandError
async def error(interaction : discord.Interaction):
    await interaction.response.send_message('you dont have permissions to use this command')
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

@bot.tree.command(name="server", description="sends invite link to server")
async def server(interaction : discord.Interaction):
    await Server.server(interaction)

@bot.tree.command(name="help", description="shows help screen")
async def help(interaction : discord.Interaction):
     await Help.help(interaction)

@bot.tree.command(name="credits", description="shows credits")
async def help(interaction : discord.Interaction):
    await Credits.credits(interaction)

@bot.tree.command(name="cucumberpic", description="sends random cucumber picture from our cucumber database")
async def help(interaction : discord.Interaction):
    await Cucumberpic.cucumberpic(interaction)

async def update_data():
    while True:
        for guild in bot.guilds:
           server = database.Server(guild)
           server.periodic_task()
        await asyncio.sleep(1)

@bot.event
async def on_ready():
    await on_script_start()

async def on_script_start():
    print('bot has started')
    await bot.tree.sync()
    await asyncio.run(await update_data())

if __name__ == "__main__":
     bot.run(TOKEN)