from core.classes import Cog_Extension
import discord
from discord.ext import commands
import json

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.server.roles, id="867642851943514203")
        await self.bot.add_roles(member, role)
        print(f'{member} joined!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} left!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if 'apple' in msg.content.lower() and msg.author != self.bot.user:
            await msg.channel.send('Yes. Apple.')
def setup(bot):
    bot.add_cog(Event(bot))