from core.classes import Cog_Extension
import discord, json
from discord.ext import commands

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    
    @commands.command()
    async def sup(self, ctx):
        await ctx.send('sup dude')
        await self.bot.get_channel(jdata["remu-chan-log"]).send(f'{ctx.author} said sup')
    
    @commands.command()
    async def repeat(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)
        await self.bot.get_channel(jdata["remu-chan-log"]).send(f'Remu chan repeated \"{msg}\" by {ctx.author}')

    @commands.command()
    async def purge(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)
        await self.bot.get_channel(jdata["remu-chan-log"]).send(f'{num} messages in {ctx.channel.mention} are purged')

    @commands.command()
    async def rules(self, ctx):
        embed=discord.Embed(title="LA PALACE Code of Conduct", description="Core rules", color=0x00f900)
        embed.add_field(name="1. No flaming, scolding, and spamming", value="We dont want the server filled with negativity.", inline=False)
        embed.add_field(name="2. Reduce frequency of inappropriate words", value="We want to make this place a peaceful and pure community.", inline=False)
        embed.add_field(name="3. Respect and follow the moderators' instructions", value="There might be some extra rules, but please follow the mods' instructons and decisions at all times.", inline=False)
        embed.add_field(name="4. Keep the chat topic the same as the channel", value="This helps with channel cleanness, topic continuity, and history tracing.", inline=False)
        embed.add_field(name="5. Last but not least, HAIL DA KING!", value="No explanation. Just Do It ", inline=False)
        await ctx.send(embed=embed)
        await self.bot.get_channel(jdata["remu-chan-log"]).send(f'rules requested in {ctx.channel.mention}')
        
def setup(bot):
    bot.add_cog(React(bot))