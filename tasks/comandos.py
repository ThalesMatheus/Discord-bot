from email import message
from urllib import response
from urllib.request import urlopen
from random import random, randrange
import requests
import json
from discord.ext import commands
import socket, os

bot = commands.Bot("%")

class Nhentai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def hbomb(self, ctx, num):
        i = 0
        num = int(num)
        for i in range(num): 
            id = randrange(0, 39)
            pg = randrange(1, 200)
            response = requests.get(f"https://yande.re/post.json?page={pg}")
            data = response.json()
            url = data[id]['jpeg_url']
            await ctx.send(url)
            i += 1
            
    @commands.command()
    async def hentai(self, ctx):
        id = randrange(0, 39)
        pg = randrange(1, 200)
        response = requests.get(f"https://yande.re/post.json?page={pg}")
        data = response.json()
        url = data[id]['jpeg_url']
        await ctx.send(url)
    
    @commands.command()
    async def waifu(self, ctx):
        response = requests.get("https://api.waifu.im/random/")
        data = response.json()
        url = data['images'][0]['url']
        await ctx.send(url)
        
    @commands.command()
    async def waifu_tag(self, ctx, tag):
        response = requests.get(f"https://api.waifu.im/random/?selected_tags={tag}")
        data = response.json()
        url = data['images'][0]['url']
        await ctx.send(url)
        
    @commands.command()
    async def waifu_bomb(self, ctx, tag, num):
        i = 0
        num = int(num)
        for i in range(num): 
            response = requests.get(f"https://api.waifu.im/random/?selected_tags={tag}")
            data = response.json()
            url = data['images'][0]['url']
            await ctx.send(url)
            i += 1
def setup(bot):
    bot.add_cog(Nhentai(bot))
    

    #     imm = json.dumps(data, separators=(","," = "))