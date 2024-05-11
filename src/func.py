import time
from globevar import user_data,monster_inventory_data,item_inventory_data,monster_data,arr_item,sudah_login
from utils import search_index,parser,printDict,fetch_data

#REALISASI FUNGSI-FUNGSI

def get_seed():
    """Menghasilkan seed berdasarkan waktu saat ini."""
    return int(time.time())

# Fungsi untuk Linear Congruential Method
def linear_congruential_method_int(seed, a, c, m, n, min_val, max_val):
    """
    Menghasilkan urutan bilangan bulat acak semu dalam rentang tertentu
    menggunakan Metode Kongruensial Linier (LCM).
    
    Parameter
        seed (int): Nilai benih awal.
        a (int): Pengali.
        c (int): Kenaikan.
        m (int): Modulus.
        n (int): Jumlah angka acak yang akan dihasilkan.
        min_val (int): Nilai minimum dari rentang.
        max_val (int): Nilai maksimum dari rentang.
        
    Pengembalian:
        daftar Daftar bilangan bulat acak semu dalam rentang yang ditentukan.
    """

    random_numbers = []
    x = seed
    
    for _ in range(n):
        x = (a * x + c) % m
        random_numbers.append(min_val + (x % (max_val - min_val + 1)))
    
    return random_numbers

# Fungsi untuk menghasilkan nilai integer random
def RNG(min_val, max_val): 
    # Mendapatkan seed secara acak
    seed = get_seed() 

    a = 1103515245
    c = 12345
    m = 2**31
    n = 10
    random_sequence = linear_congruential_method_int(seed, a, c, m, n, min_val, max_val)

    # Mengambil satu nilai acak dari array yang dihasilkan
    # Menggunakan algoritma LCM untuk memilih indeks acak dari array
    random_index = linear_congruential_method_int(seed, a, c, m, 1, 0, n-1)[0]
    random_value = random_sequence[random_index]
    return random_value

def register_user(): #F01
    global sudah_login, user_data, username
    if sudah_login: #ngecek udah login atau belum
        print("Register gagal!")
        print("Anda telah login dengan username Purry, silahkan lakukan “LOGOUT” sebelum melakukan login kembali")
        print()
    else:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        # ngecek username valid atau engga
        if not username.isalnum() and "_" not in username and "-" not in username:
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
            return

        # ngecek udah dipake atau belum
        if username in user_data['username']:
            print(f"Username {username} sudah terpakai, silahkan gunakan username lain!")
            return

        # registrasi, isi data
        user_data["id"].append(str(len(user_data["id"])+1)) 
        user_data["username"].append(username)
        user_data["password"].append(password)
        user_data["role"].append("agent")
        user_data["oc"].append("0")

        # pilih monster
        print("Silahkan pilih salah satu monster sebagai monster awalmu.")
        print("1. Charizard")
        print("2. Bulbasaur")
        print("3. Aspal")
        monster_choice = int(input("Monster pilihanmu: "))

        # Print welcome
        monsters = ["Charizard", "Bulbasaur", "Aspal"]
        print(f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monsters[monster_choice-1]}!")
        sudah_login = True

def login_user(): #F02
    global sudah_login, username
    if sudah_login:
        print("Login gagal!")
        print("Anda telah login dengan username Purry, silahkan lakukan \“LOGOUT\” sebelum melakukan login kembali")
    else:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print()
        if username in user_data['username']:
            index = search_index(user_data, "username", username)
            if user_data["password"][index]==password:
                print(f"Selamat datang, Agent {username}!")
                print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
                print()
                sudah_login = True
            else:
                print("Password salah!")
                print()
        else:
            print("Username tidak terdaftar!")
            print()

def logout():
    global sudah_login
    if sudah_login:
        sudah_login = False
    else:
        print('Logout gagal!')
        print('Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout')

def inventory():#F07
    global sudah_login, username
    if sudah_login:
        index = search_index(user_data, "username", username) #cari index dimana username berada
        current_user_id = user_data["id"][index] #cari nilai id dengan index yang sama dengan username
        print(f"=======INVENTORY LIST (User ID: {current_user_id})=======")
        print(f"Jumlah O.W.C.A. Coin-mu sekarang {900}.")

        id = 1
        inventory = {}
        for i in range(len(monster_inventory_data["user_id"])): #iterasi semua data pada monster_inventory
            if monster_inventory_data["user_id"][i]==current_user_id:
                monster_name = monster_data["type"][i]
                monster_level = monster_inventory_data["level"][i] 
                monster_hp = monster_data["hp"][i]
                monster_atk = monster_data["atk_power"][i]
                monster_def = monster_data["def_power"][i]

                print(f"{id}. Monster (Name: {monster_name}, Lvl: {monster_level}, HP: {monster_hp})")

                inventory[id] = ['Monster',
                                 f"Name      : {monster_name}",
                                 f"ATK Power : {monster_atk}",
                                 f"DEF Power : {monster_def}",
                                 f"HP        : {monster_hp}",
                                 f"Level     : {monster_level}"]

                id+=1


        for i in range(len(item_inventory_data["user_id"])): #iterasi semua data pada item_inventory
            if item_inventory_data["user_id"][i]==current_user_id:
                item_type = item_inventory_data["type"][i]
                item_quantity = item_inventory_data["quantity"][i]


                print(f"{id}. Potion (Type: {item_type}, Qty: {item_quantity})")

                inventory[id] = ['Potion',
                                 f"Type    : {item_type}", 
                                 f"Quantity: {item_quantity}"]

                id+=1
                
        print()
        pilihan = input("Ketikkan id untuk menampilkan detail item: ")
        print()
        while pilihan!=">>> KELUAR":
            if int(pilihan)<=(id-1):
                for i in inventory[int(pilihan)]:
                    print(i)
            else:
                print("Tidak dapat menampilkan detail item")

            print()
            pilihan = input("Ketikkan id untuk menampilkan detail item: ")
            print()

def calc_stats(level:int, arr_base_stats:list):
    arr_stats=[]
    for stats in arr_base_stats:
        battle_stats=int(stats)+(level-1)*0.1*int(stats)
        arr_stats.append(battle_stats)
    return arr_stats            #output --> [atk,def,hp]
    

def logout():
    global sudah_login
    if sudah_login:
        sudah_login = False
    else:
        print('Logout gagal!')
        print('Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout')


def make_arr(file_name):
    with open(f'{file_name}', 'r') as file:
        next(file)
        arr=[]
        for line in file:
            b=parser(line)
            arr.append(b)
    return arr

def SPLIT (sentence, pemisah=','):
    arr=[]
    splitted=""
    for char in sentence:
        if char==pemisah:
            arr=arr+[splitted]
            splitted=""
        if char!=pemisah:
            splitted=splitted+char
    arr=arr+[splitted]
    return arr

arr_glob_monst=make_arr('../main/data/monster.csv')
arr_monst_inventory=make_arr('../main/data/monster_inventory.csv')
arr_item=make_arr('../main/data/item_inventory.csv')

def make_inventory_list(id:str,arr_monst_invent:list,arr_glob_monster:list,arr_item:list):
    array_user_monst=[]
    array_user_potion=[]
    for elem in arr_monst_invent:
        if elem[0]==id:
            for monster in arr_glob_monster:
                if monster[0]==elem[1]:
                    kalimat=f"{monster[1]},{elem[2]}" #-->nama,level
                    array_user_monst.append(SPLIT(kalimat))
    for elem in arr_item:
        if elem[0]==id:
            sen=f"{elem[1]},{elem[2]}"#-->type,qty
            array_user_potion.append(SPLIT(sen))
    return array_user_monst,array_user_potion


def battle(id,arr_monst_invent,glob_monst,arr_item):
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
    monst=RNG(0,4)
    level_monst=RNG(1,5)

    monster_arr,potion_array=make_inventory_list(id,arr_monst_invent,glob_monst,arr_item)

    dict_enemy_monst={
        'Name':[monster_data['type'][monst]],
        'Atk':[],
        'Def':[],
        'Hp':[],
        'level': [level_monst]
    }
    base_monst=[]
    for elem in arr_glob_monst:
        if elem[1]==monster_data['type'][monst]: #mencari nama yang sama dengan yang di input user di file monster
            base_monst.append(elem[2])        #menambahkan base stats dari monster yang di pilih user
            base_monst.append(elem[3])
            base_monst.append(elem[4])
            break

    stats_monster=calc_stats(int(dict_enemy_monst['level'][0]), base_monst) #output --> [atk,def,hp]
    dict_enemy_monst['Atk'].append(stats_monster[0]) #menambahkan stats monster yang digunakan oleh user
    dict_enemy_monst['Def'].append(stats_monster[1])
    dict_enemy_monst['Hp'].append(stats_monster[2])

    printDict(dict_enemy_monst)
    print(f"RAWRRR, Monster {dict_enemy_monst['Name'][0]} telah muncul !!!")
    print("============ MONSTER LIST ============")

    for i in range (len(monster_arr)):
        print(f"{i+1}. {monster_arr[i][0]}")
    input_monst=None
    done_choosing=False
    base=[]
    while not done_choosing:
        input_monst=int(input("Pilih monster untuk bertarung: "))
        if input_monst>len(monster_arr):
            print("Pilihan nomor tidak tersedia!")
        else:
            done_choosing=True
    input_monst=input_monst-1
    for elem in arr_glob_monst:
        if elem[1]==monster_arr[input_monst][0]: #mencari nama yang sama dengan yang di input user di file monster
            base.append(elem[2])        #menambahkan base stats dari monster yang di pilih user
            base.append(elem[3])
            base.append(elem[4])
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
    RAWRRR, Agent X mengeluarkan monster {monster_arr[input_monst][0]} !!!
    '''
    print(gambar)
    print()
    dict_user_monst={
        'Name':[monster_arr[input_monst][0]],
        'Atk':[],
        'Def':[],
        'Hp':[],
        'level': [monster_arr[input_monst-1][1]]
    }

    stats=calc_stats(int(dict_user_monst['level'][0]), base) #output --> [atk,def,hp]
    dict_user_monst['Atk'].append(stats[0]) #menambahkan stats monster yang digunakan oleh user
    dict_user_monst['Def'].append(stats[1])
    dict_user_monst['Hp'].append(stats[2])

    printDict(dict_user_monst)    
    index=0
    drink_strength=False
    drink_def=False
    drink_heal=False
    while int(dict_user_monst["Hp"][0])>0 and int(dict_enemy_monst["Hp"][0])>0: #Battle
        loop_again=True   #-->untuk menentukan apakah user tdk jadi memilih potion
        index+=1
        move=False
        use_dict=None
        pilih=None
        if index%2==1:
            use_dict=dict_user_monst
            vict_dict=dict_enemy_monst
            while pilih==None: #deklarasi pilih none di awalan agar bisa melakukan opsi cancel pada saat memilih potion dan memilih perintah yang lain
                print(f"============ TURN {index} ({use_dict['Name'][0]}) ============")
                print("1. Attack")
                print("2. Use Potion")
                print("3. Quit")
                move_input=int(input("Pilih perintah: "))
                print()
                while not move:
                    if move_input==1:
                        dict_enemy_monst=attack(use_dict,vict_dict)
                        move=True
                        loop_again=False
                        break
                    elif move_input==2 :
                        pilih=input_potion(potion_array)
                        if pilih==None: #jika user memilih meng cancel use potion dan akan kembali menginput perintah yang dia inginkan
                            break
                        loop_again=False
                        potion_name=name_of_potion(pilih,potion_array) 
                        dict_user_monst=usepotion(potion_array, dict_user_monst, base, drink_strength,drink_def,drink_heal,pilih)
                        if potion_name=='STRENGTH' and not drink_strength :   #mengubah kondisi agar setiap jenis potion hanya bisa 1 kali penggunaan
                            drink_strength=True
                            potion_array[pilih-1][1]=str(int(potion_array[pilih-1][1])-1)
                        elif potion_name=='RESILIENCE' and not drink_def :
                            drink_def=True
                            potion_array[pilih-1][1]=str(int(potion_array[pilih-1][1])-1)
                        elif potion_name=='HEALING' and not drink_heal :
                            potion_array[pilih-1][1]=str(int(potion_array[pilih-1][1])-1)
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
            use_dict=dict_enemy_monst
            vict_dict=dict_user_monst
            print()
            print(f"============ TURN {index} ({use_dict['Name'][0]}) ============")
            dict_user_monst=attack(use_dict,vict_dict)
            print()

    if int(dict_user_monst["Hp"][0])==0:
        print(f"Yahhh, Anda dikalahkan monster {dict_enemy_monst['Name'][0]}. Jangan menyerah, coba lagi !!!")
    else:
        oc = RNG(5,30)
        print(f"Selamat, Anda berhasil mengalahkan monster {dict_enemy_monst['Name'][0]} !!!")
        print(f"Total OC yang diperoleh:{oc}")


def attack(dictionary:dict,victim:dict):
    penentu=RNG(-30,30) #mengambil range dari +-30
    atk_dmg=int(dictionary['Atk'][0])+int((penentu/100)*int(dictionary['Atk'][0])) #pembulatan ke bawah
    victim['Hp'][0]=str(int(victim['Hp'][0])-atk_dmg-int((int(victim['Def'][0])/100)*atk_dmg))
    if int(victim["Hp"][0])<0:
        victim["Hp"][0]='0'
    printDict(victim)
    return victim

def usepotion(potion_array:list, dict_user_monst:dict, base, cond_str: bool, cond_def:bool, cond_heal:bool,pilih:int):
    move=False
    while not move:
        if pilih<=len(potion_array):
            potion_name=name_of_potion(pilih,potion_array)
            arr=[dict_user_monst['Atk'][0]]+[dict_user_monst['Def'][0]]+[dict_user_monst['Hp'][0]] #membuat array stast monster
            if potion_name=='STRENGTH' and not cond_str:
                dict_user_monst['Atk'][0]=str(potion(potion_name, arr, base )) #mengupdate banyaknya potion yang ada setelah digunakan
            elif potion_name=='RESILIENCE' and not cond_def:
                dict_user_monst['Def'][0]=str(potion(potion_name, arr, base ))#mengupdate banyaknya potion yang ada setelah digunakan
            elif potion_name=='HEALING' and not cond_heal:
                dict_user_monst['Hp'][0]=str(potion(potion_name, arr, base ))#mengupdate banyaknya potion yang ada setelah digunakan
            else:
                print(f"Kamu mencoba memberikan ramuan ini kepada {dict_user_monst['Name']}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
            return dict_user_monst
        elif pilih==len(potion_array)+1:
            return
        else:
            print("Pilihan nomor tidak tersedia!")

def name_of_potion(pilih:int ,potion_array:list):
    chose=pilih-1       #mengindentifikasi nama potion yang dipilih
    potion_name=str(potion_array[chose][0])
    potion_name=potion_name.upper()
    return potion_name

def potion(potion:str, arr:list, base_stats:list):      #arr= [atk,def,hp]
    if potion=='STRENGTH':
        new= int(arr[0])+0.05*int(arr[0])
        print("Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi Pikachow dan gerakannya menjadi lebih cepat dan mematikan.")
        return int(new)
    elif potion=='RESILIENCE':
        new= int(arr[1])+0.05*int(arr[1])
        print(new)
        print("Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar Pikachow yang membuatnya terlihat semakin tangguh dan sulit dilukai.")
        return int(new)
    elif potion=='HEALING':
        hp= int(arr[2])+0.25*int(base_stats[2])
        print("Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh Pikachow sembuh dengan cepat. Dalam sekejap, Pikachow terlihat kembali prima dan siap melanjutkan pertempuran.")
        if int(arr[2])>hp:
            return int(hp) #jika heal melebihi hp monster saat ini
        else:
            return int(arr[2])
        
def input_potion(potion_array:list):
    print("============ POTION LIST ============")
    index=1
    for nomor, elem in enumerate (potion_array):
        print(f"{nomor+1}. {elem[0]} Potion (Qty:{elem[1]})")
        index=nomor+1
    print(f"{index+1}. Cancel")
    pilih = int(input("Pilih perintah: "))
    print()
    while pilih>=index+1:
        if pilih>index+1:
            print("Pilihan nomor tidak tersedia!")
        elif pilih==index+1:
            return None
        pilih = int(input("Pilih perintah: "))
    return pilih


monster_data = fetch_data("../main/data/monster.csv")
def shop_management():
    shop = True
    monster_shop_data = fetch_data("../main/data/monster_shop.csv")
    item_shop_data = fetch_data("../main/data/item_shop.csv")
    print("Irasshaimase! Selamat datang kembali, Mr. Monogram!")
    while shop==True:
        aksi = input(">>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")
        if aksi=="lihat":
            lihat_apa = input(">>> Mau lihat apa? (monster/potion): ")
            if lihat_apa=="monster":
                print("ID | Type | ATK Power | DEF Power | HP | Stok | Harga")
                for i in range(len(monster_shop_data["monster_id"])):
                    id = monster_shop_data["monster_id"][i]
                    index = search_index(monster_data, "id",id)
                    print(f"{id} | {monster_data['type'][index]} | {monster_data['atk_power'][index]} | {monster_data['def_power'][index]} | {monster_data['hp'][index]} | {monster_shop_data['stock'][i]} | {monster_shop_data['price'][i]}")
            elif lihat_apa=="potion":
                print("ID | Type | Stok | Harga")
                for i in range(len(item_shop_data["type"])):
                    print(f" {i+1} | {item_shop_data['type'][i]} | {item_shop_data['stock'][i]} | {item_shop_data['price'][i]}")
        elif aksi=="tambah":
            tambah_apa = input(">>> Mau tambah apa? (monster/potion): ")
            
            if tambah_apa=="monster":
                monster_not_in_shop_data = { #inisiasi untuk data monster yang tidak ada pada shop
                    "id":[],
                    "type":[],
                    "atk_power":[],
                    "def_power":[],
                    "hp":[]
                }
                for i in range(len(monster_data["id"])): #isi data monster yang tidak ada pada shop
                    if not(monster_data["id"][i] in monster_shop_data["monster_id"]):
                        monster_not_in_shop_data["id"].append(monster_data["id"][i])
                        monster_not_in_shop_data["type"].append(monster_data["type"][i])
                        monster_not_in_shop_data["atk_power"].append(monster_data["atk_power"][i])
                        monster_not_in_shop_data["def_power"].append(monster_data["def_power"][i])
                        monster_not_in_shop_data["hp"].append(monster_data["hp"][i])

                for i in range(len(monster_not_in_shop_data["id"])): #print data monster yang tidak ada pada shop
                    print(f"{monster_not_in_shop_data['id'][i]} | {monster_not_in_shop_data['type'][i]} | {monster_not_in_shop_data['atk_power'][i]} | {monster_not_in_shop_data['def_power'][i]} | {monster_not_in_shop_data['hp'][i]} | ")

                
                if len(monster_not_in_shop_data["id"])==0:
                    print("Tidak ada monster yang dapat ditambahkan!")
                else: #isi data monster yang tidak ada pada shop
                    while True:
                        id = input(">>> Masukkan id monster: ")
                        stock = input(">>> Masukkan stok awal: ")
                        price = input(">>> Masukkan harga: ")
                        if (id in monster_not_in_shop_data["id"]):
                            break
                        else: print("Masukan salah! id tidak ditemukan!")

                    #update monster di shop
                    monster_shop_data["monster_id"].append(id)
                    monster_shop_data["stock"].append(stock)
                    monster_shop_data["price"].append(price)

                    index = search_index(monster_not_in_shop_data, 'id', id)
                    print(f"{monster_not_in_shop_data['type'][index]} telah berhasil ditambahkan ke dalam shop!")


            elif tambah_apa=="potion":
                item_not_in_shop_data = { #inisiasi untuk data item yang tidak ada pada shop
                    "type":[],
                }
                for i in range(len(item_inventory_data["type"])): #isi data monster yang tidak ada pada shop
                    if not(item_inventory_data["type"][i] in item_shop_data["type"]):
                        item_not_in_shop_data["type"].append(item_inventory_data["type"][i])

                for i in range(len(item_not_in_shop_data["type"])): #print data monster yang tidak ada pada shop
                    print(f"{i+1} | {item_not_in_shop_data['type'][i]} ")

                if len(item_not_in_shop_data["type"])==0:
                    print("Tidak ada item yang dapat ditambahkan!")
                else: #isi data item yang tidak ada pada shop
                    while True:
                        id = input(">>> Masukkan id potion: ")
                        tipe = item_not_in_shop_data["type"][id]
                        stock = input(">>> Masukkan stok awal: ")
                        price = input(">>> Masukkan harga: ")
                        if (tipe in item_not_in_shop_data["type"]):
                            break
                        else: print("Masukan salah! id tidak ditemukan!")
                    #isi data item yang tidak ada pada shop
                    

                    #update item di shop
                    item_shop_data["type"].append(tipe)
                    item_shop_data["stock"].append(stock)
                    item_shop_data["price"].append(price)
                    print(item_shop_data)


                    print(f"{item_not_in_shop_data['type'][tipe]} telah berhasil ditambahkan ke dalam shop!")


        elif aksi=="ubah":
            ubah_apa = input(">>> Mau ubah apa? (monster/potion): ")
            
            if ubah_apa=="monster":
                print("ID | Type | ATK Power | DEF Power | HP | Stok | Harga")
                for i in range(len(monster_shop_data["monster_id"])):
                    id = monster_shop_data["monster_id"][i]
                    index = search_index(monster_data, "id",id)
                    print(f"{id} | {monster_data['type'][index]} | {monster_data['atk_power'][index]} | {monster_data['def_power'][index]} | {monster_data['hp'][index]} | {monster_shop_data['stock'][i]} | {monster_shop_data['price'][i]}")
                
                if len(monster_shop_data["monster_id"])==0:
                    print("Tidak ada monster yang dapat diubah!")
                else: #isi data monster yang tidak ada pada shop
                    while True:
                        id = input(">>> Masukkan id monster: ")
                        stock = input(">>> Masukkan stok baru: ")
                        price = input(">>> Masukkan harga baru: ")
                        if (id in monster_shop_data["monster_id"] and (stock or price)):
                            break
                        else: print("Masukan salah! silahkan ulang!")

                    #update monster di shop
                    if stock:
                        monster_shop_data["stock"][int(id)-1] = stock
                    if price:
                        monster_shop_data["price"][int(id)-1] = price

                    # index = search_index(monster_shop_data, 'monster_id', id)
                    
                    if stock and price:
                        print(f"{monster_data['type'][int(id)-1]} telah berhasil diubah ke dalam shop dengan stok baru {stock} dan harga baru {price}!")
                    elif stock:
                        print(f"{monster_data['type'][int(id)]-1} telah berhasil diubah ke dalam shop dengan stok baru {stock}!")
                    elif price:
                        print(f"{monster_data['type'][int(id)]-1} telah berhasil diubah ke dalam shop dengan harga baru {price}!")

            elif ubah_apa=="potion":
                print("ID | Type | Stok | Harga")
                for i in range(len(item_shop_data["type"])):
                    tipe = item_shop_data["type"][i]
                    print(f"{i+1} | {item_shop_data['type'][i]} | {item_shop_data['stock'][i]} | {item_shop_data['price'][i]}")
                
                if len(item_shop_data["type"])==0:
                    print("Tidak ada item yang dapat diubah!")
                else: #isi data item yang tidak ada pada shop
                    while True:
                        id = input(">>> Masukkan id item: ")
                        stock = input(">>> Masukkan stok baru: ")
                        price = input(">>> Masukkan harga baru: ")
                        if (int(id) <= len(item_shop_data["type"]) and (stock or price)):
                            break
                        else: print("Masukan salah! silahkan ulang!")

                    #update item di shop
                    if stock:
                        item_shop_data["stock"][int(id)-1] = stock
                    if price:
                        item_shop_data["price"][int(id)-1] = price

                    # id = search_index(item_shop_data, 'item_id', id)
                    
                    if stock and price:
                        print(f"{item_shop_data['type'][int(id)-1]} telah berhasil diubah ke dalam shop dengan stok baru {stock} dan harga baru {price}!")
                    elif stock:
                        print(f"{item_shop_data['type'][int(id)]-1} telah berhasil diubah ke dalam shop dengan stok baru {stock}!")
                    elif price:
                        print(f"{item_shop_data['type'][int(id)]-1} telah berhasil diubah ke dalam shop dengan harga baru {price}!")
        
        elif aksi=="hapus":
            hapus_apa = input(">>> Mau hapus apa? (monster/potion): ")
            if hapus_apa=="monster":
                print("ID | Type | ATK Power | DEF Power | HP | Stok | Harga")
                for i in range(len(monster_shop_data["monster_id"])):
                    id = monster_shop_data["monster_id"][i]
                    index = search_index(monster_data, "id",id)
                    print(f"{id} | {monster_data['type'][index]} | {monster_data['atk_power'][index]} | {monster_data['def_power'][index]} | {monster_data['hp'][index]} | {monster_shop_data['stock'][i]} | {monster_shop_data['price'][i]}")

                if len(monster_shop_data["monster_id"])==0:
                    print("Tidak ada monster yang dapat dihapus!")
                else: #isi data monster yang tidak ada pada shop
                    while True:
                        id = input(">>> Masukkan id monster: ")
                        if (id in monster_shop_data["monster_id"]):
                            index = search_index(monster_data, "id",id)
                            monster_name = monster_data["type"][int(index)]
                            yakin = input(f">>> Apakah anda yakin ingin menghapus {monster_name} dari shop (y/n)? ")
                            if yakin == "y":
                                index = search_index(monster_data, "id", id)
                                print(f"{monster_data['type'][index]} telah berhasil dihapus dari shop!")
                                
                                monster_shop_data["monster_id"].pop(int(id)-1)
                                monster_shop_data["stock"].pop(int(id)-1)
                                monster_shop_data["price"].pop(int(id)-1)
                                break
                        else: print("Masukan salah! silahkan ulang!")
            elif hapus_apa=="potion":
                print("ID | Type | Stok | Harga")
                for i in range(len(item_shop_data["type"])):
                    print(f"{i+1} | {item_shop_data['type'][i]} | {item_shop_data['stock'][i]} | {item_shop_data['price'][i]}")

                if len(item_shop_data["type"])==0:
                    print("Tidak ada item yang dapat dihapus!")
                else: #isi data item yang tidak ada pada shop
                    while True:
                        id = input(">>> Masukkan id item: ")
                        if (int(id) <=len(item_shop_data["type"])):
                            item_name = item_shop_data["type"][int(id)-1]
                            yakin = input(f">>> Apakah anda yakin ingin menghapus {item_name} dari shop (y/n)? ")
                            if yakin == "y":
                                print(f"{item_shop_data['type'][int(id)-1]} telah berhasil dihapus dari shop!")
                                item_shop_data["type"].pop(int(id)-1)
                                item_shop_data["stock"].pop(int(id)-1)
                                item_shop_data["price"].pop(int(id)-1)
                                break
                        else: print("Masukan salah! silahkan ulang!")

                    # index = search_index(monster_shop_data, 'monster_id', id)
                    
        elif aksi=="keluar":
            shop=False

    


        



    