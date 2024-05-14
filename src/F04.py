#REALISASI FUNGSI-FUNGSI
#KONDISI/STATUS
sudah_login = False
role = ""
username = "purry"
def login_user():
    global sudah_login
    global role
    login = input("LOGIN AKUN: ")
    role = input("ROLE: ")
    print("sudah login")
    sudah_login = True
   
def register_user():
    register = input("Register: ")

def logout_user():
    logout = input("Logout: ")

def help():
    if sudah_login:
        if isadmin :
            print("=========== HELP ===========")
            print(f"Halo Agent ADMIN. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
            print("     1. Logout: Keluar dari akun yang sedang digunakan")
            print("     2. Shop Management: Mengatur barang-barang yang dijual untuk para Agent")
            print("     3. Monster Management: Mengatur monster dalam database")
    
            print("Footnote")
            print("     1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
            print("     2. Jangan lupa untuk memasukkan input yang valid")
            help_choice = int(input())
            if help_choice == 1:
                logout_user()
            elif help_choice == 2:
                shop_management()
            elif help_choice == 3:
                monster_management() 
        
        else:
            print("=========== HELP ===========")
            print(f"Halo Agent {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
            print("     1. Logout: Keluar dari akun yang sedang digunakan")
            print("     2. Inventory: Melihat owca-dex yang dimiliki oleh Agent")
            print("     3. Battle: Melakukan pertarungan melawan monster secara random")
            print("     4. Arena: Pelatihan agent dan monster untuk meningkatkan kemampuan")
            print("     5. Shop & Currency: Tempat Agent membeli monster dan potion.")
            print("     6. Laboratory: Melakukan upgrade monster yang dimiliki di inventory")

            print("Footnote")
            print("     1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
            print("     2. Jangan lupa untuk memasukkan input yang valid")
            help_choice = int(input())
            if help_choice == 1:
                logout_user()
            elif help_choice == 2:
                inventory()
            elif help_choice == 3:
                battle()
            elif help_choice == 4:
                Arena()
            elif help_choice == 5:
                shop_currency()
            elif help_choice == 6:
                Laboratory()

    else:
        print("=========== HELP ===========")
        print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
        print("     1. Login: Masuk ke dalam akun yang sudah terdaftar")
        print("     2. Register: Membuat akun baru")
        print("Footnote")
        print("     1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
        print("     2. Jangan lupa untuk memasukkan input yang valid")
        help_choice = int(input())
        if help_choice == 1:
            login_user()
        elif help_choice == 2:
            register_user()
        else:
            print("Tidak Valid")

#PROGRAM UTAMA
while True:
    masukan = input()
    if masukan == ">>> REGISTER":
        register_user() 
        sudah_login = True
    elif masukan ==">>> LOGIN":
        login_user()
    if masukan == ">>> HELP":
        help()



