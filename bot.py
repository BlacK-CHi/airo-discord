#코드 작성 개시일자 2021년 10월 29일
#물오주접방용 이미지 짤방 업로드 디스코드 봇

import os, json, discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

airo = commands.Bot(command_prefix='+', description='Test', status=discord.Status.online, activity=discord.Game("Testing!"))
token = os.environ['token']
slash = SlashCommand(airo, sync_commands=True)
gid = 865433697657946133 #테스트용 채널


#imgres.json 이미지파일 정보 데이터베이스 불러오기
#imgres.json에 쓸 수는 없음 (heroku에서 파일 액세스 제한됨) - Read-Only
with open('imgres.json', 'r') as f:
    img_list = json.load(f)
    print("[SYS] Image Database Successfully Loaded!")


#임베드 뼈대용 함수 (명령어 단계에서 호출됨)
def embed_base(name):
    embed = discord.Embed(title=name, color=discord.Color.blue())
    embed.set_footer(text="하단 설명")
    return embed


#봇 실행 시 행동 -> Heroku 로그콘솔에 정상작동 중이라는 메시지 표시.
@airo.event
async def on_ready():
    print("[SYS] Ai-RO Bot Successfully Initiallized.")

   
#여가서부터 명령어 작성하기!
@slash.slash(
    name="aaa",
    description="simple slash test.",
    guild_ids=[gid]
)
async def _aaa(ctx:SlashContext):
    await ctx.send(embed=embed_base(name='foo'))

#-------------------코드의 끝----------------------
airo.run(token) #봇 실행(env에서 토큰 전달)

