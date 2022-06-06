# import requests
# from discord.ext import commands

# class MyClient(discord.Client):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.role_message.id = 0
#         self.emoji_to_role = {
#             discord.PartialEmoji(name='U+1F600'): 0,
#             discord.PartialEmoji(name='😀'): 0,

#         }

#     async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):

#         if payload.message_id != self.role_message_id:
#             return

#         guild = self.get_guild(payload.guild_id)
#         if guild is None:
#             return

#         try:
#             role_id = self.emoji_to_role[payload.emoji]
#         except KeyError:
#             return

#         role = guild.get_role(role_id)
#         if role is None:
#             return
        
#         try:
#             await payload.member.add_roles(role)
#         except discord.HTTPException:
#             pass

#     async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
#         if payload.message_id != self.role_message_id:
#             return

#         guild = self.get_guild(payload.guild_id)
#         if guild is None:
#             return

#         try:
#             role_id = self.emoji_to_role[payload.emoji]
#         except KeyError:
#             return
        
#         role = guild.get_role(role_id)
#         if role is None:
#             return

#         member = guild.get_member(payload.user.id)
#         if member is None:
#             return
        
#         try:
#             await member.remove_role(role)
#         except discord.HTTPException:
#             pass
        

# intents = discord.Intents.default()
# intents.members = True 

# client = MyClient(intents=intents)
# client.run('TOKEN')