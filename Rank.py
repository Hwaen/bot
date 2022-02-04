import requests
from bs4 import BeautifulSoup
import discord
import asyncio

def tier(msg):
        name = msg
        url = 'https://dak.gg/bser/players/'+name+'?season=SEASON_4&hl=ko-KR'
        response = requests.get(url)

        if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                user = soup.select_one("#wrapper > div.container.px-0.player > section > h3")
                update = soup.find(class_="player-header__last-updated")        

        #####솔로#####
                rank1 = soup.select_one("#wrapper > div.container.px-0.player > div.row.row-normal > div:nth-child(1) > div > div.player-tier__summary > div > div > span:nth-child(1)")
                if (rank1==None)==False:
                        tier1 = rank1.get_text()
                        img1 = soup.select_one("#wrapper > div.container.px-0.player > div.row.row-normal > div:nth-child(1) > div > div.player-tier__summary > img")
                        tier_img1 = img1.get("src")                                    

                if (rank1==None)==True:
                        tier1 = "언랭크"
                        img1= "https://static-cdn.dak.gg/er/images/rank/round/0.png"
                        tier_img1 = img1
        #####듀오#####
                rank2 = soup.select_one("#wrapper > div.container.px-0.player > div.row.row-normal > div:nth-child(2) > div > div.player-tier__summary > div > div > span:nth-child(1)")
                if (rank2==None)==False:
                        tier2 = rank2.get_text()
                        img2 = soup.select_one("#wrapper > div.container.px-0.player > div.row.row-normal > div:nth-child(2) > div > div.player-tier__summary > img")
                        tier_img2 = img2.get("src") 

                if (rank2==None)==True:
                        tier2 = "언랭크"
                        img2 = "https://static-cdn.dak.gg/er/images/rank/round/0.png"
                        tier_img2 = img2

        #####스쿼드#####
                rank3 = soup.select_one("#wrapper > div.container.px-0.player > div.row.row-normal > div:nth-child(3) > div > div.player-tier__summary > div > div > span:nth-child(1)")
                if (rank3==None)==False:
                        tier3 = rank3.get_text()
                        img3 = soup.select_one("#wrapper > div.container.px-0.player > div.row.row-normal > div:nth-child(3) > div > div.player-tier__summary > img")
                        tier_img3 = img3.get("src")
                                
                if (rank3==None)==True:
                        tier3="언랭크"
                        img3 = "https://static-cdn.dak.gg/er/images/rank/round/0.png"
                        tier_img3 = img3

                num = img(tier_img1[-5],tier_img2[-5],tier_img3[-5])

                embed=discord.Embed(title = user.get_text())
                embed.set_thumbnail(url = "https://static-cdn.dak.gg/er/images/rank/round/"+num+".png")
                embed.add_field(name = "솔로",  value = tier1, inline=False)
                embed.add_field(name = "듀오",  value = tier2, inline=False)
                embed.add_field(name = "스쿼드",value = tier3, inline=False)
                embed.set_footer(text=update.get_text()+"\n\ndak.gg/bser/players/"+user.get_text())
                return embed
        else:
            pass



def img(solo, duo, trio):
        if solo>= duo:
                if solo>= trio:
                        return solo
                else:
                        return trio
        else:
                if duo>=trio:
                        return duo
                else:
                        return trio

