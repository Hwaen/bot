import discord
import asyncio

###무기스킬###
def skill_w(msg):

    if msg == "단검":
        embed=discord.Embed(description="```망토\n스킬을 사용하면 2/3.5초간 투명해지고 이동 속도가 10% 증가합니다. 증가한 이동 속도는 2초에 걸쳐 감소합니다.\n\n단검\n지정한 대상의 뒤로 이동해서 162 피해와 대상의 현재 체력 10%에 해당하는 고정피해를 입히고 3초간 이동속도를 15% 감소시킵니다.```")
        embed.set_author(name="망토와 단검[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569661077225483/01._Dagger.png")
        embed.add_field(name="쿨타임:", value="45초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "양손검":
        embed=discord.Embed(description="```지정한 방향으로 0.75초 동안 자세를 취하며 모든 공격과 효과를 방어합니다. 자세가 끝나면 지정한 방향으로 3m 돌진하여 경로상에 있는 모든 적에게 175% 공격력의 피해를 입힙니다.```")
        embed.set_author(name="빗겨 흘리기 [D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569661077225483/01._Dagger.png")
        embed.add_field(name="쿨타임:", value="30초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed        

    if msg == "도끼":
        embed=discord.Embed(description="```적에게 기본 공격을 할 때마다 피의 나선 중첩을 1씩 증가합니다. 최대 중첩(4)이 되면 스킬을 사용할 수있습니다. 야생동물들에게는 중첩을 1씩 획득할 수 있습니다.\n스킬을 사용하면 지정한 방향으로 이동하며 도끼를 휘둘러서 범위 내의 모든 적들에게 공격력의 125%(+대상 최대 체력의 7%)의 고유 피해를 입힙니다. 야생동물에게는 더 많은 피해를 입히며, 입힌 피해의 100%에 해당하는 체력을 회복합니다.```")
        embed.set_author(name="빗겨 흘리기[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569661681197116/03._Axe.png")
        embed.add_field(name="쿨타임:", value="0.5초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "쌍검":
        embed=discord.Embed(description="```스킬을 사용하면 지정한 방향으로 돌진하며 경로상에 있는 모든 적들에게 25% 공격력의 피해를 6회 입힙니다.\n돌진하면서 적에게 공격을 4회 성공하면 5초 이내에 스킬을 한번 더 사용할 수 있습니다. 스킬을 다시 사용하면 지정한 방향으로 돌진하며 경로상에 있는 모든 적들에게 125%의 피해를 입힙니다.```")
        embed.set_author(name="쌍검난무[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569662033526804/04._Dual_Swords.png")
        embed.add_field(name="쿨타임:", value="40초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "권총":
        embed=discord.Embed(description="```스킬을 사용하면 1초 동안 탄환을 장전하며 이동 속도가 25% 증가합니다.\n패시브 스킬과 무기 스킬, 궁극 스킬을 제외한 모든 스킬의 남아있는 쿨다운 시간이 45% 감소합니다.```")
        embed.set_author(name="무빙 리로드[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569662398414868/05._Pistol.png")
        embed.add_field(name="쿨타임:", value="40초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "돌격소총":
        embed=discord.Embed(description="```기본 공격으로 적을 타격할 때마다 총알 1발당 5의 과열 중첩을 획득합니다. (최대 100 중첩)\n6초간 기본 공격을 하지 않으면 1초마다 과열 중첩이 10씩 감소됩니다. 과열 중첩이 100이 된 순간 과열 스킬을 사용할 수 있습니다.\n과열 스킬을 사용하면 탄환을 즉시 장전하고 6초 동안 과열 효과를 활성화합니다. 과열된 상태에서는 기본 공격 추가 피해가 6 증가하며, 공격 속도가 40% 증가합니다.\n효과 지속 중에는 공격 속도 상한을 무시합니다.```")
        embed.set_author(name="과열[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569662683631666/06._Assault_Rifle.png")
        embed.add_field(name="쿨타임:", value="40초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "저격총":
        embed=discord.Embed(description="```지정한 방향으로 저격 모드를 활성화합니다.\n저격 모드가 되면 시야가 30 증가하고 바라보고 있는 방향으로 시야 각도가 좁아집니다. 시야 내의 지정한 방향으로 스킬을 사용하여 저지 사격과 데드아이를 사용 할 수 있습니다.\n\n저지 사격\n6의 시야를 가지고 있으며 맞은 대상에게 공격력의 200%의 피해를 입히고 3초간 대상의 시야를 획득 할 수 있습니다. 피해를 입은 대상은 4초간 고정 효과를 받게 됩니다.\n\n데드아이\n1.5의 시야를 가지고 있으며 맞은 대상에게 공격력의 225~450%의 피해를 입힙니다. 데드아이는 맞은 대상의 잃은 체력에 비례해 피해량이 증가합니다.\n\n저격 상태에서 이동을 하거나 방해효과를 받으면 저격모드가 해제 됩니다.```")
        embed.set_author(name="저격[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569662901743676/07._Sniper_Rifle.png")
        embed.add_field(name="쿨타임:", value="40초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "글러브":
        embed=discord.Embed(description="```지정한 대상에게 다가가서 (100% 공격력)의 피해를 입히고, 최종 피해의 60%에 해당하는 피해와 20의 고정피해를 추가로 입힙니다. 어퍼컷 스킬로 입히는 피해는 치명타가 발생하지 않습니다.```")
        embed.set_author(name="저격[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569663144984576/08._Glove.png")
        embed.add_field(name="쿨타임:", value="10초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed
                
    if msg == "톤파":
        embed=discord.Embed(description="```스킬을 사용하면 0.75초 동안 모든 방위에서 오는 피해를 막고, 자신의 시야 내에서 공격한 대상에겐 피해를 0.4배로 되돌려줍니다.\n(공격의 효과는 막지 못합니다.)```")
        embed.set_author(name="고속회전[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569663484731402/09._Tonfa.png")
        embed.add_field(name="쿨타임:", value="25초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "방망이":
        embed=discord.Embed(description="```전방의 모든 적에게 150(+100% 공격력)의 피해를 입히고 4m 넉백시킵니다. 넉백된 적이 벽에 부딪히게 되면 0.6초간 기절하게 됩니다.```")
        embed.set_author(name="풀스윙[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569663816089610/10._Bat.png")
        embed.add_field(name="쿨타임:", value="25초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed
                
    if msg == "망치":
        embed=discord.Embed(description="```지정한 방향으로 망치를 내려쳐 125(+공격력의30%)(+방어력의45%)의 피해를 입히고 6초간 방어력을 15% 감소시킵니다.```")
        embed.set_author(name="갑옷깨기[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569690617679912/11._Hammer.png")
        embed.add_field(name="쿨타임:", value="28초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "레이피어":
        embed=discord.Embed(description="```지정한 적에게 돌진해서 100% 치명타 공격력의 피해를 입힙니다. 치명타 피해량이 증가할수록 피해량이 증가합니다.```")
        embed.set_author(name="섬격[D] ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569691234258984/14._Rapier.png")
        embed.add_field(name="쿨타임:", value="30초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "창":
        embed=discord.Embed(description="```지정한 방향으로 창을 강하게 내질러서 2m의 대상에게 100% 공격력의 피해를 한 번 입히고, 4m의 대상에게 100% 공격력의 피해를 입힙니다. 공격에 맞은 대상은 2초 동안 이동 속도가 55% 감소되고, 2m 이내에 있는 대상은 2.6m 밖으로 밀어버립니다.```")
        embed.set_author(name="그림자 찌르기[D] ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569691469148200/15._Spear.png")
        embed.add_field(name="쿨타임:", value="30초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "활":
        embed=discord.Embed(description="```지정한 지점으로 화살 다발을 발사하여 화살비가 내리게 합니다. 발사된 화살은 3초 후에 목표 지점에 떨어지며, 화살비를 맞은 대상에게 150(+100% 공격력)의 피해를 입히고, 이동 속도를 15% 감소시킵니다. 화살비의 중심에 있을 경우 300(+100% 공격력)의 피해를 입게 됩니다.```")
        embed.set_author(name="곡사[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569690860969984/12._Bow.png")
        embed.add_field(name="쿨타임:", value="20초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "석궁":
        embed=discord.Embed(description="```지정한 방향으로 석궁을 쏩니다. 맞은 대상은 50% 공격력의 피해를 입고 밀려나게 됩니다. 대상이 벽에 부딪혀 기절하게 되면 50% 공격력의 피해를 추가로 입게 됩니다.```")
        embed.set_author(name="강노[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569691053891664/13._Crossbow.png")
        embed.add_field(name="쿨타임:", value="40초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "투척":
        embed=discord.Embed(description="```지정한 위치에 연막탄을 던져서 터트립니다. 3초 동안 연막은 유지되며, 연막 안에 있는 적은 시야가 감소하고 이동 속도가 10% 감소합니다.```")
        embed.set_author(name="연막[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569691678851092/16._Throw.png")
        embed.add_field(name="쿨타임:", value="35초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "암기":
        embed=discord.Embed(description="```일정 범위에 8초 동안 유지되는 마름쇠를 뿌려 마름쇠를 밟은 적에게 65(+30% 공격력)의 피해를 입히고 2초 동안 30%의 이동 속도를 감소시킵니다. (마름쇠를 연속해서 밟으면 최초 피해의 45%만 적용됩니다.)```")
        embed.set_author(name="마름쇠 투척[D] ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569691875991552/17._Shuriken.png")
        embed.add_field(name="쿨타임:", value="30초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "기타":
        embed=discord.Embed(description="```지정한 방향으로 음파를 날려 첫 번째로 맞는 대상에게 100% 공격력의 피해를 입힙니다. 음파에 맞은 대상은 소리에 홀려 1.2초 동안 음파를 날린 대상에게 이동합니다.```")
        embed.set_author(name="Love&...[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569692094083102/18._Guitar.png")
        embed.add_field(name="쿨타임:", value="27초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "쌍절곤":
        embed=discord.Embed(description="```쌍절곤을 빠르게 휘둘러서 생긴 바람을 모아 지정한 방향으로 날립니다.\n바람의 구체는 쌍절곤을 휘두른 시간에 따라 150(+50% 공격력) ~ 300(+150% 공격력)의 피해를 입히며, 0.8초 이상 휘두르면 맞은 대상을 1초간 기절시킵니다.```")
        embed.set_author(name="맹룡과강[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569692299624448/19._Nunchaku.png")
        embed.add_field(name="쿨타임:", value="25초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "채찍":
        embed=discord.Embed(description="```채찍을 앞으로 날려 맞은 적에게 100(+30% 공격력)의 피해를 주고 앞으로 끌고 옵니다.```")
        embed.set_author(name="갈고리[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569692572237864/20._Whip.png")
        embed.add_field(name="쿨타임:", value="40초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed

    if msg == "카메라":
        embed=discord.Embed(description="```플래시를 터트려 80(+50% 공격력)의 피해를 입힙니다. 자신을 바라보던 적들은 100의 추가 스킬 피해를 입고 2초 동안 시야가 감소합니다.```")
        embed.set_author(name="플래시[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/920569768573042739/21.Camera.png")
        embed.add_field(name="쿨타임:", value="40초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed
                
    if msg == "아르카나":
        embed=discord.Embed(description="```사용 시, 실험체 주변에 VF에너지가 담긴 매개체 2/3개를 생성합니다. 다시 사용하면 구체 한 개가 목표 지점으로 날아가 짧은 시간 후 폭발하며, 40(+공격력의 50%)의 스킬 피해를 입힙니다. 구체의 수만큼 다시 사용할 수 있습니다. 대상을 5초 안에 연속으로 적중하면, 추가 효과가 발생합니다. 2회 적중: 3초 동안 이동 속도가 20% 감소합니다. 3회 적중: 1초 동안 기절합니다.```")
        embed.set_author(name="VF 매개[D]  ", icon_url="https://cdn.discordapp.com/attachments/920569615862607912/923542709954809926/23._VF_Prosthetic.png")
        embed.add_field(name="쿨타임:", value="30초", inline=True)
        embed.add_field(name="SP소모:", value="없음", inline=True)
        return embed
