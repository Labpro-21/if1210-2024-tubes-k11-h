# Yang kurang
# 1. Dihubungkan dengan Login untuk memvalidasi akun agent dan input username
# 2. Uang user (kaitan juga dengan login)
# 3. Melakukan perubahan/edit pada database

from utils import fetch_data,make_arr
from globevar import monster_data,monster_inventory_data
uang = 1000

def laboratory(sudah_login, is_admin, user_inventory, username):
    if sudah_login and not is_admin:
        global uang 
        print(f"Selamat datang di lab agent {username}")
        print("============ MONSTER LIST ============")
        for i in range(len(monster_data)):
            print(f"{i+1}. {monster_data['type'][i]} (Level: {monster_inventory_data['level'][i]})")
        print("============ UPGRADE PRICE ============")
        print("1. Level 1 -> Level 2: 250 OC")
        print("2. Level 2 -> Level 3: 450 OC")
        print("3. Level 3 -> Level 4: 800 OC")
        print("4. Level 4 -> Level 5: 1000 OC")

        pilih_monster = int(input("Pilih Monster: "))
        monster_terpilih = monster_data["type"][pilih_monster-1]
        level_monster = int(monster_inventory_data["level"][pilih_monster-1])

        if level_monster < 5:
            list_price = [250, 450, 800, 1000]
            upgrade_price = list_price[level_monster-1]
            print(f"{monster_terpilih} akan di-upgrade ke level {level_monster + 1}.")
            print(f"Harga untuk melakukan upgrade {monster_terpilih} adalah {upgrade_price} OC ")
            lanjut_upgrade = input("Lanjutkan upgrade (Yes/No): ")
            if lanjut_upgrade == "Yes": 
                if uang >= upgrade_price:
                    print(f"Selamat, {monster_terpilih} berhasil di-upgrade ke level {level_monster + 1} !")
                    user_inventory["level"][3] = level_monster +1
                    uang -= upgrade_price
                else: 
                    print("OC tidak cukup untuk melakukan upgrade")

        elif level_monster == 5:
            print("Maaf, monster yang Anda pilih sudah memiliki level maksimum")
        return user_inventory