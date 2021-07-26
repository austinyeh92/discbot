from core.classes import Cog_Extension
import discord, json
from discord.ext import commands, tasks
import asyncio

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        async def update_member():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                guild = jdata["guild"]
                await self.bot.get_channel(jdata["members-channel"]).edit(name=f"Members: {self.bot.get_guild(guild).member_count - 7}")
                await asyncio.sleep(600)
        
        self.bg_task = self.bot.loop.create_task(update_member())

def setup(bot):
    bot.add_cog(Task(bot))