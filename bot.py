import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('\n\n\n>> Bot is online <<')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(867032709263130654)
    await channel.send(f'{member} joined!')
    print(f'{member} joined!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(867032894882185276)
    await channel.send(f'{member} left!')
    print(f'{member} left!')

@bot.command('sup')
async def test(ctx):
    await ctx.send(f'Sup! {ctx.author}')
    await ctx.send('How\'s it going?')

bot.run(TOKEN)