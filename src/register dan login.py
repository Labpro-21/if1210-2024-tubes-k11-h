#REALISASI FUNGSI-FUNGSI
def register_user(): #F01
    global sudah_login, user_data
    if sudah_login:
        print("Login gagal!")
        print("Anda telah login dengan username Purry, silahkan lakukan “LOGOUT” sebelum melakukan login kembali")
    else:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        # ngecek username valid atau engga
        if not username.isalnum() and "_" not in username and "-" not in username:
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
            return

        # ngecek udah dipake atau belum
        if username in user_data['username']:
            print(f"Username {username} sudah terpakai, silahkan gunakan username lain!")
            return

        # registrasi, isi data
        user_data["id"].append(str(len(user_data["id"])+1))
        user_data["username"].append(username)
        user_data["password"].append(password)
        user_data["role"].append("agent")
        user_data["oc"].append("0")

        # pilih monster
        print("Silahkan pilih salah satu monster sebagai monster awalmu.")
        print("1. Charizard")
        print("2. Bulbasaur")
        print("3. Aspal")
        monster_choice = int(input("Monster pilihanmu: "))

        # Print welcome
        monsters = ["Charizard", "Bulbasaur", "Aspal"]
        print(f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monsters[monster_choice-1]}!")

def login_user(): #F02
    
    # global sudah_login, user_data
    global sudah_login
    if sudah_login:
        print("Login gagal!")
        print("Anda telah login dengan username Purry, silahkan lakukan \“LOGOUT\” sebelum melakukan login kembali")
    else:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username in user_data['username']:
            index = search_index(user_data, "username", username)
            if user_data["password"][index]==password:
                print(f"Selamat datang, Agent {username}!")
                print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
                sudah_login = True
            else:
                print("Password salah!")
        else:
            print("Username tidak terdaftar!")

def inventory():#F07
    print(f"=======INVENTORY LIST (User ID: {1})")
    print(f"Jumlah O.W.C.A. Coin-mu sekarang {900}.")


def fetch_data(path):
    data = {}

    file = open(path, 'r')
    lines = []
    for i in file:
        lines.append(i)
    keys = parser(lines[0])

    for i in keys:
        data[i] = []
    for i in range(1, len(lines)):
        array = parser(lines[i])
        
        for j, key in enumerate(keys):
            data[key].append(array[j])

    file.close()
    
    return data



#HELPER FUNCTION
def parser(value):
    arr = []
    kata=""
    for i in range(len(value)):
        if value[i]!=';' and value[i]!='\n':
            kata+=value[i]
        else:
            arr.append(kata)
            kata=""
    if kata:
        arr.append(kata)
    return arr

def search_index(data, key, value):
    index = 0
    while index<=len(data) and data[key][index] != value:
        index+=1
    if index == len(data)+1: #kalau gak ketemu
        return -9999
    else:
        return index #indeks kalau ketemu
    
#PENAMPUNG DATA
# user_data = {
#     'ID':[1,2],
#     'username':['gunawan','purry'],
#     'password':['gunawan12','purry12'],
#     'role':['admin','agent'],
#     'oc':[1,2],
# }

#KONDISI/STATUS
sudah_login = False
#PROGRAM UTAMA
user_data = fetch_data('main/data/monster.csv')
while True:
    masukan = input()
    if masukan == ">>> REGISTER":
        register_user() 
    elif masukan ==">>> LOGIN":
        login_user()
    # elif masukan ==">>> INVENTORY":
        # inventory()