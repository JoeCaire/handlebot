import discord
from discord.ext import commands
from src.commands.corp import corp

class CCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='c')
    async def c(self, ctx):
        await corp(ctx)

def setup(bot):
    bot.add_cog(CCommand(bot))
