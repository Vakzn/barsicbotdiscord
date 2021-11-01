from discord.ext import commands
import discord

class Premium(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def premium_info(self, ctx):
        desc = """
        Привет!
        Тебе надоело, что приходится терпеть, как другие пользуются функциями, которых у тебя нет?
        Эта подписка для тебя!
        Купи подписку и ты получишь:
        - эксклюзивную роль подписчика Барсика
        - доступ к новым функциям раньше всех
        - принимать участие в разработке бота
        - уважение от Создателя и меня лично, Барсика)
        Короче, подписывайся."""
        await ctx.send(embed=discord.Embed(title='Премиум подписка на Барсика', description=desc))


def setup(bot):
    bot.add_cog(Premium(bot))