#코드 작성 개시일자 2021년 10월 29일
#물오주접방용 이미지 짤방 업로드 디스코드 봇

import os, json, discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

airo = commands.Bot(command_prefix='+', description='Test', status=discord.Status.online, activity=discord.Game("Testing!"))
token = os.environ['token']
slash = SlashCommand(airo, sync_commands=True)
gid = 891712136689119242


#imgres.json 이미지파일 정보 데이터베이스 불러오기
#imgres.json에 쓸 수는 없음 (heroku에서 파일 액세스 제한됨) - Read-Only
with open('imgres.json', 'r') as f:
	img_list = json.load(f)
	print("[SYS] Image Database Successfully Loaded!")


#임베드 뼈대용 함수 (명령어 단계에서 호출됨)
def embed_base(ctx,name):
	embed = discord.Embed(color=discord.Color.blue())
	embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
	embed.set_image(url=img_list[name])   
	embed.set_footer(text="Ai-RO nightly1.0.30 Rev.0", icon_url="https://media.discordapp.net/attachments/882195139508989993/903823602498019368/1635558712041.png")   
	return embed


#봇 실행 시 행동 -> Heroku 로그콘솔에 정상작동 중이라는 메시지 표시.
@airo.event
async def on_ready():
	print("[SYS] Ai-RO Bot Successfully Initiallized.")

   
#여가서부터 명령어 작성하기!

#님캐결혼
@slash.slash(
	name="님캐결혼",
	description="님 캐. 나랑. 결혼.",
	guild_ids=[gid]
)
async def _mustmarry(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='mustmarry'))

#결혼식 초대짤
@slash.slash(
	name="결혼식",
	description="저.. 어머님 제가 어머님 자캐하고 결혼식을 하는데 참석해주세요",
	guild_ids=[gid]
)
async def _wantmarry(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='wantmarry'))

#월요일 싫어
@slash.slash(
	name="월요일",
	description="월요일.. 그것은 개쓰레기요일.",
	guild_ids=[gid]
)
async def _monday(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='whymonday'))

#출근 싫어
@slash.slash(
	name="출근싫어",
	description="출근 싫어 (드러눕)",
	guild_ids=[gid]
)
async def _nowork(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='nowork'))

#존나빠름
@slash.slash(
	name="존나빠름",
	description="I'm fast as fxxx boi, I'm fast as fxxx boi!!",
	guild_ids=[gid]
)
async def _fastasfuck(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='fastfox'))

#여우투광등
@slash.slash(
	name="여우찾기빔",
	description="그래서 이 분 어디로 가셨어요?",
	guild_ids=[gid]
)
async def _foxbeam(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='foxsearch'))

#드론 보노보노
@slash.slash(
	name="드론과제",
	description="왜 ㅈ같은 팀원들은 자기들만 바쁘다 생각할까? 한번 ㅈ되봐라지 난 휴학테크 탈 테니까",
	guild_ids=[gid]
)
async def _bonodrone(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='bonobono'))

#감자 도어슬램
@slash.slash(
	name="문부숨",
	description="안나오면 쳐들어간다 (쿵짝짝쿵짝)",
	guild_ids=[gid]
)
async def _doorslam(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='doorgamja'))

#퇴근
@slash.slash(
	name="퇴근",
	description="퇴근퇴근퇴근퇴근퇴근퇴근퇴근퇴근퇴근퇴근제발퇴근퇴근퇴근",
	guild_ids=[gid]
)
async def _exitwork(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='endwork'))

#출근.. 해야.. 하는거야....?
@slash.slash(
	name="출근감자",
	description="출근.. 해야.. 하는거야...? (울먹)",
	guild_ids=[gid]
)
async def _whywork(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='whywork'))

#smol AO
@slash.slash(
	name="smol",
	description="작고 소듕하고 귀여운 아오",
	guild_ids=[gid]
)
async def _smol(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='aotiny'))

#게이사물의 향기~
@slash.slash(
	name="게이사물향",
	description="음~ 이것은 게이사물의 향기.",
	guild_ids=[gid]
)
async def _gsaroma(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='gsaroma'))

#트리플 :gaysamul:
@slash.slash(
	name="3게이사물",
	description=":gaysamulfox: :gaysamul: :gaysamuldrone:",
	guild_ids=[gid]
)
async def _3gsm(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='3gaysamul'))

#거기 집게리아죠?
@slash.slash(
	name="아뇨",
	description="아뇨, 드론인데요?",
	guild_ids=[gid]
)
async def _nodrone(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='nodrone'))

#드론프린터
@slash.slash(
	name="드론프린터",
	description="(게이사물 연성 출력 중)",
	guild_ids=[gid]
)
async def _droneprint(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='droneprint'))

#I EAT POTATO
@slash.slash(
	name="POTATO",
	description="I EAT POTATO",
	guild_ids=[gid]
)
async def _eatpotato(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='eatpotato'))

#부장님!
@slash.slash(
	name="부장님",
	description="부장님! 이게 말이 된다고 생각하십니까!",
	guild_ids=[gid]
)
async def _bonodrone(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='doorslayer'))


#-------------------코드의 끝----------------------
airo.run(token)

