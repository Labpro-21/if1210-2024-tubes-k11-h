import time
import os
from utils import search_index
def ClearScreen():
    if os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Linux and macOS
        os.system('clear')

def beli_monster(monster_data, user_monster, monster_shop_data, user_oc):

    pilih_monster = int(input("Masukkan ID monster: "))
    
    user_monster_name = []
    for i in range(1, len(user_monster)+1):
        user_monster_name.append(user_monster[i]["Name"])  #menambahkan semua nama monster di inventory user ke array

    user_monster_id = []
    for i in range(len(user_monster_name)):
        index = search_index(monster_data,"type", user_monster_name[i]) #mencari index di monster data yang namanya sama dengan di user inventory 
        id = monster_data["id"][index]              #mengakses id dari tiap nama monster dengan index yang didapat                   
        user_monster_id.append(id)                                   

    idx_name_choosen_monster= search_index(monster_data, 'id', pilih_monster) #mencari indeks dari id monster yang ingin dibeli
    name_choosen_monster= monster_data['type'][idx_name_choosen_monster] #mencari nama monster yang dipilih

    if pilih_monster in user_monster_id: #mengecek apakah pilihan yang ingin dibeli sudah ada atau tidak di inventory
        print(f"Monster {name_choosen_monster} sudah ada dalam inventory-mu! Pembelian dibatalkan.")

    elif monster_shop_data["stock"] == 0: # Jika stok berjumlah 0, tidak bisa melanjutkan ke tahap berikutnya
        print("Stok monster habis") 
        
        
    else: 
        index=search_index(monster_shop_data, 'monster_id', pilih_monster)
        harga_monster = monster_shop_data["price"][index]   #mencari harga dari monster yang diinginkan user


        if  user_oc >= harga_monster:
            user_oc = user_oc - harga_monster
            monster_shop_data["stock"][index] = monster_shop_data["stock"][index] - 1 # Mengurangi jumlah stok
            print(f"Berhasil membeli item: {name_choosen_monster}. Item sudah masuk ke inventory-mu!")
            print(f"Jumlah O.W.C.A. Coin-mu sekarang {user_oc}")

            banyak_monster_di_inventory=len(user_monster)

            user_monster[banyak_monster_di_inventory+1] = {'Type': 'Monster',   #menambahkan jenis monster yang baru
                'Name'      : name_choosen_monster,
                'ATK_Power' : monster_data['atk_power'][idx_name_choosen_monster],
                'DEF_Power' : monster_data['def_power'][idx_name_choosen_monster],
                'HP'        : monster_data['hp'][idx_name_choosen_monster],
                'Level'     : 1
            }
            
            

        else : #Jika uang tidak cukup, looping berhenti
            print("OC-mu tidak cukup.")
        
    return user_monster, user_oc, monster_shop_data
        

def beli_potion(item_shop_data, user_potion, user_oc):
    pilih_potion = int(input("Masukkan ID potion: "))
    jumlah_potion = int(input("Masukkan jumlah potion: "))

    if item_shop_data["stock"] == 0: # Jika stok berjumlah 0, tidak bisa melanjutkan ke tahap berikutnya
        print("Stok potion habis") 
        
    else: 

        harga_potion = item_shop_data["price"] * jumlah_potion

        if  user_oc >= harga_potion:
            item_shop_data["stock"] = item_shop_data["stock"] - jumlah_potion  # Mengurangi jumlah stok
            user_oc = user_oc - harga_potion

            idx_potion=pilih_potion-1
            potion_name=item_shop_data['type'][idx_potion] #mengakses nama dari potion yang dipilih
            print(f"Berhasil membeli item: Potion of {potion_name}. Item sudah masuk ke inventory-mu!")
            print(f"Jumlah O.W.C.A. Coin-mu sekarang {user_oc}")

            for key in user_potion:
                if user_potion[key]['Potion_Name']==potion_name:
                    user_potion[key]['Quantity']=int(user_potion[key]['Quantity'])+jumlah_potion #menambahkan banyak potion ke inventory user
                break
        else : #Jika uang tidak cukup, looping berhenti
            print("OC-mu tidak cukup.")
    return user_potion, user_oc, item_shop_data




def shop(monster_shop_data,user_data, item_shop_data, user_monster, monster_data):

    print("Welcome to SHOP!")
    while True:
        action_shop = str(input("Pilih aksi (lihat/beli/keluar): "))
        list_action = ["lihat", "beli", "keluar"]

        if action_shop not in list_action:
            print("Invalid choice. Please try again", end=" ")
            for i in range(10):
                print(".", end="")
                time.sleep(0.1)
            ClearScreen()
            shop()

        elif action_shop == "lihat":
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
                continue


        elif action_shop == "beli":
            user_oc = int(user_data["oc"])
            print(f"Jumlah O.W.C.A. Coin-mu sekarang {user_oc}")
            beli_apa = int(input("Mau beli apa? (monster/potion) "))
            z = True

            if beli_apa == "monster":
                user_monster, user_oc, item_shop_data=beli_monster(monster_data, user_monster, monster_shop_data, user_oc)
            elif beli_apa == "potion":
                user_potion, user_oc, item_shop_data=beli_potion(item_shop_data, user_potion, user_oc)
            continue
        elif action_shop=='keluar' or action_shop=='Keluar' or action_shop=='KELUAR':
            return user_monster, user_potion, user_oc
