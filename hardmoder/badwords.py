from discord.ext import commands
import discord

class Badwords(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener
    async def on_message(self, message):
        badwords = ["хуй", "нахуй", "сука", "ебало", "сиськи", "пизда"]
        if message.context in badwords:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title='Плохие слова', description=f'{message.author} сказал парочку плохих слов.'))



def setup(bot):
    bot.add_cog(Badwords(bot))