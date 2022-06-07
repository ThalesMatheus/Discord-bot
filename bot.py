import os
import requests
from cProfile import run
from urllib import response
import discord
from discord.ext import commands
from decouple import config

bot = commands.Bot("%")
intents = discord.Intents.all()

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def shutdown(ctx):
    await ctx.bot.logout()

for file in os.listdir('./tasks'):
    if file.endswith('.py'):
        bot.load_extension(f'tasks.{file[:-3]}')
        
TOKEN = config("TOKEN")
bot.run(TOKEN) 