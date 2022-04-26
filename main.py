import os
import discord
from discord.ext import commands
from discord.commands import Option
import asyncio
from dotenv import load_dotenv
import time
from datetime import datetime
import pytz
import random

import Item
import Aug
import Rank
import Skill_C1
import Skill_C2
import Skill_C3
import Skill_C4
import Skill_W



#####토큰#####
load_dotenv()
token = os.getenv('token')

#####클라이언트#####
intents = discord.Intents().all()
intents.members = True
bot = discord.Bot()
command = commands.Bot(command_prefix='?', intents = intents)

#####로딩#####
@bot.event
async def on_ready(): 
    print('------')
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + bot.user.name)
    print("디스코드봇 ID:" + str(bot.user.id))
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("'?도움' 을 쳐보세요"))

    guild_list = bot.guilds
    for i in guild_list:
            print("서버 ID: {} / 서버 이름: {}".format(i.id, i.name))

    print("현재 들어가있는 서버 수")
    print(len(guild_list))

#########################################커맨드###########################################

######################################슬래시 커맨드########################################
#####도움말#####
@bot.slash_command(description="사용 가능한 명령어를 보여드립니다")
async def 도움(ctx):
    embed=discord.Embed(title="도움말", description="사용 가능한 명령어를 보여드립니다")
    embed.add_field(name="?도움", value="사용 가능한 명령어를 가져옵니다.", inline=False)
    embed.add_field(name="?템 <템이름>", value="아이템의 정보를 가져옵니다. `EX)?템 낭아봉`", inline=False)
    embed.add_field(name="?스킬 <캐릭터> <스킬키>", value="캐릭터의 스킬의정보를 가져옵니다. `EX)?스킬 수아 Q`", inline=False)
    embed.add_field(name="?무스 <무기종류>", value="무기스킬의 정보를 가져옵니다. `EX)?무스 망치`", inline=False)
    embed.add_field(name="?특", value="특성의 종류와 설명을 가져옵니다. `EX)?특 저항`", inline=False)
    embed.add_field(name="?랭크", value="현재 시즌의 랭크를 알려줍니다. `EX)?랭크 <닉네임>`", inline=False)
    embed.add_field(name="?시즌", value="시즌이 며칠 남았는지 알려줍니다.", inline=False)
    embed.add_field(name="?곰", value="곰이 당신에게 선물을 줍니다.", inline=False)
    embed.set_footer(text="문의: 화엔#9112")
    await ctx.send(embed=embed)

@bot.slash_command(description="핑 체크합니다.")
async def 핑(ctx):
    embed = discord.Embed(title="퐁!", description=f"Delay: {bot.latency} seconds", color=0xFFFFFF)
    await ctx.respond(embed=embed)
        
     
#####시즌#####    
@bot.slash_command(description="시즌이 며칠 남았는지 알려줍니다.")
async def 시즌(ctx):
    tz = pytz.timezone('Asia/Seoul')
    now = datetime.now(tz)
    send = datetime(2022, 5, 12, 11, 0, 0, 0, tz) #시즌마다 바꿔줄 것

    time = send - now
    day = time.days
    hour = time.seconds/3600
    
    embed=discord.Embed(title="[시즌 5] - 사냥", description="{0}일 {1:.0f}시간 남았습니다.".format(day,hour))
    embed.set_footer(text="시즌 종료: 2022년 5월 12일",icon_url="https://aya.gg/media/images/ranks/GOLD_BALL.png")
    await ctx.respond(embed=embed)
    

#####곰 가챠##### 
@bot.slash_command(description="곰이 당신에게 선물을 줍니다.")
async def 곰(ctx):
    bear = ["강철","기름먹인 천","뜨거운 오일","방전 전지","백색 가루","재","전자 부품","정교한 도면","철판","황금","달궈진 돌멩이","철사","루비","하드커버","생명의나무","운석","독약","모터","미스릴","유리판","이온전지","휴대폰","VF혈액샘플","포스코어"]
    gacha = random.choice(bear)
    await ctx.respond(f"[{gacha}] 나왔습니다!")
    return


#####아이템#####
@bot.slash_command(description="아이템의 정보를 가져옵니다.")
async def 템(ctx, 아이템: str):

    msg_out = ""
    for i in range(0,len(아이템)):
        if 아이템[i]!=' ':
            msg_out+=아이템[i]
            
    Item.Weapon(msg_out)
    await ctx.respond(embed=Item.Weapon(msg_out))

#####특성#####
@bot.slash_command(description="특성의 종류와 설명을 가져옵니다.")
async def 특성(ctx, 특성: str):
    msg_out = ""
    for i in range(0,len(특성)):
        if 특성[i]!=' ':
            msg_out+=특성[i]
    Aug.aug(msg_out)
    await ctx.respond(embed=Aug.aug(msg_out))
    
#####랭크#####
@bot.slash_command(description="현재 시즌의 티어를 알려줍니다.")
async def 랭크(ctx, 닉네임: str):
    Rank.tier(닉네임)
    await ctx.respond(embed=Rank.tier(닉네임))

#####무기스킬#####
@bot.slash_command(description="무기스킬의 정보를 가져옵니다.")
async def 무스(ctx, 무기: str):
    await ctx.respond(embed=Skill_W.skill_w(무기))

  
#####스킬#####
@bot.slash_command(description="캐릭터의 스킬의정보를 가져옵니다.")
async def 스킬(ctx: discord.ApplicationContext,
             캐릭터: Option(str, "캐릭터 이름을 적어주세요."),
             스킬키: Option(str,"스킬키를 선택하세요", choices=["Q", "W", "E", "R", "T"])):

    name = 캐릭터
    key = 스킬키
    class Button(discord.ui.View):
        @discord.ui.button(label="1", style=discord.ButtonStyle.gray)
        async def one(self, button: discord.ui.Button, interaction: discord.Interaction):
            if name == "알렉스"or name =="실비아":
                Skill_C2.skill_1(key)
                await edit.edit_original_message(embed=Skill_C2.skill_1(key))
                    
            if name == "에이든":
                Skill_C3.skill_1(key)
                await edit.edit_original_message(embed=Skill_C3.skill_1(key))
                    
            if name == "에키온":
                Skill_C4.skill_1(key)
                await edit.edit_original_message(embed=Skill_C4.skill_1(key))                   
                
            else:    
                Skill_C1.skill_1(key)
                await edit.edit_original_message(embed=Skill_C1.skill_1(key))        
                    
        
        @discord.ui.button(label="2", style=discord.ButtonStyle.gray)
        async def two(self, button: discord.ui.Button, interaction: discord.Interaction):
            if name == "알렉스"or name =="실비아":
                Skill_C2.skill_2(key)
                await edit.edit_original_message(embed=Skill_C2.skill_2(key))            

            if name == "에이든":
                Skill_C3.skill_2(key)
                await edit.edit_original_message(embed=Skill_C3.skill_2(key))
            
            if name == "에키온":
                Skill_C4.skill_2(key)
                await edit.edit_original_message(embed=Skill_C4.skill_2(key))                  
                
            else:
                Skill_C1.skill_2(key)
                await edit.edit_original_message(embed=Skill_C1.skill_2(key), view=Button())
                

        @discord.ui.button(label="3", style=discord.ButtonStyle.gray)
        async def three(self, button: discord.ui.Button, interaction: discord.Interaction):
            if name == "알렉스"or name =="실비아":
                Skill_C2.skill_1(key)
                await edit.edit_original_message(embed=Skill_C2.skill_3(key))
                    
            if name == "에이든":
                Skill_C3.skill_1(key)
                await edit.edit_original_message(embed=Skill_C3.skill_3(key))
                    
            if name == "에키온":
                Skill_C4.skill_1(key)
                await edit.edit_original_message(embed=Skill_C4.skill_3(key))                   
                
            else:    
                Skill_C1.skill_1(key)
                await edit.edit_original_message(embed=Skill_C1.skill_3(key))       
            

        @discord.ui.button(label="4", style=discord.ButtonStyle.gray)
        async def four(self, button: discord.ui.Button, interaction: discord.Interaction):
            if name == "알렉스"or name =="실비아":
                Skill_C2.skill_1(key)
                await edit.edit_original_message(embed=Skill_C2.skill_4(key))
                    
            if name == "에이든":
                Skill_C3.skill_1(key)
                await edit.edit_original_message(embed=Skill_C3.skill_4(key))
                    
            if name == "에키온":
                Skill_C4.skill_1(key)
                await edit.edit_original_message(embed=Skill_C4.skill_4(key))                   
                
            else:    
                Skill_C1.skill_1(key)
                await edit.edit_original_message(embed=Skill_C1.skill_4(key))       
           
        @discord.ui.button(label="5", style=discord.ButtonStyle.gray)
        async def five(self, button: discord.ui.Button, interaction: discord.Interaction):
            if name == "알렉스"or name =="실비아":
                Skill_C2.skill_1(key)
                await edit.edit_original_message(embed=Skill_C2.skill_5(key))
                    
            if name == "에이든":
                Skill_C3.skill_1(key)
                await edit.edit_original_message(embed=Skill_C3.skill_5(key))
                    
            if name == "에키온":
                Skill_C4.skill_1(key)
                await edit.edit_original_message(embed=Skill_C4.skill_5(key))                   
                
            else:    
                Skill_C1.skill_1(key)
                await edit.edit_original_message(embed=Skill_C1.skill_5(key))         
                        
    try:
        if name == '알렉스' or name == '실비아':
            Skill_C2.skill(name,key)
            edit = await ctx.respond(embed=Skill_C2.skill(name,key), view=Button())

        elif name == '에이든':
            Skill_C3.skill(name,key)
            edit = await ctx.respond(embed=Skill_C3.skill(name,key), view=Button())

        elif name == '에키온':
            Skill_C4.skill(name,key)
            edit = await ctx.respond(embed=Skill_C4.skill(name,key), view=Button())

        else:            
            Skill_C1.skill(name,key)
            edit = await ctx.respond(embed=Skill_C1.skill(name,key), view=Button())
            
    except :
        embed=discord.Embed(title="오류!", color=0xffbb00)
        embed.add_field(name="<캐릭터> <스킬키> 를 제대로 입력해주세요!", value="/스킬 캐릭터: 수아 스킬키:T", inline=True)
        await ctx.respond(embed=embed, ephemeral=True)


         
bot.run(token)
