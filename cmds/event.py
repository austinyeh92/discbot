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
        role = discord.utils.get(member.guild.roles, name="Trespasser")
        await member.add_roles(role)
        await self.bot.get_channel(867995199161397289).send(f'{member} joined and Trespasser given')
        print(f'{member} joined!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.bot.get_channel(867995199161397289).send(f'{member} left')
        print(f'{member} left!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if 'apple' in msg.content.lower() and msg.author != self.bot.user:
            await msg.channel.send('Yes. Apple.')
    
    # Listener in the knighting ceremonies channel
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel == self.bot.get_channel(867669689953681429):
            if msg.content.lower() == 'knight me as the royal warrior':
                role = discord.utils.get(msg.author.guild.roles, name="The Royal Warrior")
                await msg.author.add_roles(role)
                await self.bot.get_channel(867995199161397289).send(f'{msg.author} knighted as the Royal Warrior')
                await msg.delete()
            elif msg.content.lower() == 'knight me as bloody miner':
                role = discord.utils.get(msg.author.guild.roles, name="Bloody Miner")
                await msg.author.add_roles(role)
                await self.bot.get_channel(867995199161397289).send(f'{msg.author} knighted as Bloody Miner')
                await msg.delete()
            elif msg.content.lower() == 'knight me as pixel protector':
                role = discord.utils.get(msg.author.guild.roles, name="Pixel Protector")
                await msg.author.add_roles(role)
                await self.bot.get_channel(867995199161397289).send(f'{msg.author} knighted as Pixel Protector')
                await msg.delete()
            elif msg.content.lower() == 'take my roles if you really have to':
                role = discord.utils.get(msg.author.guild.roles, name="Peasant")
                await msg.author.edit(roles=[role])
                await self.bot.get_channel(867995199161397289).send(f'{msg.author}\'s all roles taken')
                await msg.delete()
            else:
                channel = msg.channel
                await msg.delete()

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        user = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
        channel = self.bot.get_channel(867429179850227753)
        msg = await channel.fetch_message(868127572616183829)
        if payload.message_id == 868127572616183829 and user.top_role == discord.utils.get(user.guild.roles, name="Trespasser"):
            role = discord.utils.get(user.guild.roles, name="Peasant")
            await user.edit(roles=[role])
            await self.bot.get_channel(867995199161397289).send(f'{user} reacted to the rules and became a Peasant')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        user = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
        channel = self.bot.get_channel(867429179850227753)
        msg = await channel.fetch_message(868127572616183829)
        if payload.message_id == 868127572616183829:
            role = discord.utils.get(user.guild.roles, name="Trespasser")
            await user.edit(roles=[role])
            await self.bot.get_channel(867995199161397289).send(f'{user} decided not to accept the rules and became a Trespasser')


def setup(bot):
    bot.add_cog(Event(bot))