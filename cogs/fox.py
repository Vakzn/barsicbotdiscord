import discord
from discord.ext import commands
import requests
import json
from discord_slash import cog_ext, SlashContext

class Fox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fox(self, ctx):
        r = requests.get("https://some-random-api.ml/img/fox")
        json_data = json.loads(r.text)

        embed = discord.Embed(title='Рандомное изображение лисы', colour=0xff9900)
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name='fox', description='Рандомное изображение лисы')
    async def _fox(self, ctx: SlashContext):
        r = requests.get("https://some-random-api.ml/img/fox")
        json_data = json.loads(r.text)

        embed = discord.Embed(title='Рандомное изображение лисы', colour=0xff9900)
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Fox(bot))