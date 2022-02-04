import discord
import asyncio
import requests
from bs4 import BeautifulSoup

client = discord.Client()

key = {#파괴
       '취약' :'Frailty_Infliction',
       '광분':'Frenzy',
       '흡혈마':'Vampiric_Bloodline',
       '벽력':'Red_Sprite',
       '철갑탄':'Stopping_Power',
       '열세극복':'Dismantle_Goliath',
       '복수자':'Vengeance',
       '수확':'Spirit_Culling',
       '갈증':'Quench',
       
       #저항
       '금강':'Diamond_Shard',
       '불괴':'Ironclad',
       '망각':'Oblivion_Can_Wait',
       '대담':'Embolden',
       '특공대':'Cavalcade',
       '견고':'Steadfast',
       '둔감':'Dulled_Blades',
       '중장갑':'Reinforced_Armor',
       
       #지원
       '초재생':'Healing_Factor',
       '치유드론':'Healing_Drone',
       '증폭드론':'Amplification_Drone',
       '가시덤불':'Thorn_Shackles',
       '집결':'Assembly',
       '후방보급':'Logistics',
       '테이아':'Theia',
       '시가전':'Urban_Warfare'}



def aug(msg):
    if msg == "저항":
        embed=discord.Embed(title="저항")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915656436212695080/916339899563659304/Fortification_2.png")
        embed.add_field(name="주특성", value="금강 불괴 망각", inline=False)
        embed.add_field(name="부특성", value="대담 특공대 견고 둔감 중장갑", inline=False)
        return embed

    if msg == "파괴":
        embed=discord.Embed(title="저항")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261271630925854/916340033722675250/Havoc_2.png")
        embed.add_field(name="주특성", value="취약 광분 흡혈마 벽력", inline=False)
        embed.add_field(name="부특성", value="철갑탄 열세극복 복수자 수확 갈증", inline=False)
        return embed

    if msg == "지원":
        embed=discord.Embed(title="저항")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261234951741450/916340062726258688/Support_2.png")
        embed.add_field(name="주특성", value="초재생 치유드론 증폭드론", inline=False)
        embed.add_field(name="부특성", value="가시덤불 집결 후방보급 테이아 시가전", inline=False)
        return embed



    global url
    url = 'https://er.inven.co.kr/db/trait/'+key[msg]
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        name = soup.select_one('#erTraitLayer > div > div > div.db_block.info_top.clearfix > div.txt > b').get_text()
        img = soup.select_one('#erTraitLayer > div > div > div.db_block.info_top.clearfix > div.icon_wrap > img').get('src')
        text = soup.select_one('#erTraitLayer > div > div > div.db_block.content_area.clearfix').get_text()
        main = soup.select_one('#erTraitLayer > div > div > div.db_block.info_top.clearfix > div.txt > span').get_text()
        des = text.replace('*','×').replace("\n","").replace("  ","")

    embed=discord.Embed(title="`"+main+"`", description= des)
    embed.set_author(name= name, icon_url= img)
    return embed

                



                
                

                
                





