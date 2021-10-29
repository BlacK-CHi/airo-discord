
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>>', description='생일을 관리하고 자동으로 축하해드리는 봇이에요!', status=discord.Status.online, activity=discord.Game(">>help로 도움말을 출력!"))
token = "ODkzNDg2MTY3NTE1ODczMzQx.YVcJ1g.5KSMHnraMGWQDkLXYozzVPG2D_A"

@bot.command(aliases=['임베드'])
async def embed(ctx):
    embed = discord.Embed(title="sample embed", url="", description="봇에 임베드 삽입을 테스트 중입니다.", color=discord.Color.blue())

client.run(token)

