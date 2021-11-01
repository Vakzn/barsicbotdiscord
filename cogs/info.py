import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        info = 'Создатель бота - timka123#0111'
        await ctx.send(embed=discord.Embed(title='Информация о боте', description=info))

def setup(bot):
    bot.add_cog(Info(bot))