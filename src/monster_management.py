from utils import in_game_validate_input,isallnumber
from typing import Dict, List, Tuple, Union, Optional

DictOfArr = Dict[str, List[Union[str, int]]]

def monster_management(monster_data: DictOfArr) -> DictOfArr:
    print("SELAMAT DATANG DI DATABASE PARA MONSTER !!!")
    print("1. Tampilkan semua Monster")
    print("2. Tambah Monster baru")
    print("3. Keluar")

    while True:
        pilih_aksi = input("Pilih Aksi (1-3): ")
        pilih_aksi=int(in_game_validate_input(pilih_aksi, 3, "Pilih Aksi (1-3): ", "Masukan salah, silahkan input ulang"))
        if pilih_aksi == 1:
            # Menentukan lebar maksimum untuk setiap kolom
            max_type_length = max(len(monster_data['type'][i]) for i in range(len(monster_data)))
            max_atk_length = len("ATK Power")
            max_def_length = len("DEF Power")
            max_hp_length = len("HP")

            # Mencetak header tabel
            print(f"{'ID':<3} | {'Type':<{max_type_length}} | {'ATK Power':<{max_atk_length}} | {'DEF Power':<{max_def_length}} | {'HP':<{max_hp_length}}")
            print("-" * (3 + max_type_length + max_atk_length + max_def_length + max_hp_length + 14))  # Garis pemisah

            # Mencetak isi tabel
            for i in range(len(monster_data['id'])):
                print(f"{i+1:<3} | {monster_data['type'][i]:<{max_type_length}} | {monster_data['atk_power'][i]:<{max_atk_length}} | {monster_data['def_power'][i]:<{max_def_length}} | {monster_data['hp'][i]:<{max_hp_length}}")

        elif pilih_aksi == 2:
            print("Memulai pembuatan monster baru")
            nama_monster = input("Masukkan Type/Nama: ")
            i = 0
            isterdaftar = False
            while not isterdaftar and i < len(monster_data["id"]):
                if monster_data['type'][i] == nama_monster:
                    isterdaftar = True
                else:
                    i += 1  

            if isterdaftar:
                print("Nama sudah terdaftar, coba lagi!")
            else:
                atk_power = input("masukkan ATK Power: ")   
                isinteger = False
                while isinteger == False:
                    if isallnumber(atk_power):
                        atk_power = int(atk_power)
                        isinteger = True
                    else:
                        print("Masukkan input bertipe integer, coba lagi!")
                        atk_power = input("masukkan ATK Power: ")

                def_power = input("Masukkan DEF Power (0-50): ")
                while True :          #validasi input 
                    if isallnumber(def_power) and 0 <= int(def_power) <= 50:
                        break
                    elif not isallnumber(def_power): 
                        print("Masukan harus bertipe integer")
                    else:
                        print("DEF Power harus bernilai 0-50, coba lagi!")
                    def_power = input("Masukkan DEF Power (0-50): ")

                hp = input("Masukkan HP (0-99999): ")
                hp= in_game_validate_input(hp, 99999, "Masukkan HP (0-99999): ", "Masukan salah, silahkan input ulang")
                print("Monster baru berhasil dibuat!")
                print(f"Type : {nama_monster}")
                print(f"ATK Power: {atk_power}")
                print(f"DEF Power: {def_power}")
                print(f"HP: {hp} ")

                tambah_monster = input("Tambahkan Monster ke database (Yes/No): ").upper()
                while True:
                    
                    if tambah_monster == "YES":
                        monster_data_id= len(monster_data['id'])+1
                        monster_data['id'].append(str(monster_data_id))
                        monster_data['type'].append(str(nama_monster))
                        monster_data['atk_power'].append(str(atk_power))
                        monster_data['def_power'].append(str(def_power))
                        monster_data['hp'].append(str(hp))
                        print("Monster baru telah ditambahkan!")
                        break
                    elif tambah_monster == "NO":
                        print("Monster gagal ditambahkan!")
                        break
                    else:
                        tambah_monster = input("Tambahkan Monster ke database (Yes/No): ").upper()
        elif pilih_aksi==3:
            return monster_data
