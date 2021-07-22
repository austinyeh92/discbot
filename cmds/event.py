from core.classes import Cog_Extension
import discord
from discord.ext import commands
import discord.utils
import json, asyncio

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name="Moron")
        await member.add_roles(role)
        print(f'{member} joined!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} left!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if 'apple' in msg.content.lower() and msg.author != self.bot.user:
            await msg.channel.send('Yes. Apple.')
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel == self.bot.get_channel(867669689953681429):    
            if msg.content.lower() == 'knight me as the royal warrior':
                role = discord.utils.get(msg.author.guild.roles, name="The Royal Warrior")
                await msg.author.add_roles(role)
                await msg.delete()
            elif msg.content.lower() == 'knight me as bloody miner':
                role = discord.utils.get(msg.author.guild.roles, name="Bloody Miner")
                await msg.author.add_roles(role)
                await msg.delete()
            elif msg.content.lower() == 'knight me as pixel protector':
                role = discord.utils.get(msg.author.guild.roles, name="Pixel Protector")
                await msg.author.add_roles(role)
                await msg.delete()
            elif msg.content.lower() == 'take my roles if you really have to':
                role = discord.utils.get(msg.author.guild.roles, name="The Royal Warrior")
                await msg.author.remove_roles(role)
                role = discord.utils.get(msg.author.guild.roles, name="Bloody Miner")
                await msg.author.remove_roles(role)
                role = discord.utils.get(msg.author.guild.roles, name="Pixel Protector")
                await msg.author.remove_roles(role)
                await msg.delete()
            else:
                channel = msg.channel
                await msg.delete()


def setup(bot):
    bot.add_cog(Event(bot))