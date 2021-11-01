import discord
from discord.ext import commands
from pymongo import MongoClient
import random

class Economic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.coll = MongoClient("mongodb://login:password@discord-shard-00-00.2b8g7.mongodb.net:27017,discord-shard-00-01.2b8g7.mongodb.net:27017,discord-shard-00-02.2b8g7.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-137c2k-shard-0&authSource=admin&retryWrites=true&w=majority").economic.economic

    @commands.command()
    @commands.cooldown(1, 60*60*6)
    async def work(self, ctx):
        user = self.coll.find_one({"id": ctx.author.id})
        if user is None:
            self.coll.insert({"id": ctx.guild.id, "bal": 0})

        cash = random.randint(50, 150)
        self.coll.update({"id": ctx.author.id, "$bal": +cash})
        await ctx.send(embed=discord.Embed(title='Экономика', description=f'Вы заработали {cash}$'))

    @commands.command()
    async def bal(self, ctx, member: discord.Member = None):
        if member is None:
            user = self.coll.find_one({"id" : ctx.author.id})
            if user is None:
                await ctx.send(embed=discord.Embed(title='Ошибка', description='У Вас нет аккаунта в экономике'))
            else:
                await ctx.send(embed=discord.Embed(title='Экономика', description=f"Ваш баланс сейчас: {user['bal']}$"))

def setup(bot):
    bot.add_cog(Economic(bot))