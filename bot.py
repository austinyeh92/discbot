import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command('sup')
async def test(ctx):
    await ctx.send(f'Sup! {ctx.author}')
    await ctx.send('How\'s it going?')

bot.run(TOKEN)