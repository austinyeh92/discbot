from core.classes import Cog_Extension
import discord
from discord.ext import commands, tasks
import asyncio
import urllib, requests, webbrowser
from bs4 import BeautifulSoup

class HowTo(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel == self.bot.get_channel(868056062371192872):
            if 'how' in msg.content.lower() and msg.content.lower().endswith('?') and msg.author != self.bot.user:
                text = msg.content
                text = urllib.parse.quote_plus(text)

                url = 'https://google.com/search?q=' + text

                response = requests.get(url)

                soup = BeautifulSoup(response.text, 'html')
                for g in soup.find_all(class_='g'):
                    print(g.text)
                    print('-----')

def setup(bot):
    bot.add_cog(HowTo(bot))
