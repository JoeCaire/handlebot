import discord
from discord.ext import commands
from src.interfaces.database.select import countHandle

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stats')
    async def stats(self, ctx):
        j = int((self.bot.uptime() % 31536000) / 86400)
        h = int((self.bot.uptime() % 86400) / 3600)
        m = int((self.bot.uptime() % 3600) / 60)
        s = int(self.bot.uptime() % 60)
        count_user = await countHandle()
        embed = discord.Embed(color=0x1681a5)
        embed.set_title("Bot Stats")
        embed.add_field(name="Servers", value=str(len(self.bot.guilds)), inline=True)
        embed.add_field(name="Users", value=str(len(set(self.bot.get_all_members()))), inline=True)
        embed.add_field(name="Users in DB", value=str(count_user), inline=True)
        embed.add_field(name="Ping", value=f"{self.bot.latency * 1000:.2f} ms", inline=True)
        embed.add_field(name="RAM Usage", value=f"{self.bot.memory_usage():.2f} MB", inline=True)
        embed.add_field(name="Uptime", value=f"{j}d {h}h {m}m {s}s", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Stats(bot))
