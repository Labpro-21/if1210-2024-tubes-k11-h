from utils import fetch_data
from RNG import RNG
import time
import os
from typing import Dict, List, Tuple, Union, Optional

DictOfArr = Dict[str, List[Union[str, int]]]

def ClearScreen():
    if os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Linux and macOS
        os.system('clear')

def jackpot(user_oc:int, user_id, monster_inventory_data: DictOfArr) -> Tuple[int, DictOfArr]:

    print(">>> JACKPOT")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$  Apakah Anda siap untuk menguji keberuntungan? $$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$     Menangkan Snorleks dengan 400 OC saja !!!  $$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    main = str(input(">>> Yakin? (y/n) ")).upper()

    if main == "Y":
        print("==== DAFTAR ITEM ====")
        print("1. Topi: 10 OC")
        print("2. Pedang: 50 OC")
        print("3. Koin: 100 OC")
        print("4. Potion: 300 OC")
        print("5. Monster: (Name: sikasik, Atk: 1000, Def: 50, HP: 1000, Lvl: 5)")
        print()
        print(">> Mulai bermain?? (y/n):")
        mulai_main = str(input(">>> ")).upper()

        if mulai_main == "Y":

            if (user_oc == 400) or ( user_oc >= 400):
                user_oc = user_oc - 400

                item_price = {1 : 10, 2 : 50, 3 : 100, 4 : 300, 5 : 800}
                item_name = {
                    1: "Topi",
                    2: "Pedang",
                    3: "Koin",
                    4: "Potion",
                    5: "Monster"
                }
                
                item_1 = RNG(1, 5)
                time.sleep(1)
                ClearScreen()
                print("Anda Mendapatkan:")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print(f"$$$$$$$$$$$$$$$$$$$$$$$$$  {item_name[item_1]}  |            |            $$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                
                item_2 = RNG(1, 5)
                time.sleep(1)
                ClearScreen()
                print("Anda Mendapatkan:")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print(f"$$$$$$$$$$$$$$$$$$$$$$$$$  {item_name[item_1]}  |  {item_name[item_2]}  |            $$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                item_3 = RNG(1, 5)
                time.sleep(1)
                ClearScreen()
                print("Anda Mendapatkan:")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print(f"$$$$$$$$$$$$$$$$$$$$$$$$$  {item_name[item_1]}  |  {item_name[item_2]}  |  {item_name[item_3]}  $$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

                if item_1 == item_2 and item_2 == item_3:
                    #cek apakah monster pernah didapat
                    cek_monster = False
                    for i in range(len(monster_inventory_data['monster_id'])):
                        if monster_inventory_data['monster_id'][i] == '6':
                            cek_monster = True
                            break

                    if cek_monster:
                        print("JACKPOT!!! Selamat, Anda mendapatkan monster sikasik.")
                        print("Anda telah memiliki monster sikasik, monster dikonversi menjadi 800 OC!")
                        user_oc+=800
                    else:
                        print("JACKPOT!!! Selamat, Anda mendapatkan monster sikasik.")
                        print("Monster telah ditambahkan ke inventory Anda.")
                        monster_inventory_data['user_id'].append(str(user_id))
                        monster_inventory_data['monster_id'].append('6')
                        monster_inventory_data['level'].append('5')
                else:
                    oc_gained =  item_price[item_1] + item_price[item_2] + item_price[item_3]
                    user_oc+=oc_gained
                    print(f"Selamat! anda mendapatkan {oc_gained} OC!")
            else:
                print("Maaf, anda tidak memiliki cukup OC untuk bermain JACKPOT.")

        elif mulai_main=="N":
            return user_oc, monster_inventory_data
        else:
            print("Masukkan tidak dikenal!")

    elif main == "N":
        return user_oc, monster_inventory_data
    else:
        print("Masukkan tidak dikenal!")

    return user_oc, monster_inventory_data
    