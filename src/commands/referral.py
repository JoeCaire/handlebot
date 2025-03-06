import discord
from discord.ext import commands
from interfaces.database.update import updateReferral
from interfaces.database.select import isRegisterFromDiscordID, getGuildPrefix
from commands.referral.referralSet import setReferral
from commands.referral.referralStatus import referralStatus
from commands.referral.randomReferal import randomReferral
from commands.referral.referralHelp import referralHelp

class Referral(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def referral(self, ctx):
        prefix = await getGuildPrefix(ctx.guild.id)
        contentArray = ctx.message.content.split(' ')
        if len(contentArray) == 1:
            await randomReferral(ctx, self.bot.lang)
        elif len(contentArray) >= 2:
            if contentArray[1] == 'set':
                await setReferral(ctx, self.bot.lang, prefix)
            elif contentArray[1] == 'status':
                await referralStatus(ctx, self.bot.lang, prefix)
            elif contentArray[1] == 'help':
                await referralHelp(ctx, self.bot.lang, prefix)

def setup(bot):
    bot.add_cog(Referral(bot))
