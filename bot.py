import discord
from discord.ext import commands
import os
from discord_components import DiscordComponents
from discord_slash import SlashCommand, SlashContext

# import defs for slash commands


# create prefix for bot
bot = commands.Bot(command_prefix="#")
slash = SlashCommand(bot, sync_commands=True)
bot.remove_command('help')

# variables
developer = [610839704186781747, 868495003146653726]
premium = [610839704186781747]
muted_id = 904325649655803915

# test slash command
@slash.slash(name='test', description="Проверка бота")
async def test(ctx: SlashContext):
    embed = discord.Embed(title='Hello')
    await ctx.send(embed=embed)

# load cogs slash command
@slash.slash(name='load', description='Загрузка когов')
async def load(ctx: SlashContext, name: str):
    if ctx.author.id in developer:
        bot.load_extension(f'cogs.{name}')
        await ctx.send('Загрузка кога...')
    else:
        await ctx.send('Ти не разработчик')

# unload cogs with slash command
@slash.slash(name='unload', description='Выгрузка когов')
async def unload(ctx: SlashContext, name: str):
    if ctx.author.id in developer:
        bot.unload_extension(f'cogs.{name}')
        await ctx.send('Выгрузка кога...')
    else:
        await ctx.send('Ти не разработчик')

@slash.slash(name='reload', description='Перезагрузка когов')
async def reload(ctx: SlashContext, name: str):
    if ctx.author.id in developer:
        bot.unload_extension(f'cogs.{name}')
        bot.load_extension(f'cogs.{name}')
        await ctx.send('Перезагрузка кога...')
    else:
        await ctx.send('Ти не разработчик')


# load all cogs for start bot
@bot.event
async def on_ready():
    DiscordComponents(bot)
    for name in os.listdir('./cogs'):
        if name.endswith('.py'):
            bot.load_extension(f'cogs.{name[:-3]}')
            print(f'Загрузка кога {name[:-3]}...')
    while True:
        game = discord.Game("#help")
        await bot.change_presence(activity=game)

# reload cogs
@bot.command()
async def reload(ctx, name: str):
    if ctx.author.id in developer:
        await ctx.send('Перезагрузка кога...')
        bot.unload_extension(f'cogs.{name}')
        bot.load_extension(f'cogs.{name}')
    else:
        await ctx.send('Ти не разработчик')

# start bot
bot.run("token")