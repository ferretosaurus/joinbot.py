#Joinbot by Aaron Coombes

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix = '##')

@bot.event
async def on_ready():
    print (bot.user.name, 'is online')

@bot.event
async def on_member_join(member):
    fmt = 'Welcome, {0.mention}, enjoy the server and read the rules'
    channel = member.server.get_channel("455798975451234304")
    await bot.send_message(channel, fmt.format(member))


bot.run(os.environ["TOKEN"])
