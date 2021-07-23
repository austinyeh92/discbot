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

    @commands.command()
    async def rules(self, ctx):
        embed=discord.Embed(title="LA PALACE Code of Conduct", description="Core rules", color=0x00f900)
        embed.add_field(name="1. No flaming, scolding, and spamming", value="We dont want the server filled with negativity.", inline=False)
        embed.add_field(name="2. Reduce frequency of inappropriate words", value="We want to make this place a peaceful and pure community.", inline=False)
        embed.add_field(name="3. Respect and follow the moderators' instructions", value="There might be some extra rules, but please follow the mods' instructons and decisions at all times.", inline=False)
        embed.add_field(name="4. Keep the chat topic the same as the channel", value="This helps with channel cleanness, topic continuity, and history tracing.", inline=False)
        embed.add_field(name="5. Last but not least, HAIL DA KING!", value="No explanation. Just Do It ", inline=False)
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(React(bot))