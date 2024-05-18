import time
from utils import search_index,printDict,isallnumber,validate_input, in_game_validate_input

#REALISASI FUNGSI-FUNGSI



def register_user(id,username,user_monster,user_potion,sudah_login, user_data,monster_inventory_data, monster_data, item_inventory_data): #F01
    id = id if id!=0 else 0
    username = username if username!="" else ""
    user_potion = user_potion if user_potion!={} else {}
    user_monster = user_monster if user_monster!={} else {}
    if sudah_login: #ngecek udah login atau belum
        print("Register gagal!")
        print("Anda telah login dengan username Purry, silahkan lakukan “LOGOUT” sebelum melakukan login kembali")
        print()
        return sudah_login,username,id,user_data,user_monster,user_potion, monster_inventory_data
    else:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        # ngecek username valid atau engga
        if not validate_input(username):
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
            return sudah_login,username,id,user_data,user_monster,user_potion, monster_inventory_data
        # ngecek udah dipake atau belum
        elif username in user_data['username']:
            print(f"Username {username} sudah terpakai, silahkan gunakan username lain!")
            return sudah_login,username,id,user_data,user_monster,user_potion, monster_inventory_data
        else:
            # registrasi, isi data
            user_data["id"].append(str(len(user_data["id"])+1)) 
            user_data["username"].append(username)
            user_data["password"].append(password)
            user_data["role"].append("agent")
            user_data["oc"].append("0")

            # pilih monster
            print("Silahkan pilih salah satu monster sebagai monster awalmu.")
            print("1. Pikachow")
            print("2. Bulbu")
            print("3. Zeze")
            monster_choice = input("Monster pilihanmu: ")
            monster_choice = int(in_game_validate_input(monster_choice, 3, "Monster pilihanmu: "))

            # Print welcome
            monsters = ["Pikachow", "Bulbu", "Zeze"]
            print(f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster_data['type'][monster_choice-1]}!")
            sudah_login = True
            id = len(user_data["id"])
            user_monster, user_potion = separate_monster_item_inventory(make_inventory(id, monster_inventory_data, monster_data, item_inventory_data))
            user_monster[1] = {'Type': 'Monster',
                                'Name'      : monsters[monster_choice-1],
                                'ATK_Power' : monster_data['atk_power'][monster_choice-1],
                                'DEF_Power' : monster_data['def_power'][monster_choice-1],
                                'HP'        : monster_data['hp'][monster_choice-1],
                                'Level'     : '1'}
            
            monster_inventory_data["user_id"].append(str(id))
            monster_inventory_data["monster_id"].append(str(monster_choice))
            monster_inventory_data["level"].append('1')
            # print(user_monster)
            # print(monster_inventory_data)
            return sudah_login,username,id,user_data,user_monster,user_potion, monster_inventory_data

def login_user(id, username, is_admin, current_oc, sudah_login, user_data): #F02
    username = username if username!="" else ""
    current_oc = current_oc if current_oc!=0 else 0
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
                if user_data["role"]=="admin":
                    is_admin = True
                else:
                    is_admin = False
                sudah_login = True
                index = search_index(user_data, "username", username) #cari index dimana username berada
                id = user_data["id"][index]
                current_oc = user_data["oc"][index]
                
            else:
                print("Password salah!")
                print()
        else:
            print("Username tidak terdaftar!")
            print()
    return (sudah_login, username, is_admin, id, current_oc)

def logout_user(sudah_login):
    if sudah_login:
        sudah_login = False
        return sudah_login
    else:
        print('Logout gagal!')
        print('Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout')

def exit(program):
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    choice = input("Enter your choice: ")

    # if choice == "y":
    #     save()
    if choice == "n":
        program = False
    else:
        print("Invalid choice. Please try again", end="")
        for i in range(10):
            print(".", end="")
            time.sleep(0.1)
    return program




def inventory(id, current_oc, monster_inventory_data, monster_data, item_inventory_data):#F07
    
    print(f"=======INVENTORY LIST (User ID: {id})=======")
    print(f"Jumlah O.W.C.A. Coin-mu sekarang {current_oc}.")
    inventory = make_inventory(id, monster_inventory_data, monster_data, item_inventory_data)
    for key in inventory:
        if inventory[key]['Type']=='Monster':
            tipe=inventory[key]['Type']
            nama=inventory[key]['Name']
            lvl=inventory[key]['Level']
            hp=inventory[key]['HP']
            print(f"{key}. {tipe} (Name: {nama}, Lvl: {lvl}, HP: {hp}) ")
        else:
            tipe=inventory[key]['Type']
            potion_name=inventory[key]['Potion_Name']
            quantity=inventory[key]['Quantity']
            print(f"{key}. {tipe} (Type: {potion_name}, Qty: {quantity}) ")

    print()
    print("Ketikkan id untuk menampilkan detail item: ")
    pilihan = input(">>> ").upper()
    print()
    while pilihan!="KELUAR":
        if int(pilihan)<=(len(inventory)) and isallnumber(pilihan):
            printDict(inventory[int(pilihan)])
        else:
            print("Tidak dapat menampilkan detail item")

        print()
        print("Ketikkan id untuk menampilkan detail item: ")
        pilihan = input(">>> ").upper()
        print()

def calc_stats(level:int, base_stats:int):
    battle_stats=int(base_stats)+(level-1)*0.1*int(base_stats)
    return int(battle_stats)            #output --> [atk,def,hp]

def make_inventory(user_id, monster_inventory_data, monster_data, item_inventory_data):
    id=1
    inventory = {}
    for i in range(len(monster_inventory_data["user_id"])): #iterasi semua data pada monster_inventory

        if int(monster_inventory_data["user_id"][i])==int(user_id):
            monster_id = monster_inventory_data["monster_id"][i]
            index = search_index(monster_data, "id", monster_id)
            monster_name = monster_data["type"][index]
            monster_level = int(monster_inventory_data["level"][index])
            monster_hp = calc_stats(monster_level, int(monster_data["hp"][index]))
            monster_atk = calc_stats(monster_level, int(monster_data["atk_power"][index]))
            monster_def = calc_stats(monster_level, int(monster_data["def_power"][index]))

            inventory[id] = {'Type': 'Monster',
                                'Name'      : monster_name,
                                'ATK_Power' : monster_atk,
                                'DEF_Power' : monster_def,
                                'HP'        : monster_hp,
                                'Level'     : monster_level}

            id+=1


    for i in range(len(item_inventory_data["user_id"])): #iterasi semua data pada item_inventory
        if item_inventory_data["user_id"][i]==id:
            item_type = item_inventory_data["type"][i]
            item_quantity = item_inventory_data["quantity"][i]

            inventory[id] = {'Type': 'Potion',
                                'Potion_Name'    : item_type, 
                                'Quantity': item_quantity}

            id+=1
    return inventory


def shop_management(monster_data,monster_shop_data,item_shop_data, item_inventory_data):

    shop = True
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
                for i in range(len(item_inventory_data["type"])): #isi data potion yang tidak ada pada shop
                    if not(item_inventory_data["type"][i] in item_shop_data["type"]):
                        item_not_in_shop_data["type"].append(item_inventory_data["type"][i])

                for i in range(len(item_not_in_shop_data["type"])): #print data potion yang tidak ada pada shop
                    print(f"{i+1} | {item_not_in_shop_data['type'][i]} ")

                if len(item_not_in_shop_data["type"])==0:
                    print("Tidak ada item yang dapat ditambahkan!")
                else: #isi data item yang tidak ada pada shop
                    while True:
                        id = input(">>> Masukkan id potion: ")
                        tipe = item_not_in_shop_data["type"][int(id)-1]
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
            return monster_shop_data,item_shop_data

def separate_monster_item_inventory (inventory:dict):
    potion_dict:dict={}
    user_monster:dict={}

    id_monst=1
    id_potion=1
    for key in (inventory):
        if inventory[key]['Type']=='Potion':
            potion_dict[id_potion]={}
            potion_dict[id_potion]['Type']=inventory[key]['Potion_Name']
            potion_dict[id_potion]['Quantity']=inventory[key]['Quantity']
            id_potion=id_potion+1
        else:
            user_monster[id_monst]={}
            user_monster[id_monst]['Name']=inventory[key]['Name']
            user_monster[id_monst]['ATK_Power']=inventory[key]['ATK_Power']
            user_monster[id_monst]['DEF_Power']=inventory[key]['DEF_Power']
            user_monster[id_monst]['HP']=inventory[key]['HP']
            user_monster[id_monst]['Level']=inventory[key]['Level']
            id_monst=id_monst+1
    return user_monster,potion_dict

