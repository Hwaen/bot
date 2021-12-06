import requests
from bs4 import BeautifulSoup
import discord
import asyncio

def tier(msg):
        name = msg
        url = 'https://dak.gg/bser/players/'+name+'?season=SEASON_4'
        response = requests.get(url)

        if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')


        #####솔로#####
                rank1 = soup.select_one("#wrapper > div.container.px-0.player > div.row.row-normal > div:nth-child(1) > div > div.player-tier__summary > div > div > span:nth-child(1)")
                if (rank1==None)==False:
                        tier1 = rank1.get_text()
                        img1 = soup.find(class_='align-middle mr-3')
                        tier_img1 = img1.get("src")
                      

                if (rank1==None)==True:
                        tier1 = "Unrank"
                        img1 = "https://dak.gg/bser/images/assets/tier/round/0.png?1"
                        tier_img1 = img1
        #####듀오#####
                rank2 = soup.select_one("#wrapper > div.container.px-0.player > div.row.row-normal > div:nth-child(2) > div > div.player-tier__summary > div > div > span:nth-child(1)")
                if (rank2==None)==False:
                        tier2 = rank2.get_text()
                        img2 = soup.find(class_='align-middle mr-3')
                        tier_img2 = img2.get("src")

                if (rank2==None)==True:
                        tier2 = "Unrank"
                        img2 = "https://dak.gg/bser/images/assets/tier/round/0.png?1"
                        tier_img2 = img2

        #####스쿼드#####
                rank3 = soup.select_one("#wrapper > div.container.px-0.player > div.row.row-normal > div:nth-child(3) > div > div.player-tier__summary > div > div > span:nth-child(1)")
                if (rank3==None)==False:
                        tier3 = rank3.get_text()
                        img3 = soup.find(class_='align-middle mr-3')
                        tier_img3 = img3.get("src")

                if (rank3==None)==True:
                        tier3="Unrank"
                        img3 = "https://dak.gg/bser/images/assets/tier/round/0.png?1"
                        tier_img3 = img3

                embed=discord.Embed(title = name)
                embed.set_thumbnail(url = tier_img1)
                embed.add_field(name = "솔로",  value = tier1, inline=False)
                embed.add_field(name = "듀오",  value = tier2, inline=False)
                embed.add_field(name = "스쿼드",value = tier3, inline=False)
                return embed
        else:
            pass