import discord
import asyncio

client = discord.Client()

def Weapon(msg):
#####망치#####
    if msg=="망치":
        embed=discord.Embed(title="망치", description="공격력 +16", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317360093442128/001._Hammer_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로 ", value="연못, 모래사장, 골목길의 상자\n멧돼지", inline=False)
        return embed

    if msg=="워해머":
        embed=discord.Embed(title="워해머", description="공격력 +40",color=0x1eb300)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317382633644034/002._Warhammer_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로 ", value="망치+단봉", inline=False)
        return embed

    if msg=="사슴망치":
        embed=discord.Embed(title="사슴망치", description="공격력 +56", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317414606823464/004._Black_Stag_Hammer__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로 ", value="워해머+가죽", inline=False)
        return embed
        
    if msg=="운명의망치":
        embed=discord.Embed(title="운명의망치", description="공격력 +40\n쿨다운 감소 +8%\n치명타 확률 +8%", color=0x1e82cd)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/891317310952988712/891317445732741190/005._Forged_Destiny__.png")
        embed.add_field(name="등급", value="희귀", inline=True)
        embed.add_field(name="휙득 경로 ", value="망치+운명의 꽃", inline=True)
        return embed

    if msg=="낭아봉":
        embed=discord.Embed(title="낭아봉", description="공격력 +55\n 스킬 공격 추가 피해 +22\n 레벨 당 스킬 공격 추가 피해 +1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317450635874375/006._Fang_Mace_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="모닝스타+달궈진 돌멩이", inline=False)
        return embed
    
    if msg=="다그다의망치":
        embed=discord.Embed(title="다그다의 망치", description="공격력 +98\n 체력 재생(%) +125%\n 기본 공격 추가 피해 +28\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317452749803540/007._Hammer_of_Dagda__.png")
        embed.add_field(name="등급", value="영웅", inline=True)
        embed.add_field(name="휙득 경로 ", value="사슴망치+성자의 유산", inline=True)
        return embed

    if msg=="토르의망치":
        embed=discord.Embed(title="토르의망치", description="공격력 +105\n 공격 속도(%) +30%\n 레벨 당 공격 속도 +1%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317472165261342/008._Hammer_of_Thor__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="사슴망치+이온전지", inline=False)
        return embed 

    if msg=="개밥바라기":
        embed=discord.Embed(title="개밥바라기", description="공격력 +105\n 스킬 증폭(%) +20%", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317472769241169/009._Evening_Star_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="모닝스타 + 문스톤", inline=False)
        return embed

    if msg=="천근추":
        embed=discord.Embed(title="천근추", description="공격력 +88\n 스킬 증폭 +8%\n 쿨다운 감소 +12%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317475961085972/010._Weight_of_the_World_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="운명의망치+진신사리", inline=False)        
        return embed
        
    if msg=="피스브링어":
        embed=discord.Embed(title="피스브링어", description="공격력 +140\n 모든 피해 흡혈 10%\n 방어력 관통 +12%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891317310952988712/891317478783873064/011._Peacebringer__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로 ", value="사슴망치+VF 혈액 샘플", inline=False)
        return embed

#####단검#####
    if msg=="식칼":
        embed=discord.Embed(title="식칼", description="공격력 +4", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342811553751060/003._Kitchen_Knife_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로 ", value="항구,호텔,절의 상자, 멧돼지", inline=False)
        return embed

    if msg =="가위":
        embed=discord.Embed(title="가위", description="공격력 +5", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342805245505556/001._Scissors_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로 ", value="골목길, 병원, 학교의 상자, 박쥐", inline=False)    
        return embed

    if msg=="만년필":
        embed=discord.Embed(title="만년필", description="공격력 +5", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342808315740230/002._Fountain_Pen_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로 ", value="고급 주택가, 번화가, 학교의 상자, 박쥐", inline=False)
        return embed

    if msg=="군용나이프":
        embed=discord.Embed(title="군용나이프", description="공격력 +14\n 이동 속도 +0.06", color=0x1eb300)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342816045830184/004._Army_Knife__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로 ", value="식칼+나뭇가지", inline=False)
        return embed

    if msg=="메스":
        embed=discord.Embed(title="메스", description="공격력 +18", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342820277899385/005._Scalpel_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로 ", value="만년필+면도칼", inline=False)
        return embed

    if msg=="자마다르":
        embed=discord.Embed(title="자마다르", description="공격력 +15", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342825336229898/006._Jamadhar_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로 ", value="식칼+너클", inline=False)
        return embed

    if msg=="장미칼":
        embed=discord.Embed(title="장미칼", description="공격력 +20\n 이동 속도 +0.08\n 쿨다운 감소 +8%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342830545543278/007._Rose_Knife_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로 ", value="군용 나이프+꽃", inline=False)
        return embed

    if msg=="스위스아미나이프" or msg=="스위스 아미 나이프":
        embed=discord.Embed(title="스위스 아미 나이프", description="공격력 +23\n 최대 체력 +100", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342835192832010/008._Swiss_Army_Knife__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로 ", value="메스+가위", inline=False)
        return embed

    if msg=="카라페이스 카타르":
        embed=discord.Embed(title="카라페이스 카타르", description="공격력 +20\n 방어력 +12", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342839248732160/009._Carapace_Katar__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로 ", value="자마다르+거북이등딱지", inline=False)
        return embed

    if msg=="카른웬난":
        embed=discord.Embed(title="카른웬난", description="공격력 +41\n 체력 재생 +1.2\n 이동 속도 +0.08\n 쿨다운 감소 +8%\n 기본 공격 추가 피해 +26\n 레벨 당 기본 공격 추가 피해 +2\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342843313004564/010._Carnwennan_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="장미칼+성자의 유산", inline=False)
        return embed

    if msg=="파산검":
        embed=discord.Embed(title="파산검", description="공격력 +30\n 이동 속도 +0.1\n 쿨다운 감소 +12%\n 레벨 당 스킬 공격 추가 피해 +2\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342847847043142/011._Mount_Slicer_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="장미칼+재", inline=False)
        return embed

    if msg=="초진동나이프"or msg=="초진동 나이프":
        embed=discord.Embed(title="초진동나이프", description="공격력 +55\n 공격 속도(%) +40%\n 이동 속도 +0.1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342852058144798/012._Vibroblade_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="군용 나이프+모터", inline=False)
        return embed


    if msg=="다마스커스 가시"or msg=="다마스커스가시":
        embed=discord.Embed(title="다마스커스 가시", description="공격력 +66\n 최대 체력 +250\n 스킬 공격 치유 방해-[고유 장착 효과]\n 스킬 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342855883333632/013._Damascus_Steel_Thorn__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="스위스 아미 나이프+가시 발판", inline=False)
        return embed

    if msg=="마하자라":
        embed=discord.Embed(title="마하자라", description="공격력 +42\n 방어력 +18\n 신속 - 루드라의 단검 - [고유 장착 효과]\n 4초 이내에 4회의 개별 피해를 가하면, 2.5초간 이동 속도가 10%, 공격력이 33% 증가합니다. (쿨타임 6초)", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342860014735390/014._Maharaja_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로 ", value="카라페이스 카타르+아이테르 깃털", inline=False)
        return embed

    if msg=="프라가라흐":
        embed=discord.Embed(title="프라가라흐", description="공격력 +82\n 이동 속도 +0.18\n 차지드 스트라이크 - [고유 장착 효과]\n 매 4초마다 다음 공격이 100%의 치명타 확률 보너스를 획득합니다.", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891322058556981298/891342864741707846/015._Fragarach_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로 ", value="군용 나이프+포스 코어", inline=False)
        return embed
        

#####쌍칼#####
    if msg=="쌍칼":
        embed=discord.Embed(title="쌍칼", description="공격력 +12", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321971483234344/001._Twin_Swords_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로", value="기본 제공, 식칼 + 녹슨 검", inline=False)
        return embed

    if msg=="조잡한 쌍칼":
        embed=discord.Embed(title="조잡한 쌍칼", description="공격력 +12", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/894235985389428806/002._Wrought_Swords__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="가위 + 곡괭이", inline=False)
        return embed

        
    if msg=="피렌체식쌍검":
        embed=discord.Embed(title="피렌체식 쌍검", description="공격력 +28\n 생명력 흡수 +10%", color=0x1e82cd)
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

    if msg =="이천일류":
        embed=discord.Embed(title="이천일류", description="공격력 +49\n 공격 속도(%) +12%\n 생명력 흡수 +20%\n 치유 방해 - [장착 효과]\n 스킬 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321979968294912/004._Divine_Dual_Swords_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="피렌체식 쌍검 + 못", inline=False)
        return embed

    if msg=="자웅일대검":
        embed=discord.Embed(title="자웅일대검", description="공격력 +60\n 공격 속도(%) +35%\n 기본 공격 추가 피해 +8\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321984187764797/005._Starsteel_Twin_Swords_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="쌍칼 + 문스톤", inline=False)
        return embed
        
    if msg =="디오스쿠로이":
        embed=discord.Embed(title="디오스쿠로이", description="공격력 +55\n 공격 속도(%) +55%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321988918968320/006._Dioscuri_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="조잡한 쌍검 + 이온 전지", inline=False)
        return embed

    if msg=="로이거차르":
        embed=discord.Embed(title="로이거 차르", description="공격력 +40\n 레벨 당 스킬 공격 추가 피해 +2.5\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891321992286961664/007._Lioigor___Zahr__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="쌍둥이 검 + 재", inline=False)
        return embed

    if msg=="아수라":
        embed=discord.Embed(title="아수라", description="공격력 +48\n 모든피해 흡혈 +8%\n 레벨 당 스킬 증폭 +1%\n 쿨다운 감소 +12%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/894235982805733416/007._Asura_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="피렌체식 쌍검 + 진신사리", inline=False)
        return embed
        

    if msg=="간장과막야":
        embed=discord.Embed(title="간장과막야", description="공격력+75\n 공격 속도 +18%\n (고유)기본 공격 사거리 +1\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891316976876650549/891322007319347240/008._Spring_and_Autumn__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로 ", value="쌍칼+포스 코어", inline=False)
        return embed

#####레이피어#####

    if msg=="바늘":
        embed=discord.Embed(title="바늘", description="공격력 +3\n 치명타 피해량 +15%\n", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251084057571338/001._Needle_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="골목길, 병원, 호텔의 상자", inline=False)
        return embed

    if msg=="레이피어":
        embed=discord.Embed(title="레이피어", description="공격력 +16\n 치명타 피해량 +15%\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251088604176394/002._Rapier_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="바늘 + 철광석", inline=False)
        return embed

    if msg=="매화검":
        embed=discord.Embed(title="매화검", description="공격력 +25\n 치명타 확률 +10%\n 치명타 피해량 +15%\n 쿨다운 감소 +6%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251096623697962/003._Apricot_Sword_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="레이피어 + 운명의 꽃", inline=False)
        return embed

    if msg=="에스톡":
        embed=discord.Embed(title="에스톡", description="공격력 +23\n 스킬 공격 추가피해 +12\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251101963034695/004._Estoc_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="바늘 + 레이피어", inline=False)
        return embed

    if msg=="활빈검":
        embed=discord.Embed(title="활빈검", description="공격력 +30\n 체력 재생 +1.5\n 스태미너 재생 +150%\n 시야 +1\n 치명타 피해량 +25%\n 쿨다운 감소 +12%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251107415654420/005._Sword_of_Justice_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="레이피어 + 어사의", inline=False)
        return embed

    if msg=="듀랜달 Mk2":
        embed=discord.Embed(title="듀랜달 Mk2", description="공격력 +55\n 시야 +1.5\n 치명타 확률 +12%\n 치명타 피해량 +25%\n 쿨다운 감소 +6%\n 생명력 흡수 +11%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251113694498856/006._Durendal_Mk2__Mk2.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="매화검 + 레이저 포인터", inline=False)
        return embed

    if msg=="볼틱레토":
        embed=discord.Embed(title="볼틱레토", description="공격력 +50\n 공격 속도(%) +50%\n 치명타 확률 +10%\n 치명타 피해량 +15%\n 쿨다운 감소 +6%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251119151300678/007._Volticletto_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="매화검 + 전자 부품", inline=False)
        return embed

    if msg=="레드팬서":
        embed=discord.Embed(title="레드 팬서", description="공격력 +46\n 최대 체력 +225\n 스테미너 재생 +80%\n 스킬 공격 추가피해 +20\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251133344813087/010._Red_Panther__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="에스톡 + 진홍 팔찌", inline=False)
        return embed

    if msg=="유성검":
        embed=discord.Embed(title="유성검", description="공격력 +64\n 치명타 피해량 +12%\n 쿨다운 감소 +12% \n차지드 스트라이크 - [고유 장착 효과]\n 매 3초마다 다음 공격이 100%의 치명타 확률 보너스를 획득합니다.\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894251045377687663/894251124587122688/008._Meteor_Claymore_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="매화검 + 운석", inline=False)
        return embed

    if msg=="주와이외즈":
        embed=discord.Embed(title="주와이외즈", description="공격력 +76\n 레벨당 공격속도 +1%\n 이동 속도 +0.1\n 치명타 피해량 +12%\n", color=0x9c4998)
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
        embed=discord.Embed(title="렌즈", description="공격력 +12\n 시야 +0.5", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865260200452116/001._Lens_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로", value="감시 카메라+유리병", inline=False)
        return embed

    if msg=="카메라건":
        embed=discord.Embed(title="카메라 건", description="공격력 +19\n 시야 +1", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865264398958602/002._Pistol_Camera__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="렌즈 + 발터 PPK", inline=False)
        return embed

    if msg=="컴팩트 카메라":
        embed=discord.Embed(title="컴팩트 카메라", description="공격력 +24\n 시야 +1", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865268589043762/003._Compact_Camera__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="위장 카메라 + 렌즈", inline=False)
        return embed

    if msg=="레인지파인더":
        embed=discord.Embed(title="레인지 파인더", description="공격력 +40\n 시야 +3.5\n 쿨다운 감소 +6%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865273802559538/004._Rangefinder_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="저격 스코프 + 고장난 시계", inline=False)
        return embed

    if msg=="카메라 라이플":
        embed=discord.Embed(title="카메라 라이플", description="공격력 +30\n 시야 +2\n 기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +0.5\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865279385174097/005._Carbine_Camera__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="카메라 건 + 페도로프 자동소총", inline=False)
        return embed

    if msg=="미러리스":
        embed=discord.Embed(title="미러리스", description="공격력 +43\n 시야 +2\n 레벨 당 스킬 증폭 +2%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865286955905044/006._Mirrorless_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="컴팩트 카메라 + 황금", inline=False)
        return embed

    if msg=="카메라캐논":
        embed=discord.Embed(title="카메라 캐논", description="공격력 +51\n 최대 체력 +280\n 시야 +4\n 기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865299903737966/008._Cannon_Camera__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="카메라 라이플 + 탄창", inline=False)
        return embed

    if msg=="컴파운드 사이트":
        embed=discord.Embed(title="컴파운드 사이트", description="공격력 +55\n 시야 +5\n 쿨다운 감소 +15%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865306039984128/008._Laser_Designator__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="레인지파인더 + 꽃", inline=False)
        return embed
    
    if msg=="V.I.C.G":
        embed=discord.Embed(title="V.I.C.G", description="공격력 +72\n 시야 +1.5\n 기본 공격 추가 피해 +45\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891865219050127390/891865312750870588/009._V.I.C.G.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="카메라 건 + 휴대폰", inline=False)
        return embed

#####쌍절곤#####
    if msg=="쇠사슬":
        embed=discord.Embed(title="쇠사슬", description="공격력 +13", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865028322558002/001._Steel_Chain_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로 ", value="모래사장, 골목길, 묘지의 상자, 멧돼지", inline=False)
        return embed

    if msg=="눈차크":
        embed=discord.Embed(title="눈차크", description="공격력 +29", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865033410244608/002._Nunchaku_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="쇠사슬 + 고철", inline=False)
        return embed

    if msg=="샤퍼":
        embed=discord.Embed(title="샤퍼", description="공격력 +29\n 스킬 공격 치유 방해 - [고유 장착 효과]\n 스킬 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865037801656340/003._Sharper_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="눈차크 + 못", inline=False)
        return embed

    if msg=="블리더":
        embed=discord.Embed(title="블리더 ", description="공격력 +38", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865042759344188/004._Bleeder_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="눈차크 + 면도칼", inline=False)
        return embed

    if msg=="대소반룡곤":
        embed=discord.Embed(title="대소반룡곤", description="공격력 +50\n 스킬 공격 추가 피해 +22\n 스킬 공격 치유 방해 - [고유 장착 효과]\n 스킬 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865046957846558/005._The_Smiting_Dragon_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="샤퍼 + 재", inline=False)
        return embed

    if msg=="초진동눈차크":
        embed=discord.Embed(title="초진동눈차크", description="공격력 +65\n 공격 속도(%) +50%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865052024553482/006._Vibro_Nunchaku_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="블리더 + 모터", inline=False)
        return embed

    if msg=="케로베로스":
        embed=discord.Embed(title="케르베로스", description="공격력 +45\n 레벨 당 공격력 +2\n 이동 속도 +0.1\n 기본 공격 치유 방해 - [고유 장착 효과]\n 기본 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다. 기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +0.5\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865056374050836/007._Cerberus_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="샤퍼 + 체인 레깅스", inline=False)
        return embed

    if msg=="히드라":
        embed=discord.Embed(title="히드라", description="공격력 +110\n 모든 피해 흡혈(%) +25%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891864999721582612/891865060136345620/008._Hydra_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로", value="샤퍼 + 체인 레깅스", inline=False)
        return embed

#####권총#####

    if msg=="발터PPK":
        embed=discord.Embed(title="발터 PPK", description="장탄 수: 6발\n 공격력 +14\n", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864754992328734/001._Walther_PPK__PPK.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="모래사장, 호텔, 공장의 상자", inline=False)
        return embed

    if msg=="매그넘파이썬":
        embed=discord.Embed(title="매그넘-파이썬", description="장탄 수: 6발\n 공격력 +15\n 공격 속도(%) +10%\n 이동속도 +0.1\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864760168108102/002._Magnum-Python_-.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="발터 PPK + 오일", inline=False)
        return embed

    if msg=="베레타M92F":
        embed=discord.Embed(title="베레타 M92F", description="장탄 수: 6발 공격력 +23 이동속도 +0.1", color=0x329632)
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

    if msg=="더블 리볼버 SP":
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
        embed=discord.Embed(title="마탄의 사수", description="장탄 수: 7발\n 공격력 +48\n 공격 속도(%) +30%\n 이동 속도 +0.1\n 스킬 증폭 +20%\n 마탄 - [고유 장착 효과]\n 마지막 탄환으로 가하는 기본 공격이 공격력 +스킬 증폭 *2 + 스킬 공격 추가 피해 * 1.5 에 해당하는 스킬 피해를 입히고, 입힌 피해의 100%만큼의 체력을 회복합니다.", color=0x9c4998)
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

    if msg=="일렉트론 블라스터":
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

    if msg=="글록 48":
        embed=discord.Embed(title="글록 48", description="장탄 수: 8발\n 공격력 +75\n 공격 속도(%) +20%\n 이동 속도 +0.1\n 시야 +3.5\n 기본 공격 사거리 - [고유 장착 효과]\n  기본 공격 사거리 +0.75\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755103726501968/891864824970088568/012._Glock_48__48.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="FN57 + EMP 드론", inline=False)
        return embed

    if msg=="스탬피드":
        embed=discord.Embed(title="스탬피드", description="장탄 수: 2발\n 공격력 +40\n 이동 속도 +0.1\n 레벨 당 스킬 증폭 +1%\n 더블 탭 - [고유 장착 효과]\n 마지막 탄환으로 가하는 기본 공격이 공격력 +스킬 증폭 *1 + 캐릭터 레벨 * 10 에 해당하는 스킬 피해를 입힙니다.\n", color=0x9c4998)
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
        embed=discord.Embed(title="단봉", description="공격력 +15", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864611832352819/002._Short_Rod_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="항구, 절, 연못의 상자, 들개", inline=False)
        return embed

    if msg=="나뭇가지":
        embed=discord.Embed(title="나뭇가지", description="공격력 +5", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864605830287380/001._Branch_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="나뭇가지더미 채집", inline=False)
        return embed

    if msg=="장봉":
        embed=discord.Embed(title="장봉", description="공격력 +22", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864617213648926/003._Long_Rod_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="단봉 + 대나무", inline=False)
        return embed

    if msg=="도깨비 방망이":
        embed=discord.Embed(title="도깨비 방망이", description="공격력 +27\n 기본 공격 치유 방해 - [고유 장착 효과]\n 기본 공격에 피격된 대상의 치유 효과가 45% 감소합니다.\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864623446372362/004._Goblin_Bat__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="장봉 + 못", inline=False)
        return embed

    if msg=="우산":
        embed=discord.Embed(title="우산", description="공격력 +30\n 스킬 공격 추가 피해 +14\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864628622143528/005._Umbrella_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="장봉 + 부채", inline=False)
        return embed

    if msg=="횃불":
        embed=discord.Embed(title="횃불", description="공격력 +36\n 체력 재생 +0.5\n 공격 속도(%) +10%\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864633655300196/006._Torch_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="단봉 + 기름먹인 천", inline=False)
        return embed

    if msg=="몽둥이":
        embed=discord.Embed(title="몽둥이", description="공격력 +40\n 이동 속도 -0.1\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864642559832115/007._Reinforced_Club_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="단봉 + 강철", inline=False)
        return embed

    if msg=="마법봉":
        embed=discord.Embed(title="마법봉", description="공격력 +59\n 생명력 흡수 +30%\n 시야 +1\n 스킬 증폭 +30%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864648436039710/008._Magic_Stick_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="장봉 + 달빛 펜던트", inline=False)
        return embed

    if msg=="금강저":
        embed=discord.Embed(title="금강저", description="공격력 +96\n 차지드 스트라이크 - [고유 장착 효과]\n 매 3초마다 다음 공격이 100%의 치명타 확률 보너스를 얻습니다.\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864653599244328/009._Vajra_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="몽둥이 + 유리판", inline=False)
        return embed

    if msg=="구원의 여신상":
        embed=discord.Embed(title="구원의 여신상", description="공격력 +64\n 레벨 당 공격력 +2\n 체력 재생 +0.6\n 스테미너 재생(%) +80%\n 공격 속도(%) +15%\n 생명력 흡수 +12%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864659102162994/010._Statue_of_Soteria__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="횃불 + 인형", inline=False)
        return embed

    if msg=="타구봉":
        embed=discord.Embed(title="타구봉", description="공격력 +85\n 공격 속도(%) +50%\n 기본 공격 치유 방해 - [고유 장착 효과]\n 기본 공격에 피격된 대상의 치유 효과가 4초 동안 45% 감소합니다.\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864665389412382/011._Mallet_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="도깨비 방망이 + 전자 부품", inline=False)
        return embed

    if msg=="스파이의 우산":
        embed=discord.Embed(title="스파이의 우산", description="공격력 +65\n 스테미너 재생 +0.8\n 스킬 공격 추가 피해 +25\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864673794818089/012._Spy_Umbrella__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="우산 + 재", inline=False)
        return embed

    if msg=="여의봉":
        embed=discord.Embed(title="여의봉", description="공격력 +135\n 공격 속도 +10%\n 기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +1\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891755056142106624/891864681067724900/013._Monkey_King_Bar_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="포스 코어 + 장봉", inline=False)
        return embed


######도끼#####

    if msg=="손도끼":
        embed=discord.Embed(title="손도끼", description="공격력 +25", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366076565303306/002._Hatchet_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로", value="연못, 모래사장, 공장의 상자, 들개", inline=False)
        return embed

    if msg=="곡괭이":
        embed=discord.Embed(title="곡괭이", description="공격력 +15", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366069443375195/001._Pickaxe_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="휙득 경로", value="연못,모래사장,묘지,숲의 상자, 박쥐", inline=False)
        return embed

    if msg== "전투도끼":
        embed=discord.Embed(title="전투도끼", description="공격력 +47", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366084677091368/04._Battle_Axe__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="손도끼+대나무", inline=False)
        return embed

    if msg=="사슬낫":
        embed=discord.Embed(title="사슬낫", description="공격력 +50\n 기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +0.2", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366080038191134/003._Chain_Scythe__.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="휙득 경로", value="곡괭이+쇠사슬", inline=False)
        return embed

    if msg=="사신의낫":
        embed=discord.Embed(title="사신의낫", description="공격력 +80\n 기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +0.5", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366100279918652/006._Reaper_s_Scythe.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="사슬 낫+단봉", inline=False)
        return embed

    if msg=="경령화 도끼"or msg=="경령화도끼":
        embed=discord.Embed(title="경령화 도끼", description="공격력 +61\n 이동속도 +0.05\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366090725290054/005._Light_Hatchet__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="전투 도끼 + 깃털", inline=False)
        return embed

    if msg=="대부":
        embed=discord.Embed(title="대부", description="공격력 +110\n 이동 속도 -0.1", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366106546176010/007._Gigantic_Axe_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="휙득 경로", value="전투 도끼 + 강철", inline=False)
        return embed

    if msg=="빔 엑스"or msg=="빔엑스":
        embed=discord.Embed(title="빔 엑스", description="공격력 +102\n 레벨당 공격력 +2\n 시야 +3\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366112263024650/008._Beam_Axe__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="대부 + 레이저 포인터", inline=False)
        return embed

    if msg=="산타무에르페":
        embed=discord.Embed(title="산타 무에르페", description="공격력 +105\n 최대 체력 +320\n 기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +0.5", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366117640122388/009._Santa_Muerte__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="사신의 낫 + 루비", inline=False)
        return embed

    if msg=="스퀴테":
        embed=discord.Embed(title="스퀴테", description="공격력 +112\n 레벨 당 스킬 증폭 +2%\n 기본 공격 사거리 - [고유 장착 효과]\n 동일한 이름의 고유 효과는 하나만 적용됩니다.\n 기본 공격 사거리 +1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366122300006421/010._Scythe_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="사신의 낫 + 황금", inline=False)
        return embed

    if msg=="파라슈":
        embed=discord.Embed(title="파라슈", description="공격력 +115\n 이동 속도 +0.07\n 쿨다운 감소 +14%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366127446405150/011._Parashu_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="경량화 도끼 + 진신사리", inline=False)
        return embed

    if msg=="저거너트":
        embed=discord.Embed(title="저거너트", description="공격력 +92\n 레벨 당 공격 속도 +3%\n 기본 공격 사거리 -0.2\n 이동 속도 +0.1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366132706054154/012._The_Juggernaut_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="경랑화 도끼 + 모터", inline=False)
        return embed
    

    if msg=="하르페":
        embed=discord.Embed(title="하르페 ", description="공격력 +110\n 생명력 흡수 +20%\n 가벼운 발걸음 - [고유 장착 효과]\n 0.2m 이동할 때마다 [가벼운 발걸음]을 최대 100회까지 중첩해서 획득합니다. 중첩에 따라 이동속도가 최대 0.12까지 증가합니다. 기본 공격 피해를 입힐 경우 중첩을 모두 소모하여 최대 120의 고유 피해를 입힙니다. 최대 중첩 상태에서 기본 공격에 피격된 대상의 이동속도를 2초간 15% 감소 시킵니다.", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891365946600591410/891366137101684766/013._Harpe_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="휙득 경로 ", value="대부+해적 깃발", inline=False)
        return embed

######톤파######
    if msg=="대나무":
        embed=discord.Embed(title="대나무", description="공격력 +12", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289517330006026/001._Bamboo_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득 경로", value="연못, 절, 양궁장, 묘지, 숲의 상자, 박쥐", inline=False)
        return embed

    if msg=="톤파":
        embed=discord.Embed(title="톤파", description="공격력 +23\n 방어력 +8\n", color=0x329632)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289522346369034/002._Wooden_Tonfa_.png")
        embed.add_field(name="등급", value="고급", inline=False)
        embed.add_field(name="획득 경로", value="대나무 + 나뭇가지", inline=False)
        return embed

    if msg=="경찰봉":
        embed=discord.Embed(title="경찰봉", description="공격력 +31\n 방어력 +10\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289527987707944/003._Police_Baton_.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="톤파 + 마패", inline=False)
        return embed

    if msg=="류쿠톤파":
        embed=discord.Embed(title="류큐톤파", description="공격력 +38\n 방어력 +18\n", color=0x1e82cd)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289533016674314/004._Ryuku_Tonfa__.png")
        embed.add_field(name="등급", value="희귀", inline=False)
        embed.add_field(name="획득 경로", value="톤파 + 백색 가루", inline=False)
        return embed

    if msg=="택티컬 톤파":
        embed=discord.Embed(title="택티컬 톤파", description="공격력 +74\n 방어력 +16\n 생명력 흡수 +20%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289537965973514/005._Tactical_Tonfa__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="경찰봉 + 정교한 도면", inline=False)
        return embed

    if msg=="마이쏙":
        embed=discord.Embed(title="마이쏙", description="공격력 +63\n 방어력 +18\n 레벨 당 방어력 +1\n 체력 재생(%) +100%\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289544559419452/006._Mai_Sok_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="류큐톤파 + 단봉", inline=False)
        return embed

    if msg=="플라즈마톤파":
        embed=discord.Embed(title="플라즈마 톤파", description="공격력 +60\n 방어력 +21\n 시야 +4\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289549835829258/007._Plasma_Tonfa__.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="류큐톤파 + 레이저 포인터", inline=False)
        return embed

    if msg=="윈드러너":
        embed=discord.Embed(title="윈드러너", description="공격력 +70\n 방어력 +8\n 이동 속도 +0.1\n 신속 - 산들바람-[고유 장착 효과]\n 4초 이내에 3회의 개별 피해를 가하면, 3초간 이동 속도가 10% 증가하고, 공격 속도가 30% 증가하며 225의 보호막을 얻습니다.\n (쿨다운 6초)\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289554332135444/008._Windrunner_.png")
        embed.add_field(name="등급", value="영웅", inline=False)
        embed.add_field(name="획득 경로", value="톤파 + 미스릴 실", inline=False)
        return embed

    if msg=="흑요석 짓테":
        embed=discord.Embed(title="흑요석 짓테", description="공격력 +75\n 방어력 +25\n 저주-[고유 장착 효과]\n 스킬 공격을 가하면 적을 4초간 저주 상태로 만듭니다. 저주 상태인 적은 이동 속도가 10%만큼 느려지고, 저주 상태에서 해제 될 때 75 +스킬 증폭 * 1.75에 해당하는 고정 피해를 입힙니다. 한번 저주 상태가 되면 8초간 (기본 공격 피격 시 1초 감소) 다시 저주 상태가 되지 않습니다.\n (쿨다운 : 2초)\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/892289488863236177/892289558861979719/009._Obsidian_Jitte__.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득 경로", value="경찰봉 + 포스 코어", inline=False)
        return embed

######저격총######
    if msg=="화승총":
        embed=discord.Embed(title="화승총", description="장탄 수: 1발\n 공격력 +30\n 체력 재생 +1.5\n 시야 +1\n 스태미너 재생(%) +150%\n 치명타 피해량 +25%\n 쿨다운 감소 +12%\n", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472485552332910/001._Long_Rifle_.png")
        embed.add_field(name="등급", value="일반", inline=False)
        embed.add_field(name="획득경로", value="항구, 숲의 상자", inline=False)
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
        embed=discord.Embed(title="인터벤션", description="장탄 수: 2발\n공격력 +100\n 시야 +4\n 기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +1\n", color=0x9c4998)
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
        embed=discord.Embed(title="현자총통", description="장탄 수: 1발\n 공격력 +160\n 기본 공격 사거리 -1\n 철환 - [고유 장착 효과]\n 다음에 가하는 기본 공격이 115의 추가 고유 피해를 주고 0.56초 동안 이동속도를 99% 만큼 감소시킵니다. (쿨다운 : 4초)", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472376164892722/896472527197573170/011._Blackfire_Cannon_.png")
        embed.add_field(name="등급", value="전설", inline=False)
        embed.add_field(name="획득경로", value="스프링필드 + 삼매진화", inline=False)
        return embed
        
######돌격소총######
    if msg=="페도로프 자동소총":
        embed=discord.Embed(title="페도로프 자동소총", description="장탄 수: 30발\n 공격력 +11\n", color=0xffffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472409845141554/001._Fedorova__.png")
        embed.add_field(name="등급 ", value="일반 ", inline=False)
        embed.add_field(name="휙득 경로", value="공장, 호텔, 고급 주택가의 상자", inline=False)
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

    if msg=="개틀링 건":
        embed=discord.Embed(title="개틀링 건", description="장탄 수: 30발\n 	 공격력 +20\n 공격 속도(%) +10%\n 시야 +1.5\n 기본 공격 추가 피해 +11\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472430569201704/005._Gatling_Gun_.png")
        embed.add_field(name="등급 ", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="STG-44 + 모터", inline=False)
        return embed
            
    if msg=="5식 자동 소총":
        embed=discord.Embed(title="95식 자동 소총", description="장탄 수: 30발\n 	공격력 +84\n 시야 +2\n 기본 공격 사거리 - [고유 장착 효과]\n 기본 공격 사거리 +1\n", color=0x9c4998)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472435556253716/006._Type_95_95_.png")
        embed.add_field(name="등급 ", value="영웅", inline=False)
        embed.add_field(name="휙득 경로", value="AK-47 + 강철", inline=False)
        return embed

    if msg=="AK-12":
        embed=discord.Embed(title="AK-12", description="장탄 수: 30발\n 	공격력 +68\n 레벨 당 공격력 +2\n 시야 +1.5\n 치명타 확률 +22%\n", color=0x9c4998)
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
        embed=discord.Embed(title="저지먼트", description="장탄 수: 120발\n 공격력 +120\n 시야 +1.5\n 방어 관통 +12%\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472448168521848/009._Judgement_.png")
        embed.add_field(name="등급 ", value="전설", inline=False)
        embed.add_field(name="휙득 경로", value="포스 코어 + STG-44", inline=False)
        return embed

    if msg=="아그니":
        embed=discord.Embed(title="아그니", description="장탄 수: 30발\n 공격력 +51\n 공격 속도 +25%\n 시야 +1.5\n 기본 공격 추가 피해 +16\n", color=0xf9d537)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/896472357156290571/896472452379607080/010._Agni_.png")
        embed.add_field(name="등급 ", value="전설", inline=False)
        embed.add_field(name="휙득 경로", value="개틀링 건 + 뜨거운 오일", inline=False)
        return embed



