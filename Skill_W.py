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

    if msg =="단검":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569661077225483/01._Dagger.png"
        
    if msg =="양손검":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569661383393310/02._Two-Handed_Sword.png"        

    if msg =="도끼":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569661681197116/03._Axe.png"

    if msg =="쌍검":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569662033526804/04._Dual_Swords.png"

    if msg =="권총":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569662398414868/05._Pistol.png"
        
    if msg =="돌격소총":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569662683631666/06._Assault_Rifle.png"

    if msg =="저격총":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569662901743676/07._Sniper_Rifle.png"

    if msg =="글러브":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569663144984576/08._Glove.png"

    if msg =="톤파":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569663484731402/09._Tonfa.png"

    if msg =="방망이":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569663816089610/10._Bat.png"
        
    if msg =="망치":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569690617679912/11._Hammer.png"

    if msg =="활":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569690860969984/12._Bow.png"

    if msg =="석궁":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569691053891664/13._Crossbow.png"

    if msg =="레이피어":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569691234258984/14._Rapier.png"

    if msg =="창":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569691469148200/15._Spear.png"

    if msg =="투척":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569691678851092/16._Throw.png"
        
    if msg =="암기":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569691875991552/17._Shuriken.png"

    if msg =="기타":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569692094083102/18._Guitar.png"

    if msg =="쌍절곤":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569692094083102/18._Guitar.png"

    if msg =="채찍":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569692572237864/20._Whip.png"

    if msg =="카메라":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569768573042739/21.Camera.png"

    if msg =="아르카나":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/920569768904364072/22._Arcana.png"
        
    if msg =="VF의수":
        img_url="https://cdn.discordapp.com/attachments/920569615862607912/923542709954809926/23._VF_Prosthetic.png"

        

    embed=discord.Embed(description="**1레벨**`쿨다운:"+time1+"`\n ```"+des1+"```\n**2레벨**`쿨다운:"+time2+"`\n```"+des2+"``` \n")
    embed.set_author(name=name, icon_url=img_url)
    embed.set_footer(text="사용 가능 캐릭터:\t " + cha)
    return embed


