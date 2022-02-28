import nextcord
import asyncio
import requests
from bs4 import BeautifulSoup
import lxml

name = {'알렉스' : 'Alex',
        '실비아' : 'Silvia'}



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

                        embed=nextcord.Embed(description=("```"+des+"```"))
                        embed.set_author(name=(str(title)+"\t"+level+"레벨"), icon_url=img)
                        embed.add_field(name="쿨타임:", value=time, inline=True)
                        embed.add_field(name="SP소모:", value=sp , inline=True)
                        embed.add_field(name="사거리:", value=dis , inline=True)
                        embed.set_footer(text= "출처:\t"+ url)
                        return embed                        
                                       
                #### Q1 ####
                if skill == "Q" or skill == "q":
                        
                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)

                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### Q2 ####
                
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillName").get_text()
                        img_2 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                b =soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill_2.append(b)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### W1 ####
                if skill == "W" or skill == "w":

                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)
                     
                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### W2 ####
               
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)"%(i+1))
                                skill_2.append(a)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### E1 ####
                if skill == "E" or skill == "e":

                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)
                     
                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")

        
                #### E2 ####
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)"%(i+1))
                                skill_2.append(a)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### R  ####
                if skill == "R" or skill == "r":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(9) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(9) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(9) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
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

                        
                embed=nextcord.Embed(description=("```"+des_1+"```\n```"+des_2+"```"))
                embed.set_author(name=(str(title_1)+"\t|\t"+str(title_2)+"\t"+level_1+"레벨"), icon_url=img_1)
                embed.add_field(name="쿨타임:", value=time_1+"\t|\t"+time_2, inline=True)
                embed.add_field(name="SP소모:", value=sp_1+"\t|\t"+sp_2 , inline=True)
                embed.add_field(name="사거리:", value=dis_1+"\t|\t"+dis_2 , inline=True)
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

                        embed=nextcord.Embed(description=("```"+des+"```"))
                        embed.set_author(name=(str(title)+"\t"+level+"레벨"), icon_url=img)
                        embed.add_field(name="쿨타임:", value=time, inline=True)
                        embed.add_field(name="SP소모:", value=sp , inline=True)
                        embed.add_field(name="사거리:", value=dis , inline=True) 
                        embed.set_footer(text= "출처:\t"+ url)
                        return embed                        
                                       
                #### Q1 ####
                if key == "Q" or key == "q":
                        
                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)

                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### Q2 ####
                
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillName").get_text()
                        img_2 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                b =soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill_2.append(b)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### W1 ####
                if key == "W" or key == "w":

                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)
                     
                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### W2 ####
               
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)"%(i+1))
                                skill_2.append(a)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### E1 ####
                if key == "E" or key == "e":

                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)
                     
                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")

        
                #### E2 ####
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)"%(i+1))
                                skill_2.append(a)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### R  ####
                if key == "R" or key == "r":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(9) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(9) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(9) > div.skillEffect > table > tbody > tr:nth-child(1) > td:nth-child(%d)" %(i+1))
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
                        
                embed=nextcord.Embed(description=("```"+des_1+"```\n```"+des_2+"```"))
                embed.set_author(name=(str(title_1)+"\t|\t"+str(title_2)+"\t"+level_1+"레벨"), icon_url=img_1)
                embed.add_field(name="쿨타임:", value=time_1+"\t|\t"+time_2, inline=True)
                embed.add_field(name="SP소모:", value=sp_1+"\t|\t"+sp_2 , inline=True)
                embed.add_field(name="사거리:", value=dis_1+"\t|\t"+dis_2  , inline=True)  
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

                        embed=nextcord.Embed(description=("```"+des+"```"))
                        embed.set_author(name=(str(title)+"\t"+level+"레벨"), icon_url=img)
                        embed.add_field(name="쿨타임:", value=time, inline=True)
                        embed.add_field(name="SP소모:", value=sp , inline=True)
                        embed.add_field(name="사거리:", value=dis , inline=True)  
                        embed.set_footer(text= "출처:\t"+ url)
                        return embed                        
                                       
                #### Q1 ####
                if key == "Q" or key == "q":
                        
                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)

                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### Q2 ####
                
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillName").get_text()
                        img_2 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                b =soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(%d)" %(i+1))
                                skill_2.append(b)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### W1 ####
                if key == "W" or key == "w":

                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)
                     
                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### W2 ####
               
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(%d)"%(i+1))
                                skill_2.append(a)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### E1 ####
                if key == "E" or key == "e":

                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)
                     
                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")

        
                #### E2 ####
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(%d)"%(i+1))
                                skill_2.append(a)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### R  ####
                if key == "R" or key == "r":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(9) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(9) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(9) > div.skillEffect > table > tbody > tr:nth-child(2) > td:nth-child(%d)" %(i+1))
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
                
                embed=nextcord.Embed(description=("```"+des_1+"```\n```"+des_2+"```"))
                embed.set_author(name=(str(title_1)+"\t|\t"+str(title_2)+"\t"+level_1+"레벨"), icon_url=img_1)
                embed.add_field(name="쿨타임:", value=time_1+"\t|\t"+time_2, inline=True)
                embed.add_field(name="SP소모:", value=sp_1+"\t|\t"+sp_2 , inline=True)
                embed.add_field(name="사거리:", value=dis_1+"\t|\t"+dis_2 , inline=True)  
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

                        embed=nextcord.Embed(description=("```"+des+"```"))
                        embed.set_author(name=(str(title)+"\t"+level+"레벨"), icon_url=img)
                        embed.add_field(name="쿨타임:", value=time, inline=True)
                        embed.add_field(name="SP소모:", value=sp , inline=True)
                        embed.add_field(name="사거리:", value=dis , inline=True)  
                        embed.set_footer(text= "출처:\t"+ url)
                        return embed                        
                                       
                #### Q1 ####
                if key == "Q" or key == "q":
                        
                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)

                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### Q2 ####
                
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillName").get_text()
                        img_2 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                b =soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(%d)" %(i+1))
                                skill_2.append(b)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### W1 ####
                if key == "W" or key == "w":

                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)
                     
                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### W2 ####
               
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(%d)"%(i+1))
                                skill_2.append(a)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### E1 ####
                if key == "E" or key == "e":

                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)
                     
                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")

        
                #### E2 ####
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(%d)"%(i+1))
                                skill_2.append(a)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### R  ####
                if key == "R" or key == "r":

                        title= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(9) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(9) > div.skillTitle > span.skillIcon > img").get("src")

                        skill=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(9) > div.skillEffect > table > tbody > tr:nth-child(3) > td:nth-child(%d)" %(i+1))
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
                        
                embed=nextcord.Embed(description=("```"+des_1+"```\n```"+des_2+"```"))
                embed.set_author(name=(str(title_1)+"\t|\t"+str(title_2)+"\t"+level_1+"레벨"), icon_url=img_1)
                embed.add_field(name="쿨타임:", value=time_1+"\t|\t"+time_2, inline=True)
                embed.add_field(name="SP소모:", value=sp_1+"\t|\t"+sp_2 , inline=True)
                embed.add_field(name="사거리:", value=dis_1+"\t|\t"+dis_2  , inline=True)  
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
                        text = skill[3]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                        embed=nextcord.Embed(description=("```"+des+"```"))
                        embed.set_author(name=(str(title)+"\t"+level+"레벨"), icon_url=img)
                        embed.add_field(name="쿨타임:", value=time, inline=True)
                        embed.add_field(name="SP소모:", value=sp , inline=True)
                        embed.add_field(name="사거리:", value=dis , inline=True)  
                        embed.set_footer(text= "출처:\t"+ url)
                        return embed                        
                                       
                #### Q1 ####
                if key == "Q" or key == "q":
                        
                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)

                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### Q2 ####
                
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillName").get_text()
                        img_2 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                b =soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(%d)" %(i+1))
                                skill_2.append(b)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### W1 ####
                if key == "W" or key == "w":

                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)
                     
                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### W2 ####
               
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(%d)"%(i+1))
                                skill_2.append(a)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### E1 ####
                if key == "E" or key == "e":

                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)
                     
                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")

        
                #### E2 ####
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillEffect > table > tbody > tr:nth-child(4) > td:nth-child(%d)"%(i+1))
                                skill_2.append(a)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                        
                embed=nextcord.Embed(description=("```"+des_1+"```\n```"+des_2+"```"))
                embed.set_author(name=(str(title_1)+"\t|\t"+str(title_2)+"\t"+level_1+"레벨"), icon_url=img_1)
                embed.add_field(name="쿨타임:", value=time_1+"\t|\t"+time_2, inline=True)
                embed.add_field(name="SP소모:", value=sp_1+"\t|\t"+sp_2 , inline=True)
                embed.add_field(name="사거리:", value=dis_1+"\t|\t"+dis_2  , inline=True)  
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
                        text = skill[3]
                        des = str(text).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                        embed=nextcord.Embed(description=("```"+des+"```"))
                        embed.set_author(name=(str(title)+"\t"+level+"레벨"), icon_url=img)
                        embed.add_field(name="쿨타임:", value=time, inline=True)
                        embed.add_field(name="SP소모:", value=sp , inline=True)
                        embed.add_field(name="사거리:", value=dis , inline=True)  
                        embed.set_footer(text= "출처:\t"+ url)
                        return embed                        
                                       
                #### Q1 ####
                if key == "Q" or key == "q":
                        
                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(3) > div.skillEffect > table > tbody > tr:nth-child(5) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)

                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                        
                #### Q2 ####
                
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillName").get_text()
                        img_2 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                b =soup.select_one("#erDb > div:nth-child(4) > div:nth-child(4) > div.skillEffect > table > tbody > tr:nth-child(5) > td:nth-child(%d)" %(i+1))
                                skill_2.append(b)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")

                #### W1 ####
                if key == "W" or key == "w":

                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(5) > div.skillEffect > table > tbody > tr:nth-child(5) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)
                     
                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### W2 ####
               
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(6) > div.skillEffect > table > tbody > tr:nth-child(5) > td:nth-child(%d)"%(i+1))
                                skill_2.append(a)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")
                           
                #### E1 ####
                if key == "E" or key == "e":

                        title_1= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillTitle > span.skillName").get_text()
                        img_1 = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_1=[]
                        for i in range(0,5,1):        
                                a=soup.select_one("#erDb > div:nth-child(4) > div:nth-child(7) > div.skillEffect > table > tbody > tr:nth-child(5) > td:nth-child(%d)" %(i+1))
                                skill_1.append(a)
                     
                        level_1 = skill_1[0].get_text()
                        sp_1 = skill_1[1].get_text()
                        time_1 = skill_1[2].get_text()
                        dis_1 = skill_1[3].get_text()
                        text_1 = skill_1[4]
                        des_1 = str(text_1).replace("<td>","").replace("</td>","").replace("<br/>","\n")

        
                #### E2 ####
                        title_2= soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillTitle > span.skillName").get_text()
                        img = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillTitle > span.skillIcon > img").get("src")

                        skill_2=[]
                        for i in range(0,5,1):        
                                a = soup.select_one("#erDb > div:nth-child(4) > div:nth-child(8) > div.skillEffect > table > tbody > tr:nth-child(5) > td:nth-child(%d)"%(i+1))
                                skill_2.append(a)

                        level_2 = skill_2[0].get_text()
                        sp_2 = skill_2[1].get_text()
                        time_2 = skill_2[2].get_text()
                        dis_2 = skill_2[3].get_text()
                        text_2 = skill_2[4]
                        des_2 = str(text_2).replace("<td>","").replace("</td>","").replace("<br/>","\n")


                        
                embed=nextcord.Embed(description=("```"+des_1+"```\n```"+des_2+"```"))
                embed.set_author(name=(str(title_1)+"\t|\t"+str(title_2)+"\t"+level_1+"레벨"), icon_url=img_1)
                embed.add_field(name="쿨타임:", value=time_1+"\t|\t"+time_2, inline=True)
                embed.add_field(name="SP소모:", value=sp_1+"\t|\t"+sp_2 , inline=True)
                embed.add_field(name="사거리:", value=dis_1+"\t|\t"+dis_2  , inline=True)  
                embed.set_footer(text= "출처:\t"+ url)
                return embed                

        
