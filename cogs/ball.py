from discord.ext import commands
import random
import discord

class Ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ball(self, ctx, *, text: str):
        answers = ['Да', 'Нет', 'Весьма вероятно', 'Конечно', 'Думай сам!', 'Пошел в зад!']
        await ctx.send(embed=discord.Embed(title=f'Вопрос: {text}', description=f'Ответ: {random.choice(answers)}'))



def setup(bot):
    bot.add_cog(Ball(bot))