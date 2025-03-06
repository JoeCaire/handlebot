import discord
from discord.ext import commands
from models.User import User
from interfaces.database import select, update, delete
from interfaces.restAPI.scAPI import getUser
from commands.handle.handleHelp import handleHelp
from commands.handle.handleProfile import handleProfile
from commands.handle.handleSet import handleSet
from commands.handle.handleInfo import handleInfo

class Handle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def handle(self, ctx):
        prefix = await select.getGuildPrefix(ctx.guild.id)
        contentArray = ctx.message.content.split(' ')
        if len(contentArray) == 1:
            user = await User.tryGetUserFromDiscord(ctx.author.id)
            if user:
                await handleProfile(ctx, user)
                await update.updateUser(await User.tryGetUserFromHandle(user.handle, True))
                await update.updatePrintStat(user.referralPrint, user.discordID)
            else:
                await ctx.send(f"⚠ **{lang.trad.handle_not_associate_1} : `{prefix}handle set {lang.trad.your_handle_cmd}` {lang.trad.to_associate_one} **")
        elif len(contentArray) >= 2:
            if contentArray[1] == 'set':
                if len(contentArray) >= 3:
                    await handleSet(ctx, contentArray[2], prefix)
                else:
                    await ctx.send(f"⚠  **{lang.trad.need_handle}**")
            elif contentArray[1] == 'unset':
                if await select.isRegisterFromDiscordID(ctx.author.id):
                    await ctx.send(f"✅ **{lang.trad.handle_rm_success}**")
                    await delete.unset(ctx.author.id)
                else:
                    await ctx.send(f"✅ **{lang.trad.handle_not_associate_unset}**")
            elif contentArray[1] == 'info':
                await handleInfo(ctx)
            elif contentArray[1] == 'help':
                await handleHelp(ctx, prefix)
            else:
                if len(contentArray) == 2:
                    if len(ctx.message.mentions) == 1:
                        user = await User.tryGetUserFromDiscord(ctx.message.mentions[0].id)
                        if user:
                            await handleProfile(ctx, user)
                            await update.updateUser(await User.tryGetUserFromHandle(user.handle, True))
                            await update.updatePrintStat(user.referralPrint, user.discordID)
                        else:
                            await ctx.send(f"⚠ **{lang.trad.member_no_handle}**")
                    else:
                        user = await User.tryGetUserFromHandle(contentArray[1])
                        if user:
                            await handleProfile(ctx, user)
                            await update.updateUser(await User.tryGetUserFromHandle(user.handle, True))
                            await update.updatePrintStat(user.referralPrint, user.discordID)
                        else:
                            await ctx.send(f"⚠ **{lang.trad.handle_not_exist}**")
        else:
            await ctx.send(f"⚠ **{lang.trad.unvalidated_cmd} `{prefix}handle help` {lang.trad.for_more_info}**")

def setup(bot):
    bot.add_cog(Handle(bot))
