from core.classes import Cog_Extension
import discord
from discord.ext import commands, tasks
import asyncio, json
import urllib.request
import re
import requests as req

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class HowTo(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel == self.bot.get_channel(jdata["what-how-channel"]):
            if ('how' in msg.content.lower() or 'what' in msg.content.lower()) and msg.content.lower().endswith('??') and msg.author != self.bot.user:
                text = msg.content
                text1 = text.replace(' ', '+').replace('?', '')
                html = urllib.request.urlopen(f'https://www.youtube.com/results?search_query={text1}')
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                await msg.channel.send(f'https://www.youtube.com/watch?v={video_ids[0]}')
                embed=discord.Embed(title=f"Other results for {text}", color=0x00f900)
                embed.set_author(name="Remu chan", url="https://imgur.com/a/cVfP2En")
                embed.add_field(name=req.get(f'https://noembed.com/embed?url=https://www.youtube.com/watch?v={video_ids[1]}').text.partition('\"title\":\"')[2].partition('\",\"')[0], value=f'https://www.youtube.com/watch?v={video_ids[1]}', inline=False)
                embed.add_field(name=req.get(f'https://noembed.com/embed?url=https://www.youtube.com/watch?v={video_ids[2]}').text.partition('\"title\":\"')[2].partition('\",\"')[0], value=f'https://www.youtube.com/watch?v={video_ids[2]}', inline=False)
                embed.add_field(name=req.get(f'https://noembed.com/embed?url=https://www.youtube.com/watch?v={video_ids[3]}').text.partition('\"title\":\"')[2].partition('\",\"')[0], value=f'https://www.youtube.com/watch?v={video_ids[3]}', inline=False)
                embed.add_field(name=req.get(f'https://noembed.com/embed?url=https://www.youtube.com/watch?v={video_ids[4]}').text.partition('\"title\":\"')[2].partition('\",\"')[0], value=f'https://www.youtube.com/watch?v={video_ids[4]}', inline=False)
                embed.add_field(name=req.get(f'https://noembed.com/embed?url=https://www.youtube.com/watch?v={video_ids[5]}').text.partition('\"title\":\"')[2].partition('\",\"')[0], value=f'https://www.youtube.com/watch?v={video_ids[5]}', inline=False)
                await msg.channel.send(embed=embed)
                await self.bot.get_channel(jdata["remu-chan-log"]).send(f'{msg.author} wants to know {text}')

def setup(bot):
    bot.add_cog(HowTo(bot))
