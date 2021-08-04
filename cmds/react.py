from core.classes import Cog_Extension
import discord, json
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import datetime, math

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

    @commands.command()
    async def meme(self, ctx, *, content):
        URL = f"https://knowyourmeme.com/search?context=images&sort=relevance&q={content.replace(' ','+')}+category_name%3Ameme"

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}

        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="infinite-scroll-wrapper")
        photo_elements = results.find_all("a", {"class": "photo"})
        await ctx.send(photo_elements[0].find("img")["data-src"])
        await ctx.send(photo_elements[1].find("img")["data-src"])
        await ctx.send(photo_elements[2].find("img")["data-src"])
        await self.bot.get_channel(jdata["remu-chan-log"]).send(f'{ctx.author} memed {content} in {ctx.guild}')

    @commands.command()
    async def joshcompound(self, ctx, action, *, content=None):
        with open("settings.json", "r") as jsonFile:
            jdata = json.load(jsonFile)

        if action == 'help':
            await ctx.send('Enter \";joshcompound set <amount>\" to set what josh owes rn\nEnter \";joshcompound rate <amount>%\" to set the rate of josh\'s compound to <amount>%\nEnter \";joshcompound add <amount>\" to add an amount to what josh owes\nEnter \";joshcompound subtract <amount>\" to subtract an amount from what josh owes\nEnter \":joshcompound check\" to check how much josh owes')
        elif action == 'set':
            jdata["money"] = content
            jdata["compound-datetime"] = datetime.date.today().strftime("%Y-%m-%d")
            await ctx.send(f'Josh\'s debt has been set to {jdata["money"]}')
        elif action == 'rate':
            jdata["rate"] = content
            await ctx.send(f'Josh\'s debt rate has been set to {jdata["rate"]}')
        elif action == 'add':
            format = "%Y-%m-%d"
            original_week = datetime.datetime.strptime(jdata["compound-datetime"], format)
            week_elapsed = datetime.date.today().isocalendar()[1] - original_week.isocalendar()[1]
            jdata["money"] = float(jdata["money"]) * math.pow((1+int(jdata['rate'])/100), week_elapsed)
            jdata["money"] += float(content)
            jdata["compound-datetime"] = datetime.date.today().strftime("%Y-%m-%d")
            await ctx.send(f'Josh\'s debt has been increased to {jdata["money"]}')
        elif action == 'subtract':
            format = "%Y-%m-%d"
            original_week = datetime.datetime.strptime(jdata["compound-datetime"], format)
            week_elapsed = datetime.date.today().isocalendar()[1] - original_week.isocalendar()[1]
            jdata["money"] = float(jdata["money"]) * math.pow((1+int(jdata['rate'])/100), week_elapsed)
            jdata["money"] -= float(content)
            jdata["compound-datetime"] = datetime.date.today().strftime("%Y-%m-%d")
            await ctx.send(f'Josh\'s debt has been decreased to {jdata["money"]}')
        elif action == 'check':
            format = "%Y-%m-%d"
            original_week = datetime.datetime.strptime(jdata["compound-datetime"], format)
            week_elapsed = datetime.date.today().isocalendar()[1] - original_week.isocalendar()[1]
            jdata["money"] = float(jdata["money"]) * math.pow((1+int(jdata['rate'])/100), week_elapsed)
            jdata["compound-datetime"] = datetime.date.today().strftime("%Y-%m-%d")
            await ctx.send(f'Josh\'s debt is currently {jdata["money"]}')

        with open("settings.json", "w") as jsonFile:
            json.dump(jdata, jsonFile, indent=4)
def setup(bot):
    bot.add_cog(React(bot))