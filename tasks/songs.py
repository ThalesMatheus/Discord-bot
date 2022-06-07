import requests
import json
from discord.ext import commands
import youtube_dl
import discord
import ffmpeg
FFMPEG_OPTIONS = {'before_options': '-reconnect 1', 'options': '-vn'}
YDL_OPTIONS = {'format':"bestaudio"}
bot = commands.Bot("%")
intents = discord.Intents.all()

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
    async def play(self, ctx, *ll):
        song = str(ll)
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:

            if not ("youtube.com/watch?" in song or "https://youtu.be/" in song):
                message = (" ").join(song)
                result = await self.search_song(1, song, get_url=True)
                url2 = result
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                vc.play(source)

            else:

                info = ydl.extract_info(ll, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                vc.play(source)


    @commands.command()
    async def exit(self, ctx):
        if ctx.voice_client is not None:
            return await ctx.voice_client.disconnect()
            
def setup(bot):
    bot.add_cog(Songs(bot))