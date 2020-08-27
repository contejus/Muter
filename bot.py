import os
import random 

from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MAX_ATTEMPTS = int(os.getenv('MAX_ATTEMPTS', default=10))

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='roulette', help='Kicks a random user from the server.')
async def roulette(ctx):
    bot_member = ctx.guild.me
    guild_members = ctx.guild.members

    num_attempts = 0
    member_to_kick = bot_member

    await ctx.send("Kicking " + str(member_to_kick) + " from the server.")

    while member_to_kick.top_role >= bot_member.top_role or member_to_kick == bot_member:
        await ctx.send("Can't kick " + str(member_to_kick) + " from the server. Their top role is higher than the bot's role.")
        if num_attempts > MAX_ATTEMPTS:
            break
        member_to_kick = random.choice(guild_members)
        await ctx.send("Kicking " + str(member_to_kick) + " from the server instead.")
        num_attempts += 1
        
    
    if num_attempts <= MAX_ATTEMPTS:
        await ctx.guild.kick(member_to_kick)
        await ctx.send("Kicked " + str(member_to_kick) + " from the server.")
    else: 
        await ctx.send("Could not find members to kick. Please check role hierarchy and make sure RouletteBot is above the lowest common role.")

bot.run(TOKEN)