import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
import socket
from discord_slash import cog_ext, SlashContext

class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ip(self, ctx):
        host = socket.gethostname()
        ipadress= socket.gethostbyname(host)

        await ctx.send(embed=discord.Embed(title='Мой ip адрес', description=f'Твой ip адрес - {ipadress}'))

    @cog_ext.cog_slash(name='ip', description='Узнать твой ip адрес')
    async def _ip(self, ctx: SlashContext):
        host = socket.gethostname()
        ipadress = socket.gethostbyname(host)

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

def setup(bot):
    bot.add_cog(User(bot))