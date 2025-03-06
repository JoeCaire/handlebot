import discord
from discord.ext import commands
from interfaces.restAPI.scAPI import StarCitizenAPI

class SCStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='scstats')
    async def scstats(self, ctx):
        r = StarCitizenAPI.get_star_citizen_stats()
        embed = discord.Embed(title="Status of Star Citizen", color=0x1681a5)
        embed.add_field(name="Fans", value=str(r['fans']), inline=True)
        if 'fleet' in r:
            embed.add_field(name="Ships Sold", value=str(r['fleet']), inline=True)
        embed.add_field(name="Money Raised", value=f"{r['funds']}{r['funds'][r['funds'].index(','):]}", inline=True)
        embed.add_field(name="Live Version", value=r['current_live'], inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(SCStats(bot))
