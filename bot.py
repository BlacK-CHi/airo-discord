import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-', status=discord.Status.online, activity=discord.Game("-help로 도움말을 출력!"))
token = os.environ['token']

@bot.command()
async def embed(ctx):
    embed = discord.Embed(title="sample embed", url="", description="봇에 임베드 삽입을 테스트 중입니다.", color=discord.Color.blue())
    await message.channel.send(embed=embed)

bot.run(token)

