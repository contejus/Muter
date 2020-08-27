import os
import random 

from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='test', help='Makes bot send test message in a channel.')
async def test(ctx):
    await ctx.send("Testing, testing, 1 2 3.")

@bot.command(name='mute', help='Mutes all users in a Discord channel.')
async def mute(ctx):
    vc_members = ctx.author.voice.channel.members
    for member in vc_members:
        await member.edit(mute=True, deafen=True)
    await ctx.send("Muted all members in the " + str(ctx.author.voice.channel) + " voice channel.")

@bot.command(name='unmute', help='Unmutes all users in a Discord channel.')
async def unmute(ctx):
    vc_members = ctx.author.voice.channel.members
    for member in vc_members:
        await member.edit(mute=False, deafen=False)
    await ctx.send("Unmuted all members in the " + str(ctx.author.voice.channel) + " voice channel.")

bot.run(TOKEN)