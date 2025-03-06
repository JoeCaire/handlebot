import discord
from discord.ext import commands

class Listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user.name} ({self.bot.user.id})')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        embed = discord.Embed(
            title="Thank you! (Click here to join the official bot discord)",
            url="https://discord.gg/JhwbdNG",
            description="Thank you very much for adding Handle Bot to your discord server, I am very grateful.",
            color=0x1681a5
        )
        embed.add_field(
            name="Info on permissions",
            value="By default, Handle Bot has the same permissions as your @everyone role. It will only see the channels that your @everyone role can see. If you want to use it in a channel that the @everyone role cannot see, add the necessary permissions to its role. If you encounter any issues, please join the official HandleBot discord: [discord.gg/JhwbdNG](https://discord.gg/JhwbdNG)"
        )
        owner = await guild.fetch_member(guild.owner_id)
        await owner.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Handle commands
        await self.bot.process_commands(message)

        # Custom message handling logic
        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')

def setup(bot):
    bot.add_cog(Listeners(bot))
