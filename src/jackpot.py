from utils import fetch_data
from RNG import RNG

def jackpot():
    user_oc_data = fetch_data("../main/data/user.csv")

    print(">>> JACKPOT")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$  Apakah Anda siap untuk menguji keberuntungan? $$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$     Menangkan Snorleks dengan 400 OC saja !!!  $$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    main = str(input("Y/N"))

    if main == "Y":
        print("==== DAFTAR ITEM ====")
        print("1. Topi: 50 OC")
        print("2. Pedang: 100 OC")
        print("3. Koin: 200 OC")
        print("4. Potion: 300 OC")
        print("5. Monster: 500 OC")
        mulai_main = str(input(">> Mulai bermain (Y/N):"))

        if mulai_main == "Y":
            user_oc = user_oc_data["oc"]

            if (user_oc == 400) or ( user_oc >= 400):
                user_oc = user_oc - 400

                arr_item = {1 : 50, 2 : 100, 3 : 200, 4 : 300, 5 : 500}

                item_1 = RNG(1, 5)
                item_2 = RNG(1, 5)
                item_3 = RNG(1, 5)

                print("Anda Mendapatkan:")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print(f"$$$$$$$$$$$$$$$$$$$$$$$$$  {item_1}  |  {item_2}  |  {item_3}  $$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

                if item_1 == item_2 and item_2 == item_3:
                    print("JACKPOT!!! Selamat, Anda mendapatkan monster TORCIK.")
                    print("Monster telah ditambahkan ke inventory Anda.")

                else:
                    user_oc = user_oc + arr_item[item_1] + arr_item[item_2] + arr_item[item_3]
                    return
            else:
                print("Maaf, anda tidak memiliki cukup OC untuk bermain JACKPOT.")
                return
        else:
            return
    else:
        return
