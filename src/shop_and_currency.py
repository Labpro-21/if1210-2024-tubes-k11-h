import time
import os
from utils import search_index,in_game_validate_input
from inventory import separate_monster_item_inventory,make_inventory
from typing import Dict, List, Tuple, Union, Optional

DictOfArr = Dict[str, List[Union[str, int]]]
DictOfDict = Dict[str, Dict[str, Union[str, int]]]

def ClearScreen():
    if os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Linux and macOS
        os.system('clear')

def beli_monster(monster_data: DictOfArr, 
                 monster_shop_data: DictOfArr, 
                 current_oc: int, 
                 monster_inventory_data: DictOfArr, 
                 item_inventory_data: DictOfArr, 
                 id_user) -> Tuple[DictOfArr, int, DictOfArr]:
    user_monster,user_potion= separate_monster_item_inventory(make_inventory(str(id_user), monster_inventory_data, monster_data,item_inventory_data))
    pilih_monster = input("Masukkan ID monster: ")
    while True:
        if pilih_monster in monster_shop_data['monster_id']:
            break
        print('Masukkan ID dengan benar')
        pilih_monster = input("Masukkan ID monster: ")

    pilih_monster=pilih_monster
    
    user_monster_name = []
    for i in range(1, len(user_monster)+1):
        user_monster_name.append(user_monster[i]["Name"])  #menambahkan semua nama monster di inventory user ke array
    user_monster_id = []
    for i in range(len(user_monster_name)):
        index = search_index(monster_data,"type", user_monster_name[i]) #mencari index di monster data yang namanya sama dengan di user inventory 
        id = monster_data["id"][index]              #mengakses id dari tiap nama monster dengan index yang didapat                   
        user_monster_id.append(id)                                   

    idx_name_choosen_monster= search_index(monster_data, 'id', f'{pilih_monster}') #mencari indeks dari id monster yang ingin dibeli
    name_choosen_monster= monster_data['type'][idx_name_choosen_monster] #mencari nama monster yang dipilih

    if pilih_monster in user_monster_id: #mengecek apakah pilihan yang ingin dibeli sudah ada atau tidak di inventory
        print(f"Monster {name_choosen_monster} sudah ada dalam inventory-mu! Pembelian dibatalkan.")

    elif monster_shop_data["stock"] == 0: # Jika stok berjumlah 0, tidak bisa melanjutkan ke tahap berikutnya
        print("Stok monster habis") 
        
        
    else: 
        index=None
        for i, item in enumerate (monster_shop_data['monster_id']):
            if item==pilih_monster:
                index=i
                break
        harga_monster = int(monster_shop_data["price"][index])   #mencari harga dari monster yang diinginkan user


        if  current_oc >= harga_monster:
            current_oc = current_oc - harga_monster
            monster_shop_data["stock"][index] = str(int(monster_shop_data["stock"][index]) - 1) # Mengurangi jumlah stok
            print(f"Berhasil membeli item: {name_choosen_monster}. Item sudah masuk ke inventory-mu!")
            print(f"Jumlah O.W.C.A. Coin-mu sekarang {current_oc}")


            monster_inventory_data['user_id'].append(str(id_user))
            monster_inventory_data['monster_id'].append(pilih_monster)
            monster_inventory_data['level'].append('1')

        else : #Jika uang tidak cukup, looping berhenti
            print("OC-mu tidak cukup.")
        
    return monster_inventory_data, current_oc, monster_shop_data
        

def beli_potion(item_shop_data: DictOfArr, 
                current_oc: int, 
                monster_inventory_data: DictOfArr, 
                item_inventory_data: DictOfArr, id, 
                monster_data: DictOfArr) -> Tuple[DictOfArr, int, DictOfArr]:
    user_monster,user_potion= separate_monster_item_inventory(make_inventory(str(id), monster_inventory_data, monster_data,item_inventory_data))
    pilih_potion = input("Masukkan ID potion: ")
    pilih_potion=int(in_game_validate_input(pilih_potion, len(item_shop_data['type']), "Masukkan ID potion: ", 'Mohon masukkan ID yang benar'))
    jumlah_potion = input("Masukkan jumlah potion: ")
    jumlah_potion=int(in_game_validate_input(jumlah_potion, int(item_shop_data['stock'][pilih_potion-1]), 'Masukkan jumlah potion: ', 'Mohon masukkan jumlah yang sesuai'))

    if item_shop_data["stock"][pilih_potion-1] == 0: # Jika stok berjumlah 0, tidak bisa melanjutkan ke tahap berikutnya
        print("Stok potion habis") 
        
    else: 
        
        harga_potion = int(item_shop_data["price"][pilih_potion-1]) * jumlah_potion

        if  current_oc >= harga_potion:
            item_shop_data["stock"][pilih_potion-1] = str(int(item_shop_data["stock"][pilih_potion-1]) - jumlah_potion)  # Mengurangi jumlah stok
            current_oc = current_oc - harga_potion

            idx_potion=pilih_potion-1
            potion_name=item_shop_data['type'][idx_potion] #mengakses nama dari potion yang dipilih
            print(f"Berhasil membeli item: Potion of {potion_name}. Item sudah masuk ke inventory-mu!")
            print(f"Jumlah O.W.C.A. Coin-mu sekarang {current_oc}")


            item_inventory_data['user_id'].append(str(id))
            item_inventory_data['type'].append(str(potion_name))
            item_inventory_data['quantity'].append(str(jumlah_potion))


            # for key in user_potion:
            #     if user_potion[key]['Potion_Name']==potion_name:
            #         user_potion[key]['Quantity']=int(user_potion[key]['Quantity'])+jumlah_potion #menambahkan banyak potion ke inventory user
            #     break
        else : #Jika uang tidak cukup, looping berhenti
            print("OC-mu tidak cukup.")
    return item_inventory_data, current_oc, item_shop_data




def shop(monster_shop_data: DictOfArr, 
         item_shop_data: DictOfArr, 
         monster_data: DictOfArr, 
         current_oc: int, 
         monster_inventory_data: DictOfArr, 
         item_inventory_data: DictOfArr, id_user) ->Tuple[DictOfArr, DictOfArr, int, DictOfArr]:

    print("Welcome to SHOP!")
    while True:
        action_shop = str(input("Pilih aksi (lihat/beli/keluar): ")).upper()
        list_action = ["LIHAT", "BELI", "KELUAR"]

        if action_shop not in list_action:
            print("Invalid choice. Please try again")
            for i in range(10):
                print(".", end="")
                time.sleep(0.1)
            print()
            ClearScreen()
            # shop(monster_shop_data, item_shop_data, monster_data, current_oc, monster_inventory_data, item_inventory_data, id_user)

        elif action_shop == "LIHAT":
                lihat_apa = input(">>> Mau lihat apa? (monster/potion): ")
                if lihat_apa=="monster":
                    print("ID | Type | ATK Power | DEF Power | HP | Stok | Harga")
                    for i in range(len(monster_shop_data["monster_id"])):
                        id = monster_shop_data["monster_id"][i]
                        index = search_index(monster_data, 'id',id)
                        print(f"{id} | {monster_data['type'][index]} | {monster_data['atk_power'][index]} | {monster_data['def_power'][index]} | {monster_data['hp'][index]} | {monster_shop_data['stock'][i]} | {monster_shop_data['price'][i]}")
                elif lihat_apa=="potion":
                    print("ID | Type | Stok | Harga")
                    for i in range(len(item_shop_data["type"])):
                        print(f" {i+1} | {item_shop_data['type'][i]} | {item_shop_data['stock'][i]} | {item_shop_data['price'][i]}")

        elif action_shop == "BELI":
            print(f"Jumlah O.W.C.A. Coin-mu sekarang {current_oc}")
            beli_apa = input("Mau beli apa? (monster/potion): ")
            list_action = ["monster", "potion"]
            
            while True:
                if beli_apa in list_action:
                    break
                beli_apa = input("Mau beli apa? (monster/potion): ")
            if beli_apa == "monster":
                monster_inventory_data, current_oc, monster_shop_data=beli_monster(monster_data, monster_shop_data, current_oc, monster_inventory_data, item_inventory_data, id_user)
            elif beli_apa == "potion":
                item_inventory_data, current_oc, item_shop_data=beli_potion(item_shop_data, current_oc, monster_inventory_data, item_inventory_data, id_user, monster_data)


        elif action_shop=='KELUAR':
            return monster_inventory_data, item_inventory_data, current_oc, item_shop_data  
