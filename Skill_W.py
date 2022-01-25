import discord
import asyncio
import pandas as pd

code = {'단검' : 0,
        '양손검' : 1,
        '도끼' : 2,
        '쌍검' : 3,
        '권총' : 4,
        '돌격소총' : 5,
        '저격총' : 6,
        '글러브' : 7,
        '톤파' : 8,
        '방망이' : 9,
        '망치' : 10,
        '활' : 11,
        '석궁' : 12,
        '레이피어' : 13,
        '창' : 14,
        '투척' : 15,
        '암기': 16,
        '기타' : 17,
        '쌍절곤' : 18,
        '채찍' : 19,
        '카메라' : 20,
        '아르카나' : 21,
        'VF의수' :22}

###무기스킬###
def skill_w(msg):
    data = pd.read_csv(r"waepon_skill.CSV",encoding='cp949')
    num = code[msg]    

    weapon = data.iloc[num]["종류"]
    name = data.iloc[num]["이름"]
    time1 = data.iloc[num]["쿨다운1"]
    time2 = data.iloc[num]["쿨다운2"]
    des1 = data.iloc[num]["설명1"]
    des2 = data.iloc[num]["설명2"]
    cha = data.iloc[num]["캐릭터"]
    img_url = data.iloc[num]["사진"]
       

    embed=discord.Embed(description="**1레벨**`쿨다운:"+time1+"`\n ```"+des1+"```\n**2레벨**`쿨다운:"+time2+"`\n```"+des2+"``` \n")
    embed.set_author(name=name, icon_url=img_url)
    embed.set_footer(text="사용 가능 캐릭터:\t " + cha)
    return embed


