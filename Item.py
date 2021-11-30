import discord
import asyncio

client = discord.Client()

def Weapon(msg):
#####망치#####
    if msg=="망치":
        embed=discord.Embed(title="망치", description=" 공격력 +16", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317360093442128/001._Hammer_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로 ", value="연못(8), 모래사장(9), 골목길(11), 멧돼지", inline=False)
        return embed

    if msg=="워해머":
        embed=discord.Embed(title="워해머", description=" 공격력 +40",color=0x1eb300)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317382633644034/002._Warhammer_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로 ", value="망치+단봉", inline=False)
        return embed

    if msg=="사슴망치":
        embed=discord.Embed(title="사슴망치", description=" 공격력 +56", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317414606823464/004._Black_Stag_Hammer__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로 ", value="워해머+가죽", inline=False)
        return embed
        
    if msg=="운명의망치":
        embed=discord.Embed(title="운명의망치", description=" 공격력 +40\n 쿨다운 감소 +8%\n 치명타 확률 +8%", color=0x1e82cd)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/891317310952988712/891317445732741190/005._Forged_Destiny__.png")
        embed.add_field(name="등급", value="희귀", inline=True)
        embed.add_field(name="휙득 경로 ", value="망치 + 운명의 꽃", inline=True)
        return embed

    if msg=="낭아봉":
        embed=discord.Embed(title="낭아봉", description=" 공격력 +55\n 스킬 공격 추가 피해 +22\n 레벨 당 스킬 공격 추가 피해 +1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317450635874375/006._Fang_Mace_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="모닝스타 + 달궈진 돌멩이", inline=False)
        return embed
    
    if msg=="다그다의망치":
        embed=discord.Embed(title="다그다의 망치", description=" 공격력 +98\n 체력 재생(%) +125%\n 기본 공격 추가 피해 +28\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317452749803540/007._Hammer_of_Dagda__.png")
        embed.add_field(name="등급", value="영웅", inline=True)
        embed.add_field(name="휙득 경로 ", value="사슴망치 + 성자의 유산", inline=True)
        return embed

    if msg=="토르의망치":
        embed=discord.Embed(title="토르의망치", description=" 공격력 +105\n 공격 속도(%) +30%\n 레벨 당 공격 속도 +1%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317472165261342/008._Hammer_of_Thor__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="사슴망치 + 이온전지", inline=False)
        return embed 

    if msg=="개밥바라기":
        embed=discord.Embed(title="개밥바라기", description=" 공격력 +105\n 스킬 증폭(%) +20%", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317472769241169/009._Evening_Star_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="모닝스타 + 문스톤", inline=False)
        return embed

    if msg=="천근추":
        embed=discord.Embed(title="천근추", description=" 공격력 +88\n 스킬 증폭 +8%\n 쿨다운 감소 +12%\n ```차지드 스트라이크 - [고유 장착 효과]\n매 4초마다 다음 공격이 100%의 치명타 확률 보너스를 획득합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317475961085972/010._Weight_of_the_World_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="운명의망치 + 진신사리", inline=False)        
        return embed
        
    if msg=="피스브링어":
        embed=discord.Embed(title="피스브링어", description=" 공격력 +140\n 모든 피해 흡혈 10%\n 방어력 관통 +12%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317478783873064/011._Peacebringer__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로 ", value="사슴망치 + VF 혈액 샘플", inline=False)
        return embed

#####단검#####
    if msg=="식칼":
        embed=discord.Embed(title="식칼", description=" 공격력 +4", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342811553751060/003._Kitchen_Knife_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로 ", value="항구(4), 호텔(5), 절(5), 멧돼지", inline=False)
        return embed

    if msg =="가위":
        embed=discord.Embed(title="가위", description=" 공격력 +5", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342805245505556/001._Scissors_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로 ", value="골목길(11), 병원(8), 학교(9), 박쥐", inline=False)    
        return embed

    if msg=="만년필":
        embed=discord.Embed(title="만년필", description=" 공격력 +5", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342808315740230/002._Fountain_Pen_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로 ", value="고급 주택가(8), 번화가(8), 학교(9), 박쥐", inline=False)
        return embed

    if msg=="군용나이프":
        embed=discord.Embed(title="군용나이프", description=" 공격력 +14\n 이동 속도 +0.06", color=0x1eb300)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342816045830184/004._Army_Knife__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로 ", value="식칼+나뭇가지", inline=False)
        return embed

    if msg=="메스":
        embed=discord.Embed(title="메스", description=" 공격력 +18", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342820277899385/005._Scalpel_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로 ", value="만년필+면도칼", inline=False)
        return embed

    if msg=="자마다르":
        embed=discord.Embed(title="자마다르", description=" 공격력 +15", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342825336229898/006._Jamadhar_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로 ", value="식칼+너클", inline=False)
        return embed

    if msg=="장미칼":
        embed=discord.Embed(title="장미칼", description=" 공격력 +20\n 이동 속도 +0.08\n 쿨다운 감소 +8%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342830545543278/007._Rose_Knife_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로 ", value="군용 나이프+꽃", inline=False)
        return embed

    if msg=="스위스아미나이프" or msg=="스위스 아미 나이프":
        embed=discord.Embed(title="스위스 아미 나이프", description=" 공격력 +23\n 최대 체력 +100", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342835192832010/008._Swiss_Army_Knife__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로 ", value="메스+가위", inline=False)
        return embed

    if msg=="카라페이스카타르":
        embed=discord.Embed(title="카라페이스 카타르", description=" 공격력 +20\n 방어력 +12", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342839248732160/009._Carapace_Katar__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로 ", value="자마다르+거북이등딱지", inline=False)
        return embed

    if msg=="카른웬난":
        embed=discord.Embed(title="카른웬난", description=" 공격력 +41\n 체력 재생 +1.2\n 이동 속도 +0.08\n 쿨다운 감소 +8%\n 기본 공격 추가 피해 +26\n 레벨 당 기본 공격 추가 피해 +2\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342843313004564/010._Carnwennan_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="장미칼+성자의 유산", inline=False)
        return embed

    if msg=="파산검":
        embed=discord.Embed(title="파산검", description=" 공격력 +30\n 이동 속도 +0.1\n 쿨다운 감소 +12%\n 레벨 당 스킬 공격 추가 피해 +2\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342847847043142/011._Mount_Slicer_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="장미칼+재", inline=False)
        return embed

    if msg=="초진동나이프"or msg=="초진동 나이프":
        embed=discord.Embed(title="초진동나이프", description=" 공격력 +55\n 공격 속도(%) +40%\n 이동 속도 +0.1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342852058144798/012._Vibroblade_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="군용 나이프+모터", inline=False)
        return embed

    if msg=="다마스커스가시"or msg=="다마스커스가시":
        embed=discord.Embed(title="다마스커스 가시", description=" 공격력 +66\n 최대 체력 +250\n ```스킬 공격 치유 방해-[고유 장착 효과]\n 스킬 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342855883333632/013._Damascus_Steel_Thorn__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="스위스 아미 나이프+가시 발판", inline=False)
        return embed

    if msg=="마하자라":
        embed=discord.Embed(title="마하자라", description=" 공격력 +42\n 방어력 +18\n ```신속 - 루드라의 단검 - [고유 장착 효과]\n 4초 이내에 4회의 개별 피해를 가하면, 2.5초간 이동 속도가 10%, 공격력이 33% 증가합니다. (쿨타임 6초)```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342860014735390/014._Maharaja_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="카라페이스 카타르+아이테르 깃털", inline=False)
        return embed

    if msg=="프라가라흐":
        embed=discord.Embed(title="프라가라흐", description=" 공격력 +82\n 이동 속도 +0.18\n ```차지드 스트라이크 - [고유 장착 효과]\n 매 4초마다 다음 공격이 100%의 치명타 확률 보너스를 획득합니다.```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342864741707846/015._Fragarach_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로 ", value="군용 나이프+포스 코어", inline=False)
        return embed
        

#####쌍칼#####
    if msg=="쌍칼":
        embed=discord.Embed(title="쌍칼", description=" 공격력 +12", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321971483234344/001._Twin_Swords_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로", value="기본 제공, 식칼 + 녹슨 검", inline=False)
        return embed

    if msg=="조잡한쌍칼":
        embed=discord.Embed(title="조잡한 쌍칼", description=" 공격력 +12", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/894235985389428806/002._Wrought_Swords__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="가위 + 곡괭이", inline=False)
        return embed

        
    if msg=="피렌체식쌍검":
        embed=discord.Embed(title="피렌체식 쌍검", description=" 공격력 +28\n 생명력 흡수 +10%", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321975295856710/002._Florentine__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="쌍칼 + 정교한 도면", inline=False)
        return embed

    if msg =="쌍둥이검":
        embed=discord.Embed(title="쌍둥이 검", description=" 공격력 +35", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321976726118450/003._Pocket_Aces_-_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="쌍칼 + 검집", inline=False)
        return embed

   
    if msg=="자웅일대검":
        embed=discord.Embed(title="자웅일대검", description=" 공격력 +60\n 공격 속도(%) +35%\n 기본 공격 추가 피해 +8\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321984187764797/005._Starsteel_Twin_Swords_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="쌍칼 + 문스톤", inline=False)
        return embed
        
    if msg =="디오스쿠로이":
        embed=discord.Embed(title="디오스쿠로이", description=" 공격력 +55\n 공격 속도(%) +35%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321988918968320/006._Dioscuri_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="조잡한 쌍검 + 이온 전지", inline=False)
        return embed

    if msg=="로이거차르":
        embed=discord.Embed(title="로이거 차르", description=" 공격력 +40\n 레벨 당 스킬 공격 추가 피해 +2.5\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321992286961664/007._Lioigor___Zahr__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="쌍둥이 검 + 재", inline=False)
        return embed

    if msg=="아수라":
        embed=discord.Embed(title="아수라", description=" 공격력 +48\n 모든피해 흡혈 +8%\n 레벨 당 스킬 증폭 +1%\n 쿨다운 감소 +12%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/894235982805733416/007._Asura_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="피렌체식 쌍검 + 진신사리", inline=False)
        return embed
        

    if msg=="간장과막야":
        embed=discord.Embed(title="간장과막야", description=" 공격력+75\n 공격 속도 +18%\n (고유)기본 공격 사거리 +1\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891322007319347240/008._Spring_and_Autumn__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로 ", value="쌍칼+포스 코어", inline=False)
        return embed

#####레이피어#####

    if msg=="바늘":
        embed=discord.Embed(title="바늘", description=" 공격력 +3\n치명타 피해량 +15%\n", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251084057571338/001._Needle_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="골목길(6), 호텔(7), 병원(6), 박쥐", inline=False)
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
        embed=discord.Embed(title="에스톡", description=" 공격력 +23\n스킬 공격 추가피해 +12\n", color=0x1e82cd)
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

    if msg=="듀랜달 Mk2":
        embed=discord.Embed(title="듀랜달 Mk2", description=" 공격력 +55\n시야 +1.5\n치명타 확률 +12%\n치명타 피해량 +25%\n쿨다운 감소 +6%\n생명력 흡수 +11%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251113694498856/006._Durendal_Mk2__Mk2.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="매화검 + 레이저 포인터", inline=False)
        return embed

    if msg=="볼틱레토":
        embed=discord.Embed(title="볼틱레토", description=" 공격력 +50\n공격 속도(%) +50%\n치명타 확률 +10%\n치명타 피해량 +15%\n쿨다운 감소 +6%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251119151300678/007._Volticletto_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="매화검 + 전자 부품", inline=False)
        return embed

    if msg=="레드팬서":
        embed=discord.Embed(title="레드 팬서", description=" 공격력 +46\n최대 체력 +225\n스테미너 재생 +80%\n스킬 공격 추가피해 +20\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251133344813087/010._Red_Panther__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="에스톡 + 진홍 팔찌", inline=False)
        return embed

    if msg=="유성검":
        embed=discord.Embed(title="유성검", description="공격력 +64\n치명타 피해량 +12%\n쿨다운 감소 +12%\n```차지드 스트라이크 - [고유 장착 효과]\n매 3초마다 다음 공격이 100%의 치명타 확률 보너스를 획득합니다.```", color=0x9c4998)
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

    if msg=="컴팩트 카메라":
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

    if msg=="카메라 라이플":
        embed=discord.Embed(title="카메라 라이플", description=" 공격력 +30\n 시야 +2\n ```기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +0.5```", color=0x1e82cd)
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
        embed=discord.Embed(title="카메라 캐논", description=" 공격력 +51\n 최대 체력 +280\n 시야 +4\n ```기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +1```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865299903737966/008._Cannon_Camera__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="카메라 라이플 + 탄창", inline=False)
        return embed

    if msg=="컴파운드 사이트":
        embed=discord.Embed(title="컴파운드 사이트", description=" 공격력 +55\n 시야 +5\n 쿨다운 감소 +15%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865306039984128/008._Laser_Designator__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="레인지파인더 + 꽃", inline=False)
        return embed
    
    if msg=="V.I.C.G":
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
        embed.add_field(name="휙득 경로 ", value="모래사장(8), 골목길(9), 묘지(8), 멧돼지", inline=False)
        return embed

    if msg=="눈차크":
        embed=discord.Embed(title="눈차크", description=" 공격력 +29", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865033410244608/002._Nunchaku_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="쇠사슬 + 고철", inline=False)
        return embed

    if msg=="샤퍼":
        embed=discord.Embed(title="샤퍼", description=" 공격력 +29\n ```스킬 공격 치유 방해 - [고유 장착 효과]\n 스킬 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.```", color=0x1e82cd)
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
        embed=discord.Embed(title="대소반룡곤", description=" 공격력 +50\n 스킬 공격 추가 피해 +22\n ```스킬 공격 치유 방해 - [고유 장착 효과]\n 스킬 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.```", color=0x9c4998)
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
        embed=discord.Embed(title="케르베로스", description=" 공격력 +45\n 레벨 당  공격력 +2\n 이동 속도 +0.1\n ```기본 공격 치유 방해 - [고유 장착 효과]\n 기본 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.``` ```기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +0.5```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865056374050836/007._Cerberus_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="샤퍼 + 체인 레깅스", inline=False)
        return embed

    if msg=="히드라":
        embed=discord.Embed(title="히드라", description=" 공격력 +110\n 모든 피해 흡혈(%) +25%\n", color=0xf9d537)
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

    if msg=="베레타M92F":
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

    if msg=="더블리볼버SP":
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
        embed=discord.Embed(title="마탄의 사수", description="장탄 수: 7발\n 공격력 +48\n 공격 속도(%) +30%\n 이동 속도 +0.1\n 스킬 증폭 +20%\n ```마탄 - [고유 장착 효과]\n 마지막 탄환으로 가하는 기본 공격이  공격력 +스킬 증폭 *2 + 스킬 공격 추가 피해 * 1.5 에 해당하는 스킬 피해를 입히고, 입힌 피해의 100%만큼의 체력을 회복합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864801951760384/008._Devil_s_Marksman__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="더블 리볼버 SP + 운석", inline=False)
        return embed

    if msg=="엘레강스":
        embed=discord.Embed(title="엘레강스", description="장탄 수: 6발\n 공격력 +63\n 레벨 당 공격력 +2\n 이동 속도 +0.2\n 시야 +2.5\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864808226443334/009._Elegance_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="FN57 + 먼지털이개", inline=False)
        return embed

    if msg=="일렉트론블라스터":
        embed=discord.Embed(title="일렉트론 블라스터", description="장탄 수: 10발\n 공격력 +66\n 공격 속도(%) +35%\n 이동 속도 +0.1\n 레벨 당 기본 공격 추가 피해 +2\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864813993619466/010._Electron_Blaster__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="베레타 M92F + 이온 전지", inline=False)
        return embed

    if msg=="매그넘보아":
        embed=discord.Embed(title="매그넘-보아", description="장탄 수: 6발\n 공격력 +84\n 공격 속도(%) +25%\n 이동 속도 +0.1\n 시야 +1.5\n 생명력 흡수 +22%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864819676897290/011._Magnum-Boa_-.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="매그넘-아나콘다 + 강철", inline=False)
        return embed

    if msg=="글록48":
        embed=discord.Embed(title="글록 48", description="장탄 수: 8발\n 공격력 +75\n 공격 속도(%) +20%\n 이동 속도 +0.1\n 시야 +3.5\n ```기본 공격 사거리 - [고유 장착 효과]\n  기본 공격 사거리 +0.75\n```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864824970088568/012._Glock_48__48.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="FN57 + EMP 드론", inline=False)
        return embed

    if msg=="스탬피드":
        embed=discord.Embed(title="스탬피드", description="장탄 수: 2발\n 공격력 +40\n 이동 속도 +0.1\n 레벨 당 스킬 증폭 +1%\n ```더블 탭 - [고유 장착 효과]\n 마지막 탄환으로 가하는 기본 공격이  공격력 +스킬 증폭 *1 + 캐릭터 레벨 * 10 에 해당하는 스킬 피해를 입힙니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864830254915604/013._Stempede_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="데린저 + 황금", inline=False)
        return embed

    if msg=="악켈테":
        embed=discord.Embed(title="악켈테", description="장탄 수: 10발\n 공격력 +95\n 공격 속도 +25%\n 이동 속도 +0.1\n 시야 +2\n 방어 관통율 +12%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864835875295252/014._Kelte_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="포스코어 + 베레타 M92F", inline=False)
        return embed

######방망이#####

    if msg=="단봉":
        embed=discord.Embed(title="단봉", description=" 공격력 +15", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864611832352819/002._Short_Rod_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="항구(8), 연못(7), 절(7), 들개", inline=False)
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
        embed=discord.Embed(title="도깨비 방망이", description=" 공격력 +27\n ```기본 공격 치유 방해 - [고유 장착 효과]\n 기본 공격에 피격된 대상의 치유 효과가 45% 감소합니다.```", color=0x1e82cd)
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
        embed=discord.Embed(title="몽둥이", description=" 공격력 +40\n 이동 속도 -0.1\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864642559832115/007._Reinforced_Club_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="단봉 + 강철", inline=False)
        return embed

    if msg=="마법봉":
        embed=discord.Embed(title="마법봉", description=" 공격력 +59\n 생명력 흡수 +30%\n 시야 +1\n 스킬 증폭 +30%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864648436039710/008._Magic_Stick_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="장봉 + 달빛 펜던트", inline=False)
        return embed

    if msg=="금강저":
        embed=discord.Embed(title="금강저", description=" 공격력 +96\n ```차지드 스트라이크 - [고유 장착 효과]\n 매 3초마다 다음 공격이 100%의 치명타 확률 보너스를 얻습니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864653599244328/009._Vajra_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="몽둥이 + 유리판", inline=False)
        return embed

    if msg=="구원의여신상":
        embed=discord.Embed(title="구원의 여신상", description=" 공격력 +64\n 레벨 당  공격력 +2\n 체력 재생 +0.6\n 스테미너 재생(%) +80%\n 공격 속도(%) +15%\n 생명력 흡수 +12%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864659102162994/010._Statue_of_Soteria__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="횃불 + 인형", inline=False)
        return embed

    if msg=="타구봉":
        embed=discord.Embed(title="타구봉", description=" 공격력 +85\n 공격 속도(%) +50%\n ```기본 공격 치유 방해 - [고유 장착 효과]\n 기본 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.```", color=0x9c4998)
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
        embed=discord.Embed(title="여의봉", description=" 공격력 +135\n 공격 속도 +10%\n ```기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +1```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864681067724900/013._Monkey_King_Bar_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="포스 코어 + 장봉", inline=False)
        return embed


######도끼#####

    if msg=="손도끼":
        embed=discord.Embed(title="손도끼", description=" 공격력 +25", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366076565303306/002._Hatchet_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로", value="연못(5), 모래사장(6), 공장(5), 들개", inline=False)
        return embed

    if msg=="곡괭이":
        embed=discord.Embed(title="곡괭이", description=" 공격력 +15", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366069443375195/001._Pickaxe_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로", value="연못,모래사장,묘지,숲의 상자, 박쥐", inline=False)
        return embed

    if msg== "전투도끼":
        embed=discord.Embed(title="전투도끼", description=" 공격력 +47", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366084677091368/04._Battle_Axe__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="손도끼+대나무", inline=False)
        return embed

    if msg=="사슬낫":
        embed=discord.Embed(title="사슬낫", description=" 공격력 +50\n ```기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +0.2```", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366080038191134/003._Chain_Scythe__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="곡괭이+쇠사슬", inline=False)
        return embed

    if msg=="사신의낫":
        embed=discord.Embed(title="사신의낫", description=" 공격력 +80\n ```기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +0.5```", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366100279918652/006._Reaper_s_Scythe.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="사슬 낫+단봉", inline=False)
        return embed

    if msg=="경령화도끼"or msg=="경령화도끼":
        embed=discord.Embed(title="경령화 도끼", description=" 공격력 +61\n 이동속도 +0.05\n", color=0x1e82cd)
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

    if msg=="빔 엑스"or msg=="빔엑스":
        embed=discord.Embed(title="빔 엑스", description=" 공격력 +102\n 레벨당  공격력 +2\n 시야 +3\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366112263024650/008._Beam_Axe__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="대부 + 레이저 포인터", inline=False)
        return embed

    if msg=="산타무에르페":
        embed=discord.Embed(title="산타 무에르페", description=" 공격력 +105\n 최대 체력 +320\n ```기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +0.5```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366117640122388/009._Santa_Muerte__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="사신의 낫 + 루비", inline=False)
        return embed

    if msg=="스퀴테":
        embed=discord.Embed(title="스퀴테", description=" 공격력 +112\n 레벨 당 스킬 증폭 +2%\n ```기본 공격 사거리 - [고유 장착 효과]\n 동일한 이름의 고유 효과는 하나만 적용됩니다.\n 기본 공격 사거리 +1```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366122300006421/010._Scythe_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="사신의 낫 + 황금", inline=False)
        return embed

    if msg=="파라슈":
        embed=discord.Embed(title="파라슈", description=" 공격력 +115\n 이동 속도 +0.07\n 쿨다운 감소 +14%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366127446405150/011._Parashu_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="경량화 도끼 + 진신사리", inline=False)
        return embed

    if msg=="저거너트":
        embed=discord.Embed(title="저거너트", description=" 공격력 +92\n 레벨 당 공격 속도 +3%\n 기본 공격 사거리 -0.2\n 이동 속도 +0.1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366132706054154/012._The_Juggernaut_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="경랑화 도끼 + 모터", inline=False)
        return embed
    

    if msg=="하르페":
        embed=discord.Embed(title="하르페 ", description=" 공격력 +110\n 생명력 흡수 +20%\n ```가벼운 발걸음 - [고유 장착 효과]\n 0.2m 이동할 때마다 [가벼운 발걸음]을 최대 100회까지 중첩해서 획득합니다.\n중첩에 따라 이동속도가 최대 0.12까지 증가합니다.\n기본 공격 피해를 입힐 경우 중첩을 모두 소모하여 최대 120의 고유 피해를 입힙니다.\n최대 중첩 상태에서 기본 공격에 피격된 대상의 이동속도를 2초간 15% 감소 시킵니다.```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366137101684766/013._Harpe_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로 ", value="대부+해적 깃발", inline=False)
        return embed

######톤파######
    if msg=="대나무":
        embed=discord.Embed(title="대나무", description=" 공격력 +12", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289517330006026/001._Bamboo_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="연못(8), 절(6), 양궁장(5), 묘지(7), 숲(7), 박쥐", inline=False)
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
        embed=discord.Embed(title="플라즈마 톤파", description=" 공격력 +60\n 방어력 +21\n 시야 +4\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289549835829258/007._Plasma_Tonfa__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="류큐톤파 + 레이저 포인터", inline=False)
        return embed

    if msg=="윈드러너":
        embed=discord.Embed(title="윈드러너", description=" 공격력 +70\n 방어력 +8\n 이동 속도 +0.1\n ```신속 - 산들바람-[고유 장착 효과]\n 4초 이내에 3회의 개별 피해를 가하면, 3초간 이동 속도가 10% 증가하고, 공격 속도가 30% 증가하며 225의 보호막을 얻습니다.\n(쿨다운 6초)```", color=0x9c4998)
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
        embed=discord.Embed(title="화승총", description="장탄 수: 1발\n공격력 +30\n체력 재생 +1.5\n시야 +1\n스태미너 재생(%) +150%\n치명타 피해량 +25%\n쿨다운 감소 +12%\n", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472485552332910/001._Long_Rifle_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="항구(3), 숲(3)", inline=False)
        return embed
        
    if msg=="스프링필드":
        embed=discord.Embed(title="스프링필드", description="장탄 수: 1발\n 공격력 +40\n 시야 +1.5\n", color=0x1eb300)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472489578872853/002._Springfield_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="화승총 + 레이저 포인터", inline=False)
        return embed
        
    if msg=="하푼건":
        embed=discord.Embed(title="하푼건", description="장탄 수: 2발\n 공격력 +60\n 시야 +2\n", color=0x1e82cd)
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
        embed=discord.Embed(title="폴라리스", description="장탄 수: 4발\n 공격력 +113\n 공격 속도(%) +18%\n 레벨당 공격속도 +2%\n 시야 +2\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472519224209478/009._Polaris_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="레일건 + 백색 가루", inline=False)
        return embed
        
    if msg=="인터벤션":
        embed=discord.Embed(title="인터벤션", description="장탄 수: 2발\n 공격력 +100\n 시야 +4\n ```기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +1```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472510999179264/007._Intervention_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="하푼건 + 망원 카메라", inline=False)
        return embed
        
    if msg=="tac-50":
        embed=discord.Embed(title="Tac-50", description="장탄 수: 2발\n 공격력 +94\n 레벨 당  공격력 +2\n 시야 +2\n 생명력 흡수 +14%\n", color=0x9c4998)
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
        embed.add_field(name="휙득 경로", value="호텔(5), 고급 주택가(5), 공장(5)", inline=False)
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
            
    if msg=="5식자동소총":
        embed=discord.Embed(title="95식 자동 소총", description="장탄 수: 30발\n 공격력 +84\n 시야 +2\n ```기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +1```", color=0x9c4998)
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
        embed=discord.Embed(title="XCR", description="장탄 수: 30발\n 공격력 +66\n 최대 체력 +200\n 시야 +1.5\n 기본 공격 추가 피해 +10\n", color=0x9c4998)
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
        embed=discord.Embed(title="양궁", description=" 공격력 +11", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473123468238928/001._Bow_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="양궁장(5), 성당(4)", inline=False)
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
        
    if msg=="컴포지트 보우":
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
        embed=discord.Embed(title="트윈보우", description=" 공격력 +40\n레벨 당  공격력 +2\n공격 속도(%) +50%\n시야 +1\n ```기본 공격 치유 방해-[고유 장착 효과]\n기본 공격에 피격된 대상의 치유 효과가 4초 동안 35% 감소합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473172008910879/012._Twinbow__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="강궁 + 컴포지트 보우", inline=False)
        return embed

    if msg=="제베의활":
        embed=discord.Embed(title="제베의 활", description=" 공격력 +84\n공격 속도 +33%\n이동 속도 +0.1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472668952481883/896473177469898752/013._Jebe_s_Altered_Bow__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="벽력궁 + 궁기병의 화살통", inline=False)
        return embed

    if msg=="아르테미스":
        embed=discord.Embed(title="아르테미스", description=" 공격력 +95\n최대 체력 +150\n최대 스태미너 +200\n시야 +2\n스킬 증폭 +25%\n", color=0x9c4998)
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
        embed=discord.Embed(title="석궁", description=" 공격력 +30", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251213300854884/001._Short_Crossbow_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="숲(5), 성당(5)", inline=False)
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
        embed=discord.Embed(title="저격궁", description=" 공격력 +30\n시야 +2.5\n", color=0x1e82cd)
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
        embed=discord.Embed(title="저격 크로스보우", description=" 공격력 +85\n시야 +3\n ```기본 공격 사거리-[고유 장착 효과]\n기본 공격 사거리 +1.25```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251268367863860/010._Sniper_Crossbow__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="저격궁 + 저격 스코프", inline=False)
        return embed

    if msg =="영광금귀신기노":
        embed=discord.Embed(title="영광금귀신기노", description=" 공격력 +66\n기본 공격 추가 피해 +22\n레벨 당 기본 공격 추가 피해 +2\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251184217534524/894251275854704680/011._The_Golden_Ghost_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="노 + RDX", inline=False)
        return embed

    if msg =="샤릉가":
        embed=discord.Embed(title="샤릉가", description=" 공격력 +128\n시야 +1.5\n ```가벼운 발놀림-[고유 장착 효과]\n0.24m 이동할 때마다 [가벼운 발놀림]을 최대 100회까지 중첩해서 획득합니다.\n중첩에 따라 이동속도가 최대 0.12까지 증가합니다.\n기본 공격 피해를 입힐 경우 중첩을 모두 소모하여 최대 120의 고유 피해를 입힙니다.```", color=0xf9d537)
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

    if msg=="감정의 컵":
        embed=discord.Embed(title="감정의 컵", description=" 공격력 +40\n체력 재생 +80%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522519302311946/005._Sensibility__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="거울구슬 + 성배", inline=False)
        return embed

    if msg=="이성의 칼":
        embed=discord.Embed(title="이성의 칼", description=" 공격력 +30\n쿨다운 감소 +8%\n이동 속도 +0.04\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522524679405588/006._Frigid_Pearl_Blade__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="얼음구슬 + 식칼", inline=False)
        return embed

    if msg=="소유의 펜타클":
        embed=discord.Embed(title="소유의 펜타클", description="공격력 +30\n쿨다운 감소 +8%\n시야 +1.5\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522529645494292/007._Possession_Pentacle__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="얼음구슬 + 마패", inline=False)
        return embed

    if msg=="은둔자":
        embed=discord.Embed(title="은둔자", description=" 공격력 +60\n ```저주-[고유 장착 효과]\n스킬 공격을 가하면 적을 4초간 저주 상태로 만듭니다.\n저주 상태인 적은 이동 속도가 8% 느려지고, 저주 상태에서 해제될 때 50 + 스킬 증폭의 2.25배에 해당하는 고정 피해를 입습니다.\n한번 저주 상태가 되면 8초 동안 다시 저주 상태에 걸리지 않으며, 저주의 사용자가 대상에게 기본 공격을 적중시킬 때 마다 저주 대기 시간이 1초 씩 감소합니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522534036926524/008._The_Hermit_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="의지의 지팡이 + 성자의 유산", inline=False)
        return embed

    if msg=="운명의 수레바퀴":
        embed=discord.Embed(title="운명의 수레바퀴", description=" 공격력 +33\n최대 체력 +225\n이동 속도 +0.1\n ```리플렉션-[고유 장착 효과]\n기본 공격 피해의 3%를 고정 피해로 반사 피격 시 치유 감소 40(근거리)/30(원거리)% 4초안에 450의 피해를 받으면, 일정 범위 내의 적에게 215의 고유 피해를 줍니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522537904054302/009._The_Hierophant__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="이성의 칼 + 운명의 꽃", inline=False)
        return embed

    if msg=="절제":
        embed=discord.Embed(title="절제", description=" 공격력 +66\n 방어력 -25\n시야 +2.5\n체력 재생 +100%\n스태미너 재생 +125%\n주는 회복 증가 +25%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522542098350121/010._Temperance_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="감정의 컵 + 정화수", inline=False)
        return embed

    if msg=="더 스타":
        embed=discord.Embed(title="더 스타", description=" 공격력 +64\n쿨다운 감소 +10%\n시야 +2.5\n스킬 증폭 +12%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522545965514752/011._The_Star__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="소유의 펜타클 + 바브드 블로섬", inline=False)
        return embed

    if msg=="더 문":
        embed=discord.Embed(title="더 문", description=" 공격력 +90\n ```굴절 - [고유 장착 효과]\n 굴절의 망토를 두릅니다.\n굴절의 망토는 적이 나에게 가하는 다음 스킬 및 트랩의 피해와 효과를 한번 보호해 준 뒤 사라지고, 35초 후 재생성 됩니다.```", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/910522113385975848/910522550210166834/012._The_Moon__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="거울구슬 + 문스톤", inline=False)
        return embed

#####기타#####
    if msg=="보급형 기타":
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
        embed=discord.Embed(title="원더풀 투나잇", description=" 공격력 +85\n기본 공격 추가 피해 +2\n ```열정 - [고유 효과]\n기본 공격이 적 실험체에게 명중하면, 적 실험체에게 현재 체력의 5%에 해당하는 고유 피해를 입히며 열정 버프를 1스택 획득합니다.\n열정: 버프\n 공격 속도 8% 증가\n 지속 시간 : 4초\n 최대 스택 : 5스택\n최대 스택이 쌓인 경우 15의  공격력과 0.1의 이동 속도를 추가로 얻습니다.```", color=0x9C4998)
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
        embed=discord.Embed(title="틴 스피릿", description=" 공격력 +18\n공격 속도 +40%\n기본 공격 추가 피해 +5\n레벨당 기본 공격 추가 피해 +1\n ```기본 공격 사거리 - [고유 장착 효과]\n기본 공격 사거리 +0.75```", color=0x9C4998)
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
        embed=discord.Embed(title="도끼창", description="공격력 +70", color=0x1e82cd)
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

    if msg=="예각창":
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
        embed=discord.Embed(title="코스믹 바이던트", description="공격력 +130\n레벨 당 공격속도 +1%\n", color=0x9C4998)
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
        embed=discord.Embed(title="화첨창", description="공격력 +100\n```발화-[고유 장착 효과]\n기본 공격의 대상에게 최대 4회 중첩되는 [타오르는 고통] 효과를 4초 동안 부여 합니다.\n[타오르는 고통]은 매 초마다 대상 최대 체력의 1.15%를 피해로 줍니다.```", color=0xf9d537)
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
        embed.add_field(name="획득경로", value="항구(7개), 양궁장(7개), 성당(6개)", inline=False)
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
        embed=discord.Embed(title="뚜언 띠엔", description="공격력 +77\n방어력 +28\n쿨다운 감소 +10%\n", color=0x9C4998)
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

    if msg=="아론다이트":
        embed=discord.Embed(title="아론다이트", description="공격력 +65\n최대 체력 +180\n체력 재생(%) +100%\n공격 속도(%) +20%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914735116436246538/011._Excalibur_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="보검 + 성배", inline=False)
        return embed

    if msg=="모노호시자오":
        embed=discord.Embed(title="모노호시자오", description="공격력 +50\n레벨 당 추가 공격력 +2\n 생명력 흡수 +22%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914732131471724564/914735122803200041/012._Monohoshizao_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="무라마사 + 정교한 도면", inline=False)
        return embed

    if msg=="호푸어드":
        embed=discord.Embed(title="호푸어드", description="공격력 +55\n최대 체력 +150\n치명타 확률 +20%\n치명타 피해량 +10%\n", color=0x9C4998)
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
        embed=discord.Embed(title="빛의 검", description="공격력 +75\n공격속도 +38%\n시야 +2\n```섬광-[고유 장착 효과]\n다음에 가하는 기본 공격이 60의 추가 고유 피해를 주고 2초 동안 이동속도를 30%만큼 감소시킵니다.\n(쿨다운 : 3초)```", color=0xf9d537)
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
        embed.add_field(name="획득경로", value="묘지(5), 숲(5)", inline=False)
        return embed

    if msg=="목장갑":
        embed=discord.Embed(title="목장갑", description="공격력 +7", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756156432449536/002._Cotton_Gloves_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="호텔(4), 병원(4)", inline=False)
        return embed

    if msg=="글러브":
        embed=discord.Embed(title="글러브", description="공격력 +18", color=0x1eb300)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756214536151090/003._Leather_Gloves__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="목장갑 + 가죽", inline=False)
        return embed

    if msg=="아이언 너클":
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

    if msg=="윙 너클":
        embed=discord.Embed(title="윙 너클", description="공격력 +20\n이동 속도 +0.1\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756323814567946/006._Wing_Knuckles__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="아이언 너클 + 깃털", inline=False)
        return embed

    if msg=="귀골 장갑":
        embed=discord.Embed(title="귀골 장갑", description="공격력 +35\n방어력 +13\n이동 속도 -0.05\n", color=0x1e82cd)
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

    if msg=="유리 너클":
        embed=discord.Embed(title="유리 너클", description="공격력 +28\n치명타 확률 +10%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756324338835466/009._Glass_Knuckles__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="건틀릿 + 화약", inline=False)
        return embed

    if msg=="회단 장갑":
        embed=discord.Embed(title="회단 장갑", description="공격력 +27\n스킬 공격 추가 피해 +15\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756324506599455/010._Phoenix_Gloves__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="글러브 + 재", inline=False)
        return embed

    if msg=="단영촌천투":
        embed=discord.Embed(title="단영촌천투", description="공격력 +50\n방어력 +18\n스테미너 재생(%) +50%\n생명력 흡수 +20%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756361626202112/011._One_Inch_Punch_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="귀골 장갑 + 인형", inline=False)
        return embed

    if msg=="디바인 피스트":
        embed=discord.Embed(title="디바인 피스트", description="공격력 +55\n이동 속도 -0.05\n기본 공격 추가 피해 +39\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756361793982484/012._Divine_Fist__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="벽력귀투 + 십자가", inline=False)
        return embed

    if msg=="블러드윙 너클":
        embed=discord.Embed(title="블러드윙 너클", description="공격력 +56\n최대 체력 +180\n이동 속도 +0.06\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756361957543956/013._Bloodwing_Knuckles__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="윙 너클 + 루비", inline=False)
        return embed

    if msg=="빙화현옥수":
        embed=discord.Embed(title="빙화현옥수", description="공격력 +44\n레벨 당 스킬 공격 추가 피해 +1\n스킬 공격 추가 피해 +20\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756362163093524/014._Frost_Petal_Hand_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="회단 장갑 + 얼음", inline=False)
        return embed

    if msg=="여래수투":
        embed=discord.Embed(title="여래수투", description="공격력 +50\n쿨다운 감소 +15%\n스킬 증폭 +19%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756362351804416/015._Buddha_s_Palm_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="회단 장갑 + 진신사리", inline=False)
        return embed

    if msg=="브레이질 건틀릿":
        embed=discord.Embed(title="브레이질 건틀릿", description="공격력 +57\n방어력 +15\n스태미너 재생 +1.2\n체력 재생 +1.2\n공격 속도(%) +40%\n", color=0x9C4998)
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
        embed=discord.Embed(title="주작자문", description="공격력 +40\n```발화-[고유 장착 효과]\n기본 공격의 대상에게 최대 4회 중첩되는 [타오르는 고통] 효과를 4초 동안 부여 합니다. [타오르는 고통]은 매 초마다 대상 최대 체력의 1.15%를 고정 피해로 줍니다.```", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756388587180112/019._Mark_of_the_Phoenix_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="삼매진화 + 글러브", inline=False)
        return embed

    if msg=="프로스트 팽":
        embed=discord.Embed(title="프로스트 팽", description="공격력 +48\n쿨다운 감소 +15%\n스킬 공격 추가 피해 +40\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/914756021208104982/914756388775936060/020._Permafrost__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="만년빙 + 회단 장갑", inline=False)
        return embed

#####암기#####
    if msg=="면도칼":
        embed=discord.Embed(title="면도칼", description="공격력 +11", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896472965573660712/001._Razor_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="병원(5개), 성당(5개), 학교(7개), 박쥐", inline=False)
        return embed

    if msg=="트럼프 카드":
        embed=discord.Embed(title="트럼프 카드", description="공격력 +4\n치명타 확률 +5%\n", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896472971055624202/002._Playing_Cards__.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="호텔(6개), 번화가(7개), 멧돼지", inline=False)
        return embed

    if msg=="분필":
        embed=discord.Embed(title="분필", description="공격력 +12", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896472975585447986/003._Chalk_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="공장(7개), 성당(5개), 학교(6개), 박쥐", inline=False)
        return embed

    if msg=="다트":
        embed=discord.Embed(title="다트", description="최대 충전 수: 20발(충전: 20초)\n공격력 +16\n치명타 피해량 +15%\n이동 속도 +0.0\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896472980476031047/004._Dart_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득경로", value="바늘 + 깃털", inline=False)
        return embed

    if msg=="빈티지 카드":
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
        embed=discord.Embed(title="부적", description="최대 충전 수: 10발(충전: 40초)\n공격력 +30\n스킬 공격 추가 피해 +5\n", color=0x1e82cd)
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

    if msg=="법륜":
        embed=discord.Embed(title="법륜", description="최대 충전 수: 50발(충전: 2초)\n공격력 +38\n스킬 증폭(%) +15%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473027066347571/013._Dharma_Chakram_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="챠크람 + 불경", inline=False)
        return embed

    if msg=="플럼바타":
        embed=discord.Embed(title="플럼바타", description="최대 충전 수: 20발(충전: 20초)\n공격력 +48\n이동 속도 +0.04\n치명타 피해량 +15%\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473031436795974/014._Plumbata_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득경로", value="다트 + 강철", inline=False)
        return embed

    if msg=="미치광이왕의 카드":
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
        embed=discord.Embed(title="풍마수리검", description="최대 충전 수: 50발(충전: 2초)\n공격력 +65\n쿨다운 감소 +15%\n스킬 공격 추가 피해 +15\n스태미너 재생 +1 최대 쿨다운 감소-[고유 장착 효과]\n최대 쿨다운 감소 +5%\n", color=0x9C4998)
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

    if msg=="플레솃":
        embed=discord.Embed(title="플레솃", description="최대 충전 수: 24발(충전: 12초)\n공격력 +88\n이동 속도 +0.06\n치명타 피해량 +15%\n기본 공격 사거리-[고유 장착 효과]\n기본 공격 사거리 +0.5\n", color=0x9C4998)
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
        embed=discord.Embed(title="생사부", description="최대 충전 수: 20발(충전: 20초)\n공격력 +83\n```저주-[고유 장착 효과]\n스킬 공격을 가하면 적을 4초간 저주 상태로 만듭니다. 저주 상태인 적은 이동 속도가 10%만큼 느려지고, 저주 상태에서 해제 될 때 100 + 스킬 증폭 * 2 에 해당하는 고정 피해를 입힙니다. 한번 저주 상태가 되면 8초간 (기본 공격 피격 시 1초 감소) 다시 저주 상태가 되지 않습니다.```\n", color=0x9C4998)
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
        embed=discord.Embed(title="만천화우", description="최대 충전 수: 4발(충전: 60초)\n공격력 +83\n기본 공격 추가 피해 +130\n스킬 공격 추가 피해 +3\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472624543174746/896473080879259738/024._Petal_Torrent_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="빙백은침 + 다이너마이트", inline=False)
        return embed

#####투척#####
    
    if msg=="쇠구슬":
        embed=discord.Embed(title="쇠구슬", description="공격력 +12", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472819167268925/001._Iron_Ball_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="양궁장(6개), 숲(7개), 공장(7개), 맷돼지", inline=False)
        return embed

    if msg=="야구공":
        embed=discord.Embed(title="야구공", description="공격력 +12", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472824670224394/002._Baseball_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="공장(3개), 고급 주택가(3개)", inline=False)
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
        embed=discord.Embed(title="볼 라이트닝", description="최대 충전 수: 50발(충전: 3초)\n공격력 +24\n공격 속도(%) +20%\n", color=0x1e82cd)
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
        embed=discord.Embed(title="필럼", description="최대 충전 수: 24발(충전: 3초)\n공격력 +28\n(고유) 기본 공격 사거리 +0.5", color=0x1e82cd)
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
        embed=discord.Embed(title="소이탄", description="최대 충전 수: 50발(충전: 3초)\n공격력 +63\n공격 속도(%) +60%\n쿨다운 감소 +8%\n", color=0x9C4998)
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
        embed=discord.Embed(title="아스트라페", description="최대 충전 수: 36발(충전: 3초) 공격력 +70\n치명타 확률 +24%\n치명타 피해량 +6%\n(고유)기본 공격 사거리 +0.75", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472918035419186/018._Astrape_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="필럼 + 유리 조각", inline=False)
        return embed

    if msg=="루테늄 구슬":
        embed=discord.Embed(title="루테늄 구슬", description="최대 충전 수: 50발(충전: 3초)\n공격력 +73\n스킬 증폭 +28%\n스킬 공격 치유 방해-[고유 장착 효과]\n스킬 공격에 피격된 대상의 치유 효과가 4초간 35% 감소합니다.\n", color=0x9C4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472923055992882/019._Ruthenium_Marble__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득경로", value="가시 탱탱볼 + 황금", inline=False)
        return embed

    if msg=="프리즘볼":
        embed=discord.Embed(title="프리즘 볼", description="최대 충전 수: 50발(충전: 3초)\n공격력 +110\n공격 속도 +33%\n", color=0xF9D537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472610097987597/896472927078350848/020._Dyadic_Prism__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="볼 라이트닝 + 포스 코어", inline=False)
        return embed





























