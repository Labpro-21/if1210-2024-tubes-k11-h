from inventory import separate_monster_item_inventory,make_inventory
from utils import in_game_validate_input
from typing import Dict, List, Tuple, Union, Optional

DictOfArr = Dict[str, List[Union[str, int]]]
DictOfDict = Dict[str, Dict[str, Union[str, int]]]

def laboratory(username: str,
               current_oc: int, 
               monster_inventory_data: DictOfArr, 
               item_inventory_data: DictOfArr, user_id,
               monster_data: DictOfArr) -> Tuple[DictOfArr,int]: 
    user_monster,user_potion=separate_monster_item_inventory(make_inventory(user_id, monster_inventory_data, monster_data, item_inventory_data))
    print(f"Selamat datang di lab agent {username}")
    print("============ MONSTER LIST ============")
    for i, key in enumerate(user_monster):
        print(f"{i+1}. {user_monster[key]['Name']} (Level: {user_monster[key]['Level']})")
    print("============ UPGRADE PRICE ============")
    print("1. Level 1 -> Level 2: 250 OC")
    print("2. Level 2 -> Level 3: 450 OC")
    print("3. Level 3 -> Level 4: 800 OC")
    print("4. Level 4 -> Level 5: 1000 OC")
    
    pilih_monster = input("Pilih Monster: ")
    pilih_monster = in_game_validate_input(pilih_monster, len(user_monster), "Pilih Monster: ", "Masukan salah, silakan input ulang!")
    pilih_monster = int(pilih_monster)

    monster_terpilih = user_monster[pilih_monster]["Name"]
    level_monster = int(user_monster[pilih_monster]["Level"])

    if level_monster < 5:
        list_price = [250, 450, 800, 1000]
        upgrade_price = int(list_price[level_monster-1])
        print(f"{monster_terpilih} akan di-upgrade ke level {level_monster + 1}.")
        print(f"Harga untuk melakukan upgrade {monster_terpilih} adalah {upgrade_price} OC ")
        lanjut_upgrade = input("Lanjutkan upgrade (Yes/No): ").upper()
        while True:
            if lanjut_upgrade == "YES": 
                if current_oc >= upgrade_price:
                    print(f"Selamat, {monster_terpilih} berhasil di-upgrade ke level {level_monster + 1} !")
                    user_monster[pilih_monster]["Level"] +=1
                    current_oc -= upgrade_price
                else: 
                    print("OC tidak cukup untuk melakukan upgrade")
                break
            elif lanjut_upgrade=='NO':
                break
            else:
                print("Masukan salah, silahkan input yang benar")
                lanjut_upgrade = input("Lanjutkan upgrade (Yes/No): ").upper()


    else:
        print("Maaf, monster yang Anda pilih sudah memiliki level maksimum")

    for i,item in enumerate (monster_inventory_data['user_id']):
        indexing=1
        if item==str(user_id):
            monster_inventory_data['level'][i]=user_monster[indexing]['Level']
            indexing+=1
    return monster_inventory_data, current_oc