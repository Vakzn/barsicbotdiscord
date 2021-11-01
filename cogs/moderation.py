from discord.ext import commands
from discord.ext.commands.core import command
from discord_slash import SlashContext, cog_ext
import discord
import asyncio
from getseconds import get_seconds

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, time: str, reason: str):
        await ctx.send(embed=discord.Embed(title='Бан!', description=f'{member.mention} был забанен на {time} по причине {reason}'))
        await member.ban()
        await asyncio.sleep(get_seconds(time))
        await member.unban()
        await ctx.send(embed=discord.Embed(title='Ура! Разбан!', description=f'{member.mention} был разбанен)'))

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, reason: str):
        await ctx.send(embed=discord.Embed(title='Кик', description=f'{member.mention} был кикнут за {reason}', colour=discord.Colour.red()))
        await member.kick()


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.Member):
        await member.unban()

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self, ctx, purge: int):
        await ctx.channel.purge(limit=purge)
        msg = await ctx.send(embed=discord.Embed(title='Очистка', description=f'Было очищено {purge} сообщений'))
        await asyncio.sleep(5)
        await msg.delete()

    @cog_ext.cog_slash(name='clear', description='Чистит сообщения в чате')
    async def _clear(self, ctx :SlashContext, purge: int):
        await ctx.channel.purge(limit=purge)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, time: str, reason: str):
        muted_id = 904325649655803915
        mute_role = discord.utils.get(ctx.guild.roles, id = muted_id)
        await ctx.send(embed=discord.Embed(title='Мут', description=f'{member.mention} был замучен за {reason} на {time}'))
        await member.add_roles(mute_role)
        await asyncio.sleep(get_seconds(time))
        await member.remove_roles(mute_role)
        await ctx.send(embed=discord.Embed(title='Размут', description=f'{member.mention} был размучен'))
    
def setup(bot):
    bot.add_cog(Moderation(bot))