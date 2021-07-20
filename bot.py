import discord
from discord.ext import commands
import json

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

TOKEN = jdata["DISCORD_TOKEN"]

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('\n\n\n>> Bot is online <<')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(jdata["welcome channel"])
    await channel.send(f'{member} joined!')
    print(f'{member} joined!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(jdata["those-who-hate-the-server channel"])
    await channel.send(f'{member} left!')
    print(f'{member} left!')

@bot.command()
async def test(ctx):
    await ctx.send(f'Sup! {ctx.author}')
    await ctx.send('How\'s it going?')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong')
    await ctx.send('And stfu')

bot.run(TOKEN)