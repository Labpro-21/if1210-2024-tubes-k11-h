from func import *


def battle(inventory:dict, username):
    global monster_data,monster_inventory_data
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
    level_monst=RNG(1,5)
    monst=RNG(0,len(monster_data['id'])-1)

    user_monster,potion_dict=sperate_monster_potion(inventory)

    dict_monst={
        'Name':monster_data['type'][monst],
        'ATK_Power':None,
        'DEF_Power':None,
        'HP':None,
        'level': level_monst
    }


    base_not_user_monster=[]   #untuk menampung --> [atk,def,hp]

#mencari nama yang sama dengan yang di input user di file monster
    base_not_user_monster.append(monster_data['atk_power'][monst])        #menambahkan base stats dari monster yang di pilih user
    base_not_user_monster.append(monster_data['def_power'][monst])
    base_not_user_monster.append(monster_data['hp'][monst])

    dict_monst['ATK_Power']=calc_stats(int(dict_monst['level']), int(base_not_user_monster[0])) 
    dict_monst['DEF_Power']=calc_stats(int(dict_monst['level']), int(base_not_user_monster[1]))
    dict_monst['HP']=calc_stats(int(dict_monst['level']), int(base_not_user_monster[2]))

    printDict(dict_monst)
    print()
    print(f"RAWRRR, Monster {dict_monst['Name']} telah muncul !!!")
    print("============ MONSTER LIST ============")

    for key in user_monster:
        print(f"{key}. {user_monster[key]['Name']}")
    input_monst=None
    done_choosing=False
    base_user_monster=[]
    while not done_choosing:
        input_monst=int(input("Pilih monster untuk bertarung: "))
        if input_monst>len(user_monster):
            print("Pilihan nomor tidak tersedia!")
        else:
            done_choosing=True

    for i, elem in enumerate (monster_data['type']):
        if elem[i]==user_monster[input_monst]['Name']: #mencari nama yang sama dengan yang di input user di file monster
            base_user_monster.append(monster_data['atk_power'][i])        #menambahkan base stats dari monster yang di pilih user
            base_user_monster.append(monster_data['def_power'][i])
            base_user_monster.append(monster_data['hp'][i])
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

    dict_user_monst=user_monster[input_monst]

    printDict(dict_user_monst)    
    index=0
    drink_strength=False
    drink_def=False
    drink_heal=False

    while int(dict_user_monst['HP'])>0 and int(dict_monst["HP"])>0: #Battle
        loop_again=True   #-->untuk menentukan apakah user tdk jadi memilih potion
        index+=1
        move=False
        use_dict=None
        pilih=None
        if index%2==1:
            use_dict=dict_user_monst
            vict_dict=dict_monst
            while pilih==None: #deklarasi pilih none di awalan agar bisa melakukan opsi cancel pada saat memilih potion dan memilih perintah yang lain
                print()
                print(f"============ TURN {index} ({use_dict['Name']}) ============")
                print("1. Attack")
                print("2. Use Potion")
                print("3. Quit")
                move_input=int(input("Pilih perintah: "))
                print()
                while not move:
                    if move_input==1:
                        dict_monst=attack(use_dict,vict_dict)
                        move=True
                        loop_again=False
                        break
                    elif move_input==2 :
                        pilih=input_potion(potion_dict)
                        if pilih==None: #jika user memilih meng cancel use potion dan akan kembali menginput perintah yang dia inginkan
                            break
                        loop_again=False
                        potion_name=potion_dict[pilih]['Type']
                        dict_user_monst=usepotion(potion_dict, dict_user_monst, base_user_monster, drink_strength,drink_def,drink_heal,pilih)
                        if potion_name=='STRENGTH' and not drink_strength :   #mengubah kondisi agar setiap jenis potion hanya bisa 1 kali penggunaan
                            drink_strength=True
                            potion_dict[pilih]['Quantity']=str(int(potion_dict[pilih]['Quantity'])-1)
                        elif potion_name=='RESILIENCE' and not drink_def :
                            drink_def=True
                            potion_dict[pilih]['Quantity']=str(int(potion_dict[pilih]['Quantity'])-1)
                        elif potion_name=='HEALING' and not drink_heal :
                            potion_dict[pilih]['Quantity']=str(int(potion_dict[pilih]['Quantity'])-1)
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
            use_dict=dict_monst
            vict_dict=dict_user_monst
            print()
            print(f"============ TURN {index} ({use_dict['Name']}) ============")
            dict_user_monst=attack(use_dict,vict_dict)
            print()

    if int(dict_user_monst["HP"])==0:
        print(f"Yahhh, Anda dikalahkan monster {dict_monst['Name']}. Jangan menyerah, coba lagi !!!")
    else:
        print(f"Selamat, Anda berhasil mengalahkan monster {dict_monst['Name']} !!!")
        print(f"Total OC yang diperoleh: {RNG(5,30)}")

def attack(dictionary:dict,victim:dict):
    penentu=RNG(-30,30) #mengambil range dari +-30
    atk_dmg=int(dictionary['ATK_Power'])+int((penentu/100)*int(dictionary['ATK_Power'])) #pembulatan ke bawah
    victim['HP']=str(int(victim['HP'])-atk_dmg-int((int(victim['DEF_Power'])/100)*atk_dmg))
    if int(victim["HP"])<0:
        victim["HP"]='0'
    printDict(victim)
    return victim

def usepotion(potion_dict:dict, dict_user_monst:dict, base, cond_str: bool, cond_def:bool, cond_heal:bool,pilih:int):
    move=False
    while not move:
        if pilih<=len(potion_dict):
            potion_name=str(potion_dict[pilih]['Type']).upper()
            print(dict_user_monst)
            arr=[dict_user_monst['ATK_Power']]+[dict_user_monst['DEF_Power']]+[dict_user_monst['HP']] #membuat array stast monster
            if potion_name=='STRENGTH' and not cond_str:
                dict_user_monst['ATK_Power']=str(potion(potion_name, arr, base )) #mengupdate banyaknya potion yang ada setelah digunakan
            elif potion_name=='RESILIENCE' and not cond_def:
                dict_user_monst['DEF_Power']=str(potion(potion_name, arr, base ))#mengupdate banyaknya potion yang ada setelah digunakan
            elif potion_name=='HEALING' and not cond_heal:
                dict_user_monst['HP']=str(potion(potion_name, arr, base ))#mengupdate banyaknya potion yang ada setelah digunakan
            else:
                print(f"Kamu mencoba memberikan ramuan ini kepada {dict_user_monst['Name']}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
            return dict_user_monst
        elif pilih==len(potion_dict)+1:
            return
        else:
            print("Pilihan nomor tidak tersedia!")

def potion(potion:str, arr:list, base_user_monster:list):      #arr= [atk,def,hp]
    if potion=='STRENGTH':
        new= int(arr[0])+0.05*int(arr[0])
        print("Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi Pikachow dan gerakannya menjadi lebih cepat dan mematikan.")
        return int(new)
    elif potion=='RESILIENCE':
        new= int(arr[1])+0.05*int(arr[1])
        print("Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar Pikachow yang membuatnya terlihat semakin tangguh dan sulit dilukai.")
        return int(new)
    elif potion=='HEALING':
        hp= int(arr[2])+0.25*int(base_user_monster[2])
        print("Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh Pikachow sembuh dengan cepat. Dalam sekejap, Pikachow terlihat kembali prima dan siap melanjutkan pertempuran.")
        if int(arr[2])>hp:
            return int(hp) #jika heal melebihi hp monster saat ini
        else:
            return int(arr[2])
        
def input_potion(potion_dict:dict):
    print("============ POTION LIST ============")
    index=1
    for elem in (potion_dict):
        print(f"{elem}. {potion_dict[elem]['Type']} Potion (Qty:{potion_dict[elem]['Quantity']})")
        index+=1
    print(f"{index}. Cancel")
    pilih = int(input("Pilih perintah: "))
    print()
    while pilih>=index:
        if pilih>index:
            print("Pilihan nomor tidak tersedia!")
        elif pilih==index:
            return None
        pilih = int(input("Pilih perintah: "))
    return pilih
