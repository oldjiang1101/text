from distutils import dep_util
import discord
from discord.ext import commands

bot = commands.Bot(common_prefix = '[')

@bot.event
async def on_ready():
    print('>>bot is online<<')

bot.run('OTUzNjQwNDU3ODQwMjMwNDEx.YjHg4g.wfpRQtJD-xTNJKPSu4Wlht-BSz8')