import discord
from discord.ext import commands
import os
import json

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

TOKEN = jdata["DISCORD_TOKEN"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=';', intents=intents)

@bot.event
async def on_ready():
    print('\n\n\n>> Bot is online <<')
    
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} succesffuly loaded.')
    await bot.get_channel(867995199161397289).send(f'{extension} successfully loaded')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} succesffuly unloaded.')
    await bot.get_channel(867995199161397289).send(f'{extension} successfully unloaded')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} succesffuly reloaded.')
    await bot.get_channel(867995199161397289).send(f'{extension} successfully reloaded')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(TOKEN)
