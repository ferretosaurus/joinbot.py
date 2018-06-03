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
    fmt = '{0.mention} joined.'
    channel = member.server.get_channel("411967511387570176")
    await bot.send_message(channel, fmt.format(member))

@bot.event
async def on_member_remove(member):
    fmt = '{0.mention} has left'
    channel = member.server.get_channel("411967511387570176")
    await bot.send_message(channel, fmt.format(member))


bot.run(os.environ["TOKEN"])
