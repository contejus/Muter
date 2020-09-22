import os
import random 

from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError
from discord.utils import get
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

@bot.command(name="au", pass_context=True)
async def checkreacts(ctx):
    msg1 = await ctx.send("React to me with :mute: to mute or :loud_sound: to unmute!")
    emojis = ['🔇', '🔊']
    for emoji in emojis:
        await msg1.add_reaction(emoji)

@bot.event
async def on_raw_reaction_add(payload):
    channel = await bot.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    if message.author.name == "Muter" and payload.member.name != "Muter":
        vc_members = payload.member.voice.channel.members
        if str(payload.emoji) == str("🔇"):
            await message.remove_reaction(str("🔊"), payload.member)
            for member in vc_members:
                await member.edit(mute=True, deafen=True)
        elif str(payload.emoji) == str("🔊"):
            await message.remove_reaction(str("🔇"), payload.member)
            for member in vc_members:
                await member.edit(mute=False, deafen=False)

bot.run(TOKEN)