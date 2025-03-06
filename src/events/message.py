import discord
from discord.ext import commands
from src.interfaces.database.select import get_guild_prefix
from src.commands.handle import handle
from src.commands.corp import corp
from src.commands.ship import ship
from src.commands.referral import referral
from src.commands.scstats import scstats

class MessageEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Handle commands
        await self.bot.process_commands(message)

        # Custom message handling logic
        prefix = await get_guild_prefix(message.guild.id)
        if message.content.startswith(f'{prefix}handle'):
            await handle(message)
        elif message.content.startswith(f'{prefix}corp'):
            await corp(message)
        elif message.content.startswith(f'{prefix}ship'):
            await ship(message)
        elif message.content.startswith(f'{prefix}referral'):
            await referral(message)
        elif message.content.startswith(f'{prefix}scstats'):
            await scstats(message)

def setup(bot):
    bot.add_cog(MessageEvent(bot))
