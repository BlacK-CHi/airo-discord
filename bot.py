import os, json, discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash,.utils.manage_commands import create_choice, create_option

airo = commands.Bot(command_prefix='+', description='Test', status=discord.Status.online, activity=discord.Game("Testing!"))
token = os.environ['token']
slash = SlashCommand(airo, sync_commands=True)

with open('imgres.json', 'r') as f:
    img_list = json.load(f)
    print("[SYS] Image Database Successfully Loaded!")
    
@airo.event
async def on_ready():
    print("[SYS] Ai-RO Bot Successfully Initiallized.")

@airo.command()
async def embed(ctx):
    embed = discord.Embed(title="sample embed", url="", description="봇에 임베드 삽입을 테스트 중입니다.", color=discord.Color.blue())
    await ctx.send(embed=embed)

@slash.slash(
    name="slash",
    description="simple slash test.",
    guild_ids=[865433697657946133]
)
async def command_slash(ctx:SlashContext):
    embed = discord.Embed(title="slash!", url="", description="testing slash..", color=discord.Color.blue())
    await ctx.send(embed=embed)



airo.run(token)

