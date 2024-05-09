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

    #import data shop
    monster = []
    # monster.data = [
    #     monster(),
    # ]

    potion = []
    # potion.data = [
    #     potion(),
    # ]

    print("Welcome to SHOP!")
    print("Pilih aksi (lihat/beli/keluar): ")
    action_shop = str(input(""))
    list_action = ["lihat", "beli", "keluar"]

    # if action_shop != "lihat" or action_shop != "beli" or action_shop != "keluar":
    if action_shop not in list_action:
        print("Invalid choice. Please try again", end=" ")
        for i in range(10):
            print(".", end="")
            time.sleep(0.1)
        ClearScreen()
        shop()

    elif action_shop == "lihat":
        print("1. Monster")
        print("2. Potion")
        print("3. Back")
        jenis_shop = int(input("Mau lihat apa?: "))

        if jenis_shop == 1:
            print()

        elif jenis_shop == 2:
            print()

        else : #jenis_shop == 3
            shop()

    elif action_shop == "beli":
        coins = 0
        print(f"Jumlah O.W.C.A. Coin-mu sekarang {coins}")
        jenis_item = int(input("Mau beli apa? (monster/potion) "))
        harga = 0
        stok = 0
        z = True

        if jenis_item == "monster":
            def beli_monster():
                while z:
                    choose_item = int(input("Masukkan ID monster: "))

                    #if (monster udah ada di inventory):
                        #print(f"Monster {monster.name} sudah ada dalam inventory-mu! Pembelian dibatalkan.")

                    if stok == 0: # Jika stok berjumlah 0, tidak bisa melanjutkan ke tahap berikutnya
                        print("Stok monster habis") 
                        selesai_beli = input("Apakah ingin membeli monster lain? [y/n]")
                        if selesai_beli == "n":
                                z = False # memberhentikan looping
                                print(f"Jumlah O.W.C.A. Coin-mu sekarang {coins}")
                        else:
                            beli_monster()
                        
                    else: 
                        stok = stok - 1 # Mengurangi jumlah stok
                        harga = monster.harga

                        if (coins == harga) or ( coins >= harga):
                            coins = coins - harga
                            print(f"Berhasil membeli item: {monster.name}. Item sudah masuk ke inventory-mu!")
                            print(f"Jumlah O.W.C.A. Coin-mu sekarang {coins}")
                            z = False # memberhentikan looping

                        else : #(coins > harga). Jika uang tidak cukup, looping berhenti
                            print("OC-mu tidak cukup.")
                            z = False # memberhentikan looping

        elif jenis_item == "potion":
            def beli_potion():
                while z:
                    choose_item = int(input("Masukkan ID potion: "))
                    jumlah_item = int(input("Masukkan jumlah potion: "))

                    if stok == 0 or jumlah_item > stok: # Jika stok berjumlah 0, tidak bisa melanjutkan ke tahap berikutnya
                        print("Stok potion habis") 
                        selesai_beli = input("Apakah ingin membeli potion lain? [y/n]")
                        if selesai_beli == "n":
                                z = False # memberhentikan looping
                                print(f"Jumlah O.W.C.A. Coin-mu sekarang {coins}")
                        else:
                            beli_potion()
                        
                    else: 
                        stok = stok - jumlah_item # Mengurangi jumlah stok
                        harga = potion.harga

                        if (coins == harga) or ( coins >= harga): # Jika saldo sama dengan harga 
                            coins = coins - harga
                            print(f"Berhasil membeli item: {potion.name}. Item sudah masuk ke inventory-mu!")
                            print(f"Jumlah O.W.C.A. Coin-mu sekarang {coins}")
                            z = False # memberhentikan looping

                        else : #(coins > harga). Jika uang tidak cukup, looping berhenti
                            print("OC-mu tidak cukup.")
                            z = False # memberhentikan looping 

        else :
            #back
            shop()

    else : #action_shop == "keluar"
        #exit shop???
        print()