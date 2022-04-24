import discord
import asyncio
import requests
from bs4 import BeautifulSoup
import lxml

name = {'에키온' : 'Echion'}

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
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                        mode = []
                        time = []
                        dis = []
                        sp = []
                        
                        for i in range(0,4,1):        
                                b = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(5)" %(i+7))
                                mode.append(b)
                                
                                c = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(3)" %(i+7))
                                time.append(c)
                                
                                d = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(4)" %(i+7))
                                dis.append(d)
                                
                                e = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(2)" %(i+7))
                                sp.append(e)

                        바이퍼 = mode[0].text;     time_1 = time[0].text;  dis_1 = dis[0].text;    sp_1 = sp[0].text;
                        데스애더 = mode[1].text;   time_2 = time[1].text;   dis_2 = dis[1].text;    sp_2 = sp[1].text;
                        블랙맘바 = mode[2].text;   time_3 = time[2].text;   dis_3 = dis[2].text;    sp_3 = sp[2].text;
                        사와 = mode[3].text;       time_4 = time[3].text;   dis_4 = dis[3].text;    sp_4 = sp[3].text;

                        


                        embed=nextcord.Embed(description=("```"+des+"```"))
                        embed.set_author(name=(title+"\t"+level+"레벨"), icon_url=img)
                        
                        embed.add_field(name="독사의 진노 - 바이퍼", value="```"+바이퍼+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_1, inline=True)
                        embed.add_field(name="SP소모:", value=sp_1 , inline=True)
                        embed.add_field(name="사거리:", value=dis_1 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 데스애더", value="```"+데스애더+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_2, inline=True)
                        embed.add_field(name="SP소모:", value=sp_2 , inline=True)
                        embed.add_field(name="사거리:", value=dis_2 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 블랙맘바", value="```"+블랙맘바+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_3, inline=True)
                        embed.add_field(name="SP소모:", value=sp_3 , inline=True)
                        embed.add_field(name="사거리:", value=dis_3 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 사이드와인더", value="```"+사와+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_4, inline=True)
                        embed.add_field(name="SP소모:", value=sp_4 , inline=True)
                        embed.add_field(name="사거리:", value=dis_4 , inline=True)
                        embed.set_footer(text= "출처:\t"+ url)
                        return embed

                embed=nextcord.Embed(description=("```"+des+"```"))
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
                soup = BeautifulSoup(html, 'html.parser')

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
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                        mode = []
                        time = []
                        dis = []
                        sp = []
                        
                        for i in range(0,4,1):        
                                b = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(5)" %(i+7))
                                mode.append(b)
                                
                                c = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(3)" %(i+7))
                                time.append(c)
                                
                                d = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(4)" %(i+7))
                                dis.append(d)
                                
                                e = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(2)" %(i+7))
                                sp.append(e)

                        바이퍼 = mode[0].text;     time_1 = time[0].text;  dis_1 = dis[0].text;    sp_1 = sp[0].text;
                        데스애더 = mode[1].text;   time_2 = time[1].text;   dis_2 = dis[1].text;    sp_2 = sp[1].text;
                        블랙맘바 = mode[2].text;   time_3 = time[2].text;   dis_3 = dis[2].text;    sp_3 = sp[2].text;
                        사와 = mode[3].text;       time_4 = time[3].text;   dis_4 = dis[3].text;    sp_4 = sp[3].text;

                        


                        embed=nextcord.Embed(description=("```"+des+"```"))
                        embed.set_author(name=(title+"\t"+level+"레벨"), icon_url=img)
                        
                        embed.add_field(name="독사의 진노 - 바이퍼", value="```"+바이퍼+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_1, inline=True)
                        embed.add_field(name="SP소모:", value=sp_1 , inline=True)
                        embed.add_field(name="사거리:", value=dis_1 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 데스애더", value="```"+데스애더+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_2, inline=True)
                        embed.add_field(name="SP소모:", value=sp_2 , inline=True)
                        embed.add_field(name="사거리:", value=dis_2 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 블랙맘바", value="```"+블랙맘바+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_3, inline=True)
                        embed.add_field(name="SP소모:", value=sp_3 , inline=True)
                        embed.add_field(name="사거리:", value=dis_3 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 사이드와인더", value="```"+사와+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_4, inline=True)
                        embed.add_field(name="SP소모:", value=sp_4 , inline=True)
                        embed.add_field(name="사거리:", value=dis_4 , inline=True)
                        embed.set_footer(text= "출처:\t"+ url)
                        return embed
                           
                embed=nextcord.Embed(description=("```"+des+"```"))
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
                soup = BeautifulSoup(html, 'html.parser')
                
                #### T ####
                if key == "T" or key == "t":
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
                if key == "Q" or key == "q":
                        
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
                if key == "W" or key == "w":

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
                if key == "E" or key == "e":

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
                if key == "R" or key == "r":
                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(%d)"%(i+1))
                                skill.append(a)
                                
                        level = skill[0].get_text()                        
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                        mode = []
                        time = []
                        dis = []
                        sp = []
                        
                        for i in range(0,4,1):        
                                b = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(5)" %(i+7))
                                mode.append(b)
                                
                                c = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(3)" %(i+7))
                                time.append(c)
                                
                                d = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(4)" %(i+7))
                                dis.append(d)
                                
                                e = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(2)" %(i+7))
                                sp.append(e)

                        바이퍼 = mode[0].text;     time_1 = time[0].text;  dis_1 = dis[0].text;    sp_1 = sp[0].text;
                        데스애더 = mode[1].text;   time_2 = time[1].text;   dis_2 = dis[1].text;    sp_2 = sp[1].text;
                        블랙맘바 = mode[2].text;   time_3 = time[2].text;   dis_3 = dis[2].text;    sp_3 = sp[2].text;
                        사와 = mode[3].text;       time_4 = time[3].text;   dis_4 = dis[3].text;    sp_4 = sp[3].text;

                        


                        embed=nextcord.Embed(description=("```"+des+"```"))
                        embed.set_author(name=(title+"\t"+level+"레벨"), icon_url=img)
                        
                        embed.add_field(name="독사의 진노 - 바이퍼", value="```"+바이퍼+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_1, inline=True)
                        embed.add_field(name="SP소모:", value=sp_1 , inline=True)
                        embed.add_field(name="사거리:", value=dis_1 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 데스애더", value="```"+데스애더+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_2, inline=True)
                        embed.add_field(name="SP소모:", value=sp_2 , inline=True)
                        embed.add_field(name="사거리:", value=dis_2 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 블랙맘바", value="```"+블랙맘바+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_3, inline=True)
                        embed.add_field(name="SP소모:", value=sp_3 , inline=True)
                        embed.add_field(name="사거리:", value=dis_3 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 사이드와인더", value="```"+사와+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_4, inline=True)
                        embed.add_field(name="SP소모:", value=sp_4 , inline=True)
                        embed.add_field(name="사거리:", value=dis_4 , inline=True)
                        embed.set_footer(text= "출처:\t"+ url)
                        return embed
                           
                embed=nextcord.Embed(description=("```"+des+"```"))
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
                soup = BeautifulSoup(html, 'html.parser')
                
                #### T ####
                if key == "T" or key == "t":
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
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                        mode = []
                        time = []
                        dis = []
                        sp = []
                        
                        for i in range(0,4,1):        
                                b = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(5)" %(i+7))
                                mode.append(b)
                                
                                c = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(3)" %(i+7))
                                time.append(c)
                                
                                d = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(4)" %(i+7))
                                dis.append(d)
                                
                                e = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(2)" %(i+7))
                                sp.append(e)

                        바이퍼 = mode[0].text;     time_1 = time[0].text;  dis_1 = dis[0].text;    sp_1 = sp[0].text;
                        데스애더 = mode[1].text;   time_2 = time[1].text;   dis_2 = dis[1].text;    sp_2 = sp[1].text;
                        블랙맘바 = mode[2].text;   time_3 = time[2].text;   dis_3 = dis[2].text;    sp_3 = sp[2].text;
                        사와 = mode[3].text;       time_4 = time[3].text;   dis_4 = dis[3].text;    sp_4 = sp[3].text;

                        


                        embed=nextcord.Embed(description=("```"+des+"```"))
                        embed.set_author(name=(title+"\t"+level+"레벨"), icon_url=img)
                        
                        embed.add_field(name="독사의 진노 - 바이퍼", value="```"+바이퍼+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_1, inline=True)
                        embed.add_field(name="SP소모:", value=sp_1 , inline=True)
                        embed.add_field(name="사거리:", value=dis_1 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 데스애더", value="```"+데스애더+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_2, inline=True)
                        embed.add_field(name="SP소모:", value=sp_2 , inline=True)
                        embed.add_field(name="사거리:", value=dis_2 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 블랙맘바", value="```"+블랙맘바+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_3, inline=True)
                        embed.add_field(name="SP소모:", value=sp_3 , inline=True)
                        embed.add_field(name="사거리:", value=dis_3 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 사이드와인더", value="```"+사와+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_4, inline=True)
                        embed.add_field(name="SP소모:", value=sp_4 , inline=True)
                        embed.add_field(name="사거리:", value=dis_4 , inline=True)
                        embed.set_footer(text= "출처:\t"+ url)
                        return embed
                           
                embed=nextcord.Embed(description=("```"+des+"```"))
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
                soup = BeautifulSoup(html, 'html.parser')
                
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
                        text = skill[4]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                        mode = []
                        time = []
                        dis = []
                        sp = []
                        
                        for i in range(0,4,1):        
                                b = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(5)" %(i+7))
                                mode.append(b)
                                
                                c = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(3)" %(i+7))
                                time.append(c)
                                
                                d = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(4)" %(i+7))
                                dis.append(d)
                                
                                e = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(%d) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(2)" %(i+7))
                                sp.append(e)

                        바이퍼 = mode[0].text;     time_1 = time[0].text;  dis_1 = dis[0].text;    sp_1 = sp[0].text;
                        데스애더 = mode[1].text;   time_2 = time[1].text;   dis_2 = dis[1].text;    sp_2 = sp[1].text;
                        블랙맘바 = mode[2].text;   time_3 = time[2].text;   dis_3 = dis[2].text;    sp_3 = sp[2].text;
                        사와 = mode[3].text;       time_4 = time[3].text;   dis_4 = dis[3].text;    sp_4 = sp[3].text;

                        


                        embed=nextcord.Embed(description=("```"+des+"```"))
                        embed.set_author(name=(title+"\t"+level+"레벨"), icon_url=img)
                        
                        embed.add_field(name="독사의 진노 - 바이퍼", value="```"+바이퍼+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_1, inline=True)
                        embed.add_field(name="SP소모:", value=sp_1 , inline=True)
                        embed.add_field(name="사거리:", value=dis_1 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 데스애더", value="```"+데스애더+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_2, inline=True)
                        embed.add_field(name="SP소모:", value=sp_2 , inline=True)
                        embed.add_field(name="사거리:", value=dis_2 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 블랙맘바", value="```"+블랙맘바+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_3, inline=True)
                        embed.add_field(name="SP소모:", value=sp_3 , inline=True)
                        embed.add_field(name="사거리:", value=dis_3 , inline=True)
                        
                        embed.add_field(name="독사의 진노 - 사이드와인더", value="```"+사와+"```", inline=False)
                        embed.add_field(name="쿨타임:", value=time_4, inline=True)
                        embed.add_field(name="SP소모:", value=sp_4 , inline=True)
                        embed.add_field(name="사거리:", value=dis_4 , inline=True)
                        embed.set_footer(text= "출처:\t"+ url)
                        return embed
                           
                embed=nextcord.Embed(description=("```"+des+"```"))
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
                soup = BeautifulSoup(html, 'html.parser')
                
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
                           
                
                           
                embed=nextcord.Embed(description=("```"+des+"```"))
                embed.set_author(name=(str(title)+"\t"+level+"레벨"), icon_url=img)
                embed.add_field(name="쿨타임:", value=time, inline=True)
                embed.add_field(name="SP소모:", value=sp , inline=True)
                embed.add_field(name="사거리:", value=dis , inline=True)                
                embed.set_footer(text= "출처:\t"+ url)
                return embed

        
