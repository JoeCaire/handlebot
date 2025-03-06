import discord

async def on_guild_join(guild):
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
