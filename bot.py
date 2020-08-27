import os
import random 

from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='test', help='Makes bot send test message in a channel.')
async def test(ctx):
    await ctx.send("Testing, testing, 1 2 3.")

bot.run(TOKEN)