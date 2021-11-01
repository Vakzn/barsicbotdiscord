from discord.ext import commands
import discord
from datetime import datetime
import pymongo

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(title='Ошибка', description='Нет аргумента, посмотри в help', colour=discord.colour.Colour.dark_red()))
        elif isinstance(error, discord.ext.commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title='Ошибка 403', description='У тебя нет прав на выполнение этой комманды', colour=discord.colour.Colour.dark_red()))
        elif isinstance(error, discord.ext.commands.MemberNotFound):
            await ctx.send(embed=discord.Embed(title='Ошибка 404', description='Участника не существует. Совет: для взаимодействия с учатником пингуй его через @', colour=discord.colour.Colour.dark_red()))
        elif isinstance(error, discord.ext.commands.MessageNotFound):
            await ctx.send(embed=discord.Embed(title='Ошибка 404', description='Данного сообщения не существует, либо было удалено', colour=discord.colour.Colour.dark_red()))
        elif isinstance(error, discord.ext.commands.CommandInvokeError):
            await ctx.send(embed=discord.Embed(title='Ошибка 1', description='Ошибки в коде. Напишите timka123#0111 для исправления', colour=discord.colour.Colour.dark_red()))
        elif isinstance(error, discord.ext.commands.CommandOnCooldown):
            embed = discord.Embed(title="Кулдаун", description=f"{ctx.command.qualified_name} можно использовать только {error.cooldown.rate} раз в {datetime.fromtimestamp(error.cooldown.per).strftime('%H:%M:%S')}. Попробуйте через {datetime.fromtimestamp(error.retry_after).strftime('%H:%M:%S')}.")
            await ctx.send(embed=embed)
        elif isinstance(error, discord.ext.commands.CommandNotFound):
            await ctx.send(embed=discord.Embed(title='Ошибка 404', description='Команды не существует', colour=discord.colour.Colour.dark_red()))
        elif isinstance(error, pymongo.errors.ServerSelectionTimeoutError):
            await ctx.send(embed=discord.Embed(title='Ошибка 500', description='Проблема с базой данных. Пытаемся решить.'))


def setup(bot):
    bot.add_cog(Error(bot))