import discord
from discord.ext import commands

class SAdmin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='sAdmin')
    @commands.has_permissions(administrator=True)
    async def sAdmin(self, ctx, *, message: str):
        """Send a global message to all guild owners."""
        for guild in self.bot.guilds:
            owner = guild.owner
            if owner:
                try:
                    await owner.send(f"Global message from {ctx.guild.name}:\n{message}")
                except discord.Forbidden:
                    await ctx.send(f"Could not send message to {owner.name} in guild {guild.name}")

def setup(bot):
    bot.add_cog(SAdmin(bot))
