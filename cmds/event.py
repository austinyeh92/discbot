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
        pass

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        member = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
        channel = self.bot.get_channel(payload.channel_id) 
        msg = await channel.fetch_message(payload.message_id) 
        emoji = payload.emoji.name
        if payload.channel_id == 867429179850227753 and payload.message_id == 868127572616183829 and member.top_role == discord.utils.get(member.guild.roles, name="Trespasser"):
            role = discord.utils.get(member.guild.roles, name="Peasant")
            await member.edit(roles=[role])
            await self.bot.get_channel(867995199161397289).send(f'{member} reacted to the rules and became a Peasant')
        
        if payload.channel_id == 867669689953681429 and payload.message_id == 867693325372358666:
            if emoji == 'piggy_warrior':
                role = discord.utils.get(member.guild.roles, name="The Royal Warrior")
                await member.add_roles(role)
                await self.bot.get_channel(867995199161397289).send(f'{member} was knighted The Royal Warrior')
            elif emoji == 'spinningminecraftsteve':
                role = discord.utils.get(member.guild.roles, name="Pixel Protector")
                await member.add_roles(role)
                await self.bot.get_channel(867995199161397289).send(f'{member} was knighted Pixel Protector')
            elif emoji == 'PikaPickaxe':
                role = discord.utils.get(member.guild.roles, name="Bloody Miner")
                await member.add_roles(role)
                await self.bot.get_channel(867995199161397289).send(f'{member} was knighted Bloody Miner')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        member = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
        channel = self.bot.get_channel(payload.channel_id) 
        msg = await channel.fetch_message(payload.message_id) 
        emoji = payload.emoji.name
        if payload.channel_id == 867429179850227753 and payload.message_id == 868127572616183829:
            role = discord.utils.get(member.guild.roles, name="Trespasser")
            await member.edit(roles=[role])
            await self.bot.get_channel(867995199161397289).send(f'{member} decided not to accept the rules and became a Trespasser')

        if payload.channel_id == 867669689953681429 and payload.message_id == 867693325372358666:
            if emoji == 'piggy_warrior':
                role = discord.utils.get(member.guild.roles, name="The Royal Warrior")
                await member.remove_roles(role)
                await self.bot.get_channel(867995199161397289).send(f'{member} was deknighted The Royal Warrior')
            elif emoji == 'spinningminecraftsteve':
                role = discord.utils.get(member.guild.roles, name="Pixel Protector")
                await member.remove_roles(role)
                await self.bot.get_channel(867995199161397289).send(f'{member} was deknighted Pixel Protector')
            elif emoji == 'PikaPickaxe':
                role = discord.utils.get(member.guild.roles, name="Bloody Miner")
                await member.remove_roles(role)
                await self.bot.get_channel(867995199161397289).send(f'{member} was deknighted Bloody Miner')


def setup(bot):
    bot.add_cog(Event(bot))