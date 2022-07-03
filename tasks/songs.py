#from turtle import position
from curses import erasechar
import requests
import json
from discord.ext import commands
import youtube_dl
import discord
import ffmpeg
from urlextract import URLExtract

FFMPEG_OPTIONS = {'before_options': '-reconnect 1', 'options': '-vn'}
YDL_OPTIONS = {'format':"bestaudio"}
bot = commands.Bot("#")
intents = discord.Intents.all()
global fila
fila = []
class Queue:
    def __init__(self, idq, url):
        self.idq = idq 
        self.url = url
        fila.append(url)
        
        
class Songs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    async def search_song(self, amount, song, get_url=False):
        x = await self.bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format" : "bestaudio", "quiet" : True}).extract_info(f"ytsearch{amount}:{song}", download=False, ie_key="YoutubeSearch")) 
        w = json.dumps(x)
        load_w = json.loads(w)
        global data
        data = load_w['entries'][0]['formats'][0]['url']
        return data

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("you not in voice channel")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else: 
            await ctx.voice_client.move_to(voice_channel)
   
    @commands.command() 
    async def queue(self, ctx, *ll):
        song = str(ll)
        vc = ctx.voice_client
        arr = []
        idt = len(fila) + 1
        message = (" ").join(song)
        result = await self.search_song(1, song, get_url=True)
        url2 = result
        fila.append({"id": idt, "url": url2})
    
    @commands.command(aliases=['play'])
    async def psy__(self, ctx, *ll):
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        song = str(ll)
        vc = ctx.voice_client
        arr = []
        pedro = True;
        
  
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            if not ("youtube.com/watch?" in song or "https://youtu.be/" in song):
                while len(fila) != -1:
                    idt = len(fila) + 1
                    message = (" ").join(song)
                    result = await self.search_song(1, song, get_url=True)
                    url2 = result
                    fila.append({"id": idt, "url": url2})
                    source = await discord.FFmpegOpusAudio.from_probe(fila[0]['url'], **FFMPEG_OPTIONS)
                    print(len(fila))
                    vc.play(source)
                    fila.pop(0)
            

                
            # extractor = URLExtract()
            # urltemp = extractor.find_urls(ll)
            # url = urltemp[0]
            # info = ydl.extract_info(url, download=False)
            # url2 = info['formats'][0]['url']
            # arr.append(url2)
            # print(arr)
            # source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            # vc.play(source)


    @commands.command()
    async def exit(self, ctx):
        if ctx.voice_client is not None:
            fila.clear()
            return await ctx.voice_client.disconnect()
    
    @commands.command(name='skip')
    async def _skip(self, ctx):
        if ctx.voice_client is not None:
            return await ctx.voice_client.skip()
        
def setup(bot):
    bot.add_cog(Songs(bot))
    

def get_player(self, obj):
    if isinstance(obj, commands.Context):
        return self.wavelink.get_player(obj.guild.id, cls=Player, context=obj)
    elif isinstance(obj, discord.Guild):
        return self.wavelink.get_player(obj.id, cls=Player)
    
