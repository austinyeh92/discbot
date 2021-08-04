from core.classes import Cog_Extension
import discord
from discord.ext import commands
import discord.utils
import json, asyncio

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

lst = ["no", "never", "not", "gay", "nah", "u"]
def check_word(str, lst):
    for i in range(len(lst)):
        if f' {lst[i]} ' in str.lower() or str.lower().endswith(f' {lst[i]}') or str.lower().startswith(f'{lst[i]} ') or str.lower() == lst[i]:
            return lst[i]
    return None

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name="Trespasser")
        await member.add_roles(role)
        await self.bot.get_channel(jdata["remu-chan-log"]).send(f'{member} joined and Trespasser given')
        print(f'{member} joined!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.bot.get_channel(jdata["remu-chan-log"]).send(f'{member} left')
        print(f'{member} left!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if 'apple' in msg.content.lower() and msg.author != self.bot.user:
            await msg.channel.send('Yes. Apple.')

        skrub_role = discord.utils.get(msg.author.guild.roles, id=683546760525906015)
        word = check_word(msg.content, lst)
        if word != None and msg.author != self.bot.user and (skrub_role in msg.author.roles):
            guild = msg.author.guild
            mutedRole = discord.utils.get(guild.roles, name="Muted")

            if not mutedRole:
                mutedRole = await guild.create_role(name="Muted")

                for channel in guild.channels:
                    await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

            await msg.author.add_roles(mutedRole, reason=f'This naughty kid said "{word}"')
            await msg.channel.send(f"Muted {msg.author.mention} for... saying \"{word}\" :\\")
            await asyncio.sleep(3)
            await msg.author.remove_roles(mutedRole)
            await msg.channel.send(f"Unmuted {msg.author.mention}")


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        member = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
        channel = self.bot.get_channel(payload.channel_id) 
        msg = await channel.fetch_message(payload.message_id) 
        emoji = payload.emoji.name
        if payload.channel_id == jdata["code-of-conducts"] and payload.message_id == jdata["rules-msg"] and member.top_role == discord.utils.get(member.guild.roles, name="Trespasser"):
            role = discord.utils.get(member.guild.roles, name="Peasant")
            await member.edit(roles=[role])
            await self.bot.get_channel(jdata["remu-chan-log"]).send(f'{member} reacted to the rules and became a Peasant')
        
        if payload.channel_id == jdata["knighting-ceremonies"] and payload.message_id == jdata["knighting-msg"]:
            if emoji == 'piggy_warrior':
                role = discord.utils.get(member.guild.roles, name="The Royal Warrior")
                await member.add_roles(role)
                await self.bot.get_channel(jdata["remu-chan-log"]).send(f'{member} was knighted The Royal Warrior')
            elif emoji == 'spinningminecraftsteve':
                role = discord.utils.get(member.guild.roles, name="Pixel Protector")
                await member.add_roles(role)
                await self.bot.get_channel(jdata["remu-chan-log"]).send(f'{member} was knighted Pixel Protector')
            elif emoji == 'PikaPickaxe':
                role = discord.utils.get(member.guild.roles, name="Bloody Miner")
                await member.add_roles(role)
                await self.bot.get_channel(jdata["remu-chan-log"]).send(f'{member} was knighted Bloody Miner')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        member = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
        channel = self.bot.get_channel(payload.channel_id) 
        msg = await channel.fetch_message(payload.message_id) 
        emoji = payload.emoji.name
        if payload.channel_id == jdata["code-of-conducts"] and payload.message_id == jdata["rules-msg"]:
            role = discord.utils.get(member.guild.roles, name="Trespasser")
            await member.edit(roles=[role])
            await self.bot.get_channel(jdata["remu-chan-log"]).send(f'{member} decided not to accept the rules and became a Trespasser')

        if payload.channel_id == jdata["knighting-ceremonies"] and payload.message_id == jdata["knighting-msg"]:
            if emoji == 'piggy_warrior':
                role = discord.utils.get(member.guild.roles, name="The Royal Warrior")
                await member.remove_roles(role)
                await self.bot.get_channel(jdata["remu-chan-log"]).send(f'{member} was deknighted The Royal Warrior')
            elif emoji == 'spinningminecraftsteve':
                role = discord.utils.get(member.guild.roles, name="Pixel Protector")
                await member.remove_roles(role)
                await self.bot.get_channel(jdata["remu-chan-log"]).send(f'{member} was deknighted Pixel Protector')
            elif emoji == 'PikaPickaxe':
                role = discord.utils.get(member.guild.roles, name="Bloody Miner")
                await member.remove_roles(role)
                await self.bot.get_channel(jdata["remu-chan-log"]).send(f'{member} was deknighted Bloody Miner')


def setup(bot):
    bot.add_cog(Event(bot))