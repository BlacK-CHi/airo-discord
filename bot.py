import os, json, discord
from discord.ext import commands
from discord_slash import SlashCommand

airo = discord.Client()
bot = commands.Bot(command_prefix='>>', description='!', status=discord.Status.online, activity=discord.Game(">>help로 도움말을 출력!"))
token = os.environ['token']
slash = SlashCommand(bot, sync_commands=True)

with open('imgres.json', 'r') as f:
    img_list = json.load(f)
    
@bot.event
async def on_ready():
    print("Ai-RO Bot Successfully Initiallized.")
    print(airo.user.name)
    print(airo.user.id)

@bot.command()
async def embed(ctx):
    embed = discord.Embed(title="sample embed", url="", description="봇에 임베드 삽입을 테스트 중입니다.", color=discord.Color.blue())
    await ctx.send(embed=embed)

@slash.slash(
    name="slash",
    description="simple slash test.",
    guild_ids=[865433697657946133]
)
async def command_slash(ctx):
    embed = discord.Embed(title="slash!", url="", description="testing slash..", color=discord.Color.blue())
    await ctx.send(embed=embed)

bot.run(token)

