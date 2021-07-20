from core.classes import Cog_Extension
import discord
from discord.ext import commands

class React(Cog_Extension):
    
    @commands.command()
    async def sup(self, ctx):
        await ctx.send('sup dude')

def setup(bot):
    bot.add_cog(React(bot))