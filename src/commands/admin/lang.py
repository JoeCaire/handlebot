import discord
from discord.ext import commands
from src.structs.Lang import Lang
from src.interfaces.database.update import updateGuildLang

class LangCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='lang')
    @commands.has_permissions(administrator=True)
    async def set_lang(self, ctx, lang_key: str):
        guild_id = ctx.guild.id
        available_langs = await Lang.readLangs()
        if lang_key not in available_langs:
            await ctx.send(f"❌ **Invalid language key. Available languages: {', '.join(available_langs)}**")
            return

        await updateGuildLang(guild_id, lang_key)
        await ctx.send(f"✅ **Language has been set to {lang_key}**")

def setup(bot):
    bot.add_cog(LangCommand(bot))
