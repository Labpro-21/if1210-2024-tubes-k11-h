from utils import validate_input, in_game_validate_input
from inventory import make_inventory,separate_monster_item_inventory
from typing import Dict, List, Tuple, Union, Optional

DictOfArr = Dict[str, List[Union[str, int]]]
DictOfDict = Dict[str, Dict[str, Union[str, int]]]

#REALISASI FUNGSI-FUNGSI
def register_user(id,username: str,
                  user_monster: DictOfArr,
                  user_potion: DictOfDict,
                  sudah_login: bool, 
                  user_data: DictOfArr,
                  monster_inventory_data: DictOfArr, 
                  monster_data: DictOfArr, 
                  item_inventory_data: DictOfArr) -> Tuple[bool, str, Union[str,int], DictOfArr,DictOfDict,DictOfDict,DictOfArr]: #F01
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