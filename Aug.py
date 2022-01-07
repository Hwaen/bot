import discord
import asyncio

client = discord.Client()

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
    
#####저항#####
    if msg == "금강":
        embed=discord.Embed(title="금강", description="상대 실험체를 이동 불가 상태로 만들면 4초 동안 방어가 (20+레벨×5) 증가합니다. 방어 상승 효과가 종료되는 즉시 주변 2m에 (레벨×12)의 스킬 피해를 입힙니다. 피해를 입은 대상은 1.5초 동안 이동속도가 50% 감소합니다. (쿨다운 45초)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915656436212695080/916339950461550622/Diamond_Shard_.png")
        return embed

    if msg == "불괴":
        embed=discord.Embed(title="불괴", description="무기 스킬 사용 시 3[근거리]/2.5[원거리]초 동안 불괴 상태가 되며 입는 피해가 10 + 레벨×1[근거리]/5 + 레벨×1[원거리]% 감소하고 방해 효과 저항이 (20+방어력×0.15)[근거리]/(15+방어력×0.15)[원거리]% 증가합니다. (쿨다운 20초))")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915656436212695080/916339950667051098/Ironclad_.png")
        return embed

    if msg == "망각":
        embed=discord.Embed(title=" 망각", description="현재 체력이 낮을수록 기본 공격 피해를 덜 입습니다. 현재 체력이 최대 체력의 60 ~ 20% 이하면 기본 공격 피해를 0 ~ 15[근거리]/12[원거리]% 덜 입습니다. 이 특성으로 기본 공격 피해를 덜 입을 때마다 그 피해의 (0.2+방어력×0.0125)배를 고유 피해로 반사합니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915656436212695080/916339951082274816/Oblivion_Can_Wait_.png")
        return embed

    if msg == "특공대":
        embed=discord.Embed(title="특공대", description="7m내 존재하는 (모든 실험체 수×1.5)% 만큼 입는 피해가 감소합니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915656436212695080/916339991481819176/Cavalcade_.png")
        return embed

    if msg == "둔감":
        embed=discord.Embed(title="둔감", description="치명타 피해를 입으면 5초 동안 입는 치명타 피해가 7.5% 감소합니다. (쿨다운 10초)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915656436212695080/916339991729275060/Dulled_Blades_.png")
        return embed

    if msg == "대담":
        embed=discord.Embed(title="대담", description="스킬에 의해 보호막이나 체력 회복 효과를 받으면 3초 동안 방어력이 (20+레벨×1.5)만큼 증가합니다. (쿨다운 12초)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915656436212695080/916339991926431784/Embolden_.png")
        return embed

    if msg == "중장갑":
        embed=discord.Embed(title="중장갑", description="아이템으로 증가하는 각종 피해 감소 옵션이 130%로 적용됩니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915656436212695080/916339992169685012/Reinforced_Armor_.png")
        return embed

    if msg == "견고":
        embed=discord.Embed(title="견고", description="이동 불가 상태일 때 입는 피해가 (6 + 레벨 당 0.2)% 감소합니다.\n피해 감소 효과가 이동 불가 종료 이후 0.5초 더 지속됩니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915656436212695080/916339992421363793/Steadfast_.png")
        return embed
    
#####파괴#####
    if msg == "취약":
        embed=discord.Embed(title="취약", description="동일 실험체에게 3초 안에 기본 공격 또는 개별의 피해를 입히는 스킬(무기, 아이템 스킬 제외)을 3회 적중 시 (레벨×4)의 고정 피해를 추가로 입히며 5초 동안 대상의 방어력을 (레벨×0.8)% 감소시킵니다. (쿨다운 30초) 기본 공격이 연타로 적용되는 무기, 스킬 및 도트 딜링 스킬은 입히는 연속 피해를 한 번의 피해로 취급합니다. 스킬 사용 후 재사용하는 스킬의 경우는 스킬의 성향에 따라 개별 스킬 취급 여부가 다르며 무기 스킬은 취약 스택을 쌓을 수 없습니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261271630925854/916262946173235200/Frailty_Infliction_.png")
        return embed
        
    if msg == "광분":
        embed=discord.Embed(title="광분", description="무기 스킬 사용 시 7[근거리]/5[원거리]초 동안 공격력이 (10+레벨×1)[근거리]/(5+레벨×0.5)[원거리], 공격 속도가 (30+레벨×1)[근거리]/(20+레벨×1)[원거리]% 증가하지만 입는 피해도 7% 증가합니다. (쿨다운 30초)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261271630925854/916262946437496853/Frenzy_.png")
        return embed
        
    if msg == "흡혈마":
        embed=discord.Embed(title="흡혈마", description="개별 스킬로 실험체에게 피해를 입힐 때마다 모든 피해 흡혈이 5%씩 상승하며 최대 4번 중첩됩니다. 최대 중첩 시 스킬 증폭이 (레벨1.5)% 증가합니다. 동시에 여러 대상에게 피해를 입힐 경우 피해를 입힌 대상 수만큼 중첩되어 상승합니다. 모든 피해 흡혈은 8초 동안 유지되며 개별 스킬로 피해를 입힐 때마다 갱신됩니다. (쿨다운 5초) 무기 스킬은 흡혈마 스택을 쌓을 수 없습니다.)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261271630925854/916262946663960636/Vampiric_Bloodline_.png")
        return embed
        
    if msg == "열세극복":
        embed=discord.Embed(title="열세극복", description="대상 실험체의 최대 체력이 자신의 최대 체력보다 많은 경우 입히는 피해가 증가합니다. 증가 피해는 상대 최대 체력이 10% ~ 40% 많을 경우에 따라 2.5% ~ 10%까지 증가합니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261271630925854/916263007653351485/Dismantle_Goliath_.png")
        return embed
        
    if msg == "갈증":
        embed=discord.Embed(title="갈증", description="실험체가 아닌 대상에게 입히는 피해가 12%증가하며, 입힌 피해의 10%만큼 체력이 회복됩니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261271630925854/916263008064376862/Quench_.png")
        return embed
        
    if msg == "수확":
        embed=discord.Embed(title="수확", description="자신 또는 자신의 소환물이 입히는 모든 피해의 15%만큼 스태미너가 회복됩니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261271630925854/916263008337010798/Spirit_Culling_.png")
        return embed
        
    if msg == "복수자":
        embed=discord.Embed(title="복수자", description="안전지대 활성화 단계 이후로 자신이 안전지대 안에 있을 때 적에게 입히는 피해가 12% 증가합니다. 임시 안전지대와 최종 안전지대 모두 해당됩니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261271630925854/916263009171697674/Vengeance_.png")
        return embed
        
    if msg == "철갑탄":
        embed=discord.Embed(title="철갑탄", description="방어 관통이 (레벨 당 0.3)%만큼 증가합니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261271630925854/916263008626425886/Stopping_Power_.png")
        return embed

    if msg == "벽력":
        embed=discord.Embed(title="벽력", description="적 실험체에게 스킬로 피해를 입혔을 때 10 + 레벨×5.5의 고유 피해를 입힙니다. (쿨다운 18초)\n스킬을 적중한 적 실험체의 4m 범위 내 적 실험체가 있으면 전류의 줄기가 전이되어 50%의 피해를 입힙니다.\n전이될 적 실험체가 없는 경우 20%의 추가 고유 피해를 입힙니다.\n적 실험체에게 개별 스킬로 피해를 입힐 때마다 쿨다운이 0.5초 감소합니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261271630925854/928688092544634890/Red_Sprite_.png")
        return embed
    
        
#####지원#####
    if msg == "초재생":
        embed=discord.Embed(title="초재생", description="자신의 스킬에 의해 발생하는 모든 보호막 및 회복량이 상시 (20+스킬 증폭×0.2)% 증가합니다. 자신에 의해 보호막 또는 회복 효과를 받은 대상은 4초 동안 공격력이 (레벨×2)만큼 증가합니다. (쿨다운 25초) 휴식, 재생, 흡혈, 음식, 음료를 통한 회복은 적용되지 않습니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261234951741450/916340062134870036/Healing_Factor_.png")
        return embed

    if msg == "치유드론":
        embed=discord.Embed(title="치유드론", description="궁극기 사용 시 5초 동안 자신을 따라다니는 치유 드론이 나타납니다. 치유 드론은 주변 3m 내 자신을 포함한 아군의 체력을 매 초 잃은 체력의 (5+레벨×0.5)%만큼 회복시킵니다. (쿨다운 45초)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261234951741450/916340061778374738/Healing_Drone_.png")
        return embed

    if msg == "증폭드론":
        embed=discord.Embed(title="증폭드론", description="궁극기 사용 시 3.5초 동안 자신을 따라다니는 증폭 드론이 나타납니다. 증폭 드론은 주변 4m 내 자신을 포함한 아군의 이동 속도를 (5+0.3×레벨)%, 스킬 증폭을 (10+1.5×레벨)% 증가시킵니다. (쿨다운 45초)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261234951741450/916340061119852574/Amplification_Drone_.png")
        return embed

    if msg == "가시덤불":
        embed=discord.Embed(title="가시덤불", description="상대를 이동 불가 상태로 만들면 6초 동안 대상이 입는 모든 피해가 4% 증가합니다. (쿨다운 20초)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261234951741450/916340063208628294/Thorn_Shackles_.png")
        return embed

    if msg == "집결":
        embed=discord.Embed(title="집결", description="궁극기 사용 시 자신의 주변 4m 내 자신을 포함한 아군은 3초 동안 (레벨×10)만큼의 보호막을 얻습니다. (쿨다운 45초)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261234951741450/916340061333770260/Assembly_.png")
        return embed

    if msg == "후방보급":
        embed=discord.Embed(title="후방보급", description="매일 밤마다 힐링 포션을 (1+자신을 포함한 생존한 아군 수)개씩 얻습니다. 아이템 칸이 부족할 경우 바닥에 떨어집니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261234951741450/916340062340395008/Logistics_.png")
        return embed

    if msg == "테이아":
        embed=discord.Embed(title="테이아", description="밤 시야가 1.25m 증가합니다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261234951741450/916340062961147974/Theia_.png")
        return embed

    if msg == "시가전":
        embed=discord.Embed(title="시가전", description="자신이 설치한 함정이 발동하면 6초 동안 공격력이 10%, 자신이 상대의 함정을 발동시키면 3초 동안 방어력이 30% 증가합니다. (쿨다운 15초)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916261234951741450/916340063447695450/Urban_Warfare_.png")
        return embed
    
