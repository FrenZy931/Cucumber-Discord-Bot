import discord
from discord.ext import commands
from config import CC_COLOR

async def embed(interaction : discord.Interaction, title, description, imageurl, channel):

    if channel:
        await interaction.response.send_message('sent embed in: ' + channel.mention, ephemeral=True)
        if imageurl is None:

            embed1=discord.Embed(
               title=title,
               description=description,
               color=CC_COLOR
            )

            await channel.send(embed=embed1)
        else:

            embed2=discord.Embed(
               title=title,
               description=description,
               color=CC_COLOR
            )

            embed2.set_image(url=imageurl)
            await channel.send(embed=embed2)

    else:
        default_channel = interaction.channel
        await interaction.response.send_message('sent embed in: ' + default_channel.mention, ephemeral=True)
        if imageurl is None:

            embed3=discord.Embed(
               title=title,
               description=description,
               color=CC_COLOR
            )

            await default_channel.send(embed=embed3)
        else:

            embed4=discord.Embed(
               title=title,
               description=description,
               color=CC_COLOR
            )

            embed4.set_image(url=imageurl)
            await default_channel.send(embed=embed4)