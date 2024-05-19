from func import *
from battle_and_arena import *
from laboratory import *

def help(sudah_login, is_Admin, username):
    if sudah_login:
        if is_Admin:
            print("=========== HELP ===========")
            print(f"Halo ADMIN {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
            print("     1. Logout: Keluar dari akun yang sedang digunakan")
            print("     2. Shop Management: Mengatur barang-barang yang dijual untuk para Agent")
            print("     3. Monster Management: Mengatur monster dalam database")
    
            print("Footnote")
            print("     1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
            print("     2. Jangan lupa untuk memasukkan input yang valid")
        
        else:
            print("=========== HELP ===========")
            print(f"Halo Agent {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
            print("     1. Logout: Keluar dari akun yang sedang digunakan")
            print("     2. Inventory: Melihat owca-dex yang dimiliki oleh Agent")
            print("     3. Battle: Melakukan pertarungan melawan monster secara random")
            print("     4. Arena: Pelatihan agent dan monster untuk meningkatkan kemampuan")
            print("     5. Shop & Currency: Tempat Agent membeli monster dan potion.")
            print("     6. Laboratory: Melakukan upgrade monster yang dimiliki di inventory")
            print("     7. Save: Melakukan saving terhadap progres Anda")

            print("Footnote")
            print("     1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
            print("     2. Jangan lupa untuk memasukkan input yang valid")

    else:
        print("=========== HELP ===========")
        print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
        print("     1. Login: Masuk ke dalam akun yang sudah terdaftar")
        print("     2. Register: Membuat akun baru")
        print("     3. Load: Memuat data pada permainan sebelumnya")
        print("Footnote")
        print("     1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
        print("     2. Jangan lupa untuk memasukkan input yang valid")
