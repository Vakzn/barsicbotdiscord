import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
import socket
from discord_slash import cog_ext, SlashContext
import requests
import json
import aiohttp

class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # определение ip адреса
    @commands.command()
    async def ip(self, ctx):
        host = socket.gethostname()
        ipadress= socket.gethostbyname(host)

        await ctx.send(embed=discord.Embed(title='Мой ip адрес', description=f'Твой ip адрес - {ipadress}'))

    @commands.command()
    async def echo(self, ctx, *, text):
        await ctx.send(text)

    # button
    @commands.command()
    async def button(self, ctx):
        await ctx.send('Я хз, лол', components = [
            Button(style=ButtonStyle.blue, label='тест гуль лол xD', emoji='🐏')
        ])

    @commands.Cog.listener()
    async def on_button_click(self, res):
           await res.respond(content='XD', ephemeral=False)

    # рандомное изображение лисы
    @commands.command()
    async def fox(self, ctx):
        r = requests.get("https://some-random-api.ml/img/fox")
        json_data = json.loads(r.text)

        embed = discord.Embed(title='Рандомное изображение лисы', colour=0xff9900)
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)

    # рандомное изображение кота
    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            r = await session.get('https://some-random-api.ml/img/cat')
            catjson = await r.json()
            embed = discord.Embed(title='Рандомное изображение кота', colour=discord.colour.Colour.random())
            embed.set_image(url=catjson['link'])

    # фотки собак
    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json()
            embed = discord.Embed(title='Песик!', colour=discord.colour.Colour.blue())
            embed.set_image(url=dogjson['link'])
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(User(bot))