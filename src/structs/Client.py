import discord
from discord.ext import commands

class Client(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')

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

    async def on_message(self, message):
        if message.author == self.user:
            return

        # Handle commands
        await self.process_commands(message)

        # Custom message handling logic
        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')

def setup(bot):
    bot.add_cog(Client(bot))
