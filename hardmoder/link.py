from discord.ext import commands
import discord

class Moder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener
    async def on_message(self, message):
        if 'https://' in message.context:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title='Нарушение', description=f'{message.author} отправил ссылку в чат.'))

def setup(bot):
    bot.add_cog(Moder(bot))