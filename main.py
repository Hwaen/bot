import os
import discord
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
client = discord.Client()

#####시즌시간#####
tz = pytz.timezone('Asia/Seoul')
now = datetime.now(tz)
send = datetime(2022, 2, 17, 11, 0, 0, 0, tz) #시즌마다 바꿔줄 것

time = send - now
day = time.days
hour = time.seconds/3600

#####수식어#####
item = "?템"
aug = "?특"
tier = "?랭크"
skill = "?스킬"
skill_w = "?무스"


#####로딩#####
@client.event
async def on_ready(): 
    print('------')
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + client.user.name)
    print("디스코드봇 ID:" + str(client.user.id))
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("'?도움말' 을 쳐보세요"))

    guild_list = client.guilds
    for i in guild_list:
            print("서버 ID: {} / 서버 이름: {}".format(i.id, i.name))

    print("현재 들어가있는 서버 수")
    print(len(guild_list))

#####도움말#####
@client.event
async def on_message(message):
    global msg
    if message.content=="?도움" or message.content=="?도움말":
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
        await message.channel.send(embed=embed)
        
     
#####시즌#####    
    if message.content=="?시즌":
        embed=discord.Embed(title="[시즌 5]", description="%d일 %d시간 남았습니다." %(day,hour))
        embed.set_footer(text="시즌 시작: 2022년 2월 17일",icon_url="https://aya.gg/media/images/ranks/GOLD_BALL.png")
        await message.channel.send(embed=embed)
        
#####곰 가챠##### 
    if message.content == "?곰":
        bear = ["강철","기름먹인 천","뜨거운 오일","방전 전지","백색 가루","재","전자 부품","정교한 도면","철판","황금","달궈진 돌멩이","철사","루비","하드커버","생명의나무","운석","독약","모터","미스릴","유리판","이온전지","휴대폰","VF혈액샘플","포스코어"]
        gacha = random.choice(bear)
        await message.reply("[%s] 나왔습니다!" %gacha)
        return 

#####아이템#####
    if message.content.startswith(item):
        msg = message.content[3:]
        msg_out = ""

        for i in range(0,len(msg)):
            if msg[i]!=' ':
                msg_out+=msg[i]

        Item.Weapon(msg_out)
        await message.channel.send(embed=Item.Weapon(msg_out))

#####특성#####
    if message.content.startswith(aug):
        msg = message.content[3:]
        msg_out = ""

        for i in range(0,len(msg)):
            if msg[i]!=' ':
                msg_out+=msg[i]
                
        Aug.aug(msg_out)
        await message.channel.send(embed=Aug.aug(msg_out))

#####랭크#####
    if message.content.startswith(tier):
        msg = message.content[4:]
        Rank.tier(msg)
        await message.channel.send(embed=Rank.tier(msg))

#####무기스킬#####
    if message.content.startswith(skill_w):
        msg = message.content[4:]
        await message.channel.send(embed=Skill_W.skill_w(msg))

        
#####스킬#####
    global emo
    if message.content.startswith(skill):
        msg = message.content[4:].split()
        if msg[0] == "알렉스" or msg[0] =="실비아":
            Skill_C2.skill(msg[0],msg[1])
            emo = await message.channel.send(embed=Skill_C2.skill(msg[0],msg[1]))

        if msg[0] == "에이든":
            Skill_C3.skill(msg[0],msg[1])
            emo = await message.channel.send(embed=Skill_C3.skill(msg[0],msg[1]))

        if msg[0] == "에키온":
            Skill_C4.skill(msg[0],msg[1])
            emo = await message.channel.send(embed=Skill_C4.skill(msg[0],msg[1]))
            
        else:            
            Skill_C1.skill(msg[0],msg[1])
            emo = await message.channel.send(embed=Skill_C1.skill(msg[0],msg[1]))
            
        await emo.add_reaction("1️⃣")
        await emo.add_reaction("2️⃣")
        await emo.add_reaction("3️⃣")
        await emo.add_reaction("4️⃣")
        await emo.add_reaction("5️⃣")

@client.event
async def on_reaction_add(reaction, user):
    if user.bot == 1: 
            return None
### 1레벨                                                                
    if reaction.message.id == emo.id and str(reaction.emoji) == "1️⃣":
        if msg[0] == "알렉스"or msg[0] =="실비아":
            Skill_C2.skill_1(msg[1])
            await emo.edit(embed=Skill_C2.skill_1(msg[1]))
            await emo.remove_reaction("1️⃣",user)

        if msg[0] == "에이든":
            Skill_C3.skill_1(msg[1])
            await emo.edit(embed=Skill_C3.skill_1(msg[1]))
            await emo.remove_reaction("1️⃣",user)

        if msg[0] == "에키온":
            Skill_C4.skill_1(msg[1])
            await emo.edit(embed=Skill_C4.skill_1(msg[1]))
            await emo.remove_reaction("1️⃣",user)
            
        else:    
            Skill_C1.skill_1(msg[1])
            await emo.edit(embed=Skill_C1.skill_1(msg[1]))        
            await emo.remove_reaction("1️⃣",user)
            
### 2레벨                                                                                 
    if reaction.message.id == emo.id and str(reaction.emoji) == "2️⃣":
        if msg[0] == "알렉스"or msg[0] =="실비아":
            Skill_C2.skill_1(msg[1])
            await emo.edit(embed=Skill_C2.skill_2(msg[1]))
            await emo.remove_reaction("2️⃣",user)

        if msg[0] == "에이든":
            Skill_C3.skill_2(msg[1])
            await emo.edit(embed=Skill_C3.skill_2(msg[1]))
            await emo.remove_reaction("2️⃣",user)

        if msg[0] == "에키온":
            Skill_C4.skill_2(msg[1])
            await emo.edit(embed=Skill_C4.skill_2(msg[1]))
            await emo.remove_reaction("2️⃣",user)
            
        else:
            Skill_C1.skill_2(msg[1])
            await emo.edit(embed=Skill_C1.skill_2(msg[1]))
            await emo.remove_reaction("2️⃣",user)
            
### 3레벨                                                                                        
    if reaction.message.id == emo.id and str(reaction.emoji) == "3️⃣":
        if msg[0] == "알렉스"or msg[0] =="실비아":
            Skill_C2.skill_1(msg[1])
            await emo.edit(embed=Skill_C2.skill_3(msg[1]))
            await emo.remove_reaction("3️⃣",user)

        if msg[0] == "에이든":
            Skill_C3.skill_3(msg[1])
            await emo.edit(embed=Skill_C3.skill_3(msg[1]))
            await emo.remove_reaction("2️⃣",user)

        if msg[0] == "에키온":
            Skill_C4.skill_3(msg[1])
            await emo.edit(embed=Skill_C4.skill_3(msg[1]))
            await emo.remove_reaction("3️⃣",user)            

        else:
            Skill_C1.skill_3(msg[1])
            await emo.edit(embed=Skill_C1.skill_3(msg[1]))
            await emo.remove_reaction("3️⃣",user)

### 4레벨                                                                
    if reaction.message.id == emo.id and str(reaction.emoji) == "4️⃣":
        if msg[0] == "알렉스" or msg[0] =="실비아":
            Skill_C2.skill_1(msg[1])
            await emo.edit(embed=Skill_C2.skill_4(msg[1]))
            await emo.remove_reaction("4️⃣",user)

        if msg[0] == "에이든":
            Skill_C3.skill_4(msg[1])
            await emo.edit(embed=Skill_C3.skill_4(msg[1]))
            await emo.remove_reaction("4️⃣",user)

        if msg[0] == "에키온":
            Skill_C4.skill_4(msg[1])
            await emo.edit(embed=Skill_C4.skill_4(msg[1]))
            await emo.remove_reaction("4️⃣",user)

        else:    
            Skill_C1.skill_4(msg[1])
            await emo.edit(embed=Skill_C1.skill_4(msg[1]))
            await emo.remove_reaction("4️⃣",user)
    
### 5레벨                                                                                        
    if reaction.message.id == emo.id and str(reaction.emoji) == "5️⃣":
        if msg[0] == "알렉스" or msg[0] =="실비아":
            Skill_C2.skill_1(msg[1])
            await emo.edit(embed=Skill_C2.skill_5(msg[1]))
            await emo.remove_reaction("5️⃣",user)

        if msg[0] == "에이든":
            Skill_C3.skill_5(msg[1])
            await emo.edit(embed=Skill_C3.skill_5(msg[1]))
            await emo.remove_reaction("5️⃣",user)

        if msg[0] == "에키온":
            Skill_C4.skill_5(msg[1])
            await emo.edit(embed=Skill_C4.skill_4(msg[1]))
            await emo.remove_reaction("5️⃣",user)

        else:    
            Skill_C1.skill_5(msg[1])
            await emo.edit(embed=Skill_C1.skill_5(msg[1]))
            await emo.remove_reaction("5️⃣",user)

##############
    else:
        return None

client.run(os.getenv("token"))
