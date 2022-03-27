"""
코드 작성 개시일자 2021년 10월 29일
리비전 0 가동 개시일자 2021년 10월 30일
물오주접방용 이미지 짤방 업로드 디스코드 봇

해야 하는 작업 : 2022년 4월 전에 다른 라이브러리로 교체하기 (PyCord, Discorpy 등)
"""

import os, json, discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

airo = commands.Bot(command_prefix='+', description='이미지 짤방이라면 저에게 맡겨주세요!', status=discord.Status.online, activity=discord.Game("이미지 정리"))
token = os.environ['token']
slash = SlashCommand(airo, sync_commands=True)
gid = [891712136689119242, 864146887627767858]


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
	guild_ids=gid
)
async def _mustmarry(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='mustmarry'))

#결혼식 초대짤
@slash.slash(
	name="결혼식",
	description="저.. 어머님 제가 어머님 자캐하고 결혼식을 하는데 참석해주세요",
	guild_ids=gid
)
async def _wantmarry(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='wantmarry'))

#월요일 싫어
@slash.slash(
	name="월요일",
	description="월요일.. 그것은 개쓰레기요일.",
	guild_ids=gid
)
async def _monday(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='whymonday'))

#출근 싫어
@slash.slash(
	name="출근싫어",
	description="출근 싫어 (드러눕)",
	guild_ids=gid
)
async def _nowork(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='nowork'))

#존나빠름
@slash.slash(
	name="존나빠름",
	description="I'm fast as fxxx boi, I'm fast as fxxx boi!!",
	guild_ids=gid
)
async def _fastasfuck(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='fastfox'))

#여우투광등
@slash.slash(
	name="여우찾기빔",
	description="그래서 이 분 어디로 가셨어요?",
	guild_ids=gid
)
async def _foxbeam(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='foxsearch'))

#드론 보노보노
@slash.slash(
	name="드론과제",
	description="왜 ㅈ같은 팀원들은 자기들만 바쁘다 생각할까? 한번 ㅈ되봐라지 난 휴학테크 탈 테니까",
	guild_ids=gid
)
async def _bonodrone(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='bonobono'))

#퇴근
@slash.slash(
	name="퇴근",
	description="퇴근퇴근퇴근퇴근퇴근퇴근퇴근퇴근퇴근퇴근제발퇴근퇴근퇴근",
	guild_ids=gid
)
async def _exitwork(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='endwork'))

#출근.. 해야.. 하는거야....?
@slash.slash(
	name="출근감자",
	description="출근.. 해야.. 하는거야...? (울먹)",
	guild_ids=gid
)
async def _whywork(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='whywork'))

#smol AO
@slash.slash(
	name="smol",
	description="작고 소듕하고 귀여운 아오",
	guild_ids=gid
)
async def _smol(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='aotiny'))

#게이사물의 향기~
@slash.slash(
	name="게이사물향",
	description="음~ 이것은 게이사물의 향기.",
	guild_ids=gid
)
async def _gsaroma(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='gsaroma'))

#트리플 :gaysamul:
@slash.slash(
	name="3게이사물",
	description=":gaysamulfox: :gaysamul: :gaysamuldrone:",
	guild_ids=gid
)
async def _3gsm(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='3gaysamul'))

#거기 집게리아죠?
@slash.slash(
	name="아뇨",
	description="아뇨, 드론인데요?",
	guild_ids=gid
)
async def _nodrone(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='nodrone'))

#드론프린터
@slash.slash(
	name="드론프린터",
	description="(게이사물 연성 출력 중)",
	guild_ids=gid
)
async def _droneprint(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='droneprint'))

#I EAT POTATO
@slash.slash(
	name="POTATO",
	description="I EAT POTATO",
	guild_ids=gid
)
async def _eatpotato(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='eatpotato'))

#부장님!
@slash.slash(
	name="부장님",
	description="부장님! 이게 말이 된다고 생각하십니까!",
	guild_ids=gid
)
async def _valentine(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='doorslayer'))

#유진 : (만족)
@slash.slash(
	name="유진만족",
	description="삭여라, 그리고 새겨라, 바꾸고 싶다면 사겨라. 돈과 명예, 그리고 사경이 제일인 세상이다.",
	guild_ids=gid
)
async def _boundaryofdeath(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='yujinhappy'))

#A토끼 뽀담뽀담
@slash.slash(
	name="토끼뽀담",
	description="토끼는 귀여워!",
	guild_ids=gid
)
async def _tokipet(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='tokipet'))

#여우도 뽀담뽀담
@slash.slash(
	name="여우뽀담",
	description="여우도 귀여워!",
	guild_ids=gid
)
async def _foxpet(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='foxpet'))

#딩깅
@slash.slash(
	name="띵킹",
	description="이게 맞나...? 아니 이게 맞나? 진짜? 장난 아니라?",
	guild_ids=gid
)
async def _thonk(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='thonk'))

#여우 헤드스핀
@slash.slash(
	name="헤드스핀",
	description="무야호!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
	guild_ids=gid
)
async def _headspin(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='headspin'))

#폴짝폴짝 뛰는 감자
@slash.slash(
	name="폴짝감자",
	description="갓캐를 보고 매우 행복해하며 폴짝폴짝 뛰는 감자라고라...!",
	guild_ids=gid
)
async def _happygamja(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='gamjahappy'))

#과제꺼져
@slash.slash(
	name="과제멈춰",
	description="뇌ㅈ... 아니, 과제 멈춰!",
	guild_ids=gid
)
async def _gwaje(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='gwaje'))
	
#(SNIVY)(BEAM)
@slash.slash(
	name="풀뱀빔",
	description="이런! 당신은 풀뱀빔에 맞았습니다! 주리비얀 귀엽다 를 30초안에 쓰지 않으면 주리비얀이 되어버립니다!",
	guild_ids=gid
)
async def _snivybeam(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='snivybeam'))

#풀뱀이 주거써!
@slash.slash(
	name="풀뱀기절",
	description="풀뱀이 주거써! 교수님이 주겨써!",
	guild_ids=gid
)
async def _snivydead(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='snivyded'))
	
#fuck im hungry
@slash.slash(
	name="광합성",
	description="fuck im hungry / delicious",
	guild_ids=gid
)
async def _pthungry(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='delicious'))
	
#피곤한 여우
@slash.slash(
	name="여우피곤",
	description="뭔가 그리곤 싶은데 피곤함",
	guild_ids=gid
)
async def _chitired(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='chiwant'))
	
#피곤한 감자
@slash.slash(
	name="감자피곤",
	description="뭔가 그리곤 싶은데 피곤함",
	guild_ids=gid
)
async def _pottired(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='ptwant'))

#감자가 주거써!
@slash.slash(
	name="흐어어억",
	description="퇴근시켜줘",
	guild_ids=gid
)
async def _ptdead(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='pttired'))
	
#깃허브 모나 귀여움
@slash.slash(
	name="모나",
	description="그냥 귀여워서 끼워넣은 깃허브 움짤",
	guild_ids=gid
)
async def _mona(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='mona'))

#깃허브 모나 귀여움
@slash.slash(
	name="치아라",
	description="안할끼다",
	guild_ids=gid
)
async def _fxxkit(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='fuckit'))

#많은 일이 있었지..
@slash.slash(
	name="많고많은일",
	description="나 너무많은일이 있었어... 힘들다진짜",
	guild_ids=gid
)
async def _lotwork(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='lotsof'))

#give me a whole tray of P E A S
@slash.slash(
	name="콩",
	description="Give me a whole tray of..... P E A S",
	guild_ids=gid
)
async def _peas(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='peas'))

#메랑지 뽀담뽀담...
@slash.slash(
	name="메랑지뽀담",
	description="싹난감ㅈ 아니 메랑지도 귀여워!",
	guild_ids=gid
)
async def _merangy(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='merangy'))

#(폴라 님 이 퇴장하섰습니다)
@slash.slash(
	name="폴라퇴장",
	description="퇴장이라기보다는 납치당하는 거 같음",
	guild_ids=gid
)
async def _pleave(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='polarout'))

#SMOL
@slash.slash(
	name="스몰드론",
	description="(장난 아니라 진짜 설정상 스몰하던 걸로 기억함)(그나마)",
	guild_ids=gid
)
async def _smool(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='smoldrone'))

#(still so fast as fxxk boiiiii)
@slash.slash(
	name="폴라쫓아옴",
	description="함!!!!! 잡솨봐!!!!!(superfast)",
	guild_ids=gid
)
async def _coming(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='speedpol'))

#굿바이(사라짐)
@slash.slash(
	name="폴라사라짐",
	description="원본 밈 영상 아시는 분 제보바람",
	guild_ids=gid
)
async def _pvan(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='polvanish'))
	
#불속성드론
@slash.slash(
	name="불속성드론",
	description="화르륵",
	guild_ids=gid
)
async def _pfire(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='firedrone'))

#납작드론
@slash.slash(
	name="납작드론",
	description="에잇 납작해져라!!! (폭*8)",
	guild_ids=gid
)
async def _napjak(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='napjak'))

#왜...?
@slash.slash(
	name="눈물젖은모닝빵",
	description="....왜?(눈물젖은모닝빵)",
	guild_ids=gid
)
async def _moning(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='why'))

#오늘도 아무것도 안했다 춤
@slash.slash(
	name="암것도안함",
	description="(오늘도 아무것도 안했다 춤)",
	guild_ids=gid
)
async def _lazy(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='lazydance'))

#셀프수확하는 감자
@slash.slash(
	name="셀프수확",
	description="내레이션 : 야생의 감자라고라는 갓캐를보면 셀프수확을 하는 습성이 있습니다",
	guild_ids=gid
)
async def _selfhavest(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='selfhav'))

#폼폼티콘! (선택형 명령어)
@slash.slash(
	name="폼폼",
	description="붕괴:스타레일의 귀여운 토끼(?) 차장 폼폼 이모티콘(무려 공식임)!",
	guild_ids=gid,
	options=[
		create_option(
			name="이모지",
			description="폼폼 이모지 종류를 선택해주세요!",
			option_type=3,
			required=True,
			choices=[
				create_choice(
					name="화남",
					value="angy"
				),
				create_choice(
					name="으쓱",
					value="hmm"
				),
				create_choice(
					name="메모",
					value="memo"
				),
				create_choice(
					name="하트",
					value="love"
				),
				create_choice(
					name="오케이",
					value="okay"
				),
				create_choice(
					name="선물",
					value="gift"
				),
				create_choice(
					name="슬픔",
					value="sad"
				)
			]
		)
	],
	connector={
		'이모지': 'emote'
	}
)
async def _pompom(ctx:SlashContext, emote:str):
	if emote == 'angy':
		pom_pom = embed_base(ctx=ctx, name='pp_angy')
	elif emote == 'hmm':
		pom_pom = embed_base(ctx=ctx, name='pp_hmm')
	elif emote == 'memo':
		pom_pom = embed_base(ctx=ctx, name='pp_memo')
	elif emote == 'love':
		pom_pom = embed_base(ctx=ctx, name='pp_love')
	elif emote == 'okay':
		pom_pom = embed_base(ctx=ctx, name='pp_ok')
	elif emote == 'gift':
		pom_pom = embed_base(ctx=ctx, name='pp_gift')
	elif emote == 'sad':
		pom_pom = embed_base(ctx=ctx, name='pp_sad')
	
	await ctx.send(embed=pom_pom)

#폴라 뽀담뽀담! (선택형 명령어)
@slash.slash(
	name="폴라뽀담",
	description="귀여운 왹져정찰드론을 뽀담뽀담해보세요!",
	guild_ids=gid,
	options=[
		create_option(
			name="속도",
			description="뽀담뽀담할 속도",
			option_type=3,
			required=False,
			choices=[
				create_choice(
					name="천천히",
					value="slow"
				),
				create_choice(
					name="빠르게",
					value="fast"
				)
			]
		)
	],
	connector={
		'속도': 'speed'
	}
)
async def _polarpet(ctx:SlashContext, speed:str='slow'):
	if speed == 'slow':
		pet_emb = embed_base(ctx=ctx, name='polarpet')
	elif speed == 'fast':
		pet_emb = embed_base(ctx=ctx, name='polarpetfast')
	
	await ctx.send(embed=pet_emb)

@slash.slash(
	name="히얼쓰",
	description="(문 부서지는 소리)",
	guild_ids=gid,
	options=[
		create_option(
			name="누구",
			description="(빼꼼)",
			option_type=3,
			required=True,
			choices=[
				create_choice(
					name="감자",
					value="potato"
				),
				create_choice(
					name="드론",
					value="drone"
				)
			]
		)
	],
	connector={
		'누구': 'who'
	}
)
async def _doorcrack(ctx:SlashContext, who:str):
	if who == 'potato':
		dooremb = embed_base(ctx=ctx, name='doorgamja')
	elif who == 'drone':
		dooremb = embed_base(ctx=ctx, name='doordrone')
	
	await ctx.send(embed=dooremb)

#저기 보세요, 야생의 드론이 방송을 기대하고 있군요
@slash.slash(
	name="기대만발",
	description="(대충 존1나게 방송을 기대하고 있는 폴라의 모습)",
	guild_ids=gid
)
async def _expectdrone(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='expectdrone'))

#저런, 오늘은 휴방이군요! 아니, 결방인가?
@slash.slash(
	name="결방",
	description="(대충 팝콘 바닥에 떨어지는 소리)",
	guild_ids=gid
)
async def _todayisrest(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='nobctoday'))

#주접참기
@slash.slash(
	name="주접참기",
	description="*i hav no speaker but i must squeal*",
	guild_ids=gid
)
async def _squeal(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='squeal'))

#가보자고
@slash.slash(
	name="ㄱㅂㅈㄱ",
	description="#ㄱㅂㅈㄱ",
	guild_ids=gid
)
async def _letsgoooo(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='YOLOOOOO'))

#아니 근데 진짜 왜 감자가 드론 스팽킹하는 짤이 왜 아니 스팽킹인가 모르겠다 ㅅㅂ
@slash.slash(
	name="찰삭찰삭",
	description="아니 진짜 주석에도 적었지만 이건 내가 뭐라고 표현해야 할지 모르겠다 찰지구나?",
	guild_ids=gid
)
async def _niceass(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='niceass'))

#이놈의 집구석(티로 꺼지면서 옮겨온 거)
@slash.slash(
	name="이놈의집구석",
	description="씨발 집구석 진짜 내가 진짜 짜증나는데 참는다 ㅅㅂ....",
	guild_ids=gid
)
async def _fuckthishouse(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='fth'))

#카토 씰룩짤이요? 이건 귀하군요
@slash.slash(
	name="카토댄스",
	description="우리 귀여운 커피톡기 카토 춤추는 것도 귀엽지 응응",
	guild_ids=gid
)
async def _catodance(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='catodance'))

#무기력의 댄스~ (but 감자)
@slash.slash(
	name="무기력감자",
	description="- 이 감자 죽었는데요? / - 안 죽었음 ㅇㅇ",
	guild_ids=gid
)
async def _noengamza(ctx:SlashContext):
	await ctx.send(embed=embed_base(ctx=ctx, name='gamjaknockdown'))

#인 제 인 남
@slash.slash(
        name="인제인남",
        description="인 제 인 남 (뭐 이거 맞잖아 설명이 이거밖에 없다고 뭐라하지마요)",
        guild_ids=gid
)
async def _justwokeup(ctx:SlashContext):
        await ctx.send(embed=embed_base(ctx=ctx, name='justwokeup'))

#-------------------코드의 끝----------------------
airo.run(token)

