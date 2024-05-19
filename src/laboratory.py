# Yang kurang
# 1. Dihubungkan dengan Login untuk memvalidasi akun agent dan input username
# 2. Uang user (kaitan juga dengan login)
# 3. Melakukan perubahan/edit pada database
from func import separate_monster_item_inventory,make_inventory

def laboratory(username,current_oc, monster_inventory_data, item_inventory_data, user_id,monster_data): 
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

    pilih_monster = int(input("Pilih Monster: "))
    monster_terpilih = user_monster[pilih_monster]["Name"]
    level_monster = int(user_monster[pilih_monster]["Level"])

    if level_monster < 5:
        list_price = [250, 450, 800, 1000]
        upgrade_price = list_price[level_monster-1]
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