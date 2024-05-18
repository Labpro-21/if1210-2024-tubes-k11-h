from func import *
from RNG import *


def attack(dictionary:dict,victim:dict):
    penentu=RNG(-30,30) #mengambil range dari +-30
    atk_dmg=int(dictionary['ATK_Power'])+int((penentu/100)*int(dictionary['ATK_Power'])) #pembulatan ke bawah
    victim['HP']=str(int(victim['HP'])-atk_dmg-int((int(victim['DEF_Power'])/100)*atk_dmg))
    if int(victim["HP"])<0:
        victim["HP"]='0'
    printDict(victim)
    return victim

def usepotion(user_potion:dict, user_choosen_monster:dict, base_hp, cond_str: bool, cond_def:bool, cond_heal:bool,choosen_potion:int):
    move=False
    while not move:
        if choosen_potion<=len(user_potion):
            potion_name=str(user_potion[choosen_potion]['Type']).upper()
            print(user_choosen_monster)
            arr=[user_choosen_monster['ATK_Power']]+[user_choosen_monster['DEF_Power']]+[user_choosen_monster['HP']] #membuat array stast monster
            if potion_name=='STRENGTH' and not cond_str:
                user_choosen_monster['ATK_Power']=str(potion(potion_name, arr, base_hp)) 
            elif potion_name=='RESILIENCE' and not cond_def:
                user_choosen_monster['DEF_Power']=str(potion(potion_name, arr, base_hp))
            elif potion_name=='HEALING' and not cond_heal:
                user_choosen_monster['HP']=str(potion(potion_name, arr, base_hp ))
            else:
                print(f"Kamu mencoba memberikan ramuan ini kepada {user_choosen_monster['Name']}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
            return user_choosen_monster
        elif choosen_potion==len(user_potion)+1:
            return
        else:
            print("Pilihan nomor tidak tersedia!")

def potion(potion:str, arr:list, base_hp):      #arr= [atk,def,hp]
    if potion=='STRENGTH':
        new= int(arr[0])+0.05*int(arr[0])
        print("Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi Pikachow dan gerakannya menjadi lebih cepat dan mematikan.")
        return int(new)
    elif potion=='RESILIENCE':
        new= int(arr[1])+0.05*int(arr[1])
        print("Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar Pikachow yang membuatnya terlihat semakin tangguh dan sulit dilukai.")
        return int(new)
    elif potion=='HEALING':
        hp= int(arr[2])+0.25*int(base_hp)
        print("Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh Pikachow sembuh dengan cepat. Dalam sekejap, Pikachow terlihat kembali prima dan siap melanjutkan pertempuran.")
        if int(arr[2])>hp:
            return int(hp) #jika heal melebihi hp monster saat ini
        else:
            return int(arr[2])
        
def input_potion(user_potion:dict):
    print("============ POTION LIST ============")
    index=1
    for elem in (user_potion):
        print(f"{elem}. {user_potion[elem]['Type']} Potion (Qty:{user_potion[elem]['Quantity']})")
        index+=1
    print(f"{index}. Cancel")
    choosen_potion = int(input("Pilih perintah: "))
    print()
    while choosen_potion>=index:
        if choosen_potion>index:
            print("Pilihan nomor tidak tersedia!")
        elif choosen_potion==index:
            return None
        choosen_potion = int(input("Pilih perintah: "))
    return choosen_potion

def user_summon(user_monster:dict, username, monster_data):
    print("Selamat datang di Arena!!")
    print("============ MONSTER LIST ============")
    for key in user_monster:
        print(f"{key}. {user_monster[key]['Name']}")
    input_monst=None
    done_choosing=False
    
    while not done_choosing:
        input_monst=int(input("Pilih monster untuk bertarung: "))
        if input_monst>len(user_monster):
            print("Pilihan nomor tidak tersedia!")
        else:
            done_choosing=True

    user_choosen_monster=user_monster[input_monst]

    for i, elem in enumerate (monster_data['type']):
        if elem[i]==user_monster[input_monst]['Name']: #mencari nama yang sama dengan yang di input user di file monster
            base_hp = monster_data['hp'][i]
            break

    gambar = f'''
          /\----/\_   
         /         \\   /
        |  | O    O | / |
        |  | .vvvvv.|/  /
       /   | |     |   /
      /    | `^^^^^   /
     | /|  |         /
      / |    ___    |
         \\  |   |   |
         |  |   |   |
          \\._\\   \\._\ 
    RAWRRR, {username} mengeluarkan monster {user_monster[input_monst]['Name']} !!!
    '''
    print(gambar)
    print()

    user_choosen_monster=user_monster[input_monst]

    printDict(user_choosen_monster) 
    return user_choosen_monster, base_hp 

def war(user_potion, user_choosen_monster, enemy_monster, base_hp):
    drink_strength=False
    drink_def=False
    drink_heal=False
    turn = 0
    while int(user_choosen_monster['HP'])>0 and int(enemy_monster["HP"])>0: #Battle
        loop_again=True   #-->untuk menentukan apakah user tdk jadi memilih potion
        turn+=1
        move=False
        # use_dict=None
        choosen_potion=None
        if turn%2==1:
            use_dict=user_choosen_monster
            vict_dict=enemy_monster
            while choosen_potion==None: #deklarasi choosen_potion none di awalan agar bisa melakukan opsi cancel pada saat memilih potion dan memilih perintah yang lain
                print()
                print(f"============ TURN {turn} ({use_dict['Name']}) ============")
                print("1. Attack")
                print("2. Use Potion")
                print("3. Quit")
                move_input=int(input("Pilih perintah: "))
                print()
                while not move:
                    if move_input==1:
                        enemy_monster=attack(use_dict,vict_dict)
                        move=True
                        loop_again=False
                        break
                    elif move_input==2 :
                        choosen_potion=input_potion(user_potion)
                        if choosen_potion==None: #jika user memilih meng cancel use potion dan akan kembali menginput perintah yang dia inginkan
                            break
                        loop_again=False
                        potion_name=user_potion[choosen_potion]['Type']
                        user_choosen_monster=usepotion(user_potion, user_choosen_monster, base_hp, drink_strength,drink_def,drink_heal,choosen_potion)
                        if potion_name=='STRENGTH' and not drink_strength :   #mengubah kondisi agar setiap jenis potion hanya bisa 1 kali penggunaan
                            drink_strength=True
                            user_potion[choosen_potion]['Quantity']=str(int(user_potion[choosen_potion]['Quantity'])-1)
                        elif potion_name=='RESILIENCE' and not drink_def :
                            drink_def=True
                            user_potion[choosen_potion]['Quantity']=str(int(user_potion[choosen_potion]['Quantity'])-1)
                        elif potion_name=='HEALING' and not drink_heal :
                            user_potion[choosen_potion]['Quantity']=str(int(user_potion[choosen_potion]['Quantity'])-1)
                            drink_heal=True
                        move=True
                    elif move_input==3:
                        move=True
                        print("Anda berhasil kabur dari BATTLE!")
                        return
                    else:
                        print("Pilihan nomor tidak tersedia!")
                if loop_again: #jika user memilihcancel maka loop dilanjut agar user dapat memilih perintah lain
                    continue
                else:
                    break #jika user memilih potion yang dia ingini maka lanjut ke turn musuh
        else:
            use_dict = enemy_monster
            vict_dict = user_choosen_monster
            print()
            print(f"============ TURN {turn} ({use_dict['Name']}) ============")
            user_choosen_monster=attack(use_dict,vict_dict)
            print()
    return user_potion

def enemy_summon(monster_data, stage=RNG(0,4) ):
    gambar = '''
           _/\----/\   
          /         \     /\\
         |  O    O   |   |  |
         |  .vvvvv.  |   |  |
         /  |     |   \\  |  |
        /   `^^^^^'    \\ |  |
      ./  /|            \\|  |_
     /   / |         |\\__     /
     \\  /  |         |   |__|
      `'   |  _      |
        _.-'-' `-'-'.'_
   __.-'               '-.__
    '''
    print(gambar)
    level_monst=stage
    monst=RNG(0,len(monster_data['id'])-1)

    enemy_monster={
        'Name':monster_data['type'][monst],
        'ATK_Power':None,
        'DEF_Power':None,
        'HP':None,
        'level': level_monst
    }


    base_enemy_monster=[]   #untuk menampung --> [atk,def,hp]

    #mencari nama yang sama dengan yang di input user di file monster
    base_enemy_monster.append(monster_data['atk_power'][monst])        #menambahkan base stats dari monster yang di pilih user
    base_enemy_monster.append(monster_data['def_power'][monst])
    base_enemy_monster.append(monster_data['hp'][monst])

    enemy_monster['ATK_Power'] = calc_stats(int(enemy_monster['level']), int(base_enemy_monster[0])) 
    enemy_monster['DEF_Power'] = calc_stats(int(enemy_monster['level']), int(base_enemy_monster[1]))
    enemy_monster['HP']=calc_stats(int(enemy_monster['level']), int(base_enemy_monster[2]))

    printDict(enemy_monster)
    print()
    print(f"RAWRRR, Monster {enemy_monster['Name']} telah muncul !!!")

    return enemy_monster





def battle(username, user_monster, user_potion, monster_data,current_oc=0):

    enemy_monster = enemy_summon(monster_data)
    user_choosen_monster, base_hp = user_summon(user_monster, username, monster_data)    
    user_potion = war(user_potion, user_choosen_monster, enemy_monster,base_hp)

    if int(user_choosen_monster["HP"])<=0:
        print()
        print(f"Yahhh, Anda dikalahkan monster {enemy_monster['Name']}. Jangan menyerah, coba lagi !!!")
        print()
    else:
        oc_gained = RNG(5,30)
        current_oc+=oc_gained
        print()
        print(f"Selamat, Anda berhasil mengalahkan monster {enemy_monster['Name']} !!!")
        print(f"Total OC yang diperoleh: {oc_gained}")
        print()
        print()
    return user_potion, current_oc

def arena(username, user_monster, user_potion, monster_data,current_oc=0):

    user_choosen_monster,base_hp = user_summon(user_monster, username, monster_data)
    win = True
    stage = 0
    while win and stage<5:
        stage+=1
        print(f"============= STAGE {stage} =============")
        enemy_monster = enemy_summon(monster_data,stage)
        user_potion = war(user_potion, user_choosen_monster, enemy_monster, base_hp)
        if int(user_choosen_monster["HP"])==0:
            print(f"Yahhh, Anda dikalahkan monster {enemy_monster['Name']}. Jangan menyerah, coba lagi !!!")
            print(f"GAME OVER! Sesi latihan berakhir pada stage {stage}!")
            win = False
        else:
            oc_gained = 10+20*stage
            current_oc+=oc_gained
            print(f"Selamat, Anda berhasil mengalahkan monster {enemy_monster['Name']} !!!")
            print(f"STAGE CLEARED! Anda akan mendapatkan {oc_gained} OC pada sesi ini!")
            print(f"Memulai stage berikutnya...")
    return user_potion,current_oc
