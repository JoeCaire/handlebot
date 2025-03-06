import discord
from discord.ext import commands
from src.models.User import User
from src.interfaces.database.select import getGuildPrefix
from src.models.Organization import Organization
from src.commands.corp.corpPage import corpPage
from src.commands.corp.corpHelp import corpHelp

class CorpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='corp')
    async def corp(self, ctx):
        prefix = await getGuildPrefix(ctx.guild.id)
        content_array = ctx.message.content.split(' ')
        if len(content_array) == 1:
            user = await User.tryGetUserFromDiscord(ctx.author.id)
            if user:
                if user.organizationSID:
                    await corpPage(ctx, await Organization.tryGetOrganizationFromSID(user.organizationSID))
                else:
                    await ctx.send(f"⚠ **{ctx.lang.trad.err_you_not_in_org}**")
            else:
                await ctx.send(f"⚠ **{ctx.lang.trad.handle_not_associate_1} : `{prefix}handle set {ctx.lang.trad.your_handle_cmd}` {ctx.lang.trad.to_associate_one} **")
        elif len(content_array) >= 2:
            if content_array[1] == "help":
                await corpHelp(ctx, prefix)
            elif len(ctx.message.mentions) == 1:
                user = await User.tryGetUserFromDiscord(ctx.message.mentions[0].id)
                if user:
                    if user.organizationSID:
                        await corpPage(ctx, await Organization.tryGetOrganizationFromSID(user.organizationSID))
                    else:
                        await ctx.send(f"⚠ **{ctx.lang.trad.member_no_orga}**")
                else:
                    await ctx.send(f"⚠ **{ctx.lang.trad.member_no_handle}**")
            else:
                organization = await Organization.tryGetOrganizationFromSID(content_array[1])
                if organization:
                    await corpPage(ctx, organization)
                else:
                    await ctx.send(f"⚠ **{ctx.lang.trad.sid_not_exist}**")

def setup(bot):
    bot.add_cog(CorpCommand(bot))
