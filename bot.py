#코드 작성 개시일자 2021년 10월 29일
#물오주접방용 이미지 짤방 업로드 디스코드 봇

import os, json, discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

airo = commands.Bot(command_prefix='+', description='이미지 짤방이라면 저에게 맡겨주세요!', status=discord.Status.online, activity=discord.Game("이미지 정리"))
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
async def _valentine(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='doorslayer'))

#유진 : (만족)
@slash.slash(
	name="유진만족",
	description="삭여라, 그리고 새겨라, 바꾸고 싶다면 사겨라. 돈과 명예, 그리고 사경이 제일인 세상이다.",
	guild_ids=[gid]
)
async def _boundaryofdeath(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='yujinhappy'))

#A토끼 뽀담뽀담
@slash.slash(
	name="토끼뽀담",
	description="토끼는 귀여워!",
	guild_ids=[gid]
)
async def _tokipet(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='tokipet'))

#여우도 뽀담뽀담
@slash.slash(
	name="여우뽀담",
	description="여우도 귀여워!",
	guild_ids=[gid]
)
async def _foxpet(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='foxpet'))

#딩깅
@slash.slash(
	name="띵킹",
	description="이게 맞나...? 아니 이게 맞나? 진짜? 장난 아니라?",
	guild_ids=[gid]
)
async def _thonk(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='thonk'))

#여우 헤드스핀
@slash.slash(
	name="헤드스핀",
	description="무야호!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
	guild_ids=[gid]
)
async def _headspin(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='headspin'))

#폴짝폴짝 뛰는 감자
@slash.slash(
	name="폴짝감자",
	description="갓캐를 보고 매우 행복해하며 폴짝폴짝 뛰는 감자라고라...!",
	guild_ids=[gid]
)
async def _happygamja(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='gamjahappy'))

#과제꺼져
@slash.slash(
	name="과제멈춰",
	description="뇌ㅈ... 아니, 과제 멈춰!",
	guild_ids=[gid]
)
async def _gwaje(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='gwaje'))
	
#(SNIVY)(BEAM)
@slash.slash(
	name="풀뱀빔",
	description="이런! 당신은 풀뱀빔에 맞았습니다! 주리비얀 귀엽다 를 30초안에 쓰지 않으면 주리비얀이 되어버립니다!",
	guild_ids=[gid]
)
async def _snivybeam(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='snivybeam'))

#풀뱀이 주거써!
@slash.slash(
	name="풀뱀기절",
	description="풀뱀이 주거써! 교수님이 주겨써!",
	guild_ids=[gid]
)
async def _snivydead(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='snivyded'))
	
#fuck im hungry
@slash.slash(
	name="광합성",
	description="fuck im hungry / delicious",
	guild_ids=[gid]
)
async def _pthungry(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='delicious'))
	
#피곤한 여우
@slash.slash(
	name="여우피곤",
	description="뭔가 그리곤 싶은데 피곤함",
	guild_ids=[gid]
)
async def _chitired(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='chiwant'))
	
#피곤한 감자
@slash.slash(
	name="감자피곤",
	description="뭔가 그리곤 싶은데 피곤함",
	guild_ids=[gid]
)
async def _pottired(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='ptwant'))

#감자가 주거써!
@slash.slash(
	name="흐어어억",
	description="퇴근시켜줘",
	guild_ids=[gid]
)
async def _ptdead(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='pttired'))
	
#깃허브 모나 귀여움
@slash.slash(
	name="모나",
	description="그냥 귀여워서 끼워넣은 깃허브 움짤",
	guild_ids=[gid]
)
async def _mona(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='mona'))

#폴라 뽀담뽀담 *아마 제일 복잡한 명령어일 듯?*
'''
@slash.slash(
	name="폴라뽀담",
	description="귀여운 왹져드론을 뽀담뽀담해보세요 함잡솨봐",
	options=[
		create_option( #뽀담뽀담 속도를 정하는 선택지를 만든다.
			name="속도",
			description="뽀담뽀담 속도!",
			option_type=3,
			required=False,
			choices=[
				create_choice(
					name='천천히', #기본값
					value='slow'
				),
				create_choice(
					name='빠르게',
					value='fast'
				)
			]
		)
	],
	connector={
		'속도': 'speed' #속도로 받은 value값을 speed라는 변수로 처리해야 명령어에서 받을 수 있음!
	}
)
async def _polarpet(ctx:SlashContext, speed:str='slow'): #speed의 기본값을 slow로 설정해서, 아무 인자를 넣지 않아도 자동으로 천천히 뽀담뽀담
	if speed == 'slow':
		await ctx.send(embed=embed_base(ctx=ctx, name='polarpet')
	elif speed == 'fast':
		await ctx.send(embed=embed_base(ctx=ctx, name='polarpetfast')
	else:
		embed = discord.Embed(title='오류', description='정의되지 않은 명령어에요!', color=discord.Color.red())
		embed.set_footer(text="Ai-RO nightly1.0.30 Rev.0", icon_url="https://media.discordapp.net/attachments/882195139508989993/903823602498019368/1635558712041.png")
		await ctx.send(embed=embed)
'''
		
#-------------------코드의 끝----------------------
airo.run(token)

