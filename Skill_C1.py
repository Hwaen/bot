import discord
import asyncio
import requests
from bs4 import BeautifulSoup
import lxml

name = {'재키' : 'Jackie',
        '아야' : 'Aya',
        '현우' : 'Hyunwoo',
        '매그너스' : 'Magnus',
        '피오라' : 'Fiora',
        '나딘' : 'Nadine',
        '자히르' : 'Zahir',
        '하트' : 'Hart',
        '아이솔' : 'Isol',
        '리다이린' : 'Li_Dailin',
        '유키' : 'Yuki',
        '혜진' : 'Hyejin',
        '쇼우' : 'XiuKai',
        '시셀라' : 'Sissela',
        '키아라' : 'Chiara',
        '아드리아나' : 'Adriana',
        '쇼이치' : 'Shoichi',
        '엠마' : 'Emma',
        '레녹스' : 'Lenox',
        '로지' : 'Rozzi',
        '루크' : 'Luke',
        '캐시' : 'Cathy',
        '아델라' : 'Adela',
        '버니스' : 'Bernice',
        '바바라' : 'Barbara',
        '수아' : 'Sua',
        '레온' : 'Leon',
        '일레븐' : 'Eleven',
        '셀린' : 'Celine',
        '리오' : 'Rio',
        '윌리엄' : 'William',
        '니키' : 'nicky',
        '나타폰' : 'Nathapon',
        '얀' : 'Jan',
        '이바' : 'Eva',
        '다니엘' : 'Daniel',
        '제니' : 'Jenny',
        '카밀로' : 'Camilo',
        '클로에' : 'Chloe',
        '요한' : 'Johann',
        '비앙카' : 'Bianca',
        '마이' : 'Mai',
        '라우라' : 'Laura',
        '띠아' : 'Tia',
        '펠릭스' : 'Felix',
        '엘레나' : 'Elena',
        '프리야' : 'Priya',
        }

def skill(msg,skill):
        global url
        url = 'https://er.inven.co.kr/db/character/'+name[msg]
         
        response = requests.get(url)
        if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'lxml')

                #### T ####
                if skill == "T" or skill == "t":
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillTitle > span.skillIcon > img").get("src")
         
                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill.append(a)
             
                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                               
                #### Q ####
                if skill == "Q" or skill == "q":
                        
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### W ####
                if skill == "W" or skill == "w":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### E ####
                if skill == "E" or skill == "e":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill.append(a)
                     
                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### R ####
                if skill == "R" or skill == "r":
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)"%(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                embed=discord.Embed(description=("```"+des+"```"))
                embed.set_author(name=(str(title)+"\t"+level+"레벨"), icon_url=img)
                embed.add_field(name="쿨타임:", value=time, inline=True)
                embed.add_field(name="SP소모:", value=sp , inline=True)
                embed.add_field(name="사거리:", value=dis , inline=True)
                embed.set_footer(text= "출처:\t"+ url)
                return embed
        
def skill_1(key):
        response = requests.get(url)
        if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'lxml')

                #### T ####
                if key == "T" or key == "t":
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillTitle > span.skillIcon > img").get("src")
         
                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill.append(a)
             
                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                               
                #### Q ####
                if key == "Q" or key == "q":
                        
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### W ####
                if key == "W" or key == "w":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### E ####
                if key == "E" or key == "e":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill.append(a)
                     
                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### R ####
                if key == "R" or key == "r":
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)"%(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                embed=discord.Embed(description=("```"+des+"```"))
                embed.set_author(name=(str(title)+"\t"+level+"레벨"), icon_url=img)
                embed.add_field(name="쿨타임:", value=time, inline=True)
                embed.add_field(name="SP소모:", value=sp , inline=True)
                embed.add_field(name="사거리:", value=dis , inline=True)
                embed.set_footer(text= "출처:\t"+ url)
                return embed


def skill_2(key):       
        response = requests.get(url)
        if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'lxml')

                global des
                
                #### T ####
                if key == "T":
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillTitle > span.skillIcon > img").get("src")
                
                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(%d)" %(i+1))
                                skill.append(a)
                                                        
                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### Q ####
                if key == "Q":                        
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(%d)" %(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### W ####
                if key == "W":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(%d)" %(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### E ####
                if key == "E":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(%d)" %(i+1))
                                skill.append(a)
                     
                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### R ####
                if key == "R":
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(%d)"%(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
     
                embed=discord.Embed(description=("```"+ des +"```"))
                embed.set_author(name=(str(title)+"\t"+level+"레벨"), icon_url=img)
                embed.add_field(name="쿨타임:", value=time, inline=True)
                embed.add_field(name="SP소모:", value=sp , inline=True)
                embed.add_field(name="사거리:", value=dis , inline=True)
                embed.set_footer(text= "출처:\t"+ url)
                return embed
                                
def skill_3(key):
        response = requests.get(url)
        if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'lxml')
                
                #### T ####
                if key == "T":
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillTitle > span.skillIcon > img").get("src")
                
                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(%d)" %(i+1))
                                skill.append(a)
                                                        
                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                
                #### Q ####
                if key == "Q" or key == "q":
                        
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(%d)" %(i+1))
                                skill.append(a)

                        level = "3"
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### W ####
                if key == "W" or key == "w":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(%d)" %(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### E ####
                if key == "E" or key == "e":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(%d)" %(i+1))
                                skill.append(a)
                     
                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### R ####
                if key == "R" or key == "r":
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(%d)"%(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                embed=discord.Embed(description=("```"+des+"```"))
                embed.set_author(name=(str(title)+"\t"+level+"레벨"), icon_url=img)
                embed.add_field(name="쿨타임:", value=time, inline=True)
                embed.add_field(name="SP소모:", value=sp , inline=True)
                embed.add_field(name="사거리:", value=dis , inline=True)
                embed.set_footer(text= "출처:\t"+ url)
                return embed

        

def skill_4(key):
        response = requests.get(url)
        if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'lxml')
                
                #### T ####
                if key == "T" or key == "t":
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillTitle > span.skillIcon > img").get("src")
                
                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(%d)" %(i+1))
                                skill.append(a)
                                                        
                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### Q ####
                if key == "Q" or key == "q":
                        
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(%d)" %(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### W ####
                if key == "W" or key == "w":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(%d)" %(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### E ####
                if key == "E" or key == "e":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(%d)" %(i+1))
                                skill.append(a)
                     
                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### R ####
                if key == "R" or key == "r":
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(%d)"%(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                embed=discord.Embed(description=("```"+des+"```"))
                embed.set_author(name=(str(title)+"\t"+level+"레벨"), icon_url=img)
                embed.add_field(name="쿨타임:", value=time, inline=True)
                embed.add_field(name="SP소모:", value=sp , inline=True)
                embed.add_field(name="사거리:", value=dis , inline=True)
                embed.set_footer(text= "출처:\t"+ url)
                return embed


def skill_5(key):
        response = requests.get(url)
        if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'lxml')
                
                #### T ####
                if key == "T" or key == "t":
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillTitle > span.skillIcon > img").get("src")
                
                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(2) > div.skillEffect > table > tbody > tr:nth-child(5) > td:nth-child(%d)" %(i+1))
                                skill.append(a)
                                                        
                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### Q ####
                if key == "Q" or key == "q":
                        
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillEffect > table > tbody > tr:nth-child(5) > td:nth-child(%d)" %(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### W ####
                if key == "W" or key == "w":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillEffect > table > tbody > tr:nth-child(5) > td:nth-child(%d)" %(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### E ####
                if key == "E" or key == "e":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillEffect > table > tbody > tr:nth-child(5) > td:nth-child(%d)" %(i+1))
                                skill.append(a)
                     
                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### R ####
                if key == "R" or key == "r":
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillEffect > table > tbody > tr:nth-child(5) > td:nth-child(%d)"%(i+1))
                                skill.append(a)

                        level = skill[0].get_text()
                        sp = skill[1].get_text()
                        time = skill[2].get_text()
                        dis = skill[3].get_text()
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                embed=discord.Embed(description=("```"+des+"```"))
                embed.set_author(name=(str(title)+"\t"+level+"레벨"), icon_url=img)
                embed.add_field(name="쿨타임:", value=time, inline=True)
                embed.add_field(name="SP소모:", value=sp , inline=True)
                embed.add_field(name="사거리:", value=dis , inline=True)                
                embed.set_footer(text= "출처:\t"+ url)
                return embed

        
