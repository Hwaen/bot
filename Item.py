import discord
import asyncio

client = discord.Client()

def Weapon(msg):
    if msg==" ":
        pass    
#####망치#####
    if msg=="망치":
        embed=discord.Embed(title="망치", description="공격력 +16", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317360093442128/001._Hammer_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로 ", value="연못(8) 모래사장(9) 골목길(11)\n사냥 멧돼지", inline=False)
        return embed

    if msg=="워해머":
        embed=discord.Embed(title="워해머", description="공격력 +40",color=0x1eb300)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317382633644034/002._Warhammer_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="망치 + 단봉", inline=False)
        return embed

    if msg=="운명의망치":
        embed=discord.Embed(title="모닝 스타", description="공격력 +55", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/920641046365483098/003._Morning_Star__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="워해머 + 쇠구슬", inline=False)
        return embed

    if msg=="사슴망치":
        embed=discord.Embed(title="사슴망치", description="공격력 +56", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317414606823464/004._Black_Stag_Hammer__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로 ", value="워해머 + 가죽", inline=False)
        return embed
        
    if msg=="운명의망치":
        embed=discord.Embed(title="운명의망치", description=" 공격력 +40\n쿨다운 감소 +8%\n치명타 확률 +8%", color=0x1e82cd)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/891317310952988712/891317445732741190/005._Forged_Destiny__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로 ", value="망치 + 운명의 꽃", inline=False)
        return embed

    if msg=="낭아봉":
        embed=discord.Embed(title="낭아봉", description=" 공격력 +55\n스킬 공격 추가 피해 +22\n레벨 당 스킬 공격 추가 피해 +1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317450635874375/006._Fang_Mace_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="모닝스타 + 달궈진 돌멩이", inline=False)
        return embed
    
    if msg=="다그다의망치":
        embed=discord.Embed(title="다그다의 망치", description=" 공격력 +98\n체력 재생(%) +125%\n기본 공격 추가 피해 +29\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317452749803540/007._Hammer_of_Dagda__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="사슴망치 + 성자의 유산", inline=False)
        return embed

    if msg=="토르의망치":
        embed=discord.Embed(title="토르의망치", description=" 공격력 +105\n공격 속도(%) +30%\n레벨 당 공격 속도 +1%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317472165261342/008._Hammer_of_Thor__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="사슴망치 + 이온전지", inline=False)
        return embed 

    if msg=="개밥바라기":
        embed=discord.Embed(title="개밥바라기", description=" 공격력 +105\n스킬 증폭(%) +20%", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317472769241169/009._Evening_Star_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="모닝스타 + 문스톤", inline=False)
        return embed

    if msg=="천근추":
        embed=discord.Embed(title="천근추", description=" 공격력 +88\n스킬 증폭 +8%\n쿨다운 감소 +12%\n ```차지드 스트라이크-[고유 장착 효과]\n매 3초마다 다음 공격이 100%의 치명타 확률 보너스를 획득합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317475961085972/010._Weight_of_the_World_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="운명의망치 + 진신사리", inline=False)        
        return embed
        
    if msg=="피스브링어":
        embed=discord.Embed(title="피스브링어", description=" 공격력 +140\n모든 피해 흡혈 10%\n방어력 관통 +12%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317478783873064/011._Peacebringer__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로 ", value="사슴망치 + VF 혈액 샘플", inline=False)
        return embed

#####단검#####
    if msg=="식칼":
        embed=discord.Embed(title="식칼", description=" 공격력 +4", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342811553751060/003._Kitchen_Knife_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로 ", value="항구(4) 호텔(5) 절(5)\n사냥 멧돼지", inline=False)
        return embed

    if msg =="가위":
        embed=discord.Embed(title="가위", description=" 공격력 +5", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342805245505556/001._Scissors_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로 ", value="골목길(11) 병원(8) 학교(9)\n사냥 박쥐", inline=False)    
        return embed

    if msg=="만년필":
        embed=discord.Embed(title="만년필", description=" 공격력 +5", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342808315740230/002._Fountain_Pen_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로", value="고급 주택가(8) 번화가(8) 학교(9)\n사냥 박쥐", inline=False)
        return embed

    if msg=="군용나이프":
        embed=discord.Embed(title="군용나이프", description=" 공격력 +14\n 이동 속도 +0.06", color=0x1eb300)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342816045830184/004._Army_Knife__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로 ", value="식칼 + 나뭇가지", inline=False)
        return embed

    if msg=="메스":
        embed=discord.Embed(title="메스", description=" 공격력 +18", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342820277899385/005._Scalpel_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로 ", value="만년필 + 면도칼", inline=False)
        return embed

    if msg=="자마다르":
        embed=discord.Embed(title="자마다르", description=" 공격력 +15", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342825336229898/006._Jamadhar_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로 ", value="식칼 + 너클", inline=False)
        return embed

    if msg=="장미칼":
        embed=discord.Embed(title="장미칼", description=" 공격력 +20\n이동 속도 +0.08\n쿨다운 감소 +8%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342830545543278/007._Rose_Knife_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로 ", value="군용 나이프 + 꽃", inline=False)
        return embed

    if msg=="스위스아미나이프" or msg=="스위스 아미 나이프":
        embed=discord.Embed(title="스위스 아미 나이프", description=" 공격력 +23\n최대 체력 +100", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342835192832010/008._Swiss_Army_Knife__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로 ", value="메스 + 가위", inline=False)
        return embed

    if msg=="카라페이스카타르":
        embed=discord.Embed(title="카라페이스 카타르", description=" 공격력 +20\n방어력 +12", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342839248732160/009._Carapace_Katar__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로 ", value="자마다르 + 거북이등딱지", inline=False)
        return embed

    if msg=="카른웬난":
        embed=discord.Embed(title="카른웬난", description=" 공격력 +41\n체력 재생 +1.2\n이동 속도 +0.08\n쿨다운 감소 +8%\n\레벨 당 기본 공격 추가 피해 +2\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342843313004564/010._Carnwennan_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="장미칼 + 성자의 유산", inline=False)
        return embed

    if msg=="파산검":
        embed=discord.Embed(title="파산검", description=" 공격력 +30\n이동 속도 +0.1\n쿨다운 감소 +10%\n레벨 당 스킬 공격 추가 피해 +2\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342847847043142/011._Mount_Slicer_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="장미칼 + 재", inline=False)
        return embed

    if msg=="초진동나이프"or msg=="초진동 나이프":
        embed=discord.Embed(title="초진동나이프", description=" 공격력 +60\n공격 속도(%) +60%\n이동 속도 +0.1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342852058144798/012._Vibroblade_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="군용 나이프 + 모터", inline=False)
        return embed

    if msg=="다마스커스가시"or msg=="다마스커스가시":
        embed=discord.Embed(title="다마스커스 가시", description=" 공격력 +66\n최대 체력 +200\n```스킬 공격 치유 방해-[고유 장착 효과]\n스킬 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342855883333632/013._Damascus_Steel_Thorn__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="스위스 아미 나이프 + 가시 발판", inline=False)
        return embed

    if msg=="마하라자":
        embed=discord.Embed(title="마하라자", description=" 공격력 +49\n방어력 +15\n ```신속-루드라의 단검-[고유 장착 효과]\n4초 이내에 3회의 개별 피해를 가하면, 3초간 이동 속도가 15%, 공격력이 33% 증가합니다.\n(쿨타임 6초)```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342860014735390/014._Maharaja_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="카라페이스 카타르 + 아이테르 깃털", inline=False)
        return embed

    if msg=="프라가라흐":
        embed=discord.Embed(title="프라가라흐", description=" 공격력 +92\n이동 속도 +0.12\n ```차지드 스트라이크-[고유 장착 효과]\n 매 4초마다 다음 공격이 100%의 치명타 확률 보너스를 획득합니다.```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342864741707846/015._Fragarach_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로 ", value="군용 나이프 + 포스 코어", inline=False)
        return embed
        

#####쌍검#####
    if msg=="쌍칼":
        embed=discord.Embed(title="쌍칼", description=" 공격력 +8", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321971483234344/001._Twin_Swords_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로", value="식칼 + 녹슨 검", inline=False)
        return embed

    if msg=="조잡한쌍칼":
        embed=discord.Embed(title="조잡한 쌍칼", description=" 공격력 +12", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/894235985389428806/002._Wrought_Swords__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="가위 + 곡괭이", inline=False)
        return embed

        
    if msg=="피렌체식쌍검":
        embed=discord.Embed(title="피렌체식 쌍검", description=" 공격력 +28\n생명력 흡수 +10%", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321975295856710/002._Florentine__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="쌍칼 + 정교한 도면", inline=False)
        return embed

    if msg =="쌍둥이검":
        embed=discord.Embed(title="쌍둥이 검", description="공격력 +35", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321976726118450/003._Pocket_Aces_-_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="쌍칼 + 검집", inline=False)
        return embed

    if msg=="이천일류":
        embed=discord.Embed(title="이천일류", description="공격력 +49\n공격 속도(%) +20%\n생명력 흡수+12%\n```스킬 공격 치유 방해-[고유 장착 효과]\n스킬 공격에 피격된 대상의 치유 효과가 4초 동안 40% 감소합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321979968294912/004._Divine_Dual_Swords_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="피렌체식 쌍검 + 가시 발판", inline=False)
        return embed

   
    if msg=="자웅일대검":
        embed=discord.Embed(title="자웅일대검", description=" 공격력 +60\n공격 속도(%) +45%\n기본 공격 추가 피해 +10\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321984187764797/005._Starsteel_Twin_Swords_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="쌍칼 + 문스톤", inline=False)
        return embed
        
    if msg =="디오스쿠로이":
        embed=discord.Embed(title="디오스쿠로이", description=" 공격력 +50\n공격 속도(%) +35%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321988918968320/006._Dioscuri_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="조잡한 쌍검 + 이온 전지", inline=False)
        return embed

    if msg=="로이거차르":
        embed=discord.Embed(title="로이거 차르", description=" 공격력 +45\n 레벨 당 스킬 공격 추가 피해 +2.5\n```저주-[고유 장착 효과]\n스킬 공격을 가하면 적을 초간 저주 상태로 만듭니다.\n저주 상태인 적은 이동 속도가 6%만큼 느려지고, 저주 상태에서 해제 될 때 85 +스킬 증폭*1.5 에 해당하는 고정 피해를 입힙니다.\n한번 저주 상태가 되면 8초간 (기본 공격 피격 시 1초 감소) 다시 저주 상태가 되지 않습니다. (쿨다운 : 2초)```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321992286961664/007._Lioigor___Zahr__.png")
        embed.add_field(name="등급", value="전설", inline=False) 
        embed.add_field(name="휙득 경로", value="쌍둥이 검 + 생명의 나무", inline=False)
        return embed

    if msg=="아수라":
        embed=discord.Embed(title="아수라", description=" 공격력 +48\n쿨다운 감소 +12%\n모든피해 흡혈 +7%\n레벨 당 스킬 증폭 +1%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/894235982805733416/007._Asura_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="피렌체식 쌍검 + 진신사리", inline=False)
        return embed
        

    if msg=="간장과막야":
        embed=discord.Embed(title="간장과막야", description=" 공격력+75\n 공격 속도 +18%\n (고유)기본 공격 사거리 +1\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891322007319347240/008._Spring_and_Autumn__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로 ", value="쌍칼 + 포스 코어", inline=False)
        return embed

#####레이피어#####

    if msg=="바늘":
        embed=discord.Embed(title="바늘", description=" 공격력 +5\n치명타 피해량 +5%\n", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251084057571338/001._Needle_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="골목길(6) 호텔(7) 병원(6)\n사냥 박쥐", inline=False)
        return embed

    if msg=="레이피어":
        embed=discord.Embed(title="레이피어", description=" 공격력 +16\n치명타 피해량 +15%\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251088604176394/002._Rapier_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="바늘 + 철광석", inline=False)
        return embed

    if msg=="매화검":
        embed=discord.Embed(title="매화검", description=" 공격력 +25\n치명타 확률 +10%\n 치명타 피해량 +15%\n 쿨다운 감소 +6%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251096623697962/003._Apricot_Sword_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="레이피어 + 운명의 꽃", inline=False)
        return embed

    if msg=="에스톡":
        embed=discord.Embed(title="에스톡", description=" 공격력 +31", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251101963034695/004._Estoc_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="바늘 + 레이피어", inline=False)
        return embed

    if msg=="활빈검":
        embed=discord.Embed(title="활빈검", description=" 공격력 +30\n체력 재생 +1.5\n스태미너 재생 +150%\n시야 +1\n치명타 피해량 +25%\n쿨다운 감소 +12%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251107415654420/005._Sword_of_Justice_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="레이피어 + 어사의", inline=False)
        return embed

    if msg=="듀랜달Mk2":
        embed=discord.Embed(title="듀랜달 Mk2", description=" 공격력 +55\n시야 +1\n치명타 확률 +12%\n치명타 피해량 +20%\n쿨다운 감소 +6%\n생명력 흡수 +9%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251113694498856/006._Durendal_Mk2__Mk2.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="매화검 + 레이저 포인터", inline=False)
        return embed

    if msg=="볼틱레토":
        embed=discord.Embed(title="볼틱레토", description=" 공격력 +47\n공격 속도(%) +50%\n치명타 확률 +10%\n치명타 피해량 +12%\n쿨다운 감소 +6%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251119151300678/007._Volticletto_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="매화검 + 전자 부품", inline=False)
        return embed

    if msg=="레드팬서":
        embed=discord.Embed(title="레드 팬서", description=" 공격력 +55\n최대 체력 +120\n스테미너 재생 +80%\n스킬 공격 추가피해 +17\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251133344813087/010._Red_Panther__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="에스톡 + 진홍 팔찌", inline=False)
        return embed

    if msg=="유성검":
        embed=discord.Embed(title="유성검", description="공격력 +61\n치명타 피해량 +12%\n쿨다운 감소 +12%\n```차지드 스트라이크-[고유 장착 효과]\n매 3초마다 다음 공격이 100%의 치명타 확률 보너스를 획득합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251124587122688/008._Meteor_Claymore_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="매화검 + 운석", inline=False)
        return embed

    if msg=="주와이외즈":
        embed=discord.Embed(title="주와이외즈", description="공격력 +76\n레벨당 공격속도 +1%\n이동 속도 +0.1\n치명타 피해량 +12%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251128684961872/009._Joyeuse_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="레이피어 + 미스릴", inline=False)
        return embed

    if msg=="미스텔테인":
        embed=discord.Embed(title="미스텔테인", description="공격력 +35\n 체력 재생 +1.5\n 스태미너 재생 +150%\n 치명타 피해량 +25%\n 쿨다운 감소 +15%\n 스킬 증폭 +15%\n 시야 +1\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251138126315611/011._Mistilteinn_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="활빈검 + 나뭇가지", inline=False)
        return embed

    if msg=="에스프리":
        embed=discord.Embed(title="에스프리", description="공격력 +68\n스태미너 재생 +1\n치명타 피해량 +12%\n(고유) 기본 공격 사거리 +0.75\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/916294353306132500/011._Esprit_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="에스톡 + 사격 교본", inline=False)
        return embed
        

#####카메라#####
    if msg=="렌즈":
        embed=discord.Embed(title="렌즈", description="공격력 +12\n시야 +0.5", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865260200452116/001._Lens_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로", value="감시 카메라+유리병", inline=False)
        return embed

    if msg=="카메라건":
        embed=discord.Embed(title="카메라 건", description="공격력 +19\n시야 +1", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865264398958602/002._Pistol_Camera__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="렌즈 + 발터 PPK", inline=False)
        return embed

    if msg=="컴팩트카메라":
        embed=discord.Embed(title="컴팩트 카메라", description=" 공격력 +24\n시야 +1", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865268589043762/003._Compact_Camera__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="위장 카메라 + 렌즈", inline=False)
        return embed

    if msg=="레인지파인더":
        embed=discord.Embed(title="레인지 파인더", description=" 공격력 +40\n 시야 +3.5\n 쿨다운 감소 +6%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865273802559538/004._Rangefinder_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="저격 스코프 + 고장난 시계", inline=False)
        return embed

    if msg=="카메라라이플":
        embed=discord.Embed(title="카메라 라이플", description=" 공격력 +30\n 시야 +2\n(고유)기본 공격 사거리 +0.5", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865279385174097/005._Carbine_Camera__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="카메라 건 + 페도로프 자동소총", inline=False)
        return embed

    if msg=="미러리스":
        embed=discord.Embed(title="미러리스", description=" 공격력 +43\n 시야 +2\n 레벨 당 스킬 증폭 +2%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865286955905044/006._Mirrorless_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="컴팩트 카메라 + 황금", inline=False)
        return embed

    if msg=="카메라캐논":
        embed=discord.Embed(title="카메라 캐논", description=" 공격력 +55\n 최대 체력 +200\n 시야 +4\n (고유)기본 공격 사거리 +1", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865299903737966/008._Cannon_Camera__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="카메라 라이플 + 탄창", inline=False)
        return embed

    if msg=="컴파운드사이트":
        embed=discord.Embed(title="컴파운드 사이트", description=" 공격력 +58\n 시야 +5\n 쿨다운 감소 +15%\n(고유) 최대 쿨다운 감소 +5%", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865306039984128/008._Laser_Designator__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="레인지파인더 + 꽃", inline=False)
        return embed
    
    if msg=="V.I.C.G" or msg=="VICG":
        embed=discord.Embed(title="V.I.C.G", description=" 공격력 +72\n 시야 +1.5\n 기본 공격 추가 피해 +45\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865312750870588/009._V.I.C.G.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="카메라 건 + 휴대폰", inline=False)
        return embed

#####쌍절곤#####
    if msg=="쇠사슬":
        embed=discord.Embed(title="쇠사슬", description=" 공격력 +13", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865028322558002/001._Steel_Chain_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로 ", value="모래사장(8) 골목길(9) 묘지(8)\n사냥 멧돼지", inline=False)
        return embed

    if msg=="눈차크":
        embed=discord.Embed(title="눈차크", description=" 공격력 +29", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865033410244608/002._Nunchaku_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="쇠사슬 + 고철", inline=False)
        return embed

    if msg=="샤퍼":
        embed=discord.Embed(title="샤퍼", description=" 공격력 +29\n ```스킬 공격 치유 방해-[고유 장착 효과]\n 스킬 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.```", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865037801656340/003._Sharper_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="눈차크 + 못", inline=False)
        return embed

    if msg=="블리더":
        embed=discord.Embed(title="블리더 ", description=" 공격력 +38", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865042759344188/004._Bleeder_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="눈차크 + 면도칼", inline=False)
        return embed

    if msg=="대소반룡곤":
        embed=discord.Embed(title="대소반룡곤", description=" 공격력 +50\n 스킬 공격 추가 피해 +22\n ```스킬 공격 치유 방해-[고유 장착 효과]\n 스킬 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865046957846558/005._The_Smiting_Dragon_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="샤퍼 + 재", inline=False)
        return embed

    if msg=="초진동눈차크":
        embed=discord.Embed(title="초진동눈차크", description=" 공격력 +65\n 공격 속도(%) +50%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865052024553482/006._Vibro_Nunchaku_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="블리더 + 모터", inline=False)
        return embed

    if msg=="케로베로스":
        embed=discord.Embed(title="케르베로스", description=" 공격력 +48\n 레벨 당  공격력 +2\n 이동 속도 +0.06\n(고유)기본 공격 사거리 +0.5```기본 공격 치유 방해 - [고유 장착 효과]\n 기본 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.``` ", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865056374050836/007._Cerberus_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="샤퍼 + 체인 레깅스", inline=False)
        return embed

    if msg=="히드라":
        embed=discord.Embed(title="히드라", description=" 공격력 +110\n 모든 피해 흡혈(%) +25%\n쿨다운 감소 +10%", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865060136345620/008._Hydra_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로", value="샤퍼 + 체인 레깅스", inline=False)
        return embed

#####권총#####

    if msg=="발터PPK":
        embed=discord.Embed(title="발터 PPK", description="장탄 수: 6발\n 공격력 +14\n", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864754992328734/001._Walther_PPK__PPK.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="모래사장(4), 호텔(5), 공장(5)", inline=False)
        return embed

    if msg=="매그넘파이썬":
        embed=discord.Embed(title="매그넘-파이썬", description="장탄 수: 6발\n 공격력 +15\n 공격 속도(%) +10%\n 이동속도 +0.1\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864760168108102/002._Magnum-Python_-.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="발터 PPK + 오일", inline=False)
        return embed

    if msg=="베레타M92F" or msg=="베레타":
        embed=discord.Embed(title="베레타 M92F", description="장탄 수: 6발\n 공격력 +23\n 이동속도 +0.1", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864767046766592/003._Beretta_M92F.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="발터 PPK + 가죽", inline=False)
        return embed

    if msg=="매그넘아나콘다":
        embed=discord.Embed(title="매그넘-아나콘다", description="장탄 수: 6발\n 공격력 +43\n 공격 속도(%) +10%\n 이동 속도 +0.1\n 생명력 흡수 +10%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864789679218688/006._Magnum-Anaconda_-.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="매그넘-파이선 + 정교한 도면", inline=False)
        return embed

    if msg=="데린저":
        embed=discord.Embed(title="데린저", description="장탄 수: 2발\n 공격력 +50\n 이동 속도 +0.1\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864795031142521/008._Derringer_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="다이너마이트 + 발터 PPK", inline=False)
        return embed

    if msg=="더블리볼버SP" or msg=="더블리볼버":
        embed=discord.Embed(title="더블 리볼버 SP", description="장탄 수: 6발\n 공격력 +30\n 공격 속도(%) +10%\n 이동 속도 +0.1\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864773610860606/004._FN57.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="매그넘-파이선 + 발터 PPK", inline=False)
        return embed

    if msg=="FN57":
        embed=discord.Embed(title="FN57", description="장탄 수: 6발\n 공격력 +29\n 이동 속도 +0.1\n 시야 +2.5\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864773610860606/004._FN57.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="베레타 M92F + 레이저 포인터", inline=False)
        return embed

    if msg=="마탄의사수":
        embed=discord.Embed(title="마탄의 사수", description="장탄 수: 7발\n 공격력 +48\n 공격 속도(%) +30%\n 이동 속도 +0.1\n 스킬 증폭 +20%\n ```최후의 한발-마탄-[고유 장착 효과]\n 마지막 탄환으로 가하는 기본 공격이 스킬 증폭 * 3 + 스킬 공격 추가 피해 * 2 + 적 최대 체력의 8% 에 해당하는 스킬 피해를 입히고, 입힌 피해의 100%만큼의 체력을 회복합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864801951760384/008._Devil_s_Marksman__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="더블 리볼버 SP + 운석", inline=False)
        return embed

    if msg=="엘레강스":
        embed=discord.Embed(title="엘레강스", description="장탄 수: 6발\n 공격력 +60\n 레벨 당 공격력 +2\n 이동 속도 +0.15\n 시야 +2.5\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864808226443334/009._Elegance_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="FN57 + 먼지털이개", inline=False)
        return embed

    if msg=="일렉트론블라스터":
        embed=discord.Embed(title="일렉트론 블라스터", description="장탄 수: 10발\n 공격력 +63\n 공격 속도(%) +35%\n 이동 속도 +0.1\n 레벨 당 기본 공격 추가 피해 +2\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864813993619466/010._Electron_Blaster__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="베레타 M92F + 이온 전지", inline=False)
        return embed

    if msg=="매그넘보아":
        embed=discord.Embed(title="매그넘-보아", description="장탄 수: 6발\n 공격력 +84\n 공격 속도(%) +25%\n 이동 속도 +0.1\n 생명력 흡수 +22%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864819676897290/011._Magnum-Boa_-.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="매그넘-아나콘다 + 강철", inline=False)
        return embed

    if msg=="글록48":
        embed=discord.Embed(title="글록 48", description="장탄 수: 8발\n 공격력 +77\n 공격 속도(%) +20%\n 이동 속도 +0.1\n 시야 +2.5\n (고유)기본 공격 사거리 +0.75\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864824970088568/012._Glock_48__48.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="FN57 + EMP 드론", inline=False)
        return embed

    if msg=="스탬피드":
        embed=discord.Embed(title="스탬피드", description="장탄 수: 2발\n 공격력 +40\n 이동 속도 +0.1\n 레벨 당 스킬 증폭 +1%\n ```최후의 한발-더블 탭-[고유 장착 효과]\n 마지막 탄환으로 가하는 기본 공격이 스킬 증폭 * 2 + 캐릭터 레벨 * 10 + 적 최대 체력의 8% 에 해당하는 스킬 피해를 입힙니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864830254915604/013._Stempede_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="데린저 + 황금", inline=False)
        return embed

    if msg=="악켈테":
        embed=discord.Embed(title="악켈테", description="장탄 수: 10발\n 공격력 +95\n 공격 속도 +25%\n 이동 속도 +0.1\n 시야 +2\n 방어 관통 +12%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864835875295252/014._Kelte_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="포스코어 + 베레타 M92F", inline=False)
        return embed

######방망이#####

    if msg=="단봉":
        embed=discord.Embed(title="단봉", description=" 공격력 +15", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864611832352819/002._Short_Rod_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="항구(8) 연못(7) 절(7)\n사냥 들개", inline=False)
        return embed

    if msg=="나뭇가지":
        embed=discord.Embed(title="나뭇가지", description=" 공격력 +5", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864605830287380/001._Branch_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="나뭇가지더미 채집", inline=False)
        return embed

    if msg=="장봉":
        embed=discord.Embed(title="장봉", description=" 공격력 +22", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864617213648926/003._Long_Rod_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="단봉 + 대나무", inline=False)
        return embed

    if msg=="도깨비방망이":
        embed=discord.Embed(title="도깨비 방망이", description=" 공격력 +27\n ```기본 공격 치유 방해-[고유 장착 효과]\n기본 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.```", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864623446372362/004._Goblin_Bat__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="장봉 + 못", inline=False)
        return embed

    if msg=="우산":
        embed=discord.Embed(title="우산", description=" 공격력 +30\n 스킬 공격 추가 피해 +14\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864628622143528/005._Umbrella_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="장봉 + 부채", inline=False)
        return embed

    if msg=="횃불":
        embed=discord.Embed(title="횃불", description=" 공격력 +36\n 체력 재생 +0.5\n 공격 속도(%) +10%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864633655300196/006._Torch_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="단봉 + 기름먹인 천", inline=False)
        return embed

    if msg=="몽둥이":
        embed=discord.Embed(title="몽둥이", description=" 공격력 +40\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864642559832115/007._Reinforced_Club_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="단봉 + 강철", inline=False)
        return embed

    if msg=="마법봉":
        embed=discord.Embed(title="마법봉", description=" 공격력 +61\n 모든 피해 흡혈 +15%\n 시야 +1\n 스킬 증폭 +25%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864648436039710/008._Magic_Stick_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="장봉 + 달빛 펜던트", inline=False)
        return embed

    if msg=="금강저":
        embed=discord.Embed(title="금강저", description=" 공격력 +96\n ```차지드 스트라이크-[고유 장착 효과]\n 매 3초마다 다음 공격이 100%의 치명타 확률 보너스를 얻습니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864653599244328/009._Vajra_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="몽둥이 + 유리판", inline=False)
        return embed

    if msg=="구원의여신상":
        embed=discord.Embed(title="구원의 여신상", description=" 공격력 +66\n 레벨 당 공격력 +2\n 체력 재생 +0.6\n 스테미너 재생(%) +80%\n 공격 속도(%) +15%\n 생명력 흡수 +12%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864659102162994/010._Statue_of_Soteria__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="횃불 + 인형", inline=False)
        return embed

    if msg=="타구봉":
        embed=discord.Embed(title="타구봉", description=" 공격력 +81\n 공격 속도(%) +50%\n ```기본 공격 치유 방해-[고유 장착 효과]\n 기본 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864665389412382/011._Mallet_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="도깨비 방망이 + 전자 부품", inline=False)
        return embed

    if msg=="스파이의우산":
        embed=discord.Embed(title="스파이의 우산", description=" 공격력 +65\n 스테미너 재생 +0.8\n 스킬 공격 추가 피해 +25\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864673794818089/012._Spy_Umbrella__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="우산 + 재", inline=False)
        return embed

    if msg=="여의봉":
        embed=discord.Embed(title="여의봉", description=" 공격력 +135\n 공격 속도 +10%\n (고유)기본 공격 사거리 +1", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864681067724900/013._Monkey_King_Bar_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="포스 코어 + 장봉", inline=False)
        return embed


######도끼#####

    if msg=="손도끼":
        embed=discord.Embed(title="손도끼", description=" 공격력 +25", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366076565303306/002._Hatchet_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로", value="연못(5) 모래사장(5) 공장(5)\n사냥 들개", inline=False)
        return embed

    if msg=="곡괭이":
        embed=discord.Embed(title="곡괭이", description=" 공격력 +15", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366069443375195/001._Pickaxe_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로", value="연못(9) 모래사장(8) 묘지(8) 숲(9)\n사냥 박쥐", inline=False)
        return embed

    if msg== "전투도끼":
        embed=discord.Embed(title="전투도끼", description=" 공격력 +47", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366084677091368/04._Battle_Axe__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="손도끼+대나무", inline=False)
        return embed

    if msg=="사슬낫":
        embed=discord.Embed(title="사슬낫", description=" 공격력 +50\n (고유)기본 공격 사거리 +0.2", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366080038191134/003._Chain_Scythe__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="곡괭이+쇠사슬", inline=False)
        return embed

    if msg=="사신의낫":
        embed=discord.Embed(title="사신의낫", description=" 공격력 +80\n (고유)기본 공격 사거리 +0.5", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366100279918652/006._Reaper_s_Scythe.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="사슬 낫+단봉", inline=False)
        return embed

    if msg=="경령화도끼":
        embed=discord.Embed(title="경령화 도끼", description=" 공격력 +61\n 이동속도 +0.04\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366090725290054/005._Light_Hatchet__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="전투 도끼 + 깃털", inline=False)
        return embed

    if msg=="대부":
        embed=discord.Embed(title="대부", description=" 공격력 +110\n 이동 속도 -0.1", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366106546176010/007._Gigantic_Axe_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="전투 도끼 + 강철", inline=False)
        return embed

    if msg=="빔엑스":
        embed=discord.Embed(title="빔 엑스", description=" 공격력 +102\n 레벨당  공격력 +2\n 시야 +3\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366112263024650/008._Beam_Axe__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="대부 + 레이저 포인터", inline=False)
        return embed

    if msg=="산타무에르페":
        embed=discord.Embed(title="산타 무에르페", description=" 공격력 +110\n 최대 체력 +200\n (고유)기본 공격 사거리 +0.75", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366117640122388/009._Santa_Muerte__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="사신의 낫 + 루비", inline=False)
        return embed

    if msg=="스퀴테":
        embed=discord.Embed(title="스퀴테", description=" 공격력 +115\n 레벨 당 스킬 증폭 +2%\n (고유)기본 공격 사거리 +1", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366122300006421/010._Scythe_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="사신의 낫 + 황금", inline=False)
        return embed

    if msg=="파라슈":
        embed=discord.Embed(title="파라슈", description=" 공격력 +118\n 이동 속도 +0.06\n 쿨다운 감소 +15%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366127446405150/011._Parashu_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="경량화 도끼 + 진신사리", inline=False)
        return embed

    if msg=="저거너트":
        embed=discord.Embed(title="저거너트", description=" 공격력 +92\n기본 공격 사거리 -0.2\n이동 속도 +0.04\n공격 속도 20%\n```열정-[고유 장착 효과]\n기본 공격이 적 실험체에게 적중 시, 적 실험체의 현재 체력의 7%의 피해를 주고, 5초간 열정 스택을 획득하며, 중첩된 열정 스택 당 8%의 공격 속도를 얻습니다.\n최대 3 중첩이 되면 20 의 공격력과 0.2의 이동 속도를 추가로 얻습니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366132706054154/012._The_Juggernaut_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="경랑화 도끼 + 모터", inline=False)
        return embed
    

    if msg=="하르페":
        embed=discord.Embed(title="하르페 ", description=" 공격력 +108\n 생명력 흡수 +20%\n ```가벼운 발걸음-[고유 장착 효과]\n0.2m 이동할 때마다 [가벼운 발걸음]을 최대 100회까지 중첩해서 획득합니다.\n중첩에 따라 이동속도가 최대 0.08까지 증가합니다.\n기본 공격 피해를 입힐 경우 중첩을 모두 소모하여 최대 120의 고유 피해를 입힙니다.\n최대 중첩 상태에서 기본 공격에 피격된 대상의 이동속도를 2초간 25% 감소 시킵니다.```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366137101684766/013._Harpe_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로 ", value="대부+해적 깃발", inline=False)
        return embed

    if msg=="반고부":
        embed=discord.Embed(title="하르페 ", description="공격력 +145\n(고유) 방해 효과 저항 30%", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366137101684766/013._Harpe_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로 ", value="전투 도끼 + 포스 코어", inline=False)
        return embed
        

######톤파######
    if msg=="대나무":
        embed=discord.Embed(title="대나무", description=" 공격력 +12", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289517330006026/001._Bamboo_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="연못(8) 절(6) 양궁장(5) 묘지(7) 숲(7)\n사냥 박쥐", inline=False)
        return embed

    if msg=="톤파":
        embed=discord.Embed(title="톤파", description=" 공격력 +23\n 방어력 +8\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289522346369034/002._Wooden_Tonfa_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="대나무 + 나뭇가지", inline=False)
        return embed

    if msg=="경찰봉":
        embed=discord.Embed(title="경찰봉", description=" 공격력 +31\n 방어력 +10\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289527987707944/003._Police_Baton_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="톤파 + 마패", inline=False)
        return embed

    if msg=="류쿠톤파":
        embed=discord.Embed(title="류큐톤파", description=" 공격력 +38\n 방어력 +18\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289533016674314/004._Ryuku_Tonfa__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="톤파 + 백색 가루", inline=False)
        return embed

    if msg=="택티컬톤파":
        embed=discord.Embed(title="택티컬 톤파", description=" 공격력 +74\n 방어력 +16\n 생명력 흡수 +20%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289537965973514/005._Tactical_Tonfa__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="경찰봉 + 정교한 도면", inline=False)
        return embed

    if msg=="마이쏙":
        embed=discord.Embed(title="마이쏙", description=" 공격력 +63\n 방어력 +18\n 레벨 당 방어력 +1\n 체력 재생(%) +100%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289544559419452/006._Mai_Sok_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="류큐톤파 + 단봉", inline=False)
        return embed

    if msg=="플라즈마톤파":
        embed=discord.Embed(title="플라즈마 톤파", description=" 공격력 +60\n 방어력 +21\n 시야 +2\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289549835829258/007._Plasma_Tonfa__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="류큐톤파 + 레이저 포인터", inline=False)
        return embed

    if msg=="윈드러너":
        embed=discord.Embed(title="윈드러너", description=" 공격력 +70\n 방어력 +8\n 이동 속도 +0.1\n ```신속-산들바람-[고유 장착 효과]\n 4초 이내에 3회의 개별 피해를 가하면, 2.5초간 이동 속도가 8% 증가하고, 공격 속도가 30% 증가하며 225의 보호막을 얻습니다.\n(쿨다운 6초)```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289554332135444/008._Windrunner_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="톤파 + 미스릴 실", inline=False)
        return embed

    if msg=="흑요석짓테":
        embed=discord.Embed(title="흑요석 짓테", description=" 공격력 +75\n 방어력 +25\n ```저주-[고유 장착 효과]\n 스킬 공격을 가하면 적을 4초간 저주 상태로 만듭니다.\n저주 상태인 적은 이동 속도가 10%만큼 느려지고, 저주 상태에서 해제 될 때 75 +스킬 증폭 * 1.75에 해당하는 고정 피해를 입힙니다.\n한번 저주 상태가 되면 8초간 (기본 공격 피격 시 1초 감소) 다시 저주 상태가 되지 않습니다.\n(쿨다운 : 2초)```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289558861979719/009._Obsidian_Jitte__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="경찰봉 + 포스 코어", inline=False)
        return embed

######저격총######
    if msg=="화승총":
        embed=discord.Embed(title="화승총", description="장탄 수: 1발\n공격력 +30", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472485552332910/001._Long_Rifle_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="항구(3) 숲(3)", inline=False)
        return embed
        
    if msg=="스프링필드":
        embed=discord.Embed(title="스프링필드", description="장탄 수: 1발\n 공격력 +40\n 시야 +1.5\n", color=0x1eb300)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472489578872853/002._Springfield_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="화승총 + 레이저 포인터", inline=False)
        return embed
        
    if msg=="하푼건":
        embed=discord.Embed(title="하푼건", description="장탄 수: 2발\n 공격력 +60\n시야 +2\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472493865435196/003._Harpoon_Gun_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="스프링필드 + 단창", inline=False)
        return embed
        
    if msg=="레일건":
        embed=discord.Embed(title="레일건", description="장탄 수: 3발\n 공격력 +65\n 공격 속도(%) +20%\n 시야 +2\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472501926899772/005._Railgun_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="스프링필드 + 전자 부품", inline=False)
        return embed    

    if msg=="금교전":
        embed=discord.Embed(title="금교전", description="장탄 수: 1발\n 공격력 +50\n 시야 +1.5\n 스킬 증폭 +18%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472497824874546/004._Golden_Rifle_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="스프링필드 + 황금", inline=False)
        return embed
        
    if msg=="폴라리스":
        embed=discord.Embed(title="폴라리스", description="장탄 수: 4발\n 공격력 +107\n 공격 속도(%) +18%\n 레벨당 공격속도 +2%\n 시야 +2\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472519224209478/009._Polaris_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="레일건 + 백색 가루", inline=False)
        return embed
        
    if msg=="인터벤션":
        embed=discord.Embed(title="인터벤션", description="장탄 수: 2발\n 공격력 +100\n 시야 +3\n (고유)기본 공격 사거리 +1", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472510999179264/007._Intervention_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="하푼건 + 망원 카메라", inline=False)
        return embed
        
    if msg=="tac-50":
        embed=discord.Embed(title="Tac-50", description="장탄 수: 2발\n 공격력 +94\n 레벨 당 공격력 +2\n 시야 +2\n 생명력 흡수 +14%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472506435780638/006._Tac-50.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="하푼건 + 정교한 도면", inline=False)
        return embed
        
    if msg=="NTW-20":
        embed=discord.Embed(title="NTW-20", description="장탄 수: 1발\n 공격력 +82\n 시야 +1.5\n 스킬 증폭 +18%\n", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472515193495614/008._NTW-20.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="금교전 + 철판", inline=False)
        return embed
        
    if msg=="사사성광":
        embed=discord.Embed(title="사사성광", description="장탄 수: 2발\n 공격력 +100\n 시야 +2.5\n 스킬 증폭 +24%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472522919407676/010._The_Deadly_Ray_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="문스톤 + 금교전", inline=False)
        return embed
        
    if msg=="현자총통":
        embed=discord.Embed(title="현자총통", description="장탄 수: 1발\n 공격력 +155\n기본 공격 사거리 -1\n```철환-[고유 장착 효과]\n다음에 가하는 기본 공격이 115의 추가 고유 피해를 주고 0.56초 동안 이동속도를 99% 만큼 감소시킵니다.\n(쿨다운 : 4초)```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472527197573170/011._Blackfire_Cannon_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="스프링필드 + 삼매진화", inline=False)
        return embed
        
######돌격소총######
    if msg=="페도로프자동소총":
        embed=discord.Embed(title="페도로프 자동소총", description="장탄 수: 30발\n공격력 +11\n", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472409845141554/001._Fedorova__.png")
        embed.add_field(name="등급 ", value="일반 ", inline=False)
        embed.add_field(name="휙득 경로", value="호텔(5) 고급 주택가(5) 공장(5)", inline=False)
        return embed

    if msg=="STG-44":
        embed=discord.Embed(title="STG-44", description="장탄 수: 30발\n 공격력 +18\n 시야 +1.5\n 기본 공격 추가 피해 +2\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472413016031312/002._STG-44.png")
        embed.add_field(name="등급 ", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="페도로프 자동소총 + 화약", inline=False)
        return embed

    if msg=="AK-47":
        embed=discord.Embed(title="AK-47", description="장탄 수: 30발\n 공격력 +29\n 시야 +1.5\n 기본 공격 추가 피해 +2\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472416920936499/003._AK-47.png")
        embed.add_field(name="등급 ", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="STG-44 + 피아노선", inline=False)
        return embed

    if msg=="M16A1":
        embed=discord.Embed(title="M16A1", description="장탄 수: 30발\n 공격력 +25\n 시야 +1.5\n 기본 공격 추가 피해 +4\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472422931374080/004._M16A1.png")
        embed.add_field(name="등급 ", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="STG-44 + 가죽", inline=False)
        return embed

    if msg=="개틀링건":
        embed=discord.Embed(title="개틀링 건", description="장탄 수: 30발\n 공격력 +20\n 공격 속도(%) +10%\n 시야 +1.5\n 기본 공격 추가 피해 +11\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472430569201704/005._Gatling_Gun_.png")
        embed.add_field(name="등급 ", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="STG-44 + 모터", inline=False)
        return embed
            
    if msg=="95식자동소총":
        embed=discord.Embed(title="95식 자동 소총", description="장탄 수: 30발\n 공격력 +84\n 시야 +2\n (고유)기본 공격 사거리 +1", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472435556253716/006._Type_95_95_.png")
        embed.add_field(name="등급 ", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="AK-47 + 강철", inline=False)
        return embed

    if msg=="AK-12":
        embed=discord.Embed(title="AK-12", description="장탄 수: 30발\n 공격력 +68\n 레벨 당  공격력 +2\n 시야 +1.5\n 치명타 확률 +22%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472439746355240/007._AK-12.png")
        embed.add_field(name="등급 ", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="AK-47 + 유리판", inline=False)
        return embed

    if msg=="XCR":
        embed=discord.Embed(title="XCR", description="장탄 수: 30발\n 공격력 +61\n 최대 체력 +200\n 시야 +1.5\n 기본 공격 추가 피해 +10\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472444225847376/008._XCR.png")
        embed.add_field(name="등급 ", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="M16A1 + 탄창", inline=False)
        return embed

    if msg=="저지먼트":
        embed=discord.Embed(title="저지먼트", description="장탄 수: 120발\n공격력 +120\n시야 +1.5\n방어 관통 +12%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472448168521848/009._Judgement_.png")
        embed.add_field(name="등급 ", value="전설", inline=False)
        embed.add_field(name="휙득 경로", value="포스 코어 + STG-44", inline=False)
        return embed

    if msg=="아그니":
        embed=discord.Embed(title="아그니", description="장탄 수: 30발\n공격력 +51\n공격 속도 +25%\n시야 +1.5\n기본 공격 추가 피해 +16\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472452379607080/010._Agni_.png")
        embed.add_field(name="등급 ", value="전설", inline=False)
        embed.add_field(name="휙득 경로", value="개틀링 건 + 뜨거운 오일", inline=False)
        return embed

######활######
    
    if msg=="양궁":
        embed=discord.Embed(title="양궁", description="공격력 +11", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473123468238928/001._Bow_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="양궁장(5) 성당(4)", inline=False)
        return embed

    if msg=="목궁":
        embed=discord.Embed(title="목궁", description=" 공격력 +26", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473127687684166/002._Wooden_Bow_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="양궁 + 피아노선", inline=False)
        return embed

    if msg=="장궁":
        embed=discord.Embed(title="장궁", description=" 공격력 +25", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473132129456188/003._Longbow_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="양궁 + 고무", inline=False)
        return embed
        
    if msg=="컴포지트보우":
        embed=discord.Embed(title="컴포지트 보우", description=" 공격력 +25\n ```기본 공격 치유 방해-[고유 장착 효과]\n기본 공격에 피격된 대상의 치유 효과가 4초 동안 35% 감소합니다.```", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473136508321812/004._Composite_Bow__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="장궁 + 못", inline=False)
        return embed

    if msg=="강궁":
        embed=discord.Embed(title="강궁", description=" 공격력 +35", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473140513873930/005._Strong_Bow_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="목궁 + 오일", inline=False)
        return embed

    if msg=="국궁":
        embed=discord.Embed(title="국궁", description=" 공격력 +20\n기본 공격 추가 피해 +25\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473145081491466/006._Stallion_Bow_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="벽력궁 + 마패", inline=False)
        return embed

    if msg=="벽력궁":
        embed=discord.Embed(title="벽력궁", description=" 공격력 +25\n기본 공격 추가 피해 +11", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473149342904360/007._Mighty_Bow_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="장궁 + 화약", inline=False)
        return embed

    if msg=="탄궁":
        embed=discord.Embed(title="탄궁", description=" 공격력 +55", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473153625292810/008._Pellet_Bow_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="목궁 + 달궈진 돌맹이", inline=False)
        return embed

    if msg=="화전":
        embed=discord.Embed(title="화전", description=" 공격력 +22\n스킬 공격 추가 피해 +14", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473157907673159/009._Scorchbow_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="장궁 + 라이터", inline=False)
        return embed

    if msg=="편전":
        embed=discord.Embed(title="편전", description=" 공격력 +65\n레벨 당 기본 공격 추가 피해 +2", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473163481886760/010._Ancient_Bolt_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="국궁 + 대나무", inline=False)
        return embed
        
    if msg=="골든래쇼보우":
        embed=discord.Embed(title="골든래쇼 보우", description=" 공격력 +68\n쿨다운 감소 +15%\n스킬 증폭 +10%\n레벨 당 스킬 증폭 +1%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473167248384100/011._Golden-Ratio_Bow__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="탄궁 + 황금", inline=False)
        return embed

    if msg=="트윈보우":
        embed=discord.Embed(title="트윈보우", description=" 공격력 +40\n레벨 당  공격력 +2\n공격 속도(%) +40%\n시야 +1\n ```기본 공격 치유 방해-[고유 장착 효과]\n기본 공격에 피격된 대상의 치유 효과가 4초 동안 35% 감소합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473172008910879/012._Twinbow__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="강궁 + 컴포지트 보우", inline=False)
        return embed

    if msg=="제베의활":
        embed=discord.Embed(title="제베의 활", description=" 공격력 +82\n공격 속도 +33%\n이동 속도 +0.06\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473177469898752/013._Jebe_s_Altered_Bow__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="벽력궁 + 궁기병의 화살통", inline=False)
        return embed

    if msg=="아르테미스":
        embed=discord.Embed(title="아르테미스", description=" 공격력 +90\n최대 체력 +150\n시야 +2\n스킬 증폭 +25%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473181156683796/014._Artemis_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="강궁 + 문스톤", inline=False)
        return embed

    if msg=="엘리멘탈보우":
        embed=discord.Embed(title="엘리멘탈 보우", description=" 공격력 +60\n 이동 속도 +0.06\n 스킬 공격 추가 피해 +35\n ```스킬 공격 치유 방해-[고유 장착 효과]\n스킬 공격에 피격된 대상의 치유 효과가 4초 동안 35% 감소합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473185728467014/015._Elemental_Bow__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="화전 + 백우선", inline=False)
        return embed

    if msg=="페일노트":
        embed=discord.Embed(title="페일노트", description=" 공격력 +110\n레벨 당 공격속도 +2%\n모든 피해 흡혈 +15%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473190484819988/016._Failnaught_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="VF 혈액 샘플 + 강궁", inline=False)
        return embed
            
    if msg=="아르기로톡소스":
        embed=discord.Embed(title="아르기로톡소스", description=" 공격력 +103\n스킬 증폭 +20%\n방어 관통 10%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473194481995847/017._Argyrotoxus_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="포스코어 + 장궁", inline=False)
        return embed

#####석궁#####
    if msg =="석궁":
        embed=discord.Embed(title="석궁", description=" 공격력 +12", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251213300854884/001._Short_Crossbow_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="숲(5) 성당(5)", inline=False)
        return embed

    if msg =="쇠뇌":
        embed=discord.Embed(title="쇠뇌", description=" 공격력 +30", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251219546144798/002._Long_Crossbow_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="석궁 + 피아노선", inline=False)
        return embed

    if msg =="크로스보우":
        embed=discord.Embed(title="크로스보우", description=" 공격력 +30", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251223660769301/003._Crossbow_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="석궁 + 대나무", inline=False)
        return embed

    if msg =="노":
        embed=discord.Embed(title="노", description=" 공격력 +42", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251229474070578/004._Power_Crossbow_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="쇠뇌 + 고무", inline=False)
        return embed

    if msg =="저격궁":
        embed=discord.Embed(title="저격궁", description=" 공격력 +30\n시야 +1\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251233978773564/005._Laser_Crossbow_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="크로스보우 + 레이저 포인터", inline=False)
        return embed

    if msg =="헤비크로스보우":
        embed=discord.Embed(title="헤비 크로스보우", description=" 공격력 +55", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251242354798622/006._Heavy_Crossbow__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="쇠뇌 + 강철", inline=False)
        return embed

    if msg =="철궁":
        embed=discord.Embed(title="철궁", description=" 공격력 +52", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251249145360404/007._Steel_Bow_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="크로스보우 + 철판", inline=False)
        return embed

    if msg =="대황":
        embed=discord.Embed(title="대황", description=" 공격력 +75\n체력 재생 +2\n공격 속도(%) +50%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251255805927496/008._The_Legend_of_The_General_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="철궁 + 기름먹인 천", inline=False)
        return embed

    if msg =="발리스타":
        embed=discord.Embed(title="발리스타", description=" 공격력 +75\n레벨 당 스킬 증폭 +2%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251261841526834/009._Ballista_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="헤비 크로스보우 + 단창", inline=False)
        return embed

    if msg =="저격크로스보우":
        embed=discord.Embed(title="저격 크로스보우", description=" 공격력 +83\n시야 +2\n (고유)기본 공격 사거리 +0.75", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251268367863860/010._Sniper_Crossbow__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="저격궁 + 저격 스코프", inline=False)
        return embed

    if msg =="영광금귀신기노":
        embed=discord.Embed(title="영광금귀신기노", description=" 공격력 +73\n기본 공격 추가 피해 +22\n레벨 당 기본 공격 추가 피해 +2\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251275854704680/011._The_Golden_Ghost_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="노 + RDX", inline=False)
        return embed

    if msg =="샤릉가":
        embed=discord.Embed(title="샤릉가", description=" 공격력 +128\n시야 +2.5\n ```가벼운 발놀림-[고유 장착 효과]\n0.24m 이동할 때마다 [가벼운 발놀림]을 최대 100회까지 중첩해서 획득합니다.\n중첩에 따라 이동속도가 최대 0.12까지 증가합니다.\n기본 공격 피해를 입힐 경우 중첩을 모두 소모하여 최대 120의 고유 피해를 입힙니다.```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251282200662097/012._Sharanga_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="포스 코어 + 크로스보우", inline=False)
        return embed

#####아르카나######
    if msg=="유리구슬":
        embed=discord.Embed(title="유리구슬", description=" 공격력 +10", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522502680297512/001._Glass_Bead_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="유리병 + 라이터", inline=False)    
        return embed

    if msg=="거울구슬":
        embed=discord.Embed(title="거울구슬", description=" 공격력 +25", color=0x1eb300)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522505830211624/002._Mirror_Core_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="유리구슬 + 알코올", inline=False)
        return embed

    if msg=="얼음구슬":
        embed=discord.Embed(title="얼음구슬", description=" 공격력 +15\n쿨다운 감소 +5%\n", color=0x1eb300)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522510397825084/003._Frigid_Pearl_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="유리구슬 + 얼음", inline=False)
        return embed

    if msg=="의지의지팡이":
        embed=discord.Embed(title="의지의 지팡이", description=" 공격력 +47", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522513879072868/004._Staff_of_Reliance_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="거울구슬 + 단봉", inline=False)
        return embed

    if msg=="감정의컵":
        embed=discord.Embed(title="감정의 컵", description=" 공격력 +40\n체력 재생 +80%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522519302311946/005._Sensibility__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="거울구슬 + 성배", inline=False)
        return embed

    if msg=="이성의칼":
        embed=discord.Embed(title="이성의 칼", description=" 공격력 +30\n쿨다운 감소 +8%\n이동 속도 +0.04\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522524679405588/006._Frigid_Pearl_Blade__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="얼음구슬 + 식칼", inline=False)
        return embed

    if msg=="소유의펜타클":
        embed=discord.Embed(title="소유의 펜타클", description="공격력 +30\n쿨다운 감소 +8%\n시야 +1.5\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522529645494292/007._Possession_Pentacle__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="얼음구슬 + 마패", inline=False)
        return embed

    if msg=="은둔자":
        embed=discord.Embed(title="은둔자", description=" 공격력 +66\n ```저주-[고유 장착 효과]\n스킬 공격을 가하면 적을 4초간 저주 상태로 만듭니다.\n저주 상태인 적은 이동 속도가 8% 느려지고, 저주 상태에서 해제될 때 50 + 스킬 증폭의 2.25배에 해당하는 고정 피해를 입습니다.\n한번 저주 상태가 되면 8초 동안 다시 저주 상태에 걸리지 않으며, 저주의 사용자가 대상에게 기본 공격을 적중시킬 때 마다 저주 대기 시간이 1초 씩 감소합니다.\n(쿨다운: 2초)```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522534036926524/008._The_Hermit_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="의지의 지팡이 + 성자의 유산", inline=False)
        return embed

    if msg=="운명의수레바퀴":
        embed=discord.Embed(title="운명의 수레바퀴", description=" 공격력 +36\n최대 체력 +225\n이동 속도 +0.1\n ```리플렉션-[고유 장착 효과]\n기본 공격 피해의 3%를 고정 피해로 반사 피격 시 치유 감소 40(근거리)/30(원거리)% 4초안에 450의 피해를 받으면, 일정 범위 내의 적에게 215의 고유 피해를 줍니다.\n(쿨다운: 1초)```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522537904054302/009._The_Hierophant__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="이성의 칼 + 운명의 꽃", inline=False)
        return embed

    if msg=="절제":
        embed=discord.Embed(title="절제", description=" 공격력 +66\n 방어력 -25\n체력 재생 +100%\n스태미너 재생 +125%\n주는 회복 증가 +25%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522542098350121/010._Temperance_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="감정의 컵 + 정화수", inline=False)
        return embed

    if msg=="더스타":
        embed=discord.Embed(title="더 스타", description=" 공격력 +69\n쿨다운 감소 +10%\n시야 +2\n스킬 증폭 +15%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522545965514752/011._The_Star__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="소유의 펜타클 + 바브드 블로섬", inline=False)
        return embed

    if msg=="더문":
        embed=discord.Embed(title="더 문", description=" 공격력 +90\n스킬 증폭 +10%\n시야 +3\n ```굴절-[고유 장착 효과]\n 굴절의 망토를 두릅니다.\n굴절의 망토는 적이 나에게 가하는 다음 스킬 및 트랩의 피해와 효과를 한번 보호해 준 뒤 사라지고, 35초 후 재생성 됩니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522550210166834/012._The_Moon__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="거울구슬 + 문스톤", inline=False)
        return embed

#####기타#####
    if msg=="보급형기타":
        embed=discord.Embed(title="보급형 기타", description=" 공격력 +5", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652762091032627/001._Starter_Guitar__.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="대나무 + 피아노선", inline=False)
        return embed

    if msg=="골든브릿지":
        embed=discord.Embed(title="골든 브릿지", description=" 공격력 +8\n스킬 증폭 +14%\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652770337038417/002._Golden_Bridge__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="보급형 기타 + 황금", inline=False)
        return embed

    if msg=="싱글픽업":
        embed=discord.Embed(title="싱글 픽업", description=" 공격력 +8\n공격 속도 +15%\n기본 공격 추가 피해 +2\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652770337038417/002._Golden_Bridge__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="보급형 기타 + 방전 전지", inline=False)
        return embed

    if msg=="루비스페셜":
        embed=discord.Embed(title="루비 스페셜", description=" 공격력 +20\n최대 체력 +150\n공격 속도(%) +20%\n기본 공격 추가 피해 +2\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652770337038417/002._Golden_Bridge__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="싱글 픽업 + 루비", inline=False)
        return embed

    if msg=="험버커픽업":
        embed=discord.Embed(title="험버커 픽업", description=" 공격력 +25\n시야 +3\n스킬 증폭 +15%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652795515441172/005._Humbucker_Pickup__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="골든 브릿지 + 저격 스코프", inline=False)
        return embed

    if msg=="King-V":
        embed=discord.Embed(title="King-V", description=" 공격력 +13\n 스킬 증폭 +16%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652795515441172/005._Humbucker_Pickup__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="골든 브릿지 + 가위", inline=False)
        return embed

    if msg=="노캐스터":
        embed=discord.Embed(title="노캐스터", description=" 공격력 +15\n 공격 속도 +20%\n 생명력 흡수 +10%\n 기본 공격 추가 피해 +10\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652811642540033/007._Nocaster_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="싱글 픽업 + 정교한 도면", inline=False)
        return embed

    if msg=="슈퍼스트랫":
        embed=discord.Embed(title="슈퍼스트랫", description=" 공격력 +19\n 공격 속도 +15%\n 기본 공격 추가 피해 +2\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652819175510066/008._Superstrat__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="싱글 픽업 + 대나무", inline=False)
        return embed

    if msg=="야생마":
        embed=discord.Embed(title="야생마", description=" 공격력 +9\n 공격 속도 +25%\n 기본 공격 추가 피해 +6\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652819175510066/008._Superstrat__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="싱글 픽업 + 오일", inline=False)
        return embed

    if msg=="보헤미안":
        embed=discord.Embed(title="보헤미안", description=" 공격력 +50\n최대 체력 +200\n공격 속도 +40%\n치명타 확률 +22%\n기본 공격 추가 피해 +2\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652839173976135/010._Bohemian_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="루비 스폐셜 + 트럼프 카드", inline=False)
        return embed

    if msg=="천국의계단":
        embed=discord.Embed(title="천국의 계단", description=" 공격력 +66\n체력 재생 +200%\n시야 +3\n쿨다운 감소 +5%\n스킬 증폭 +18%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652849143840788/011._Stairway_to_Heaven__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="험버커 픽업 + 성배", inline=False)
        return embed

    if msg=="퍼플헤이즈":
        embed=discord.Embed(title="퍼플 헤이즈", description=" 공격력 +85\n스킬 증폭 +23%\n스태미너 재생 +1\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652860128702525/012._Purple_Haze__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="King-V + 재", inline=False)
        return embed

    if msg=="새티스팩션":
        embed=discord.Embed(title="새티스팩션", description=" 공격력 +30\n공격 속도 +40%\n생명력 흡수 +18%\n기본 공격 추가 피해 +15\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652870463479818/013._Satisfaction_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="노캐스터 + 분필", inline=False)
        return embed

    if msg=="원더풀투나잇":
        embed=discord.Embed(title="원더풀 투나잇", description=" 공격력 +85\n공격 속도 +15%\n기본 공격 추가 피해 +2\n ```열정-[고유 효과]\n기본 공격이 적 실험체에게 명중하면, 적 실험체에게 현재 체력의 5%에 해당하는 고유 피해를 입히며 열정 버프를 1스택 획득합니다.\n 열정: 버프\n 공격 속도 8% 증가\n 지속 시간: 4초\n 최대 스택: 5스택\n최대 스택이 쌓인 경우 15의 공격력과 0.1의 이동 속도를 추가로 얻습니다.```", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652879128920154/014._Wonderful_Tonight__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="슈퍼스트랫 + 운석", inline=False)
        return embed

    if msg=="더월":
        embed=discord.Embed(title="더 월", description=" 공격력 +75\n공격 속도 +20%\n기본 공격 추가 피해 +2\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652892101881906/015._The_Wall__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="슈퍼스트랫 + 백색 가루", inline=False)
        return embed

    if msg=="틴스피릿":
        embed=discord.Embed(title="틴 스피릿", description=" 공격력 +18\n공격 속도 +40%\n기본 공격 추가 피해 +5\n레벨당 기본 공격 추가 피해 +1\n (고유)기본 공격 사거리 +0.75", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894652734987448330/894652904898723860/016._Wild_Horst__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="야생마 + 진신사리", inline=False)
        return embed

#####창#####
    if msg=="단창":
        embed=discord.Embed(title="단창", description="공격력 +15", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472580054192138/896472706374074448/001._Short_Spear_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="연못(4), 절(5), 숲(5), 멧돼지", inline=False)
        return embed

    if msg=="죽창":
        embed=discord.Embed(title="죽창", description="공격력 +32", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472580054192138/896472710362845214/002._Bamboo_Spear_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="단창 + 대나무", inline=False)
        return embed

    if msg=="바이던트":
        embed=discord.Embed(title="바이던트", description="공격력 +52", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472580054192138/896472715194675281/003._Bident_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="죽창 + 식칼", inline=False)
        return embed

    if msg=="파이크":
        embed=discord.Embed(title="파이크", description="공격력 +45", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472580054192138/896472719342854274/004._Pike_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="단창 + 강철", inline=False)
        return embed

    if msg=="도끼창":
        embed=discord.Embed(title="도끼창", description="공격력 +60", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472580054192138/896472724401180682/005._Halberd_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="손도끼 + 파이크", inline=False)
        return embed

    if msg=="강창":
        embed=discord.Embed(title="강창", description="공격력 +40\n이동 속도 +0.06", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472580054192138/896472729044271174/006._Shapened_Spear_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="죽창 + 깃털", inline=False)
        return embed

    if msg=="애각창":
        embed=discord.Embed(title="애각창", description="공격력 +85\n레벨 당 공격력 +2\n이동 속도 +0.08", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472580054192138/896472735516098590/007._Gentian_Silver_Gun_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="강창 + 백색 가루", inline=False)
        return embed

    if msg=="장팔사모":
        embed=discord.Embed(title="장팔사모", description="공격력 +110\n공격 속도(%) +40%\n이동 속도 +0.06", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472580054192138/896472738548580372/008._Eighteen_Foor_Spear_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="강창 + 이온 전지", inline=False)
        return embed

    if msg=="코스믹바이던트":
        embed=discord.Embed(title="코스믹 바이던트", description="공격력 +135\n레벨 당 공격속도 +1%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472580054192138/896472744097620018/009._Cosmic_Bident__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="바이던트 + 문스톤", inline=False)
        return embed

    if msg=="트리아이나":
        embed=discord.Embed(title="트리아이나", description="공격력 +90\n스킬 증폭 +21%\n쿨다운 감소 +5%", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472580054192138/896472749105643520/011._Lance_of_Poseidon_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="바이던트 + 파이크", inline=False)
        return embed

    if msg=="청룡언월도":
        embed=discord.Embed(title="청룡언월도", description="공격력 +118\n최대 체력 +120\n레벨 당 최대 체력 +5\n이동 속도 -0.05\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472580054192138/896472752691744838/012._Dragon_Guandao_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="도끼창 + 철판", inline=False)
        return embed

    if msg=="방천화극":
        embed=discord.Embed(title="방천화극", description="공격력 +84\n이동 속도 -0.07\n스킬 공격 추가 피해 +21\n레벨 당 스킬 공격 추가피해 +1\n```스킬 공격 치유 방해-[고유 장착 효과]\n스킬 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.```", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472580054192138/896472757758488586/012._Fangtian_Huaji_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="도끼창 + 군선", inline=False)
        return embed

    if msg=="화첨창":
        embed=discord.Embed(title="화첨창", description="공격력 +60\n공격 속도 +30%```발화-[고유 장착 효과]\n기본 공격의 대상에게 최대 4회 중첩되는 [타오르는 고통] 효과를 4초 동안 부여 합니다.\n[타오르는 고통]은 매 초마다 대상 최대 체력의 1.2%를 피해로 줍니다.```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472580054192138/896472761352990760/013._Blazing_Lance_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="삼매진화 + 죽창", inline=False)
        return embed

    if msg=="룽기누스의창":
        embed=discord.Embed(title="롱기누스의 창", description="공격력 +110\n생명력 흡수 +15%\n```세컨드 윈드-핏빛 계약-[고유 장착 효과]\n착용자가 적 실험체에게 피해를 받아 체력이 40% 이하가 될 때, 모든 해로운 상태이상이 해제되며, 2.5초간 (300+ 레벨당 10)의 보호막과 50% 방해효과 저항을 얻습니다.\n또한, 8초 동안 공격력이 15 증가하고 받는 회복이 15% 증가합니다.\n(쿨다운 : 80초)```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472580054192138/896472767132758016/014._Spear_of_Longinus__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="VF 혈액 샘플 + 파이크", inline=False)
        return embed

#####양손검#####
    if msg=="녹슨검":
        embed=discord.Embed(title="녹슨 검", description="공격력 +11", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914732342571065374/001._Rusty_Sword__.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="항구(6) 양궁장(7) 성당(6)", inline=False)
        return embed

    if msg=="샴쉬르":
        embed=discord.Embed(title="샴쉬르", description="공격력 +27", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914732356567437342/002._Shamshir_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="녹슨 검 + 라이터", inline=False)
        return embed

    if msg=="플라즈마소드":
        embed=discord.Embed(title="플라즈마 소드", description="공격력 +25\n시야 +2\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914735088162459668/008._Plasma_Sword__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="녹슨 검 + 레이저 포인터", inline=False)
        return embed

    if msg=="일본도":
        embed=discord.Embed(title="일본도", description="공격력 +35", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914732364880572457/003._Katana_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="녹슨 검 + 철판", inline=False)
        return embed

    if msg=="마사무네":
        embed=discord.Embed(title="마사무네", description="공격력 +40\n공격 속도(%) +15%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914732498594963486/004._Masamune_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="일본도 + 오일", inline=False)
        return embed

    if msg=="무라마사":
        embed=discord.Embed(title="무라마사", description="공격력 +50", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914735038292164638/005._Muramasa_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="일본도 + 원석", inline=False)
        return embed

    if msg=="바스타드소드":
        embed=discord.Embed(title="바스타드 소드", description="공격력 +45", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914735065991372840/006._Bastard_Sword__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="녹슨 검 + 강철", inline=False)
        return embed

    if msg=="보검":
        embed=discord.Embed(title="보검", description="공격력 +40\n최대 체력 +100\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914735075340484698/006._Jewel_Sword_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="샴쉬르 + 루비", inline=False)
        return embed

    if msg=="뚜언띠엔":
        embed=discord.Embed(title="뚜언 띠엔", description="공격력 +77\n방어력 +28\n쿨다운 감소 +8%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914735095666057296/009._Thuan_Thien__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="바스타드 소드 + 거북 도복", inline=False)
        return embed

    if msg=="아론다이트":
        embed=discord.Embed(title="아론다이트", description="공격력 +50\n공격 속도(%) +30%\n기본 공격 추가 피해 +30\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914735102171422780/010._Arondight_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="마사무네 + 십자가", inline=False)
        return embed

    if msg=="엑스칼리버":
        embed=discord.Embed(title="엑스칼리버", description="공격력 +65\n최대 체력 +180\n체력 재생(%) +100%\n공격 속도(%) +20%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914735116436246538/011._Excalibur_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="보검 + 성배", inline=False)
        return embed

    if msg=="모노호시자오":
        embed=discord.Embed(title="모노호시자오", description="공격력 +53\n레벨 당 추가 공격력 +2\n 생명력 흡수 +22%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914735122803200041/012._Monohoshizao_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="무라마사 + 정교한 도면", inline=False)
        return embed

    if msg=="호푸어드":
        embed=discord.Embed(title="호푸어드", description="공격력 +52\n최대 체력 +150\n치명타 확률 +20%\n치명타 피해량 +10%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914735129178546246/013._Hovud_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="보검 + 유리 조각", inline=False)
        return embed

    if msg=="레바테인":
        embed=discord.Embed(title="레바테인", description="공격력 +60\n```발화-[고유 장착 효과]\n기본 공격의 대상에게 최대 4회 중첩되는 [타오르는 고통] 효과를 4초 동안 부여 합니다.\n[타오르는 고통]은 매 초마다 대상 최대 체력의 1%를 고정 피해로 줍니다.```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914735142638088192/014._Laevateinn_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="삼매진화 + 샴쉬르", inline=False)
        return embed

    if msg=="빛의검":
        embed=discord.Embed(title="빛의 검", description="공격력 +77\n공격속도 +38%\n시야 +2\n```섬광-[고유 장착 효과]\n다음에 가하는 기본 공격이 60의 추가 고유 피해를 주고 2초 동안 이동속도를 30%만큼 감소시킵니다.\n(쿨다운 : 6초)```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914735149592215562/015._Aurora_Longsword__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="플라즈마 소드 + 운석", inline=False)
        return embed

    if msg=="다인슬라이프":
        embed=discord.Embed(title="다인슬라이프", description="공격력 +100\n생명력 흡수 +25%\n```세컨드 윈드-핏빛 계약-[고유 장착 효과]\n착용자가 적 실험체에게 피해를 받아 체력이 40% 이하가 될 때, 모든 해로운 상태이상이 해제되며, 2.5초간 (300+ 레벨당 10)의 보호막과 50% 방해효과 저항을 얻습니다. 또한, 8초 동안 공격력이 15 증가하고 받는 회복이 15% 증가합니다.\n(쿨다운 : 80초)```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914735156164710470/c93c455f601b09d2.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="VF 혈액 샘플 + 일본도", inline=False)
        return embed

#####글러브#####
    if msg=="너클":
        embed=discord.Embed(title="너클", description="공격력 +10", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756156210155551/001._Brass_Knuckles_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="묘지(5) 숲(5)", inline=False)
        return embed

    if msg=="목장갑":
        embed=discord.Embed(title="목장갑", description="공격력 +7", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756156432449536/002._Cotton_Gloves_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="호텔(4) 병원(4)", inline=False)
        return embed

    if msg=="글러브":
        embed=discord.Embed(title="글러브", description="공격력 +18", color=0x1eb300)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756214536151090/003._Leather_Gloves__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="목장갑 + 가죽", inline=False)
        return embed

    if msg=="아이언너클":
        embed=discord.Embed(title="아이언 너클", description="공격력 +20", color=0x1eb300)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756214771056660/004._Iron_Knuckles__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="너클 + 철광석", inline=False)
        return embed

    if msg=="건틀릿":
        embed=discord.Embed(title="건틀릿", description="공격력 +28\n이동 속도 -0.05\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756323617439754/005._Gauntlet_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="목장갑 + 강철", inline=False)
        return embed

    if msg=="윙너클":
        embed=discord.Embed(title="윙 너클", description="공격력 +20\n이동 속도 +0.05\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756323814567946/006._Wing_Knuckles__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="아이언 너클 + 깃털", inline=False)
        return embed

    if msg=="귀골장갑":
        embed=discord.Embed(title="귀골 장갑", description="공격력 +35\n방어력 +10\n이동 속도 -0.05\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756323990716436/007._Bone_Gauntlet_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="건틀릿 + 거북이 등딱지", inline=False)
        return embed

    if msg=="벽력귀투":
        embed=discord.Embed(title="벽력귀투", description="공격력 +32\n이동 속도 -0.05\n기본 공격 추가 피해 +15\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756324179447828/008._Shatter_Shell_Gauntlet_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="건틀릿 + 화약", inline=False)
        return embed

    if msg=="유리너클":
        embed=discord.Embed(title="유리 너클", description="공격력 +28\n치명타 확률 +10%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756324338835466/009._Glass_Knuckles__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="건틀릿 + 화약", inline=False)
        return embed

    if msg=="회단장갑":
        embed=discord.Embed(title="회단 장갑", description="공격력 +27\n스킬 공격 추가 피해 +15\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756324506599455/010._Phoenix_Gloves__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="글러브 + 재", inline=False)
        return embed

    if msg=="단영촌천투":
        embed=discord.Embed(title="단영촌천투", description="공격력 +50\n방어력 +18\n스테미너 재생(%) +50%\n모든 피해 흡수 +15%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756361626202112/011._One_Inch_Punch_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="귀골 장갑 + 인형", inline=False)
        return embed

    if msg=="디바인피스트":
        embed=discord.Embed(title="디바인 피스트", description="공격력 +55\n이동 속도 -0.05\n기본 공격 추가 피해 +39\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756361793982484/012._Divine_Fist__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="벽력귀투 + 십자가", inline=False)
        return embed

    if msg=="블러드윙너클":
        embed=discord.Embed(title="블러드윙 너클", description="공격력 +56\n최대 체력 +180\n이동 속도 +0.06\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756361957543956/013._Bloodwing_Knuckles__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="윙 너클 + 루비", inline=False)
        return embed

    if msg=="빙화현옥수":
        embed=discord.Embed(title="빙화현옥수", description="공격력 +46\n레벨 당 스킬 공격 추가 피해 +1\n스킬 공격 추가 피해 +20\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756362163093524/014._Frost_Petal_Hand_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="회단 장갑 + 얼음", inline=False)
        return embed

    if msg=="여래수투":
        embed=discord.Embed(title="여래수투", description="공격력 +50\n쿨다운 감소 +15%\n스킬 증폭 +15%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756362351804416/015._Buddha_s_Palm_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="회단 장갑 + 진신사리", inline=False)
        return embed

    if msg=="브레이질건틀릿":
        embed=discord.Embed(title="브레이질 건틀릿", description="공격력 +57\n방어력 +10\n스태미너 재생 +1.2\n체력 재생 +1.2\n```열정-[고유 장착 효과]\n기본 공격이 적 실험체에게 적중 시, 적 실험체의 현재 체력의 2%의 피해를 주고, 5초간 열정 스택을 획득하며, 중첩된 열정 스택 당 10%의 공격 속도를 얻습니다.\n최대 4 중첩이 되면 10 의 공격력을 추가로 얻습니다.```", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756362527977472/016._Brasil_Gauntlet__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="귀골 장갑 + 기름먹인 천", inline=False)
        return embed

    if msg=="소수":
        embed=discord.Embed(title="소수", description="공격력 +58\n치명타 확률 +33%\n치명타 피해량 +7%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756362771243038/017._White_Claw_Punch_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="유리 너클 + 백색 가루", inline=False)
        return embed

    if msg=="천잠장갑":
        embed=discord.Embed(title="천잠장갑", description="공격력 +88\n이동 속도 +0.1\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756362976788500/018.Imperial_Skil_Gloves_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="미스릴 실 + 글러브", inline=False)
        return embed

    if msg=="주작자문":
        embed=discord.Embed(title="주작자문", description="공격력 +40\n```발화-[고유 장착 효과]\n기본 공격의 대상에게 최대 4회 중첩되는 [타오르는 고통] 효과를 4초 동안 부여 합니다. [타오르는 고통]은 매 초마다 대상 최대 체력의 0.85%를 고정 피해로 줍니다.```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756388587180112/019._Mark_of_the_Phoenix_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="삼매진화 + 글러브", inline=False)
        return embed

    if msg=="프로스트팽":
        embed=discord.Embed(title="프로스트 팽", description="공격력 +48\n쿨다운 감소 +10%\n스킬 공격 추가 피해 +40\n```한파-[고유 장착 효과]\n스킬로 적에게 피해를 입히면 2초간 이동 속도를 20%, 공격 속도를 10% 만큼 느리게 만듭니다.\n(쿨다운: 4초)```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756388775936060/020._Permafrost__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="만년빙 + 회단 장갑", inline=False)
        return embed

#####암기#####
    if msg=="면도칼":
        embed=discord.Embed(title="면도칼", description="최대 충전 수: 50발(충전: 2초)\n공격력 +11", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896472965573660712/001._Razor_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="병원(5개), 성당(5개), 학교(7개), 박쥐", inline=False)
        return embed

    if msg=="트럼프카드":
        embed=discord.Embed(title="트럼프 카드", description="최대 충전 수: 52발(충전: 2초)\n공격력 +4\n치명타 확률 +5%\n", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896472971055624202/002._Playing_Cards__.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="호텔(6개), 번화가(7개), 멧돼지", inline=False)
        return embed

    if msg=="분필":
        embed=discord.Embed(title="분필", description="최대 충전 수: 50발(충전: 2초)\n공격력 +12", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896472975585447986/003._Chalk_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="공장(7개), 성당(5개), 학교(6개), 박쥐", inline=False)
        return embed

    if msg=="다트":
        embed=discord.Embed(title="다트", description="최대 충전 수: 24발(충전: 20초)\n공격력 +16\n치명타 피해량 +8%\n이동 속도 +0.04\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896472980476031047/004._Dart_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="바늘 + 깃털", inline=False)
        return embed

    if msg=="빈티지카드":
        embed=discord.Embed(title="빈티지 카드", description="최대 충전 수: 50발(충전: 2초)\n공격력 +15\n치명타 확률 +10%\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896472985513394216/005._Vintage_Cards__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="트럼프 카드 + 만년필", inline=False)
        return embed

    if msg=="표창":
        embed=discord.Embed(title="표창", description="최대 충전 수: 50발(충전: 2초)\n공격력 +25\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896472994468229170/006._Throwing_Stars_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="면도칼 + 피아노선", inline=False)
        return embed

    if msg=="흑건":
        embed=discord.Embed(title="흑건", description="최대 충전 수: 50발(충전: 2초)\n공격력 +17\n스킬 공격 추가 피해 +5\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896472999962755142/007._Onyx_Dagger_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="면도칼 + 십자가", inline=False)
        return embed

    if msg=="부적":
        embed=discord.Embed(title="부적", description="최대 충전 수: 10발(충전: 30초)\n공격력 +30\n스킬 공격 추가 피해 +5\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473004207407154/008._Charm_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="빈티지 카드 + 분필", inline=False)
        return embed

    if msg=="유엽비도":
        embed=discord.Embed(title="유엽비도", description="최대 충전 수: 50발(충전: 2초)\n공격력 +17\n쿨다운 감소 +8%\n스킬 공격 추가 피해 +12\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473009899077662/009._Willow_Leaf_Spike_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="매화비표 + 나뭇가지", inline=False)
        return embed

    if msg=="챠크람":
        embed=discord.Embed(title="챠크람", description="최대 충전 수: 50발(충전: 2초)\n공격력 +30\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473013548093501/010._Chakram_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="표창 + 마패", inline=False)
        return embed

    if msg=="매화비표":
        embed=discord.Embed(title="매화비표", description="최대 충전 수: 50발(충전: 2초)\n공격력 +17\n쿨다운 감소 +5%\n스킬 공격 추가 피해 +8\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473019856334939/011._Apricot_Flower_Tag_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="흑건 + 꽃", inline=False)
        return embed

    if msg=="독침":
        embed=discord.Embed(title="독침", description="최대 충전 수: 3발(충전: 80초)\n공격력 +55\n스킬 공격 추가 피해 +15\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473019856334939/011._Apricot_Flower_Tag_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="흑건 + 꽃", inline=False)
        return embed
    
    if msg=="법륜":
        embed=discord.Embed(title="법륜", description="최대 충전 수: 50발(충전: 2초)\n공격력 +38\n스킬 증폭(%) +15%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473027066347571/013._Dharma_Chakram_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="챠크람 + 불경", inline=False)
        return embed

    if msg=="플럼바타":
        embed=discord.Embed(title="플럼바타", description="최대 충전 수: 24발(충전: 20초)\n공격력 +48\n이동 속도 +0.04\n치명타 피해량 +10%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473031436795974/014._Plumbata_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="다트 + 강철", inline=False)
        return embed

    if msg=="미치광이왕의카드":
        embed=discord.Embed(title="미치광이왕의 카드", description="최대 충전 수: 52발(충전: 2초)\n공격력 +49\n공격 속도(%) +40%\n치명타 확률 +15%\n치명타 피해량 +15%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473037195608064/015._Cards_of_Tyranny__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="빈티지 카드 + 이온 전지", inline=False)
        return embed

    if msg=="옥전결":
        embed=discord.Embed(title="옥전결", description="최대 충전 수: 20발(충전: 20초)\n공격력 +60\n스킬 공격 추가 피해 +5\n레벨 당 스킬 공격 추가 피해 +1\n스킬 증폭 +15%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473041188565072/016._Mystic_Jade_Charm_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="부적 + 황금", inline=False)
        return embed

    if msg=="풍마수리검":
        embed=discord.Embed(title="풍마 수리검", description="최대 충전 수: 50발(충전: 2초)\n공격력 +65\n쿨다운 감소 +15%\n스킬 공격 추가 피해 +15\n스태미너 재생 +1\n(고유)최대 쿨다운 감소 +5%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473044900528230/017._Fuhma_Shuriken__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="유엽비도 + 알코올", inline=False)
        return embed

    if msg=="빙백은침":
        embed=discord.Embed(title="빙백은침", description="최대 충전 수: 3발(충전: 80초)\n공격력 +70\n스킬 공격 추가 피해 +20\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473050357309510/018._Frost_Venom_Dart_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="독침 + 만년빙", inline=False)
        return embed

    if msg=="푸른색단도":
        embed=discord.Embed(title="푸른색 단도", description="최대 충전 수: 50발(충전: 2초)\n공격력 +35\n쿨다운 감소 +5%\n스킬 공격 추가 피해 +35\n스킬 공격 치유 방해-[고유 장착 효과]\n스킬 공격에 피격된 대상의 치유 효과가 4초간 35% 감소합니다.\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473055113642004/019._Azure_Dagger__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="매화비표 + 독약", inline=False)
        return embed

    if msg=="플레솃" or msg=="플레셋":
        embed=discord.Embed(title="플레솃", description="최대 충전 수: 24발(충전: 12초)\n공격력 +86\n이동 속도 +0.06\n치명타 피해량 +12%\n(고유)기본 공격 사거리 +0.5\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473061652574248/020._Flechette_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="플럼바타 + 백색 가루", inline=False)
        return embed

    if msg=="건곤권":
        embed=discord.Embed(title="건곤권", description="최대 충전 수: 50발(충전: 2초)\n공격력 +55\n스킬 증폭 +25%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473067990155344/021._Wind_and_Fire_Wheels_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="법륜 + 대나무", inline=False)
        return embed

    if msg=="생사부":
        embed=discord.Embed(title="생사부", description="최대 충전 수: 20발(충전: 20초)\n공격력 +83\n시야 +1\n```저주-[고유 장착 효과]\n스킬 공격을 가하면 적을 4초간 저주 상태로 만듭니다.\n저주 상태인 적은 이동 속도가 10%만큼 느려지고, 저주 상태에서 해제 될 때 100 + 스킬 증폭 * 2 에 해당하는 고정 피해를 입힙니다. 한번 저주 상태가 되면 8초간 (기본 공격 피격 시 1초 감소) 다시 저주 상태가 되지 않습니다.\n(쿨다운: 2초)```\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473071442096128/022._Death_Rune_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="부적 + 운석", inline=False)
        return embed

    if msg=="수다르사나":
        embed=discord.Embed(title="수다르사나", description="최대 충전 수: 50발(충전: 2초)\n공격력 +100\n스킬 증폭 +25%\n시야 +2\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473075770597386/023._Sudarsana_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="포스 코어 + 표창", inline=False)
        return embed

    if msg=="만천화우":
        embed=discord.Embed(title="만천화우", description="최대 충전 수: 4발(충전: 60초)\n공격력 +80\n기본 공격 추가 피해 +110\n스킬 공격 추가 피해 +31\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473080879259738/024._Petal_Torrent_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="빙백은침 + 다이너마이트", inline=False)
        return embed

#####투척#####
    
    if msg=="쇠구슬":
        embed=discord.Embed(title="쇠구슬", description="최대 충전 수: 50발(충전: 3초)\n공격력 +12", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472819167268925/001._Iron_Ball_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="양궁장(8) 숲(7) 공장(7)\n사냥 맷돼지", inline=False)
        return embed

    if msg=="야구공":
        embed=discord.Embed(title="야구공", description="최대 충전 수: 50발(충전: 3초)\n공격력 +12", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472824670224394/002._Baseball_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="공장(3개) 고급 주택가(3개)", inline=False)
        return embed

    if msg=="수류탄":
        embed=discord.Embed(title="수류탄", description="최대 충전 수: 8발(충전: 45초)\n공격력 +25\n기본 공격 추가 피해 +20\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472828516401182/003._Grenade_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="쇠구슬 + 화약", inline=False)
        return embed

    if msg=="화염병":
        embed=discord.Embed(title="화염병", description="최대 충전 수: 20발(충전: 25초)\n공격력 +22\n공격 속도(%) +15%\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472834728149032/004_Molotov_Cocktail_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="유리병 + 오일", inline=False)
        return embed

    if msg=="싸인볼":
        embed=discord.Embed(title="싸인볼", description="최대 충전 수: 50발(충전: 3초)\n공격력 +30\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472842093346817/005._Autographed_Baseball_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="야구공 + 만년필", inline=False)
        return embed

    if msg=="슬링":
        embed=discord.Embed(title="슬링", description="최대 충전 수: 50발(충전: 3초)\n공격력 +42\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472851266285598/006._Sling_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="싸인볼 + 고무", inline=False)
        return embed

    if msg=="밀가루폭탄":
        embed=discord.Embed(title="밀가루 폭탄", description="최대 충전 수: 20발(충전: 25초)\n공격력 +50\n공격 속도(%) +15%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472854634311750/007._Flour_Bomb__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="백색 가루 + 화염병", inline=False)
        return embed

    if msg=="볼라이트닝":
        embed=discord.Embed(title="볼 라이트닝", description="최대 충전 수: 50발(충전: 3초)\n공격력 +24\n공격 속도(%) +15%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472862985162774/008._Ball_Lightning__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="쇠구슬 + 방전 전지", inline=False)
        return embed

    if msg=="플러버":
        embed=discord.Embed(title="플러버", description="최대 충전 수: 50발(충전: 3초)\n공격력 +35\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472865535299675/009._Flubber_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="고무 + 뜨거운 물", inline=False)
        return embed

    if msg=="필럼":
        embed=discord.Embed(title="필럼", description="최대 충전 수: 24발(충전: 3초)\n공격력 +28\n(고유)기본 공격 사거리 +0.5", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472872040689704/010._Pilum_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="사격 교본 + 단창", inline=False)
        return embed

    if msg=="가시탱탱볼":
        embed=discord.Embed(title="가시 탱탱볼", description="최대 충전 수: 50발(충전: 3초)\n공격력 +37\n```스킬 공격 치유 방해-[고유 장착 효과]\n스킬 공격에 피격된 대상의 치유 효과가 4초 동안 35% 감소합니다.```\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472880030842920/011._Spiky_Bouncy_Ball__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="플러버 + 못", inline=False)
        return embed

    if msg=="소이탄":
        embed=discord.Embed(title="소이탄", description="최대 충전 수: 50발(충전: 3초)\n공격력 +67\n공격 속도(%) +200%\n쿨다운 감소 +12%\n스킬 증폭 +17%", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472886548779018/012._Incendiary_Bomb_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="화염병 + 볼 라이트닝", inline=False)
        return embed

    if msg=="안티오크의수류탄":
        embed=discord.Embed(title="안티오크의 수류탄", description="최대 충전 수: 18발(충전: 24초)\n공격력 +80\n기본 공격 추가 피해 +45\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472893867847800/013._Grenade_of_Antioch__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="고폭 수류탄 + 십자가", inline=False)
        return embed

    if msg=="다비드슬링":
        embed=discord.Embed(title="다비드슬링", description="최대 충전 수: 50발(충전: 3초)\n공격력 +68\n체력 재생(%) +150%\n기본 공격 추가 피해 +36\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472897965682688/014._David_s_Sling_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="슬링 + 성자의 유산", inline=False)
        return embed

    if msg=="연막탄":
        embed=discord.Embed(title="연막탄", description="최대 충전 수: 30발(충전: 12초)\n공격력 +85\n공격 속도(%) +40%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472903359553556/015._Smoke_Bomb_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="밀가루 폭탄 + 콜라", inline=False)
        return embed

    if msg=="고폭수류탄":
        embed=discord.Embed(title="고폭 수류탄", description="최대 충전 수: 8발(충전: 50초)\n공격력 +56\n기본 공격 추가 피해 +50\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472908585656320/016._High_Explosive_Grenade__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="수류탄 + RDX", inline=False)
        return embed

    if msg=="파이어볼":
        embed=discord.Embed(title="파이어 볼", description="최대 충전 수: 50발(충전: 3초)\n공격력 +22\n레벨 당 스킬 공격 추가 피해 +2.5", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472913333600266/017._Fireball__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="싸인볼 + 화염 트랩", inline=False)
        return embed

    if msg=="아스트라페":
        embed=discord.Embed(title="아스트라페", description="최대 충전 수: 36발(충전: 3초) 공격력 +66\n치명타 확률 +24%\n치명타 피해량 +6%\n(고유)기본 공격 사거리 +0.75", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472918035419186/018._Astrape_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="필럼 + 유리 조각", inline=False)
        return embed

    if msg=="루테늄구슬":
        embed=discord.Embed(title="루테늄 구슬", description="최대 충전 수: 50발(충전: 3초)\n공격력 +73\n스킬 증폭 +22%\n```스킬 공격 치유 방해-[고유 장착 효과]\n스킬 공격에 피격된 대상의 치유 효과가 4초간 35% 감소합니다.```\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472923055992882/019._Ruthenium_Marble__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="가시 탱탱볼 + 황금", inline=False)
        return embed

    if msg=="프리즘볼":
        embed=discord.Embed(title="프리즘 볼", description="최대 충전 수: 50발(충전: 3초)\n공격력 +115\n공격 속도 +33%\n", color=0xF9D537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472927078350848/020._Dyadic_Prism__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="볼 라이트닝 + 포스 코어", inline=False)
        return embed
    
    if msg=="점착폭탄":
        embed=discord.Embed(title="점착폭탄", description="최대 충전 수 20발(충전: 12초)\n공격력 +80\n공격 속도 +20%\n```충전-섬광-[고유 장착 효과]\n다음에 가하는 기본 공격이 캐릭터 레벨 * 8(+스킬 증폭 * 1)의 추가 고유 피해를 주고 1초 동안 이동속도를 20% 만큼 감소시킵니다.\n(쿨다운 : 5초)```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/920632984481169428/Sticky_Bomb__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="수류탄 + 볼 라이트닝", inline=False)
        return embed

#####채찍#####
    if msg=="채찍":
        embed=discord.Embed(title="채찍", description="공격력 +12", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865097411100683/891865135772225536/001._Whip_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로", value="공장(3) 학교(3)", inline=False)
        return embed

    if msg=="철편":
        embed=discord.Embed(title="철편", description="공격력 +30", color=0x329532)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865097411100683/891865144886444032/003._Bullwhip_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="채찍 + 면도칼", inline=False)
        return embed
        
    if msg=="오랏줄":
        embed=discord.Embed(title="오랏줄", description="공격력 +24\n 스킬 공격 추가 피해 +6\n", color=0x329532)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865097411100683/891865140151058483/002._Rope_Cuffs_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="채찍 + 마패", inline=False)
        return embed    

    if msg=="바람채찍":
        embed=discord.Embed(title="바람 채찍", description="공격력 +36\n 이동 속도 +0.06\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865097411100683/891865149395312660/004._Wind_Whip__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="오랏줄 + 깃털", inline=False)
        return embed

    if msg=="벽력편":
        embed=discord.Embed(title="벽력편", description="공격력 +42\n 공격 속도 +10%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865097411100683/891865149395312660/004._Wind_Whip__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="철편 + 방전 전지", inline=False)
        return embed

    if msg=="글레이프니르":
        embed=discord.Embed(title="글레이프니르", description="공격력 +55\n 이동 속도 +0.06\n 스킬 공격 추가 피해 +30\n 스킬 공격 치유 방해 - [고유 장착 효과]\n 스킬 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865097411100683/891865163169407077/007._Gleipnir_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="바람 채찍 + 가시발판", inline=False)
        return embed

    if msg=="플라즈마웜":
        embed=discord.Embed(title="플라즈마 웜", description="공격력 +60\n 공격 속도 +40%\n 레벨 당 기본 공격 추가 피해 +1.5\n 시야 +1.5\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865097411100683/891865167414042624/008._Plasma_Whip__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="벽력편 + 레이저 포인터", inline=False)
        return embed

    if msg=="뇌룡편":
        embed=discord.Embed(title="뇌룡편", description="공격력 +60\n 공격 속도 +10%\n 스킬 증폭 + 10%\n 레벨 당 스킬 증폭 +1%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865097411100683/891865158740213800/006._Thunder_Whip_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="벽력편 + 황금", inline=False)
        return embed

    if msg=="혈화구절편":
        embed=discord.Embed(title="혈화구절편", description="공격력 +70\n쿨다운 감소 +10%\n 모든 피해 흡혈 +15%\n 레벨 당 스킬 공격 추가 피해 +3\n", color=0xf8d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865097411100683/891865172640170004/009._Bloody_Nine_Tails_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로 ", value="VF 혈액 샘플 + 오랏줄", inline=False)
        return embed

    if msg=="캐소드라쉬":
        embed=discord.Embed(title="캐소드 라쉬", description="공격력 +77\n쿨다운 감소 +10%\n```신속-플라즈마-[고유 장착 효과\n4초 이내에 3회의 개별 피해를 가하면, 초간 이동 속도가 캐릭터 레벨 * 1% 증가하고, 105의 보호막을 얻습니다.\n(쿨다운 6초)```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865097411100683/920632964382097418/Cathod_Lash__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="철편 + 아이테르 깃털", inline=False)
        return embed

#####VF의수#####

    if msg=="바이퍼":
        embed=discord.Embed(title="바이퍼", description="공격력 +25", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450484017233930/003._Viper_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="기본 지급", inline=False)
        return embed

    if msg=="데스애더":
        embed=discord.Embed(title="데스애더", description="공격력 +43\n레벨 당 기본 공격 추가 피해 +1\n```의념 [고유 장착 효과]-데스애더&데스애더퀸\nVF폭주 상태일 때 스킬을 사용하면 의념을 충전합니다.\n충전된 상태에서 다음 3초 안에 이루어지는 기본 공격이 추가 고유 피해를 입힙니다.\n(쿨다운 : 0.2초)\n 캐릭터 레벨 * 5 에 해당하는 피해를 입힙니다.",color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450505915695144/004._Deathadder_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="패시브 lv2에서 선택 진화", inline=False)
        return embed

    if msg=="데스애더퀸":
        embed=discord.Embed(title="데스애더퀸", description="공격력 +63\n레벨 당 기본 공격 추가 피해 +2\n공격 속도 +15%```의념-[고유 장착 효과]-데스애더&데스애더퀸\nVF폭주 상태일 때 스킬을 사용하면 의념을 충전합니다.\n충전된 상태에서 다음 3초 안에 이루어지는 기본 공격이 추가 고유 피해를 입힙니다.\n(쿨다운 : 0.2초)\n 캐릭터 레벨 * 5 에 해당하는 피해를 입힙니다.",color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450527331782656/007._Deathadder_Queen__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="패시브 lv3에서 선택 진화", inline=False)
        return embed

    if msg=="데스애더퀸MT":
        embed=discord.Embed(title="데스애더퀸 - MT",description="공격력 +71\n공격 속도 +20%\n레벨 당 기본 공격 추가 피해 +2\n공격 속도 +15%```의념-[고유 장착 효과]-데스애더&데스애더퀸\nVF폭주 상태일 때 스킬을 사용하면 의념을 충전합니다.\n충전된 상태에서 다음 3초 안에 이루어지는 기본 공격이 추가 고유 피해를 입힙니다.\n(쿨다운 : 0.2초)\n 캐릭터 레벨 * 7 에 해당하는 피해를 입힙니다.``` ```독사의 맹독-[고유 장착 효과]\n독사의 진노(R)에 적중한 적 대상의 방어력을 5초 동안 6% 감소시킵니다.\n이 효과는 최대 2중첩까지 중첩됩니다.```",color=0xF9D537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450557966999552/010._Deathadder_Queen_MT_-MT.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="데스애더퀸 + 운석", inline=False)
        return embed

    if msg=="데스애더퀸FC":
        embed=discord.Embed(title="데스애더퀸 - FC", description="공격력 +77\n공격 속도 +25%\n레벨 당 기본 공격 추가 피해 +2\n (고유) 방해 효과 저항 15%\n ```의념-[고유 장착 효과]\nVF폭주 상태일 때 스킬을 사용하면 의념을 충전합니다.\n충전된 상태에서 다음 3초 안에 이루어지는 기본 공격이 추가 고유 피해를 입힙니다.\n(쿨다운 : 0.2초)\n캐릭터 레벨 * 7에 해당하는 피해를 입힙니다.```",color=0xF9D537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450558168313856/011._Deathadder_Queen_FC_-FC.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="데스애더퀸 + 포스코어", inline=False)
        return embed

    if msg=="데스애더퀸VBS":
        embed=discord.Embed(title="데스애더퀸 - VBS", description="공격력 +81\n공격 속도 +25%\n 레벨 당 기본 공격 추가 피해 +2\n(고유) 받는 회복 증가 +20%\n ```의념-[고유 장착 효과]\nVF폭주 상태일 때 스킬을 사용하면 의념을 충전합니다.\n충전된 상태에서 다음 3초 안에 이루어지는 기본 공격이 추가 고유 피해를 입힙니다.\n(쿨다운 : 0.2초)\n캐릭터 레벨 * 7에 해당하는 피해를 입힙니다.```",color=0xF9D537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450558516437012/012._Deathadder_Queen_VBS_-VBS.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="데스애더퀸 +VF 혈액 샘플", inline=False)
        return embed

    if msg=="블랙맘바":
        embed=discord.Embed(title="블랙맘바", description="공격력 +45\n 모든 피해 흡혈 +10%",color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450506184097812/005._Black_Mamba_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="패시브 lv2에서 선택 ", inline=False)
        return embed

    if msg=="블랙맘바킹":
        embed=discord.Embed(title="블랙맘바킹", description="공격력 +65\n레벨 당 최대 체력 +9\n모든 피해 흡혈 +12%",color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450527642165278/008._Black_Mamba_King_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="패시브 lv3에서 선택 ", inline=False)
        return embed

    if msg=="블랙맘바킹TL":
        embed=discord.Embed(title="블랙맘바킹 - TL", description="공격력 +73\n레벨 당 최대 체력 +11\n 모든 피해 흡혈 +12%\n  ```불꽃 결계[고유 장착 효과]\n  VF폭주 상태일 때 전투에 돌입하면 매 1초마다 주변 2.5m의 적에게 고유 피해를 입힙니다.\n적에게 최대 체력의 5%의 고유 피해를 입힙니다.```",color=0xF9D537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450574458982420/013._Black_Mamba_King_TL_-TL.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="블랙맘바킹 + 생명의 나무", inline=False)
        return embed

    if msg=="블랙맘바킹FC":
        embed=discord.Embed(title="블랙맘바킹 - FC", description="공격력 +79\n레벨 당 최대 체력 +11\n모든 피해 흡혈 +17% \n(고유) 방해 효과 저항 +15%",color=0xF9D537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450574647722046/014._Black_Mamba_King_FC_-FC.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="블랙맘바킹 + 포스 코어", inline=False)
        return embed

    if msg=="블랙맘바킹VBS":
        embed=discord.Embed(title="블랙맘바킹 - VBS", description="공격력 +83\n레벨 당 최대 체력 +11\n 모든 피해 흡혈 +17%\n(고유) 받는 회복 증가 +20%",color=0xF9D537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450574903586816/015._Black_Mamba_King_VBS_-VBS.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="블랙맘바킹 +VF 혈액 샘플", inline=False)
        return embed

    if msg=="사이드와인더":
        embed=discord.Embed(title="사이드와인더", description="공격력 +41\n이동 속도 +0.06\n```가벼운 발걸음-[고유 장착 효과]-사이드와인더&슈퍼사이드와인더\nVF폭주 상태일 때 0.1m 이동할 때마다 [가벼운 발걸음]을 최대 100회까지 중첩해서 획득합니다.\n중첩에 따라 이동 속도가 최대 0.1까지 증가합니다.\n 기본 공격 피해를 입힐 경우 중첩을 모두 소모하여 최대 70의 고유 피해를 입힙니다. 최대 중첩 상태에서 기본 공격에 피격된 대상의 이동 속도를 2초 동안 30% 감소시킵니다.```",color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450506398023690/006._Sidewinder_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="패시브 lv2에서 선택 진화", inline=False)
        return embed

    if msg=="슈퍼사이드와인더":
        embed=discord.Embed(title="슈퍼사이드와인더", description="공격력 +61\n이동 속도+0.08\n쿨다운 감소 +6%\n```가벼운 발걸음-[고유 장착 효과]사이드와인더&슈퍼사이드와인더\nVF폭주 상태일 때 0.1m 이동할 때마다 [가벼운 발걸음]을 최대 100회까지 중첩해서 획득합니다.\n중첩에 따라 이동 속도가 최대 0.1까지 증가합니다.\n기본 공격 피해를 입힐 경우 중첩을 모두 소모하여 최대 70의 고유 피해를 입힙니다.\n최대 중첩 상태에서 기본 공격에 피격된 대상의 이동 속도를 2초 동안 30% 감소시킵니다.```",color=0xF9D537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450527944171560/009._Alpha_Sidewinder_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="패시브 lv3에서 선택 진화", inline=False)
        return embed

    if msg=="슈퍼사이드와인더ML":
        embed=discord.Embed(title="슈퍼사이드와인더 - ML", description="공격력 +69\n이동 속도 +0.1\n쿨다운 감소 +10%\n(고유) 최대 쿨다운 감소 +5%\n```가벼운 발걸음-[고유 장착 효과] 사이드와인더&슈퍼사이드와인더\nVF폭주 상태일 때 0.08m이동할 때마다 [가벼운 발걸음]을 최대 100회까지 중첩해서 획득합니다.\n중첩에 따라 이동 속도가 최대 0.1까지 증가합니다.\n기본 공격 피해를 입힐 경우 중첩을 모두 소모하여 최대 160의 고유 피해를 입힙니다.\n최대 중첩 상태에서 기본 공격에 피격된 대상의 이동 속도를 2초 동안 40% 감소시킵니다.\n``` ```VF제어 강화 - [고유 장착 효과]\n에키온의 과부하 상태의 지속 시간이 VF폭주(R) 레벨에 따라 영구적으로 30/35/40/45% 감소합니다.```",color=0xF9D537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450589193580554/016._Alpha_Siderwinder_ML_-ML.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="슈퍼사이드와인더 + 미스릴", inline=False)
        return embed

    if msg=="슈퍼사이드와인더FC":
        embed=discord.Embed(title="슈퍼사이드와인더 - FC", description="공격력 +75\n이동 속도 +0.1\n쿨다운 감소 +15%\n(고유) 방해 효과 저항 +15%\n```가벼운 발걸음-[고유 장착 효과] 사이드와인더&슈퍼사이드와인더\nVF폭주 상태일 때 0.08m이동할 때마다 [가벼운 발걸음]을 최대 100회까지 중첩해서 획득합니다.\n중첩에 따라 이동 속도가 최대 0.1까지 증가합니다.\n기본 공격 피해를 입힐 경우 중첩을 모두 소모하여 최대 160의 고유 피해를 입힙니다.\n최대 중첩 상태에서 기본 공격에 피격된 대상의 이동 속도를 2초 동안 40% 감소시킵니다.\n``` ",color=0xF9D537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450589445234688/017._Alpha_Sidewinder_FC_-FC.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="슈퍼사이드와인더 + 포스 코어", inline=False)
        return embed

    if msg=="슈퍼사이드와인더VBS":
        embed=discord.Embed(title="슈퍼사이드와인더 - VBS", description="공격력 +79\n이동 속도 +0.1\n쿨다운 감소 +15%\n(고유) 받는 회복 증가 +20%\n ```가벼운 발걸음-[고유 장착 효과] 사이드와인더&슈퍼사이드와인더\nVF폭주 상태일 때 0.08m 이동할 때마다 [가벼운 발걸음]을 최대 100회까지 중첩해서 획득합니다.\n중첩에 따라 이동 속도가 최대 0.1까지 증가합니다.\n기본 공격 피해를 입힐 경우 중첩을 모두 소모하여 최대 160의 고유 피해를 입힙니다.\n최대 중첩 상태에서 기본 공격에 피격된 대상의 이동 속도를 2초 동안 40% 감소시킵니다.```",color=0xF9D537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/923207804980981800/923450589688528916/018._Alpha_Sidewinder_VBS_-VBS.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="슈퍼사이드와인더 + 포스 코어", inline=False)
        return embed



#####설치#####
        
    if msg=="감시카메라":
        embed=discord.Embed(title="감시 카메라", description="시야: 7m\n최대 수량: 5", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271133144703066/001._Surveillance_Camera__.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="항구(3) 고급 주택가(3) 번화가(5) 병원(5) 양궁장(3) 묘지(6) 학교(6)\n박쥐(100%) 멧돼지 들개", inline=False)
        return embed

    if msg=="올가미":
        embed=discord.Embed(title="올가미",description="트랩 피해 +10\n최대 수량: 5",color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271133396340776/002._Snare_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="항구(3), 연못(4), 모래사장(4), 양궁장(4), 숲(3), 멧돼지", inline=False)
        return embed

    if msg=="쥐덫":
        embed=discord.Embed(title="쥐덫", description="트랩 피해 +50\n최대 수량: 5",color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271133975162910/003._Mousetrap_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="연못(6), 모래사장(7), 묘지(6), 멧돼지", inline=False)
        return embed

    if msg=="가시발판":
        embed=discord.Embed(title="가시발판", description="트랩 피해 +120\n트랩 발동: 대상의 이동속도가 1.5초간 20% 감소합니다.\n최대 수량: 5", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271369598582824/004._Spiked_Plank__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="쥐덫 + 못", inline=False)
        return embed

    if msg=="개량형쥐덫":
        embed=discord.Embed(title="개량형 쥐덫", description="트랩 피해 +160\n최대 수량: 5", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271369904750652/005._Enhanced_Mousetrap__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="쥐덫 + 철광석", inline=False)
        return embed

    if msg=="다이너마이트":
        embed=discord.Embed(title="다이너마이트", description="트랩 피해 +220\n트랩 발동: 1.5초 후 넓은 범위로 폭발합니다.\n최대 수량:5", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271370466799626/006._Dynamite_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="피아노선 + 화약", inline=False)
        return embed

    if msg=="대나무트랩":
        embed=discord.Embed(title="대나무 트랩", description="트랩 피해 +30\n트랩 발동: 대상을 0.5초 간 속박합니다.\n최대 수량: 5", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271370743615498/007._Bamboo_Trap__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="올가미 + 대나무", inline=False)
        return embed

    if msg=="부비트랩":
        embed=discord.Embed(title="부비 트랩", description="트랩 피해 +30\n트랩 발동: 대상을 0.5초 간 속박합니다.\n최대 수량: 5", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271371033018378/008._Booby_Trap_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="올가미 + 접착제", inline=False)
        return embed

    if msg=="소란발생기":
        embed=discord.Embed(title="소란 발생기", description="트랩 피해 +40\n최대 수량: 5", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271371293098044/009._Clang_Clatter__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="캔 + 쇠구슬", inline=False)
        return embed

    if msg=="망원카메라":
        embed=discord.Embed(title="망원 카메라", description="시야: 11m\n최대 수량: 6", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271371506999357/010._Telephoto_Camera__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="감시 카메라 + 쌍안경", inline=False)
        return embed

    if msg=="정찰드론":
        embed=discord.Embed(title="정찰 드론", description="7초간 시야를 밝힙니다.\n최대 수량: 6", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271371746058240/011._Recon_Drone__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="감시 카메라 + 화약", inline=False)
        return embed

    if msg=="위장카메라":
        embed=discord.Embed(title="위장 카메라", description="시야: 13m\n최대 수량: 6\n\n`나타폰 제작 가능`", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271371989319750/012._Trail_Camera__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="감시 카메라 + 나뭇가지", inline=False)
        return embed

    if msg=="정글기요틴":
        embed=discord.Embed(title="정글 기요틴", description="트랩 피해 +100\n트랩 발동: 대상을 0.5초 간 속박합니다.\n최대 수량: 5 ", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271372396179526/013._Jungle_Guillotine__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="쥐덫 + 녹슨검", inline=False)
        return embed

    if msg=="폭발트랩":
        embed=discord.Embed(title="폭발 트랩", description="트랩 피해 +180\n트랩 발동: 1.5초 후 넓은 범위로 폭발합니다.\n최대 수량: 5 ", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271384878419998/014._Explosive_Trap__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="쥐덫 + 화약", inline=False)
        return embed

    if msg=="지뢰":
        embed=discord.Embed(title="지뢰", description="트랩 피해 +80\n트랩 발동: 좁은 범위로 폭발하며, 피격된 대상은 1초간 기절합니다.\n최대 수량: 5", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271468156338256/015._Mine_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="부비트랩 + 화약", inline=False)
        return embed

    if msg=="펜듈럼도끼":
        embed=discord.Embed(title="펜듈럼 도끼", description="트랩 피해 +100\n트랩 발동: 대상을 0.75초 간 속박합니다\n최대 수량: 5", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271468366069770/016._Pendulum_Axe__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="대나무 트랩 + 손도끼", inline=False)
        return embed

    if msg=="RDX":
        embed=discord.Embed(title="RDX", description="트랩 피해 +250\n트랩 발동: 1.5초 후 넓은 범위로 폭발합니다.\n최대 수량: 5", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271468584149032/017._RDX.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="다이너마이트 + 고철", inline=False)
        return embed

    if msg=="EMP드론":
        embed=discord.Embed(title="EMP 드론", description="7초 간 목표 지점 주변의 트랩을 무력화하고 시야를 밝힙니다.\n최대 수량 : 6", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271468865175652/018._EMP_Drone_EMP_.png_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="정찰 드론 + 배터리", inline=False)
        return embed

    if msg=="화염트랩":
        embed=discord.Embed(title="화염 트랩", description="트랩 피해 +280\n트랩 발동: 1.5초 후 넓은 범위로 폭발합니다.\n최대 수량: 5", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271469494312970/020._Fire_Trap__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="폭발 트랩 + 기름먹인 천", inline=False)
        return embed

    if msg=="히든메이든":
        embed=discord.Embed(title="히든 메이든", description="트랩 피해 +300\n트랩 발동: 대상의 이동속도가 2초간 30% 감소합니다.\n최대 수량: 5", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271469741793330/021._Hidden_Maiden__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="가시발판 + 정글 기요틴", inline=False)
        return embed

    if msg=="폭뢰침":
        embed=discord.Embed(title="폭뢰침", description="트랩 피해 +330\n트랩 발동: 대상의 이동속도가 2.5초간 40% 감소합니다.\n최대 수량: 5", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271572137316352/022._Stingburst_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="RDX + 가시 발판", inline=False)
        return embed

    if msg=="C4" or msg=="C-4":
        embed=discord.Embed(title="C-4", description="트랩 피해 +320\n트랩 발동: 1.5초 후 넓은 범위로 폭발합니다.\n최대 수량: 5", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271572338659358/023._C-4.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="RDX + 백색 가루", inline=False)
        return embed

    if msg=="더블기요틴":
        embed=discord.Embed(title="더블 기요틴", description="트랩 피해 +280\n트랩 발동: 대상을 1초 간 속박합니다.\n최대 수량: 5", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271572938432512/024._Double_Guillotine__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="정글 기요틴 + 펜듈럼 도끼", inline=False)
        return embed

    if msg=="크레모어":
        embed=discord.Embed(title="크레모어", description="트랩 피해 +260\n트랩 발동: 좁은 범위로 폭발하며, 피격된 대상은 0.5초간 기절합니다.\n최대 수량: 5", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271573173317632/025._Claymore_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="지뢰 + 폭발 트랩", inline=False)
        return embed

    if msg=="리모트마인":
        embed=discord.Embed(title="리모트 마인", description="트랩 피해 +450\n트랩 발동: 1.5초 후 넓은 범위로 폭발합니다.\n최대 수량: 5", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271583969464330/026._Remote_Mine__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="포스 코어 + 개량형 쥐덫", inline=False)
        return embed

    if msg=="스마트폭탄":
        embed=discord.Embed(title="스마트 폭탄", description="트랩 피해 +370\n트랩 발동: 0.7초 후 넓은 범위로 폭발합니다.\n최대 수량: 5", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910213917391872050/915271584158199848/027._Smart_Bomb__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="RDX + 휴대폰", inline=False)
        return embed

#####재료#####
    
    if msg=="돌멩이" or msg=="돌":
        embed=discord.Embed(title="돌멩이", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271728102518784/001._Stone_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="돌무더기 채집", inline=False)
        return embed

    if msg=="유리병":
        embed=discord.Embed(title="유리병", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271728345808906/002._Glass_Bottle_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 항구(8) 번화가(9) 성당(8)\n사냥 멧돼지 ", inline=False)
        return embed

    if msg=="못":
        embed=discord.Embed(title="못", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271728563879936/003._Nail_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 번화가(11) 양궁장(6) 공장(9)\n사냥 박쥐(4.4%)", inline=False)
        return embed

    if msg=="가죽":
        embed=discord.Embed(title="가죽", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271728916226098/004._Leather_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="사냥 닭(100%) 박쥐(22.1%) 들개(100%) 늑대(100%) 곰(100%)", inline=False)
        return embed

    if msg=="거북이등딱지":
        embed=discord.Embed(title="거북이 등딱지", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271729235001395/005._Turtle_Shell__.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 항구(8) 연못(7) 모래사장(8)\n사냥 박쥐(4.4%)", inline=False)
        return embed

    if msg=="고무":
        embed=discord.Embed(title="고무", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271729524392007/006._Rubber_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 항구(8) 골목길(7) 양궁장(6)\n사냥 박쥐 ", inline=False)
        return embed

    if msg=="고철":
        embed=discord.Embed(title="고철", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271729809588254/007._Scrap_Metal_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 항구(9) 호텔(11) 병원(9) 공장(13)\n사냥 들개(9.8%)", inline=False)
        return embed

    if msg=="라이터":
        embed=discord.Embed(title="라이터", description="최대 수량: 2", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271730040287362/008._Lighter_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 항구(9) 골목길(11) 공장(13) 학교(9)\n사냥 들개(9.8%)", inline=False)
        return embed

    if msg=="레이저포인터":
        embed=discord.Embed(title="레이저 포인터", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271730258382908/009._Laser_Pointer__.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 고급 주택가(7) 병원(6) 학교(7)\n사냥 들개 ", inline=False)
        return embed

    if msg=="마패":
        embed=discord.Embed(title="마패", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271730614911067/010._Stallion_Medal_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 모래사장(7) 골목길(6) 절(8)\n사냥 멧돼지(3.3%)", inline=False)
        return embed

    if msg=="배터리":
        embed=discord.Embed(title="배터리", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271740458950736/011._Battery_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 항구(9) 번화가(12) 공장(13)\n사냥 들개(9.8%)", inline=False)
        return embed

    if msg=="알코올":
        embed=discord.Embed(title="알코올", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271740672847893/012._Alcohol_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 병원(6) 공장(7) 학교(6)\n사냥 멧돼지(3.3%)", inline=False)
        return embed

    if msg=="오일" or msg=="기름":
        embed=discord.Embed(title="오일", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271740861608006/013._Oil_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 고급 주택가(9) 번화가(8) 양궁장(7) 공장(9)\n사냥 박쥐 ", inline=False)
        return embed

    if msg=="옷감":
        embed=discord.Embed(title="옷감", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271741067120653/014._Cloth_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 호텔(9) 번화가(9) 절(9)\n사냥 멧돼지 ", inline=False)
        return embed

    if msg=="원석":
        embed=discord.Embed(title="원석", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271741272645672/015._Gemstone_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 연못(11) 모래사장(11) 절(9) 숲(11)\n사냥 들개(9.8%)", inline=False)
        return embed

    if msg=="접착제":
        embed=discord.Embed(title="접착제", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271741612371978/016._Glue_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 골목길(8) 병원(8) 공장(9)\n사냥 박쥐 ", inline=False)
        return embed

    if msg=="종이":
        embed=discord.Embed(title="종이", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271741822091334/017._Paper_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 절(9) 양궁장(8) 성당(9)\n사냥 박쥐 ", inline=False)
        return embed

    if msg=="철광석":
        embed=discord.Embed(title="철광석", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271742019211344/018._Iron_Ore_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 호텔(8) 묘지(7) 숲(8)\n사냥 멧돼지 ", inline=False)
        return embed

    if msg=="캔":
        embed=discord.Embed(title="캔", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271742207950928/019._Can_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 모래사장(5) 번화가(5) 학교(5)\n사냥 멧돼지(3.3%)", inline=False)
        return embed

    if msg=="화약":
        embed=discord.Embed(title="화약", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271742447034408/020._Gunpowder_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 절(9) 양궁장(8) 묘지(8)\n사냥 박쥐(4.4%)", inline=False)
        return embed

    if msg=="피아노선":
        embed=discord.Embed(title="피아노선", description="최대 수량: 3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271750068076574/021._Piano_Wire_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 모래사장(8) 고급 주택가(9) 호텔(8) 성당(9)\n사냥 멧돼지(3.3%) 알파(6.3%)", inline=False)
        return embed

    if msg=="강철":
        embed=discord.Embed(title="강철", description="최대 수량: 3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271857580671046/022._Steel_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="고철 + 철광석", inline=False)
        return embed

    if msg=="기름먹인천":
        embed=discord.Embed(title="기름먹인 천", description="최대 수량: 3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271857790402610/023._Oilcloth__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="오일 + 붕대", inline=False)
        return embed

    if msg=="뜨거운오일":
        embed=discord.Embed(title="뜨거운 오일", description="최대 수량: 3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271858092380160/024._Heated_Oil__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="라이터 + 오일", inline=False)
        return embed

    if msg=="방전전지":
        embed=discord.Embed(title="방전 전지", description="최대 수량: 3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271858348236851/025._Dead_Battery__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="배터리 + 물", inline=False)
        return embed

    if msg=="백색가루":
        embed=discord.Embed(title="백색 가루", description="최대 수량: 3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271858557943848/026._White_Powder__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="분필 + 돌멩이", inline=False)
        return embed

    if msg=="재":
        embed=discord.Embed(title="재", description="최대 수량: 3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271858780266587/027._Ash_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="종이 + 라이터", inline=False)
        return embed

    if msg=="전자부품":
        embed=discord.Embed(title="전자 부품", description="최대 수량: 3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271859057094676/028._Electronic_Parts__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="배터리 + 피아노선", inline=False)
        return embed

    if msg=="정교한도면":
        embed=discord.Embed(title="정교한 도면", description="최대 수량: 3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271859237421107/029._Blueprint__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="만년필 + 종이", inline=False)
        return embed

    if msg=="철판":
        embed=discord.Embed(title="철판", description="최대 수량: 3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271859489095700/030._Iron_Sheet_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="고철 + 망치", inline=False)
        return embed

    if msg=="황금":
        embed=discord.Embed(title="황금", description="최대 수량: 3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271859937902642/031._Gold_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="원석 + 곡괭이", inline=False)
        return embed

    if msg=="달궈진돌멩이":
        embed=discord.Embed(title="달궈진 돌멩이", description="최대 수량: 3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271962215997460/032._Heated_Stone__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="돌멩이 + 라이터", inline=False)
        return embed

    if msg=="철사":
        embed=discord.Embed(title=" 철사", description="최대 수량: 3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271962551533618/033._Barbed_Wire_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="망치 + 피아노선", inline=False)
        return embed

    if msg=="루비":
        embed=discord.Embed(title="루비", description="최대 수량: 3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271962861903892/034._Ruby_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="원석 + 망치", inline=False)
        return embed

    if msg=="하드커버":
        embed=discord.Embed(title="하드커버", description="최대 수량: 3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915271963151323196/035._Hardcover_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="가죽 + 종이", inline=False)
        return embed

    if msg=="생명의나무" or msg =="생나" :
        embed=discord.Embed(title="생명의 나무", description="최대 수량: 3", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915272012652511302/036._Tree_of_Life__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="채집 신비한 나무에서 채집\n`\t(1일 밤 호텔과 묘지, 2일 밤 숲과 병원)`\n 사냥 위클라인(14.3%) 재생성된 곰(3.6%)", inline=False)
        return embed

    if msg=="운석":
        embed=discord.Embed(title="운석", description="최대 수량: 3", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915272012887384074/037._Meteorite_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="채집 떨어진 유성\t`(절,학교,연못,공장,골목길 랜덤)`\n사냥 위클라인(14.3%) 재생성된 곰(3.6%) 재생성된 늑대(3.8%)", inline=False)
        return embed

    if msg=="문스톤":
        embed=discord.Embed(title="문스톤", description="최대 수량: 3", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915272013080305715/038._Meteorite_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="운석 + 돌멩이", inline=False)
        return embed

    if msg=="독약":
        embed=discord.Embed(title="독약", description="최대 수량: 3", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915272013306789888/039._Poison_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="재 + 물", inline=False)
        return embed

    if msg=="모터":
        embed=discord.Embed(title="모터", description="최대 수량: 3", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915272013516513360/040._Motor_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="전자 부품 + 고철", inline=False)
        return embed

    if msg=="미스릴":
        embed=discord.Embed(title="미스릴", description="최대 수량: 3", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915272013692670003/041._Mithril_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="사냥 알파(100%) 위클라인(14.3%) 재생성된 곰(3.6%) 재생성된 늑대(3.8%) ", inline=False)
        return embed

    if msg=="유리판":
        embed=discord.Embed(title="유리판", description="최대 수량: 3", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915272013889830962/042._Glass_Panel_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="유리 조각 + 접착제", inline=False)
        return embed

    if msg=="이온전지":
        embed=discord.Embed(title="이온 전지", description="최대 수량: 3", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915272014124691536/043._Ion_Battery_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="방전 전지 + 탄산수", inline=False)
        return embed

    if msg=="휴대폰":
        embed=discord.Embed(title="휴대폰", description="최대 수량: 3", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915272014334418994/044._Cell_Phone_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="정교한 도면 + 전자 부품", inline=False)
        return embed

    if msg=="VF혈액샘플" or msg=="혈액샘플":
        embed=discord.Embed(title="VF 혈액 샘플", description="최대 수량: 3", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915272027210940426/045._VF_Blood_Sample_VF_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="사냥 위클라인(100%) 재생성된 곰(1.8%)", inline=False)
        return embed

    if msg=="포스코어" or msg=="포코":
        embed=discord.Embed(title="포스 코어", description="최대 수량: 3", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322810771836988/915272027403870259/046._Force_Core__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="생명의 나무 + 운석\n사냥 오메가(100%) 재생성된 곰s(3.6%)\n", inline=False)
        return embed

#####음식#####
    
    if msg=="감자":
        embed=discord.Embed(title="감자", description="체력 재생 +130", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274213487673384/001._Potato_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="채집 연못(4) 골목길(4) 절(8)", inline=False)
        return embed

    if msg=="대구":
        embed=discord.Embed(title="대구", description="체력 재생 +130", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274213718364160/002._Cod_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="낚시 항구(5) 모래사장(4) 고급 주택가(4)", inline=False)
        return embed

    if msg=="레몬":
        embed=discord.Embed(title="레몬", description="체력 재생 +100", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274214045548644/003._Lemon_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="고급 주택가(4) 호텔(5) 병원(5)", inline=False)
        return embed

    if msg=="마늘":
        embed=discord.Embed(title="마늘", description="체력 재생 +200", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274214351699968/004._Garlic_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="골목길(6) 절(7) 묘지(5)", inline=False)
        return embed

    if msg=="붕어":
        embed=discord.Embed(title="붕어", description="체력 재생 +130", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274214578196510/005._Carp_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="낚시 연못(9) 묘지(2) 숲(2)", inline=False)
        return embed

    if msg=="빵":
        embed=discord.Embed(title=" 빵", description="체력 재생 +325", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274214783725648/006._Bread_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="병원(5) 학교(6)", inline=False)
        return embed

    if msg=="고기":
        embed=discord.Embed(title="고기", description="체력 재생 +300", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274215043776602/007._Meat_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="사냥 닭(66.7%) 멧돼지(100%) 늑대(100%) 곰(100%)", inline=False)
        return embed

    if msg=="달걀":
        embed=discord.Embed(title="", description="체력 재생 +200", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274215408664576/008._Egg_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 묘지(5) 숲(6)\n사냥 닭(16.7%)", inline=False)
        return embed

    if msg=="생라면"or msg=="라면":
        embed=discord.Embed(title="생라면", description="체력 재생 +275", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274215773573120/009._Ramen_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="항구(5) 절(5) 공장(7)", inline=False)
        return embed

    if msg=="약초":
        embed=discord.Embed(title=" 약초", description="체력 재생 +300", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274216176230450/010._Oriental_Herb_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="연못(6) 절(6) 숲(6)", inline=False)
        return embed

    if msg=="초콜릿":
        embed=discord.Embed(title=" 초콜릿", description="체력 재생 +275", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274223520448522/011._Chocolate_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="고급 주택가(6) 번화가(6) 양궁장(5)", inline=False)
        return embed

    if msg=="꿀바른대구살":
        embed=discord.Embed(title="꿀 바른 대구살", description="체력 재생 +625", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274419599986778/012.__Honey_Cod_Steak.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="꿀 + 대구", inline=False)
        return embed

    if msg=="대구간통조림":
        embed=discord.Embed(title=" 대구 간 통조림", description="체력 재생 +650", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274419922935858/013._Canned_Cod_Liver__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="캔 + 대구", inline=False)
        return embed

    if msg=="마늘빵":
        embed=discord.Embed(title=" 마늘빵", description="체력 재생 +500", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274420233338910/014._Garlic_Bread_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="빵 + 마늘", inline=False)
        return embed

    if msg=="버터":
        embed=discord.Embed(title=" 버터", description="체력 재생 +450", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274420468207646/015._Butter_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="우유 + 나뭇가지", inline=False)
        return embed

    if msg=="붕어빵":
        embed=discord.Embed(title=" 붕어빵", description="체력 재생 +550", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274420732440617/016._Carp_Bread_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="빵 + 붕어", inline=False)
        return embed

    if msg=="초코파이":
        embed=discord.Embed(title=" 초코파이", description="체력 재생 +600", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274422758301706/017._Choco_Pie_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="빵 + 초콜렛", inline=False)
        return embed

    if msg=="난초":
        embed=discord.Embed(title="난초", description="체력 재생 +480", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274578346012672/018._Orchid_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="약초 + 꽃", inline=False)
        return embed

    if msg=="마늘베이컨말이":
        embed=discord.Embed(title="마늘 베이컨 말이", description="체력 재생 +650", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274578568302592/019._Bacon_and_Garlic_Sticks__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="마늘 + 고기", inline=False)
        return embed

    if msg=="햄버거":
        embed=discord.Embed(title="햄버거", description="체력 재생 +650", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274579117748234/021._Hamburger_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="고기 + 빵", inline=False)
        return embed

    if msg=="달걀생선필레":
        embed=discord.Embed(title=" 달걀 생선 필레", description="체력 재생 +700", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274579415560253/022._Fish_Fillet_With_Egg__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="붕어 + 달걀", inline=False)
        return embed

    if msg=="시트러스케이크":
        embed=discord.Embed(title=" 시트러스 케이크", description="체력 재생 +325", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274579847557171/023._Citrus_Cake__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="레몬 + 빵", inline=False)
        return embed

    if msg=="마늘꿀절임":
        embed=discord.Embed(title="마늘 꿀절임", description="체력 재생 +495", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274580053065778/024._Honey_Garlic__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="마늘 + 꿀", inline=False)
        return embed

    if msg=="계란빵":
        embed=discord.Embed(title="계란빵", description="체력 재생 +550", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274580283756584/025._Egg_Bun_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="달걀 + 빵", inline=False)
        return embed

    if msg=="초코아이스크림":
        embed=discord.Embed(title=" 초코 아이스크림", description="체력 재생 +550", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274580719980614/026._Choco_Ice_Cream__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="얼음 + 초콜렛", inline=False)
        return embed

    if msg=="매운탕":
        embed=discord.Embed(title="매운탕", description="체력 재생 +550", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274611707498526/027._Spicy_Fish_Stew_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="대구 + 뜨거운 물", inline=False)
        return embed

    if msg=="감자튀김":
        embed=discord.Embed(title="감자튀김", description="체력 재생 +700", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274611963359292/028._French_Fries_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="감자 + 뜨거운 오일", inline=False)
        return embed

    if msg=="구운감자":
        embed=discord.Embed(title="구운 감자", description="체력 재생 +600", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274612324073602/029._Baked_Potato__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="감자 + 달궈진 돌멩이", inline=False)
        return embed

    if msg=="구운붕어":
        embed=discord.Embed(title="구운 붕어", description="체력 재생 +600", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274612814782464/030._Baked_Carp__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="붕어 + 달궈진 돌멩이", inline=False)
        return embed

    if msg=="성수":
        embed=discord.Embed(title="성수", description="체력 재생 +800\n방어력 +10", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274613095796746/031._Holy_Water_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="미스릴 + 물", inline=False)
        return embed

    if msg=="메로구이":
        embed=discord.Embed(title="메로구이", description="체력 재생 +495", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274614106652732/032._Grilled_Chilean_Sea_Bass_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="대구 + 달궈진 돌멩이", inline=False)
        return embed

    if msg=="뜨거운라면":
        embed=discord.Embed(title="뜨거운 라면", description="체력 재생 +550", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274652455145542/033._Hot_Ramen__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="생라면 + 뜨거운 물", inline=False)
        return embed

    if msg=="모카빵":
        embed=discord.Embed(title=" 모카빵", description="체력 재생 +700", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274652706832404/034._Mocha_Bread_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="빵 + 커피 리큐르", inline=False)
        return embed

    if msg=="스크램블에그":
        embed=discord.Embed(title="스크램블 에그", description="체력 재생 +600", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274652908146728/035._Scrambled_Egg__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="달걀 + 뜨거운 오일", inline=False)
        return embed

    if msg=="초코칩쿠키":
        embed=discord.Embed(title="초코칩 쿠키", description="체력 재생 +733", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274653285638225/036._Chocolate_Chip_Cookies__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="초콜렛 + 버터", inline=False)
        return embed

    if msg=="초코파이상자":
        embed=discord.Embed(title="초코파이 상자", description="체력 재생 +733", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274653579223060/037._Choco_Pie_Box__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="초코파이 + 상자", inline=False)
        return embed

    if msg=="탕약":
        embed=discord.Embed(title="탕약", description="체력 재생 +600", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274653818302505/038._Oriental_Concoction_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="약초 + 뜨거운 물", inline=False)
        return embed

    if msg=="허니버터":
        embed=discord.Embed(title="허니버터", description="체력 재생 +650", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274654040612924/039._Honey_Butter_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="버터 + 꿀", inline=False)
        return embed

    if msg=="후라이드치킨":
        embed=discord.Embed(title="", description="체력 재생 +700", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274654233530408/040._Fried_Chicken__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="고기 + 뜨거운 오일", inline=False)
        return embed

    if msg=="힐링포션":
        embed=discord.Embed(title="힐링 포션", description="체력 재생 +700", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274671954489395/041._Healing_Potion__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="난초 + 유리병", inline=False)
        return embed

    if msg=="삶은달걀":
        embed=discord.Embed(title="삶은 달걀", description="체력 재생 +600", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274672386494464/042._Hard_Boiled_Egg__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="달걀 + 뜨거운 물", inline=False)
        return embed

    if msg=="술빵":
        embed=discord.Embed(title=" 술빵", description="체력 재생 +600", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274672654934066/043._Soggy_Bread_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="소주 + 빵", inline=False)
        return embed

    if msg=="스테이크":
        embed=discord.Embed(title="스테이크", description="체력 재생 +420", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274672931749888/044._Steak_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="고기 + 달궈진 돌멩이", inline=False)
        return embed

    if msg=="구급상자":
        embed=discord.Embed(title="구급상자", description="체력 재생 +1200", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274673242120322/045._First_Aid_Kit_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="사냥 위클라인(100%)", inline=False)
        return embed

    if msg=="버터감자구이":
        embed=discord.Embed(title="버터 감자구이", description="체력 재생 +766", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274673489604678/046._Butter-Fried_Potatoes__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="감자 + 버터", inline=False)
        return embed

    if msg=="생선까스":
        embed=discord.Embed(title=" 생선까스", description="체력 재생 +700", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274673753849917/047._Fish_Cutlet_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="대구 + 뜨거운 오일", inline=False)
        return embed

    if msg=="볶음라면":
        embed=discord.Embed(title="볶음라면", description="체력 재생 +600", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274674043248650/048._Stir_Fried_Ramen_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="생라면 + 뜨거운 오일", inline=False)
        return embed

    if msg=="냉면":
        embed=discord.Embed(title="냉면", description="체력 재생 +650", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274687792168970/049._Cold_Noodles_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="생라면 + 얼음물", inline=False)
        return embed

    if msg=="생일케이크":
        embed=discord.Embed(title="생일 케이크", description="체력 재생 +650", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274689876746251/050._Birthday_Cake__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="달걀 + 시트러스 케이크", inline=False)
        return embed

    if msg=="마늘라면":
        embed=discord.Embed(title="마늘라면", description="체력 재생 +700", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274690094837780/051._Garlic_Ramen__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="뜨거운 라면 + 마늘", inline=False)
        return embed

    if msg=="대환단":
        embed=discord.Embed(title="대환단", description="체력 재생 +960", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274703617290310/052._Zen_Vitality_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="생명의 나무 + 불경", inline=False)
        return embed

    if msg=="피쉬앤칩스":
        embed=discord.Embed(title="피쉬 앤 칩스", description="체력 재생 +920", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274703843770368/053._Fish_And_Chips__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="생선까스 + 감자튀김", inline=False)
        return embed

    if msg=="일레븐세트":
        embed=discord.Embed(title="일레븐 세트", description="체력 재생 +980\n\n`일레븐 제작가능`", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/913318922772709377/915274704279969822/054._11_Combo_Meal__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="햄버거 + 감자튀김", inline=False)
        return embed


#####음료#####
        
    if msg=="꿀":
        embed=discord.Embed(title="꿀", description="스태미너 재생 +250", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624089654013952/001._Honey_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="골목길(8) 번화가(6) 숲(6)", inline=False)
        return embed

    if msg=="물":
        embed=discord.Embed(title=" 물", description="스태미너 재생 +225", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624093202407434/002._Water_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="채집 연못(10) 호텔(4) 묘지(4) 숲(3) 성당(1)", inline=False)
        return embed

    if msg=="얼음":
        embed=discord.Embed(title="얼음", description="스태미너 재생 +200", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624097069551616/003._Ice_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="호텔(9) 병원(7) 묘지(8)", inline=False)
        return embed

    if msg=="위스키":
        embed=discord.Embed(title="위스키", description="스태미너 재생 +450", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624101393887262/004._Whiskey_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="고급 주택가(5) 호텔(5) 성당(3)", inline=False)
        return embed

    if msg=="커피콩":
        embed=discord.Embed(title="커피콩", description="스태미너 재생 +380", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624107219750982/005._Coffee_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="항구(5) 고급 주택가(5) 묘지(6)", inline=False)
        return embed

    if msg=="탄산수":
        embed=discord.Embed(title="탄산수", description="스태미너 재생 +380", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624110449377330/006._Carbonated_Water_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="모래사장(8) 고급 주택가(8) 호텔(8)", inline=False)
        return embed

    if msg=="우유":
        embed=discord.Embed(title="우유", description="스태미너 재생 +200", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624115142807552/007._Milk_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="번화가(6) 병원(5) 성당(4)", inline=False)
        return embed

    if msg=="뜨거운물":
        embed=discord.Embed(title="뜨거운 물", description="스태미너 재생 +350", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624120121446400/008._Boiling_Water__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="물 + 라이터", inline=False)
        return embed

    if msg=="레몬에이드":
        embed=discord.Embed(title="레몬에이드", description="스태미너 재생 +450", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624123699195924/009._Lemonade_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="탄산수 + 진짜 레몬", inline=False)
        return embed

    if msg=="물병":
        embed=discord.Embed(title="물병", description="스태미너 재생 +380", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624127746670652/010._Water_Bottle_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="물 + 유리병", inline=False)
        return embed

    if msg=="백주":
        embed=discord.Embed(title="백주", description="스태미너 재생 +1000", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624265739305020/011._Baijiu_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="알코올 + 유리병", inline=False)
        return embed

    if msg=="소주":
        embed=discord.Embed(title="소주", description="스태미너 재생 +400", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624272085282866/012._Soju_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="알코올 + 물", inline=False)
        return embed

    if msg=="아이스커피":
        embed=discord.Embed(title="아이스 커피", description="스태미너 재생 +550", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624279630823444/013._Iced_Coffee__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="얼음 + 커피콩", inline=False)
        return embed

    if msg=="칵테일":
        embed=discord.Embed(title="칵테일", description="스태미너 재생 +350", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624286027128842/014._Cocktail_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="위스키 + 레몬", inline=False)
        return embed

    if msg=="커피리큐르":
        embed=discord.Embed(title="커피 리큐르", description="스태미너 재생 +530", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624293492981760/015._Coffee_Liqueur__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="커피콩 + 알코올", inline=False)
        return embed

    if msg=="콜라":
        embed=discord.Embed(title="콜라", description="스태미너 재생 +400", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624298710724628/016._Cola_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="탄산수 + 꿀", inline=False)
        return embed

    if msg=="카페라테":
        embed=discord.Embed(title="카페라테", description="스태미너 재생 +530", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624304364646410/017._Latte_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="우유 + 커피콩", inline=False)
        return embed

    if msg=="꿀탄우유":
        embed=discord.Embed(title="꿀탄 우유", description="스태미너 재생 +530", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624307359363112/018._Honey_Milk__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="우유 + 꿀", inline=False)
        return embed

    if msg=="하이볼":
        embed=discord.Embed(title="하이볼", description="스태미너 재생 +530", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624313235570708/019._Highball_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="위스키 + 탄산수", inline=False)
        return embed

    if msg=="초코우유":
        embed=discord.Embed(title="초코 우유", description="스태미너 재생 +450", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624318436507658/020._Choco_Milk__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="초콜렛 + 우유", inline=False)
        return embed

    if msg=="꿀물":
        embed=discord.Embed(title="꿀물", description="스태미너 재생 +400", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624323830394880/021._Honey_Water_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="꿀 + 물", inline=False)
        return embed

    if msg=="얼음물":
        embed=discord.Embed(title="얼음물", description="스태미너 재생 +350", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624329018757120/022._Ice_Water_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="얼음 + 물", inline=False)
        return embed

    if msg=="온더락":
        embed=discord.Embed(title="온더락", description="스태미너 재생 +530", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624336270688256/023._On_The_Rock.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="얼음 + 위스키", inline=False)
        return embed

    if msg=="카우보이":
        embed=discord.Embed(title="카우보이", description="스태미너 재생 +530", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624343401017414/024._Cowboy_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="우유 + 위스키", inline=False)
        return embed

    if msg=="고량주":
        embed=discord.Embed(title=" 고량주", description="스태미너 재생 +800", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624348153180231/025._Kaoliang_Liquor_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="백주 + 라이터", inline=False)
        return embed

    if msg=="백일취":
        embed=discord.Embed(title="백일취", description="스태미너 재생 +750", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624358555029545/027._Flower_Liquor_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="백주 + 꽃", inline=False)
        return embed

    if msg=="뜨거운꿀물":
        embed=discord.Embed(title=" 뜨거운 꿀물", description="스태미너 재생 +1080", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624352393621514/026._Hot_Honey_Water_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="뜨거운 물 + 꿀", inline=False)
        return embed

    if msg== "아메리카노":
        embed=discord.Embed(title=" 아메리카노", description="스태미너 재생 +1080", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624362032115712/028._Americano_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="뜨거운 물 + 커피콩", inline=False)
        return embed

    if msg=="약주":
        embed=discord.Embed(title="약주", description="스태미너 재생 +1080", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624369892257812/029._Herbal_Liquor_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="백주 + 약초", inline=False)
        return embed

    if msg=="정화수":
        embed=discord.Embed(title="정화수", description="스태미너 재생 +1080", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624377622351903/031._Purified_Water_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="뜨거운 물 + 얼음", inline=False)
        return embed

    if msg=="위스키콕":
        embed=discord.Embed(title="위스키 콕", description="스태미너 재생 +600", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624374245928990/030._Whiskey_Cocktail__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="콜라 + 위스키", inline=False)
        return embed

    if msg=="캔콜라":
        embed=discord.Embed(title="캔 콜라", description="스태미너 재생 +1400", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624382659710976/032._Can_of_Cola__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="콜라 + 캔", inline=False)
        return embed

    if msg=="핫초코":
        embed=discord.Embed(title="핫초코", description="스태미너 재생 +500", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624386828840990/033._Hot_Choco_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="뜨거운 물 + 초콜렛", inline=False)
        return embed

    if msg=="깔루아밀크":
        embed=discord.Embed(title="깔루아 밀크", description="스태미너 재생 +750", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624392499535882/034._White_Russian__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="커피 리큐르 + 우유", inline=False)
        return embed

    if msg=="셀레네의눈물":
        embed=discord.Embed(title="셀레네의 눈물", description="스태미너 재생 +1080\n공격력 +10", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891623996704051241/891624395683024956/035._Tear_of_Selene__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="문스톤 + 물", inline=False)
        return embed


#####머리#####
    if msg=="머리띠":
        embed=discord.Embed(title="머리띠", description="방어력 +4\n최대 스태미너 +130\n", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443076801478656/001._Hairband_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="번화가(8) 절(9) 묘지(8)\n사냥 박쥐 ", inline=False)
        return embed

    if msg=="모자":
        embed=discord.Embed(title="모자", description="방어력 +4\n쿨다운 감소 +5%\n", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443081713000508/002._Hat_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="연못(8) 양궁장(6) 학교(8)\n사냥 박쥐 ", inline=False)
        return embed

    if msg=="자전거헬멧":
        embed=discord.Embed(title="자전거 헬멧", description="최대 체력 +30", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443086720991292/003._Bike_Helmet__.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="모래사장(8) 성당(8) 학교(8)\n사냥 멧돼지(3.3%)", inline=False)
        return embed

    if msg=="가면":
        embed=discord.Embed(title="가면", description="방어력 +10\n최대 스태미너 +150\n(고유) 이동 속도 +0.04\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443091720618044/004._Mask_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="머리띠 + 깃털", inline=False)
        return embed

    if msg=="머리테":
        embed=discord.Embed(title="머리테", description="방어력 +14\n최대 스태미너 +270", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443096577630260/005._Circlet_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="머리띠 + 나뭇가지", inline=False)
        return embed

    if msg=="베레모":
        embed=discord.Embed(title="베레모", description="방어력 +10\n최대 체력 +45\n쿨다운 감소 +7%\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443100843221012/006._Beret_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="모자 + 가위", inline=False)
        return embed

    if msg=="사슬코이프":
        embed=discord.Embed(title="사슬 코이프", description="방어력 +14\n쿨다운 감소 +6%\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443106677502022/008._Chain_Coif__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="모자 + 쇠사슬", inline=False)
        return embed

    if msg=="안전모":
        embed=discord.Embed(title="안전모", description="최대 체력 +90", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443111396089926/008._Safety_Helmet_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="자전거 헬멧 + 돌멩이", inline=False)
        return embed

    if msg=="방탄모":
        embed=discord.Embed(title="방탄모", description="방어력 +15\n최대 체력 +90\n쿨다운 감소 +8%", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443115720425542/009._Ballistic_Helmet_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="베레모 + 자전거 헬멧", inline=False)
        return embed

    if msg=="소방헬멧":
        embed=discord.Embed(title="소방 헬멧", description="최대 체력 +140\n스태미너 재생 +50%", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443122469048330/010._Fire_Helmet__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="안전모 + 뜨거운 물", inline=False)
        return embed

    if msg=="티아라":
        embed=discord.Embed(title="티아라", description="방어력 +16\n최대 스태미너 +400", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443127112142848/011._Tiara_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="머리테 + 마패", inline=False)
        return embed

    if msg=="왕관":
        embed=discord.Embed(title="왕관", description="방어력 +16\n최대 체력 +90\n스킬 증폭 +8%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443132782854174/012._Crown_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="베레모 + 황금", inline=False)
        return embed

    if msg=="투구":
        embed=discord.Embed(title="투구", description="방어력 +20\n최대 스태미너 +200\n쿨다운 감소 +7%\n(고유) 이동 속도 +0.06\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443138944270356/013._Close_Helm_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="사슬 코이프 + 가면", inline=False)
        return embed

    if msg=="오토바이헬멧":
        embed=discord.Embed(title="오토바이 헬멧", description="공격력 +10\n최대 체력 +200\n시야 +2\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443144409456720/014._Motorcycle_Helmet__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="안전모 + 저격 스코프", inline=False)
        return embed

    if msg=="미스릴투구" or msg=="미뚝":
        embed=discord.Embed(title="미스릴 투구", description="방어력 +38\n공격 속도 +30%\n이동 속도 +0.1\n쿨다운 감소 +15%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443149073539142/015._Mithril_Helm__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="미스릴 + 사슬 코이프", inline=False)
        return embed

    if msg=="수정티아라":
        embed=discord.Embed(title="수정 티아라", description="방어력 +24\n최대 스태미너 +500\n치명타 확률 +20%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443153599184996/016._Crystal_Tiara__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="티아라 + 유리 조각", inline=False)
        return embed

    if msg=="전술OPS헬멧" or msg == "ops":
        embed=discord.Embed(title="전술-OPS 헬멧", description="방어력 +15\n최대 체력 +115\n공격 속도 +23%\n시야 +1\n쿨다운 감소 +8%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443160310083634/017._Tactical_OPS_Helmet_-OPS_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="방탄모 + 전자 부품", inline=False)
        return embed

    if msg=="기사단장의투구":
        embed=discord.Embed(title="기사단장의 투구", description="방어력 +20\n최대 스태미너 +200\n쿨다운 감소 +8%\n스킬 피해 감소 +13%\n(고유) 이동 속도 +0.08\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443166081417246/018._Helm_of_Banneret__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="투구 + 고무", inline=False)
        return embed

    if msg=="제국왕관":
        embed=discord.Embed(title="제국 왕관", description="방어력 +28\n최대 체력 +140\n스킬 증폭 +11%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443171601145856/019._Imperial_Crown__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="왕관 + 원석", inline=False)
        return embed

    if msg=="황실부르고넷":
        embed=discord.Embed(title="황실 부르고넷", description="방어력 +10\n최대 스태미너 +400\n쿨다운 감소 +10%\n스킬 증폭 +18%\n(고유) 이동 속도 +0.06\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443176722386964/020._Imperial_Burgonet__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="투구 + 황금", inline=False)
        return embed

    if msg=="모호크헬멧":
        embed=discord.Embed(title="모호크 헬멧", description="최대 체력 +200\n스태미너 재생 +50%\n리플렉션-[고유 장착 효과]\n기본 공격으로 받은 피해의 4.5%를 공격자에게 고정 피해로 되돌려 줍니다. (근거리) 4초 동안 45%의 치유 감소 효과를 줍니다. (원거리) 4초 동안 35%의 치유 감소 효과를 줍니다. 또한 4초간 누적해서 600의 피해를 받으면, 주변에 150의 피해를 줍니다.\n(쿨다운: 3초)", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443181784924181/021._Mohawk_Headgear__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="소방 헬멧 + 가시 발판", inline=False)
        return embed

    if msg=="비질란테":
        embed=discord.Embed(title="비질란테", description="최대 체력 +175\n스태미너 재생 +50%\n스킬 피해 감소 +12\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443185601708062/022._Vigilante_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="소방 헬멧 + 개량형 쥐덫", inline=False)
        return embed

    if msg=="다이아뎀":
        embed=discord.Embed(title="다이아뎀", description="공격력 +10\n방어력 +15\n최대 스태미너 +270\n쿨다운 감소 +12%\n기본 공격 추가 피해 +11\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/896473504894029845/Diadem_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="머리테 + 바브드 블로섬", inline=False)
        return embed

    if msg=="월계관":
        embed=discord.Embed(title="월계관", description="공격력 +10\n방어력 +20\n최대 스태미너 +580\n스태미너 재생 +2\n기본 공격 추가 피해 +19\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443193524776960/023._Laurel_Wreath_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="삼매진화 + 머리테", inline=False)
        return embed

    if msg=="변검":
        embed=discord.Embed(title="변검", description="공격력 +20\n방어력 +20\n최대 스태미너 +200\n이동 속도 +0.1\n모든 피해 흡수 +20%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443199711379506/024._Chinese_Opera_Mask_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="가면 + VF 혈액 샘플", inline=False)
        return embed

    if msg=="천사의고리" or msg=="천고":
        embed=discord.Embed(title="천사의 고리", description="공격력 +25\n방어력 +40\n최대 스태미너 +300\n```의념-[고유 장착 효과]\n스킬을 사용하면 의념을 충전합니다. 충전된 상태에서 다음 3초 안에 이루어지는 기본 공격이 추가 고유 피해를 입힙니다. \n(쿨다운 : 2.5초)\n(근거리)적 최대 체력의 10%에 해당하는 피해를 입힙니다.\n(원거리)적 최대 체력의 8%에 해당하는 피해를 입힙니다.```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443203586895882/025._Elysian_Halo__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="포스코어 + 머리테", inline=False)
        return embed

    if msg=="빛의증표" or msg=="빛증":
        embed=discord.Embed(title="빛의 증표", description="방어력 +28\n최대 스태미너 +500\n치명타 확률 +24%\n치명타 피해량 +12%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322199078744074/892443209723174932/026._Fallen_Pegasus__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="수정 티아라 + 운석", inline=False)
        return embed

#####옷#####
    if msg=="바람막이":
        embed=discord.Embed(title="바람막이", description="방어력 +5\n기본 공격 피해 감소 +3", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184357929512960/001._Windbreaker_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 고급 주택가(7) 호텔(7) 학교(8)\n사냥 들개", inline=False)
        return embed

    if msg=="승복":
        embed=discord.Embed(title="승복", description="방어력 +5\n쿨다운 감소 +5%", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184358139199488/002._Monk_s_Robe_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 절(9) 양궁장(7)\n사냥 멧돼지", inline=False)
        return embed

    if msg=="전신수영복":
        embed=discord.Embed(title="전신 수영복", description="방어력 +5\n스킬 피해 감소 +3%", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184358411849738/003._Wetsuit__.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 항구(7) 모래사장(6) 골목길(8)\n사냥 들개", inline=False)
        return embed

    if msg=="천갑옷":
        embed=discord.Embed(title="천 갑옷", description="방어력 +11", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184358592208906/004._Fabric_Armor__.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="지역 절(9) 양궁장(7) 묘지(8)\n사냥 들개", inline=False)
        return embed

    if msg=="가죽갑옷":
        embed=discord.Embed(title="가죽 갑옷", description="방어력 +15", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184470370385980/005._Leather_Armor__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="천 갑옷 + 가죽", inline=False)
        return embed

    if msg=="가죽자켓":
        embed=discord.Embed(title="가죽 자켓", description="방어력 +10\n기본 공격 피해 감소 +3", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184470626271253/006._Leather_Jacket__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="바람막이 + 가죽", inline=False)
        return embed

    if msg=="거북도복":
        embed=discord.Embed(title="거북 도복", description="방어력 +10\n쿨다운 감소 +7%", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184471142146088/007._Turtle_Dobok__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="승복 + 거북이 등딱지", inline=False)
        return embed

    if msg=="군복":
        embed=discord.Embed(title="군복", description="방어력 +8\n최대 체력 +30\n기본 공격 피해 감소 +5\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184471360262184/008._Miltary_Suit_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="바람막이 + 나뭇가지", inline=False)
        return embed

    if msg=="덧댄로브":
        embed=discord.Embed(title="덧댄 로브", description="방어력 +5\n체력 재생 +1\n쿨다운 감소 +7%\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184471578345522/009._Patched_Robe__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="승복 + 붕대", inline=False)
        return embed

    if msg=="드레스":
        embed=discord.Embed(title="드레스", description="공격력 +8\n방어력 +8\n스태미너 재생 +80%\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184471813238814/010._Dress_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="옷감 + 가위", inline=False)
        return embed

    if msg=="비키니":
        embed=discord.Embed(title="비키니", description="방어력 +6\n스킬 피해 감소 +8%", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184472060694608/011._Bikini_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="전신 수영복 + 가위", inline=False)
        return embed

    if msg=="잠수복":
        embed=discord.Embed(title="잠수복", description="방어력 +10\n스킬 피해 감소 +6%", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184472408825926/012._Diving_Suit_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="전신 수영복 + 고무", inline=False)
        return embed

    if msg=="사제복":
        embed=discord.Embed(title="사제복", description="최대 체력 +80\n스킬 공격 추가 피해 +4", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184472786333696/013._Deacon_Robes_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="옷감 + 십자가", inline=False)
        return embed

    if msg=="라이더자켓":
        embed=discord.Embed(title="라이더 자켓", description="방어력 +10\n기본 공격 피해 감소 +4", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184520244875284/015._Rider_Jacket__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="가죽 자켓 + 쇠사슬", inline=False)
        return embed

    if msg=="사슬갑옷":
        embed=discord.Embed(title="사슬 갑옷", description="방어력 +28", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184519947083866/014._Chain_Armor__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="가죽 갑옷 + 쇠사슬", inline=False)
        return embed

    if msg=="정장":
        embed=discord.Embed(title="정장", description="생명력 흡수 +15%\n기본 공격 피해 감소 +4", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184520551067708/016._Suit_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="가죽 자켓 + 리본", inline=False)
        return embed

    if msg=="치파오":
        embed=discord.Embed(title="치파오", description="공격력 +10\n방어력 +10\n스태미너 재생 +100%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184520769159198/017._Qipao_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="드레스 + 면도칼", inline=False)
        return embed

    if msg=="판금갑옷":
        embed=discord.Embed(title="판금 갑옷", description="방어력 +28\n최대 체력 +50", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184521041772554/018._Sheet_Metal_Armor__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="천 갑옷 + 강철", inline=False)
        return embed

    if msg=="한복":
        embed=discord.Embed(title="한복", description="방어력 +12\n체력 재생 +1\n쿨다운 감소 +10%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184521318617148/019._Hanbok_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="덧댄 로브 + 꽃", inline=False)
        return embed

    if msg=="고위사제복":
        embed=discord.Embed(title="고위 사제복", description="방어력 +10\n최대 체력 +140\n체력 재생 +0.9\n스킬 공격 추가 피해 +12", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184521591250964/020._Cardinal_Robes__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="사제복 + 기름먹인 천", inline=False)
        return embed

    if msg=="방탄조끼":
        embed=discord.Embed(title="방탄조끼", description="방어력 +15\n최대 체력 +100\n기본 공격 피해 감소 +8\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184521842905088/021._Bulletproof_Vest_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="군복 + 철판", inline=False)
        return embed

    if msg=="어사의":
        embed=discord.Embed(title="어사의", description="방어력 +30\n체력 재생 +1\n시야 +1\n쿨다운 감소 +15%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184522463657994/023._Covert_Agent_Uniform_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="한복 + 마패", inline=False)
        return embed

    if msg=="석양의갑옷":
        embed=discord.Embed(title="석양의 갑옷", description="방어력 +33\n최대 체력 +220\n시야 +1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184522157482004/022._Sunset_Armor__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="사슬 갑옷 + 루비", inline=False)
        return embed

    if msg=="광학미채슈트":
        embed=discord.Embed(title="광학미채 슈트", description="공격력 +10\n방어력 +18\n치명타 확률 +24%\n스킬 피해 감소 +10%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184644773773332/024._Optical_Camouflage_Suit__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="잠수복 + 유리판", inline=False)
        return embed

    if msg=="락커의자켓":
        embed=discord.Embed(title="락커의 자켓", description="공격력 +25\n방어력 +10\n비 전투중 이동 속도 +0.1\n기본 공격 피해 감소 +5\n```스킬 공격 치유 방해-[고유 장착 효과]\n스킬 공격 시 피격된 대상의 치유 효과가 감소합니다.\n(근거리) 치유 효과가 45% 감소합니다.\n(원거리) 치유 효과가 35% 감소합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184644773773332/024._Optical_Camouflage_Suit__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="라이더 자켓 + 소란 발생기", inline=False)
        return embed

    if msg=="미스릴갑옷" or msg=="미갑":
        embed=discord.Embed(title="미스릴 갑옷", description="방어력 +60\n이동 속도 +0.1\n스킬 피해 감소 +14\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184645201563678/026._Mithril_Armor__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="미스릴 + 가죽 갑옷", inline=False)
        return embed

    if msg=="성기사의갑옷":
        embed=discord.Embed(title="성기사의 갑옷", description="방어력 +30\n최대 체력 +50\n체력 재생 +150%\n기본 공격 추가 피해 +14\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184645419683840/027._Crusader_Armor__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="판금 갑옷 + 성자의 유산", inline=False)
        return embed

    if msg=="아마조네스아머":
        embed=discord.Embed(title="아마조네스 아머", description="방어력 +28\n최대 체력 +155\n스킬 피해 감소 +17%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184645650366504/028._Amazoness_Armor__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="판금 갑옷 + 비키니", inline=False)
        return embed

    if msg=="용의도복":
        embed=discord.Embed(title="용의 도복", description="공격력 +10\n방어력 +15\n스태미너 재생 +100%\n쿨다운 감소 +10%\n(고유) 기본 공격 사거리 +0.75\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184646048808980/029._Dragon_Dobok__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="치파오 + 거북 도복", inline=False)
        return embed

    if msg=="지휘관의갑옷":
        embed=discord.Embed(title="지휘관의 갑옷", description="방어력 +28\n스킬 증폭 +20%", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184646262738944/030._Commander_s_Armor__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="사슬 갑옷 + 황금", inline=False)
        return embed

    if msg=="집사복":
        embed=discord.Embed(title="집사복", description="공격력 +25\n생명력 흡수 +18%\n기본 공격 피해 감소 +5\n(고유) 이동 속도 +0.08", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184646464069652/031._Butler_s_Suit_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="정장 + 먼지털이개", inline=False)
        return embed

    if msg=="배틀슈트":
        embed=discord.Embed(title="배틀 슈트", description="방어력 +25\n최대 체력 +120\n치명타 피해 감소 +8%\n기본 공격 피해 감소 +8\n스킬 피해 감소 +8%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184646673793074/032._Battle_Suit__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="방탄조끼 + 잠수복", inline=False)
        return embed

    if msg=="EOD슈트":
        embed=discord.Embed(title="EOD 슈트", description="방어력 +25\n최대 체력 +165\n체력 재생 +1\n쿨다운 감소 +10%\n기본 공격 피해 감소 +8\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184644455002182/033._EOD_Suit_EOD_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="방탄조끼 + 덧댄 로브", inline=False)
        return embed

    if msg=="턱시도":
        embed=discord.Embed(title="턱시도", description="방어력 +20\n생명력 흡수 +11%\n레벨 당 기본 공격 추가 피해 +1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184670677786624/034._Tuxedo_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="정장 + 드레스", inline=False)
        return embed

    if msg=="제사장의예복":
        embed=discord.Embed(title="제사장의 예복", description="방어력 +30\n체력 재생 +1\n스태미너 재생 +85%\n쿨다운 감소 +15%\n(고유) 최대 쿨다운 감소 +5%", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184671260786698/035._High_Priest_Robes__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="한복 + 정화수", inline=False)
        return embed

    if msg=="창파오":
        embed=discord.Embed(title="창파오", description="공격력 +20\n방어력 +10\n스태미너 재생 +2\n공격 속도 +35%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184670451302441/036._Changpao_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="치파오 + 백일취", inline=False)
        return embed

    if msg=="불꽃드레스" or msg=="불드":
        embed=discord.Embed(title="불꽃 드레스", description="공격력 +16\n방어력 +30\n스태미너 재생 +100%\n```불꽃 결계-[고유 장착 효과]\n전투에 돌입하면 매 초마다 주변 3m의 적에게 고유 피해를 입힙니다.\n(근거리) 적에게 최대 체력의 4.5%의 고유 피해를 입힙니다.\n(원거리) 적에게 최대 체력의 4%의 고유 피해를 입힙니다.```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184688734257152/037._Blazing_Dress__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="삼매진화 + 드레스", inline=False)
        return embed

    if msg=="카바나":
        embed=discord.Embed(title="카바나", description="방어력 +40\n시야 +1\n스킬 증폭 +22%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184688981712916/038._Kabana_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="운석 + 지휘관의 갑옷", inline=False)
        return embed

    if msg=="퀸오브하트"  or msg=="퀸오하":
        embed=discord.Embed(title="퀸 오브 하트", description="방어력 +40\n체력 재생 +2\n쿨다운 감소 +30%\n(고유) 최대 쿨다운 감소 +10%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184689292087326/039._Queen_of_Hearts__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="VF 혈액 샘플 + 덧댄 로브", inline=False)
        return embed

    if msg=="성법의":
        embed=discord.Embed(title="성법의", description="최대 체력 +225\n치명타 피해 감소 +5%\n스킬 공격 추가 피해 +15\n```굴절-[고유 장착 효과]\n굴절의 망토를 두릅니다. 굴절의 망토는 적이 나에게 가하는 다음 스킬 및 트랩의 피해와 효과를 한번 보호해 준 뒤 사라지고, 20초 후 재생성 됩니다.```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184689522798604/040._Holy_Orders_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="포스 코어 + 사제복", inline=False)
        return embed

    if msg=="버건디 47" or msg=="버건디":
        embed=discord.Embed(title="버건디 47", description="공격력 +25\n이동 속도 +0.1\n생명력 흡수 +20%\n기본 공격 피해 감소 +7\n```세컨드 윈드-핏빛 갈증-[고유 장착 효과]\n착용자가 적 실험체에게 피해를 받아 체력이 40% 이하가 될 때, 1.5초간 400 + 캐릭터 레벨 * 10의 보호막을 얻습니다. 또한 8초 동안 공격력이 25 증가하고,\n(근거리) 받는 회복량이 % 증가합니다.\n(쿨다운 : 80초)\n(원거리) 받는 회복량이 % 증가합니다.\n(쿨다운 : 80초)```\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/920184689740894248/041._Burgundy_47__47.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="VF 혈액 샘플 + 정장", inline=False)
        return embed

    if msg=="미스릴크롭":
        embed=discord.Embed(title="미스릴 크롭", description="방어력 +65\n공격 속도 +18%\n이동 속도 +0.2\n\n`마이 제작가능`", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/928692926333206608/Mithril_Crop__.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="비키니 + 미스릴", inline=False)
        return embed

    if msg=="아오자이":
        embed=discord.Embed(title="아오자이", description="공격력 +45\n방어력 +65\n스태미너 재생 +100%\n\n`마이 제작 가능`", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/928692926106718299/Ao_Dai_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="드레스 + 포스 코어", inline=False)
        return embed

    if msg=="팬텀자켓":
        embed=discord.Embed(title="팬텀자켓", description="방어력 +25\n기본 공격 피해 감소 +7\n기본 공격 사거리 -0.35\n```발화-(고유 장착 효과)\n(기본 공격 시) 초당 근거리 1.1%/원거리 0.6%의 고정 피해를 4초간 입힙니다. (최대 4스택)```\n`마이 제작 가능`", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916320335131987998/928692926576488448/Phantom_Jacket_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="라이더 자켓 + 삼매진화", inline=False)
        return embed

    

    

#####팔#####
    if msg=="손목시계":
        embed=discord.Embed(title="손목시계", description="공격 속도 +10%", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443814206275665/001._Watch_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="고급 주택가(7) 호텔(6) 번화가(8)\n사냥 들개 ", inline=False)
        return embed

    if msg=="붕대":
        embed=discord.Embed(title="붕대", description="체력 재생 +0.8", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443819780485230/002._Bandage_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="항구(8) 골목길(8) 병원(8) 학교(9)\n사냥 박쥐 (4.4%) ", inline=False)
        return embed

    if msg=="팔찌":
        embed=discord.Embed(title="팔찌", description="최대 스태미너 +220", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443824503263272/003._Bracelet_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="연못(7) 고급 주택가(7) 골목길(7)\n 사냥  들개 ", inline=False)
        return embed

    if msg=="가죽방패":
        embed=discord.Embed(title="가죽 방패", description="공격력 +5\n방어력 +15", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443829494489109/004._Leather_Shield__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="거북이 등딱지 + 가죽", inline=False)
        return embed

    if msg=="분대장완장":
        embed=discord.Embed(title="분대장 완장", description="체력 재생 +0.6\n치명타 피해량 +15%", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443835186163732/005._Squad_Leader_Armband__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="붕대 + 바늘", inline=False)
        return embed

    if msg=="브레이서":
        embed=discord.Embed(title="브레이서", description="방어력 +13\n체력 재생 +1", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443841137877062/006._Bracer_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="붕대 + 가죽", inline=False)
        return embed

    if msg=="고장난시계":
        embed=discord.Embed(title="고장난 시계", description="쿨다운 감소 +5%", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443846456254545/007._Broken_Watch__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="손목시계 + 접착제", inline=False)
        return embed

    if msg=="검집":
        embed=discord.Embed(title="검집", description="공격력 +18\n기본 공격 피해 감소 +5", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443850906435604/008._Sheath_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="가죽 + 철판", inline=False)
        return embed

    if msg=="금팔찌":
        embed=discord.Embed(title="금팔찌", description="최대 스태미너 +220\n스킬 증폭 +12%", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443856736501801/009._Golden_Bracelet_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="팔찌 + 황금", inline=False)
        return embed

    if msg=="바주반드":
        embed=discord.Embed(title="바주반드", description="방어력 +28\n기본 공격 피해 감소 +4", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443862931476510/010._Bazuband_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="브레이서 + 철판", inline=False)
        return embed

    if msg=="진홍팔찌":
        embed=discord.Embed(title="진홍 팔찌", description="최대 체력 +100\n최대 스태미너 +250", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443867566211092/011._Crimson_Bracelet__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="팔찌 + 가시 발판", inline=False)
        return embed

    if msg=="바브드블로섬":
        embed=discord.Embed(title="바브드 블로섬", description="공격력 +10\n쿨다운 감소 +7%", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443874209980526/012._Barbed_Blossom__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="꽃 + 철사", inline=False)
        return embed

    if msg=="강철방패":
        embed=discord.Embed(title="강철 방패", description="공격력 +20\n방어력 +20", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443877959688222/013._Steel_Shield__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="방패 + 강철", inline=False)
        return embed

    if msg=="소드스토퍼":
        embed=discord.Embed(title="소드 스토퍼", description="방어력 +28\n기본 공격 피해 감소 +4\n```리플렉션-[고유 장착 효과]\n기본 공격으로 받은 피해의 4.5%를 공격자에게 고정 피해로 되돌려 줍니다. (근거리) 4초 동안 45%의 치유 감소 효과를 줍니다. (원거리) 4초 동안 35%의 치유 감소 효과를 줍니다. 또한 4초 안에 600 이상의 피해를 입으면 6m(반지름) 범위 안에 150의 고유 피해를 입힙니다. \n쿨다운 : 3초```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443884381143090/014._Sword_Stopper__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="바주반드 + 못", inline=False)
        return embed

    if msg=="드라우프니르":
        embed=discord.Embed(title="드라우프니르", description="방어력 +20\n최대 스태미너 +240\n체력 재생 +1\n스킬 증폭 +19%", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443890135748698/015._Draupnir_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="금팔찌 + 브레이서", inline=False)
        return embed

    if msg=="미스릴방패":
        embed=discord.Embed(title="미스릴 방패", description="공격력 +30\n방어력 +30\n공격 속도 +12%\n이동 속도 +0.1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443895420563456/016._Mithril_Shield__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="미스릴 + 가죽 방패", inline=False)
        return embed

    if msg=="바이탈센서":
        embed=discord.Embed(title="바이탈 센서", description="방어력 +15\n공격 속도 +40%", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443900386607114/017._Vital_Sign_Censor__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="손목 시계 + 휴대폰", inline=False)
        return embed

    if msg=="기사의신조":
        embed=discord.Embed(title="기사의 신조", description="공격력 +22\n방어력 +22\n체력 재생 +0.8\n치명타 피해량 +20%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443904736100382/018._Creed_of_the_Knight__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="강철 방패 + 분대장 완장", inline=False)
        return embed

    if msg=="샤자한의검집":
        embed=discord.Embed(title="샤자한의 검집", description="공격력 +33\n최대 체력 +110\n기본 공격 피해 감소 +10", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443909597302834/019._Sheath_of_Shah_Jahan__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="검집 + 루비", inline=False)
        return embed

    if msg=="큐브워치":
        embed=discord.Embed(title="큐브 워치", description="방어력 +18\n공격 속도 +60%\n쿨다운 감소 +10%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443916459192341/020._Cube_Watch__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="고장난 시계 + 문스톤", inline=False)
        return embed

    if msg=="아이기스":
        embed=discord.Embed(title="아이기스", description="공격력 +8\n방어력 +25\n최대 체력 +175\n최대 스태미너 +300\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443921085501490/021._Burnished_Aegis_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="진홍 팔찌 + 가죽 방패", inline=False)
        return embed

    if msg=="틴달로스의팔찌":
        embed=discord.Embed(title="틴달로스의 팔찌", description="최대 스태미너 +240\n쿨다운 감소 +12%\n스킬 증폭 +14%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443926336786472/022._Tindalos_Band__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="금팔찌 + 고장난 시계", inline=False)
        return embed

    if msg=="나이팅게일":
        embed=discord.Embed(title="나이팅게일", description="공격력 +20\n최대 체력 +160\n(고유) 받는 회복 증가 +15%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443931730653204/023._Nightingale_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="분대장 완장 + 힐링 포션", inline=False)
        return embed

    if msg=="플라즈마아크":
        embed=discord.Embed(title="플라즈마 아크", description="공격력 +20\n방어력 +20\n공격 속도 +28%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443937065824256/024._Plasma_Arc__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="강철 방패 + 전자 부품", inline=False)
        return embed

    if msg=="스마트밴드":
        embed=discord.Embed(title="스마트 밴드", description="공격력 +30\n쿨다운 감소 +12%\n생명력 흡수 +6%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443948444962876/026._Smart_Band__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="바브드 블로섬 + +정교한 도면", inline=False)
        return embed

    if msg=="스카디의팔찌" or msg == "스카디":
        embed=discord.Embed(title="스카디의 팔찌", description="최대 체력 +100\n최대 스태미너 +250\n스태미너 재생 +1.2\n스킬 공격 추가 피해 +24\n```한파-[고유 장착 효과]\n스킬로 적에게 피해를 입히면 1초간 이동 속도를 20%만큼 느리게 만듭니다.\n(쿨다운: 3초)```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892444049032773732/027._Bracelet_of_Skadi__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="만년빙 + 진홍 팔찌", inline=False)
        return embed

    if msg=="텔루리안타임피스":
        embed=discord.Embed(title="텔루리안 타임피스", description="방어력 +33\n쿨다운 감소 +15%\n공격 속도 +20%\n 굴절-[고유 장착 효과]\n굴절의 망토를 두릅니다. 굴절의 망토는 적이 나에게 가하는 다음 스킬 및 트랩의 피해와 효과를 한번 보호해 준 뒤 사라지고, 20초 후 재생성 됩니다.", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892443942681976862/025._Tellurian_Timepiece__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="고장난 시계 + 포스 코어", inline=False)
        return embed

    if msg=="레이더":
        embed=discord.Embed(title="레이더", description="방어력 +20\n공격 속도 +40%\n치명타 확률 +24%", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892444094197018644/028._Radar_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="바이탈 센서 + 유리판", inline=False)
        return embed

    if msg=="오토암즈" or msg == "오암":
        embed=discord.Embed(title="오토-암즈", description="공격력 +45\n방어력 +35\n체력 재생 +1\n치명타 피해 감소 +8%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892444176908709938/029._Auto-arms_-.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="브레이서 + 포스 코어", inline=False)
        return embed

    if msg=="프로미넌스":
        embed=discord.Embed(title="프로미넌스", description="최대 체력 +215\n최대 스태미너 +250\n쿨다운 감소 +30%\n(고유) 최대 쿨다운 감소 +10%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322279160602634/892444245112266762/030._Prominence_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="진홍 팔찌 + VF 혈액 샘플", inline=False)
        return embed


#####다리#####
    if msg=="슬리퍼":
        embed=discord.Embed(title="슬리퍼", description="스태미너 재생 +0.5\n이동 속도 +0.04", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443314287169617/001._Slippers_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="지역 항구(7) 번화가(9) 학교(9)\n사냥 박쥐", inline=False)
        return embed

    if msg=="운동화":
        embed=discord.Embed(title="", description="이동 속도 +0.06", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443318762496052/002._Running_Shoes_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="지역 고급 주택가(8) 골목길(9) 양궁장(8)\n사냥 들개", inline=False)
        return embed

    if msg=="타이즈":
        embed=discord.Embed(title="타이즈", description="방어력 +5\n이동 속도 +0.04", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443323514617926/003._Tights_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="지역 번화가(8) 병원(7) 숲(8)\n사냥 멧돼지(3.3%)", inline=False)
        return embed

    if msg=="무릎보호대":
        embed=discord.Embed(title="무릎 보호대", description="방어력 +8\n이동 속도 +0.13", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443328392605816/004._Knee_Pads__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="타이즈 + 접착체", inline=False)
        return embed

    if msg=="체인레깅스":
        embed=discord.Embed(title="체인 레깅스", description="방어력 +10\n이동 속도 +0.11", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443332641435739/005._Chain_Leggings__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="타이즈 + 쇠사슬", inline=False)
        return embed

    if msg=="하이힐":
        embed=discord.Embed(title="하이힐", description="스태미너 재생 +0.8\n이동 속도 +0.14", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443336940617799/006._High_Heels_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="슬리퍼 + 고철", inline=False)
        return embed

    if msg=="힐리스":
        embed=discord.Embed(title="힐리스", description="이동 속도 +0.06\n비 전투중 이동 속도 +0.17", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443342825218098/007._Heelys_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="운동화 + 쇠구슬", inline=False)
        return embed

    if msg=="나막신":
        embed=discord.Embed(title="나막신", description="이동 속도 +0.12", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443347078225990/008._Clogs_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="올가미 + 나뭇가지", inline=False)
        return embed

    if msg=="덧댄슬리퍼":
        embed=discord.Embed(title="덧댄 슬리퍼", description="스태미너 재생 +0.5\n스태미너 재생 +30%\n이동 속도 +0.13\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443353348706344/009._Repaired_Slippers__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="슬리퍼 + 옷감", inline=False)
        return embed

    if msg=="부츠":
        embed=discord.Embed(title="부츠", description="체력 재생 +0.6\n공격 속도 +2%\n이동 속도 +0.17\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443359233343538/010._Boots_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="운동화 + 기름먹인 천", inline=False)
        return embed

    if msg=="등산화":
        embed=discord.Embed(title="등산화", description="이동 속도 +0.27", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443364224540752/011._Hiking_Boots_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="나막신 + 돌멩이", inline=False)
        return embed

    if msg=="강철무릎보호대":
        embed=discord.Embed(title="강철 무릎 보호대", description="방어력 +15\n이동 속도 +0.21", color=0x1e92cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443373452021880/012._Steel_Knee_Pads__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="무릎 보호대 + 강철", inline=False)
        return embed

    if msg=="전투화":
        embed=discord.Embed(title="전투화", description="체력 재생 +0.6\n공격 속도 +7%\n이동 속도 +0.21\n", color=0x1e92cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443378250293338/013._Combat_Boots_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="부츠 + 가죽", inline=False)
        return embed

    if msg=="킬힐":
        embed=discord.Embed(title="킬힐", description="공격력 +5\n스태미너 재생 +0.8\n이동 속도 +0.19\n치명타 확률 +10%\n", color=0x1e92cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443382545281094/014._Killer_Heels_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="하이힐 + 유리 조각", inline=False)
        return embed

    if msg=="아이젠":
        embed=discord.Embed(title="아이젠", description="방어 관통 +8%\n이동 속도 +0.25", color=0x1e92cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/920196370378395658/012._Glacier_Crampons_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="고철 + 철사", inline=False)
        return embed

    if msg=="경량화부츠":
        embed=discord.Embed(title="경량화 부츠", description="체력 재생 +1\n공격 속도 +30%\n이동 속도 +0.32\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443387414859836/015._Feather_Boots__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="전투화 + 깃털", inline=False)
        return embed

    if msg=="매버릭러너":
        embed=discord.Embed(title="매버릭 러너", description="공격력 +15\n이동 속도 +0.32\n(고유) 방해 효과 저항 +15%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443391860822026/016._Maverick_Runner__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="힐리스 + 휴대폰", inline=False)
        return embed

    if msg=="풍화륜":
        embed=discord.Embed(title="풍화륜", description="스태미너 재생 +0.5\n스태미너 재생 +50%\n이동 속도 +0.27\n스킬 공격 추가 피해 +10\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443399007928360/017._Straitjacket_Sneakers_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="덧댄 슬리퍼 + 재", inline=False)
        return embed

    if msg=="미스릴부츠":
        embed=discord.Embed(title="미스릴 부츠", description="방어력 +18\n공격 속도+22%\n이동 속도 +0.42", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443401113436270/018._Mithril_Boots__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="미스릴 + 체인 레깅스", inline=False)
        return embed

    if msg=="부케팔로스":
        embed=discord.Embed(title="부케팔로스", description="공격력 +5\n방어력 +10\n스태미너 재생 +1\n이동 속도 +0.27\n치명타 확률 +20%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443406125629470/019._Bucephalus_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="킬힐 + 체인 레깅스", inline=False)
        return embed

    if msg=="클링온부츠":
        embed=discord.Embed(title="클링온 부츠", description="체력 재생 +0.7\n공격 속도 +15%\n이동 속도 +0.27\n```기본 공격 치유 방해-[고유 장착 효과]\n기본 공격에 피격된 대상의 치유 효과가 4초 동안 감소합니다.\n(근거리) 치유 효과가 45% 감소합니다.\n(원거리) 치유 효과가 35% 감소합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443413734105118/020._White_Rhinos__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="전투화 + 못", inline=False)
        return embed

    if msg=="타키온브레이스":
        embed=discord.Embed(title="타키온 브레이스", description="방어력 +15\n이동 속도 +0.27\n쿨다운 감소 +8%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443417370583120/021._Tachyon_Brace__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="모터 + 무릎 보호대", inline=False)
        return embed

    if msg=="아이언메이든":
        embed=discord.Embed(title="아이언 메이든", description="방어 관통 +10%\n이동 속도 +0.33", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/920196370160300072/023._Iron_Maiden__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="아이젠 + 운석", inline=False)
        return embed

    if msg=="탭루트":
        embed=discord.Embed(title="탭루트", description="최대 체력 +150\n이동 속도 +0.37\n(고유) 받는 회복 증가 +20%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443422143696936/022._Taproot_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="나막신 + 구급 상자", inline=False)
        return embed

    if msg=="EOD부츠":
        embed=discord.Embed(title="EOD 부츠", description="방어력 +24\n체력 재생 +1\n스태미너 재생 +0.5\n이동 속도 +0.3\n트랩 피해 감소 +10%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443426593837087/023._EOD_Boots_EOD_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="부츠 + 강철 무릎 보호대", inline=False)
        return embed

    if msg=="글레이셜슈즈" or msg=="글슈":
        embed=discord.Embed(title="글레이셜 슈즈", description="체력 재생 +1.2\n스태미너 재생 +1.2\n스태미너 재생 +60%\n이동 속도 +0.33\n스킬 공격 추가 피해 +14\n레벨 당 스킬 공격 추가 피해 +0.5\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443433896132608/024._Glacial_Shoes__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="덧댄 슬리퍼 + 만년빙", inline=False)
        return embed

    if msg=="헤르메스의부츠" or msg=="헤르메스":
        embed=discord.Embed(title="헤르메스의 부츠", description="방어력 +32\n이동 속도 +0.37\n비 전투중 이동 속도 +0.1\n(고유) 방해 효과 저항 +25%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443437851377704/025._Boots_of_Hermes__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="포스 코어 + 힐리스", inline=False)
        return embed

    if msg=="분홍신":
        embed=discord.Embed(title="분홍신", description="공격력 +25\n스태미너 재생 +1\n이동 속도 +0.42\n모든 피해 흡혈 +15%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322212408238131/892443443605958796/026._Red_Shoes_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="하이힐 + VF 혈액 샘플", inline=False)
        return embed

#####장식#####
    if msg=="깃털":
        embed=discord.Embed(title="깃털", description="(고유) 이동 속도 +0.04", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443490712178728/001._Feather_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="지역 병원(9) 묘지(9) 숲(11)\n사냥 멧돼지", inline=False)
        return embed

    if msg=="꽃":
        embed=discord.Embed(title="꽃", description="쿨다운 감소 +5%", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443495380447312/002._Flower_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="지역 연못(8) 고급 주택가(7) 묘지(8) 숲(8)\n사냥 멧돼지", inline=False)
        return embed

    if msg=="리본":
        embed=discord.Embed(title="리본", description="생명력 흡수 +5%", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443499172077629/003._Ribbon_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="지역 연못(8) 고급 주택가(7) 학교(8)\n사냥 들개", inline=False)
        return embed

    if msg=="부채":
        embed=discord.Embed(title="부채", description="스킬 공격 추가 피해 +5", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443503374790697/004._Fan_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="지역 번화가(9) 숲(8) 성당(8)\n사냥 들개", inline=False)
        return embed

    if msg=="불경":
        embed=discord.Embed(title="불경", description="스킬 증폭 +7%", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443512191197214/005._Buddhist_Scripture_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="지역 절(11)\n사냥 박쥐", inline=False)
        return embed

    if msg=="상자":
        embed=discord.Embed(title="상자", description="최대 체력 +45", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443516486185001/006._Box_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="지역 항구(8) 연못(7) 성당(8)\n사냥 박쥐", inline=False)
        return embed

    if msg=="성배":
        embed=discord.Embed(title="성배", description="체력 재생 +60%", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443521829699604/007._Holy_Grail_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="지역 성당(11)\n사냥 박쥐", inline=False)
        return embed

    if msg=="십자가":
        embed=discord.Embed(title="십자가", description="기본 공격 추가 피해 +5", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443526711902248/008._Cross_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="지역 골목길(8) 성당(11)\n사냥 들개", inline=False)
        return embed

    if msg=="쌍안경":
        embed=discord.Embed(title="쌍안경", description="공격력 +2\n시야 +1", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443531782787082/009._Binoculars_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="지역 모래사장(5) 골목길 (6) 호텔(5) 공장(6)\n사냥 박쥐(4.4%)", inline=False)
        return embed

    if msg=="운명의꽃":
        embed=discord.Embed(title="운명의 꽃", description="치명타 확률 +15%\n쿨다운 감소 +8%", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443542943830078/011._Flower_of_Fate__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="꽃 + 트럼프 카드", inline=False)
        return embed

    if msg=="유리조각":
        embed=discord.Embed(title="유리 조각", description="치명타 확률 +7%", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443551642828920/012._Glass_Pieces__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="유리병 + 돌맹이", inline=False)
        return embed

    if msg=="인형":
        embed=discord.Embed(title="인형", description="스태미너 재생 +50%\n생명력 흡수 +12%", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443557934284800/013._Doll_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="리본 + 옷감", inline=False)
        return embed

    if msg=="저격스코프":
        embed=discord.Embed(title="저격 스코프", description="공격력 +8\n시야 +2.5", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443573197344768/014._Sniper_Scope__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="레이저 포인터 + 쌍안경", inline=False)
        return embed

    if msg=="진신사리":
        embed=discord.Embed(title="진신사리", description="쿨다운 감소 +5%\n스킬 증폭 +9%", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443580189261895/015._Buddha_Sarira_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="불경 + 승복", inline=False)
        return embed

    if msg=="화살통":
        embed=discord.Embed(title="화살통", description="공격 속도 +18%", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443587978068050/016._Quiver_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="가죽 + 대나무", inline=False)
        return embed

    if msg=="먼지털이개":
        embed=discord.Embed(title="먼지털이개", description="공격력 +9\n(고유) 이동 속도 +0.06", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443597138456596/017._Feather_Duster__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="단봉 + 깃털", inline=False)
        return embed

    if msg=="군선":
        embed=discord.Embed(title="군선", description="스킬 공격 추가 피해 +8\n```스킬 공격 치유 방해-[고유 장착 효과]\n스킬 공격 시 피격된 대상의 치유 효과가 감소합니다.\n(근거리) 치유 효과가 45% 감소합니다.\n(원거리) 치유 효과가 35% 감소합니다.```", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443603056590919/018._Glided_Quill_Fan_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="부채 + 못", inline=False)
        return embed

    if msg=="비파단도":
        embed=discord.Embed(title="비파단도", description="공격력 +5\n스킬 증폭 +8%\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443607854886922/019._Shaman_s_Bronze_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="녹슨 검 + 마패", inline=False)
        return embed

    if msg=="캐리비안장식총":
        embed=discord.Embed(title="캐리비안 장식총", description="공격력 +10\n생명력 흡수 +6%", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443612321828915/020._Decorative_Flintlock__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="발터PPK + 리본", inline=False)
        return embed

    if msg=="사격교본":
        embed=discord.Embed(title="사격 교본", description="공격력 +8\n(고유) 기본 공격 사거리 +0.35", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443617338216499/021._Marksman_Handbook__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="석궁 + 페도로프 자동소총", inline=False)
        return embed

    if msg=="백우선":
        embed=discord.Embed(title="백우선", description="스킬 공격 추가 피해 +15\n(고유) 이동 속도 +0.06\n```스킬 공격 치유 방해-[고유 장착 효과]\n스킬 공격 시 피격된 대상의 치유 효과가 감소합니다.\n(근거리) 치유 효과가 45% 감소합니다.\n(원거리) 치유 효과가 35% 감소합니다.```", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443621998084106/022._White_Crane_Fan_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="군선 + 깃털", inline=False)
        return embed

    if msg=="우치와":
        embed=discord.Embed(title="우치와", description="스태미너 재생 +70%\n생명력 흡수 +14%\n스킬 공격 추가 피해 +19\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443630793551952/023._Uchiwa_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="인형 + 부채", inline=False)
        return embed

    if msg=="탄창":
        embed=discord.Embed(title="탄창", description="최대 체력 +110\n기본 공격 피해 감소 +4\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443632366387260/024._Magazine_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="상자 + 철판", inline=False)
        return embed

    if msg=="궁기병의화살통":
        embed=discord.Embed(title="궁기병의 화살통", description="공격력 +10\n공격 속도 +30%\n(고유) 이동 속도 +0.08\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443637093388329/025._Laced_Quiver__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="화살통 + 먼지털이개", inline=False)
        return embed

    if msg=="월왕구천":
        embed=discord.Embed(title="월왕구천", description="공격력 +15\n스킬 증폭 +15%", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443642294321182/026._Revenge_of_Goujian_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="비파단도 + 정교한 도면", inline=False)
        return embed

    if msg=="해적의증표":
        embed=discord.Embed(title="해적의 증표", description="공격력 +15\n치명타 확률 +12%\n생명력 흡수 +8%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443648417996800/027._Buccaneer_Doubloon_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="캐리비안 장식총 + 식칼", inline=False)
        return embed

    if msg=="호크아이":
        embed=discord.Embed(title="호크 아이", description="공격력 +13\n시야 +2\n(고유) 기본 공격 사거리 +0.75\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443653665075230/028._Hawkeye__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="사격 교본 + 저격 스코프", inline=False)
        return embed

    if msg=="해적깃발":
        embed=discord.Embed(title="해적 깃발", description="공격력 +12\n생명력 흡수 +10%\n ```가벼운 발걸음-[고유 장착 효과]\n 0.2m 이동할 때마다 [가벼운 발걸음]을 최대 100회까지 중첩해서 획득합니다. 중첩에 따라 이동 속도가 최대 0.06까지 증가합니다. 기본 공격 피해를 입힐 경우 중첩을 모두 소모하여 최대 100의 고유 피해를 입힙니다.\n(근거리) 최대 중첩 상태에서 기본 공격에 피격된 대상의 이동속도를 2초 동안 25% 감소 시킵니다.```", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443658664706069/029._Jolly_Roger__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="먼지털이개 + 캐리비안 장식총", inline=False)
        return embed

    if msg=="오르골":
        embed=discord.Embed(title="오르골", description="최대 체력 +175\n공격 속도 +20%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443664381538304/030._Music_Box_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="상자 + 모터", inline=False)
        return embed

    if msg=="능동위장":
        embed=discord.Embed(title="능동 위장", description="최대 체력 +220\n기본 공격 피해 감소 +12", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443669947371580/031._Active_Camouflage__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="탄창 + 군복", inline=False)
        return embed

    if msg=="마도서":
        embed=discord.Embed(title="마도서", description="```저주-[고유 장착 효과]\n스킬 공격을 가하면 적을 4초간 저주 상태로 만듭니다. 저주 상태인 적은 이동 속도가 6%만큼 느려지고, 저주 상태에서 해제 될 때 75 + 스킬 증폭 * 1.25 에 해당하는 고정 피해를 입힙니다. 한번 저주 상태가 되면 8초간 (기본 공격 피격 시 1초 감소) 다시 저주 상태가 되지 않습니다.\n(쿨다운 : 2초)```", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443675311869993/032._Grimoire_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="하드 커버 + 운명의 꽃", inline=False)
        return embed

    if msg=="아이테르깃털":
        embed=discord.Embed(title="아이테르 깃털", description="치명타 확률 +20%\n쿨다운 감소 +10%\n(고유) 이동 속도 +0.08\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443680525389844/033._Aether_Fringe__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="깃털 + 운명의 꽃", inline=False)
        return embed

    if msg=="슈뢰딩거의상자":
        embed=discord.Embed(title="슈뢰딩거의 상자", description="최대 체력 +200\n스킬 공격 추가 피해 +4\n```스킬 공격 치유 방해-[고유 장착 효과]\n스킬 공격 시 피격된 대상의 치유 효과가 감소합니다.\n(근거리) 치유 효과가 45% 감소합니다.\n(원거리) 치유 효과가 35% 감소합니다.```", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443686061887520/034._Schrodinger_s_Box__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="깃털 + 운명의 꽃", inline=False)
        return embed

    if msg=="진리는나의빛":
        embed=discord.Embed(title="진리는 나의 빛", description="체력 재생 +100%\n쿨다운 감소 +10%\n기본 공격 추가 피해 +12\n 스킬 증폭 +12%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443690646261860/035._Veritas_Lux_Mea__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="진신사리 + 성자의 유산", inline=False)
        return embed

    if msg=="달빛펜던트":
        embed=discord.Embed(title="달빛 펜던트", description="공격력 +24\n시야 +1\n모든 피해 흡혈 +15%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443696455368775/036._Moonlight_Pendant__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="리본 + 문스톤", inline=False)
        return embed

    if msg=="만년빙":
        embed=discord.Embed(title="만년빙", description="체력 재생 +1.5\n스태미너 재생 +1.5\n스킬 공격 추가 피해 +18\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443700771307520/037._Glacial_Ice_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="생명의 나무 + 얼음", inline=False)
        return embed

    if msg=="삼매진화":
        embed=discord.Embed(title="삼매진화", description="공격력 +10\n방어력 +10\n기본 공격 추가 피해 +15\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443706404245544/038._True_Samadhi_Fire_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="생명의 나무 + 라이터", inline=False)
        return embed

    if msg=="요명월":
        embed=discord.Embed(title="요명월", description="방어력 +20\n스태미너 재생 +100%\n시야 +2\n```굴절-[고유 장착 효과]\n굴절의 망토를 두릅니다. 굴절의 망토는 적이 나에게 가하는 다음 스킬 및 트랩의 피해와 효과를 한번 보호해 준 뒤 사라지고, 20초 후 재생성 됩니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443711743598612/039._Lunar_Embrace_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="정화수 + 문스톤", inline=False)
        return embed

    if msg=="미스릴퀴버" or msg=="미퀴":
        embed=discord.Embed(title="미스릴 퀴버", description="방어력 +12\n공격 속도 +18%\n이동 속도 +0.1\n(고유) 기본 공격 사거리 +0.75\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443716684484658/040._Mithril_Quiver__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="화살통 + 미스릴", inline=False)
        return embed

    if msg=="에메랄드타블렛" or msg=="에타":
        embed=discord.Embed(title="에메랄드 타블렛", description="공격력 +24\n치명타 확률 +15%\n치명타 피해량 +12%\n쿨다운 감소 +15%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443721692491816/041._Emerald_Tablet__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="포스 코어 + 운명의 꽃", inline=False)
        return embed

    if msg=="파초선":
        embed=discord.Embed(title="파초선", description="쿨다운 감소 +12%\n```가벼운 발걸음-[고유 장착 효과]\n 0.2m 이동할기본 때마다 [가벼운 발걸음]을 최대 100회까지 중첩해서 획득합니다. 중첩에 따라 이동 속도가 최대 0.15까지 증가합니다.  공격 피해를 입힐 경우 중첩을 모두 소모하여 최대 200의 고유 피해를 입힙니다.\n(근거리) 최대 중첩 상태에서 피격된 대상의 이동속도를 2초 동안 30% 감소 시킵니다.``` ```스킬 공격 치유 방해-[고유 장착 효과]\n스킬 공격 시 피격된 대상의 치유 효과가 감소합니다.\n(근거리) 치유 효과가 45% 감소합니다.\n(원거리) 치유 효과가 35% 감소합니다.```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443726184611940/042._Sanguine_Gunbai_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="VF 혈액 샘플 + 군선", inline=False)
        return embed

    if msg=="쿤달라":
        embed=discord.Embed(title="쿤달라", description="최대 체력 +120\n이동 속도 +0.1\n시야 +1.5\n스킬 증폭 +17%\n```의념-[고유 장착 효과]\n스킬을 사용하면 의념을 충전합니다. 충전된 상태에서 다음 3초 안에 이루어지는 기본 공격이 추가 고유 피해를 입힙니다.\n(쿨다운 : 2.5초)\n(근거리)스킬 증폭 * 2.5에 해당하는 피해를 입힙니다.\n(원거리)스킬 증폭 * 2에 해당하는 피해를 입힙니다.```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322263075450882/892443729984622643/043._Kundala_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="미스릴 + 문스톤", inline=False)
        return embed

