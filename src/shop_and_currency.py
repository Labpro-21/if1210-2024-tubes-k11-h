import time
import os
def ClearScreen():
    if os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Linux and macOS
        os.system('clear')

def shop():

    monster_shop_data = fetch_data("../main/data/monster_shop.csv")
    item_shop_data = fetch_data("../main/data/item_shop.csv")
    user_oc_data = fetch_data("../main/data/user.csv")
    user_monster_data = fetch_data("../main/data/monster_inventory.csv")
 
    print("Welcome to SHOP!")
    print("Pilih aksi (lihat/beli/keluar): ")
    action_shop = str(input(""))
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


    elif action_shop == "beli":
        user_oc = user_oc_data["oc"]
        print(f"Jumlah O.W.C.A. Coin-mu sekarang {user_oc}")
        beli_apa = int(input("Mau beli apa? (monster/potion) "))
        harga = 0
        z = True

        if beli_apa == "monster":
            def beli_monster():
                while z:
                    pilih_monster = int(input("Masukkan ID monster: "))

                    if pilih_monster == user_monster_data["monster_id"][i]:
                        print(f"Monster {pilih_monster} sudah ada dalam inventory-mu! Pembelian dibatalkan.")

                    elif monster_shop_data["stock"] == 0: # Jika stok berjumlah 0, tidak bisa melanjutkan ke tahap berikutnya
                        print("Stok monster habis") 
                        selesai_beli = input("Apakah ingin membeli monster lain? [y/n]")
                        if selesai_beli == "n":
                                z = False # memberhentikan looping
                                print(f"Jumlah O.W.C.A. Coin-mu sekarang {user_oc}")
                        else:
                            beli_monster()
                        
                    else: 
                        monster_shop_data["stock"] = monster_shop_data["stock"] - 1  # Mengurangi jumlah stok
                        harga_monster = monster_shop_data["price"]

                        if (user_oc == harga_monster) or ( user_oc >= harga_monster):
                            user_oc = user_oc - harga
                            print(f"Berhasil membeli item: {pilih_monster}. Item sudah masuk ke inventory-mu!")
                            print(f"Jumlah O.W.C.A. Coin-mu sekarang {user_oc}")
                            z = False # memberhentikan looping

                        else : #Jika uang tidak cukup, looping berhenti
                            print("OC-mu tidak cukup.")
                            z = False # memberhentikan looping

        elif beli_apa == "potion":
            def beli_potion():
                while z:
                    pilih_potion = int(input("Masukkan ID potion: "))
                    jumlah_potion = int(input("Masukkan jumlah potion: "))
                   
                    if item_shop_data["stock"] == 0: # Jika stok berjumlah 0, tidak bisa melanjutkan ke tahap berikutnya
                        print("Stok potion habis") 
                        selesai_beli = input("Apakah ingin membeli potion lain? [y/n]")
                        if selesai_beli == "n":
                                z = False # memberhentikan looping
                                print(f"Jumlah O.W.C.A. Coin-mu sekarang {user_oc}")
                        else:
                            beli_potion()
                        
                    else: 
                        item_shop_data["stock"] = item_shop_data["stock"] - jumlah_potion  # Mengurangi jumlah stok
                        harga_potion = item_shop_data["price"] * jumlah_potion

                        if (user_oc == harga_potion) or ( user_oc >= harga_potion):
                            user_oc = user_oc - harga_potion
                            print(f"Berhasil membeli item: {pilih_potion}. Item sudah masuk ke inventory-mu!")
                            print(f"Jumlah O.W.C.A. Coin-mu sekarang {user_oc}")
                            z = False # memberhentikan looping

                        else : #Jika uang tidak cukup, looping berhenti
                            print("OC-mu tidak cukup.")
                            z = False # memberhentikan looping

        else :
            return

    else : #action_shop == "keluar"
        return