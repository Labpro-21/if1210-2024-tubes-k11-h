from utils import fetch_data


def monster_management(sudah_login, is_admin):
    if sudah_login and is_admin:
        monster_data = fetch_data('../main/data/monster.csv')
        new:dict=monster_data
        
        print("SELAMAT DATANG DI DATABASE PARA MONSTER !!!")
        print("1. Tampilkan semua Monster")
        print("2. Tambah Monster baru")

        pilih_aksi = int(input("Pilih Aksi: "))
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
            for i in range(len(new['id'])):
                print(f"{i+1:<3} | {monster_data['type'][i]:<{max_type_length}} | {monster_data['atk_power'][i]:<{max_atk_length}} | {monster_data['def_power'][i]:<{max_def_length}} | {monster_data['hp'][i]:<{max_hp_length}}")

        elif pilih_aksi == 2:
            print("Memulai pembuatan monster baru")
            nama_monster = input("Masukkan Type/Nama: ")
            i = 0
            isterdaftar = False
            while isterdaftar == False and i < len(monster_data["id"]):
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
                    if atk_power.isdigit():
                        atk_power = int(atk_power)
                        isinteger = True
                    else:
                        print("Masukkan input bertipe integer, coba lagi!")
                        atk_power = input("masukkan ATK Power: ")

                def_power = int(input("Masukkan DEF Power (0-50): "))
                ispowerrange = False
                while ispowerrange == False:
                    if 0 <= def_power <= 50:
                        hp = input("Masukkan HP: ")
                        ispowerrange = True 
                    else: 
                        print("DEF Power harus bernilai 0-50, coba lagi!")
                        def_power = int(input("Masukkan DEF Power (0-50): "))
        
                print("Monster baru berhasil dibuat!")
                print(f"Type : {nama_monster}")
                print(f"ATK Power: {atk_power}")
                print(f"DEF Power: {def_power}")
                print(f"HP: {hp} ")

                tambah_monster = input("Tambahkan Monster ke database (Yes/No): ")
                if tambah_monster == "Yes":
                    new_id= len(monster_data['id'])+1
                    new['id'].append(str(new_id))
                    new['type'].append(str(nama_monster))
                    new['atk_power'].append(str(atk_power))
                    new['def_power'].append(str(def_power))
                    new['hp'].append(str(hp))
                    print("Monster baru telah ditambahkan!")
                elif tambah_monster == "No":
                    print("Monster gagal ditambahkan!")

                return new

        
            