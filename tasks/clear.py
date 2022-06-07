from discord.ext import commands
import requests

bot = commands.Bot("#")


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def clear(self, ctx, amount=15):
        await ctx.channel.purge(limit=amount)

def setup(bot):
    bot.add_cog(Clear(bot))
        