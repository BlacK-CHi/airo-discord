import os, json, discord
from discord.ext import commands

airo = discord.Client()
bot = commands.Bot(command_prefix='-')
token = os.environ['token']

with open('imgres.json', 'r') as f:
    img_list = json.load(f)
    
@bot.event
async def on_ready():
    await airo.change_presence(status=discord.Status.online, activity=discord.Game("-help"))
    print("봇 실행됨!")
    print(client.user.name)
    print(client.user.id)

@bot.command()
async def embed(ctx):
    embed = discord.Embed(title="sample embed", url="", description="봇에 임베드 삽입을 테스트 중입니다.", color=discord.Color.blue())
    await ctx.send(embed=embed)

bot.run(token)

