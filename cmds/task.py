from core.classes import Cog_Extension
import discord
from discord.ext import commands, tasks
import asyncio

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        async def update_member():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                await self.bot.get_channel(868030837919219742).edit(name=f"Members: {self.bot.get_guild(858926051462742026).member_count - 7}")
                await asyncio.sleep(600)
        
        self.bg_task = self.bot.loop.create_task(update_member())

def setup(bot):
    bot.add_cog(Task(bot))