from core.classes import Cog_Extension
import discord
from discord.ext import commands

class Main(Cog_Extension):
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong')
        await ctx.send('And stfu')
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('hi')
        
def setup(bot):
    bot.add_cog(Main(bot))