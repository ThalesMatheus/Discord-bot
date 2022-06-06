import requests
from discord.ext import commands
import discord 
bot = commands.Bot('%')

class MyClient(commands.Cog):
    def __init__(self, bot, role_message, emoji_to_role):
        self.bot = bot
        self.role_message = role_message
        self.emoji_to_role = {
            discord.PartialEmoji(name='U+1F600'): 0,
            discord.PartialEmoji(name='😀'): 0,

        }
    @commands.command()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):

        if payload.message_id != self.role_message:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            return

        role = guild.get_role(role_id)
        if role is None:
            return
        
        try:
            await payload.member.add_roles(role)
        except discord.HTTPException:
            pass
        
    @commands.command()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        if payload.message_id != self.role_message:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            return
        
        role = guild.get_role(role_id)
        if role is None:
            return

        member = guild.get_member(payload.user.id)
        if member is None:
            return
        
        try:
            await member.remove_role(role)
        except discord.HTTPException:
            pass
        

intents = discord.Intents.default()
intents.members = True 

def setup(bot):
    bot.add_cog(MyClient(bot))