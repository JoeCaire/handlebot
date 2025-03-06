import discord
from discord.ext import commands
from src.interfaces.database import insert

class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def prefix(self, ctx, *, new_prefix: str = None):
        if new_prefix is None:
            await ctx.send("⚠ **You need to provide a new prefix.**")
            return

        if len(new_prefix) > 3:
            await ctx.send("⚠ **The prefix cannot be longer than 3 characters.**")
            return

        await insert.insertPrefix(ctx.guild.id, new_prefix)
        await ctx.send(f"✅ **The prefix has been updated to `{new_prefix}`.**")

def setup(bot):
    bot.add_cog(Prefix(bot))
