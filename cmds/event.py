from core.classes import Cog_Extension
import discord
from discord.ext import commands
import json

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(jdata["welcome channel"])
        await channel.send(f'{member} joined!')
        print(f'{member} joined!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(jdata["those-who-hate-the-server channel"])
        await channel.send(f'{member} left!')
        print(f'{member} left!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if 'apple' in msg.content.lower() and msg.author != self.bot.user:
            await msg.channel.send('Yes. Apple.')
def setup(bot):
    bot.add_cog(Event(bot))