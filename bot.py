import os, json, discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

airo = commands.Bot(command_prefix='+', description='Test', status=discord.Status.online, activity=discord.Game("Testing!"))
token = os.environ['token']
slash = SlashCommand(airo, sync_commands=True)
gid = 865433697657946133

with open('imgres.json', 'r') as f:
    img_list = json.load(f)
    print("[SYS] Image Database Successfully Loaded!")

def embed_base(name):
    embed = discord.Embed(title=name, color=discord.Color.blue())
    embed.set_footer(text="하단 설명")
    return embed

@airo.event
async def on_ready():
    print("[SYS] Ai-RO Bot Successfully Initiallized.")


@slash.slash(
    name="slash",
    description="simple slash test.",
    guild_ids=[gid]
)
async def command_slash(ctx:SlashContext):
    embed = discord.Embed(title="slash!", url="", description="testing slash..", color=discord.Color.blue())
    embed.set_footer(text="하단 설명")
    await ctx.send(embed=embed)
    
@slash.slash(
    name="aaa",
    description="simple slash test.",
    guild_ids=[gid]
)
async def _aaa(ctx:SlashContext, embed_base, embedded):
    await ctx.send(embed=embed_base(name='foo'))




airo.run(token)

