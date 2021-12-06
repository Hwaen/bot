import os
import discord
import asyncio
from dotenv import load_dotenv
from datetime import datetime

import Item
import Aug
import rank

#####토큰#####
load_dotenv()
token = os.getenv('token')

#####클라이언트#####
client = discord.Client()

#####시즌시간#####
now = datetime.now()
send = datetime(2022, 2, 3, 11) #시즌마다 바꿔줄 것
day = (send-now).days
hour = (send-now).seconds / 3600

#수식어
item = "?템"
aug = "?특성"
tier = "?전적"

####로딩####
@client.event
async def on_ready(): 
    print('------')
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + client.user.name)
    print("디스코드봇 ID:" + str(client.user.id))
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("베타버전 테스트"))

#####도움말#####
@client.event
async def on_message(message):
    if message.content=="?도움" or message.content=="?도움말":
        embed=discord.Embed(title="도움말", description="사용 가능한 명령어를 보여드립니다")
        embed.add_field(name="?도움", value="사용 가능한 명령어를 가져옵니다.", inline=False)
        embed.add_field(name="?템 (템이름)", value="아이템의 정보를 가져옵니다. EX)?템 낭아봉", inline=False)
        embed.add_field(name="~~?제작 (템이름)~~", value="~~아이템의 제작방법을 가져옵니다. EX)?제작 낭아봉~~", inline=False)
        embed.add_field(name="~~?스킬 (캐릭터 이름) (스킬키)~~", value="~~캐릭터의 스킬의정보를 가져옵니다. EX)?스킬 수아 Q~~", inline=False)
        embed.add_field(name="~~?무기스킬 (무기종류)~~", value="~~무기스킬의 정보를 가져옵니다. EX)?무기스킬 망치~~", inline=False)
        embed.add_field(name="?특성", value="특성의 종류와 설명을 가져옵니다. EX)특성 저항", inline=False)
        embed.add_field(name="~~?정보 (캐릭터이름)~~", value="~~캐릭터의 정보를 가져옵니다. EX)?정보 수아~~", inline=False)
        embed.add_field(name="?패치정보", value="현재 적용된 게임 패치 정보를 알려줍니다.", inline=False)
        embed.add_field(name="?시즌", value="시즌이 며칠 남았는지 알려줍니다.", inline=False)
        embed.set_footer(text="")
        await message.channel.send(embed=embed)
        
#####패치정보#####
    if message.content=="?패치정보" or message.content=="?패치":
       await message.channel.send("현재 시험중입니다.")
       
#####시즌#####    
    if message.content=="?시즌":
        embed=discord.Embed()
        embed.add_field(name="[시즌 4] ", value="%d일 %d시간 남았습니다." %(day,hour), inline=False)
        embed.set_footer(text="시즌 종료: 2022년 2월 3일",icon_url="https://aya.gg/media/images/ranks/GOLD_BALL.png")
        await message.channel.send(embed=embed)

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
        msg = message.content[4:]
        Aug.aug(msg)
        await message.channel.send(embed=Aug.aug(msg))


#####랭크#####
    if message.content.startswith(tier):
        msg = message.content[4:]
        rank.tier(msg)
        await message.channel.send(embed=rank.tier(msg))
    


##############
    else:
        return None

client.run(os.getenv("token"))
