from utils import search_index,printDict,isallnumber,validate_input, in_game_validate_input

#REALISASI FUNGSI-FUNGSI


def login_user(id, username, is_admin, sudah_login, user_data, current_oc=0): #F02
    username = username if username!="" else ""
    current_oc = current_oc if current_oc!=0 else 0
    if sudah_login:
        print("Login gagal!")
        print(f"Anda telah login dengan username {username}, silahkan lakukan \“LOGOUT\” sebelum melakukan login kembali") 
    else:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print()
        if username in user_data['username']:
            index = search_index(user_data, "username", username)
            if user_data["password"][index]==password:
                print(f"Selamat datang, {user_data['role'][index]} {username}!")
                print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
                print()
                if user_data["role"][index]=="admin":
                    is_admin = True
                else:
                    is_admin = False
                sudah_login = True
                index = search_index(user_data, "username", username) #cari index dimana username berada
                id = user_data["id"][index]
                current_oc = user_data["oc"][index]
                
            else:
                print("Password salah!")
                print()
        else:
            print("Username tidak terdaftar!")
            print()
    return (sudah_login, username, is_admin, id, current_oc)

def logout_user(sudah_login):
    if sudah_login:
        sudah_login = False
        print("Anda berhasil logout")
        return sudah_login
    else:
        print('Logout gagal!')
        print('Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout')