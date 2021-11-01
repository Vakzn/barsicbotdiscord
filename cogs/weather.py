# данную команду написал ZeynX92#6262
from discord.ext import commands
import discord
import pyowm
from discord_slash import cog_ext

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weather(self, ctx, city: str):
        OWM = pyowm.OWM('91a4fb5f88618a3166d01957bdca9930')
        observation = OWM.weather_at_place(city)
        w = observation.get_weather()
        temperature = w.get_temperature('celsius')['temp']
        wind = w.get_wind()['speed']
        weather = f'Температура сейчас: {str(temperature)} в цельсиях\n Конкретнее: {w.get_detailed_status()} \nСкорость ветра: {str(wind)} м/с'
        await ctx.send(embed=discord.Embed(title='Погода', description=weather, colour=discord.colour.Colour.dark_blue()))

def setup(bot):
    bot.add_cog(Weather(bot))