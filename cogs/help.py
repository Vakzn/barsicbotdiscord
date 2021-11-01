import discord
from discord.ext import commands
from discord_slash import SlashContext, cog_ext

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx: SlashContext):
        help = """
        ball [вопрос] - задать вопрос
        info - информация по боту
        weather [город] - погода в городе, который Вы написали
        ip - узнать Ваш ip адрес(ip адрес Вашего vpn)
        Экономика:
        work - работать и получать за это деньги)
        bal <участник> - узнать свой баланс(если без аргументов) и баланс друга, указанного в аргументах
        pay - пока в разработке
        Модерация - пока в разработке
        """
        await ctx.send(embed=discord.Embed(title='Помощь по боту', description=help))


    


def setup(bot):
    bot.add_cog(Help(bot))