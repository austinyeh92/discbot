from core.classes import Cog_Extension
import discord
from discord.ext import commands

class React(Cog_Extension):
    
    @commands.command()
    async def sup(self, ctx):
        await ctx.send('sup dude')
    
    @commands.command()
    async def repeat(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def purge(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)
        await self.bot.get_channel(867995199161397289).send(f'{num} messages in {ctx.channel.mention} are purged')

def setup(bot):
    bot.add_cog(React(bot))