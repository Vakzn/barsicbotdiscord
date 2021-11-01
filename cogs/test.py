from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 15)
    async def test(self, ctx):
        await ctx.send('Hello world')

def setup(bot):
    bot.add_cog(MyCog(bot))