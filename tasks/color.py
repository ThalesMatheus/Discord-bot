from ast import Num
from tkinter import E
from turtle import color
from unicodedata import digit
import requests
import json
from discord.ext import commands
import socket, os
import colorsys
import math
import discord

bot = commands.Bot("#")

class Color(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def hex(self, ctx, value):
        value = value.lstrip('#')
        lv = len(value)
        await ctx.send(tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)))
    
    @commands.command()
    async def rgb(self, ctx, rc, gc, bc):
       r = int(rc)
       g = int(gc)
       b = int(bc)
       color = '#%02x%02x%02x' % (r, g, b)
       await ctx.send(f'``{color}``')
       
    @commands.command()
    async def hsv(self, ctx, rs, gs, bs):
        r = int(rs)
        g = int(gs)
        b = int(bs)
        (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
        await ctx.send(f"``{trunc(h, 4)} {trunc(s, 4)} {trunc(v, 4)}``")
    
    @commands.command()
    async def mono(self, ctx, rs, gs, bs):
        r = int(rs)
        g = int(gs)
        b = int(bs)
        (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
        vs = str(v)
        if (len(vs) == 3):
            temp = vs[0]
            temp2 = vs[1]
            ww = "0"
            strv = temp + temp2 + ww
            tonhos = int(strv)
            newV = v - tonhos
            x = 25
            y = 1

            arr = []
            for y in range(10):
                arr.append(f"{trunc(h, 4)}, {trunc(s, 4)}, {newV + x * y}")
                y += 1
            if (y == 10):
                ath = ctx.message.author.name
                img = ctx.message.author
                embed = discord.Embed(
                    title=f"{ath} Color pallet", 
                    description="description",
                    colour = 16252900
                    )
                
                pfp = img.avatar_url
                embed.set_thumbnail(url=f'{pfp}')

                for x in arr:
                    embed.add_field(name="Monochromatic", value=f"{x}", inline=False)
                await ctx.send(embed=embed)



        elif (len(vs) == 2):
            temp = vs[0]
            ww = "0"
            strv = temp + ww
            tonhos = int(strv)
            newV = v - tonhos
            x = 25
            y = 1
            for y in range(10):
                await ctx.send(f"{h}, {s}, {newV + x * y}")
                y += 1
        
def setup(bot):
    bot.add_cog(Color(bot))
    
def trunc(num,n):
    temp = str(num)
    for x in range(len(temp)):
        if temp[x] == '.':
            try:
                return float(temp[:x+n+1])
            except:
                return float(temp)      
    return float(temp)
