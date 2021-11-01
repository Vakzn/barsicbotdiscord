from discord.ext import commands

class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setup(self, ctx):
        await ctx.send('Заходите позже.')

def setup(bot):
    bot.add_cog(Setup(bot))