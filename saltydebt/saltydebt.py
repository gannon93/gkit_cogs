"""Feed your Salty Bet gambling addiction."""

from discord.ext import commands


class SaltyDebt:

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='salty', pass_context=True)
    async def _salty(self, ctx):
        """Feed your Salty Bet gambling addiction."""
        if ctx.invoked_subcommand is None:
            await self.bot.say("Type `[p]help salty` for info.")

    @_salty.command(name='balance', pass_context=True)
    async def balance(self, ctx):
        """Check SB bank balance."""
        await self.bot.say('`balance` command not yet implemented.')

    @_salty.command(name='bet', pass_context=True)
    async def bet(self, ctx):
        """Bet on an SB contender."""
        await self.bot.say('`bet` command not yet implemented.')

    @_salty.command(name='cashout', pass_context=True)
    async def cashout(self, ctx):
        """Liquidate your SB account assets."""
        await self.bot.say('`cashout` command not yet implemented.')


def setup(bot):
    bot.add_cog(SaltyDebt(bot))
