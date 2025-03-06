import discord
from discord.ext import commands

class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='command')
    async def command(self, ctx):
        await ctx.send('This is a command!')

    async def handle(self, ctx):
        await ctx.send('Handle command executed!')

    async def corp(self, ctx):
        await ctx.send('Corp command executed!')

    async def ship(self, ctx):
        await ctx.send('Ship command executed!')

    async def referral(self, ctx):
        await ctx.send('Referral command executed!')

    async def scstats(self, ctx):
        await ctx.send('SCStats command executed!')

def setup(bot):
    bot.add_cog(Command(bot))
