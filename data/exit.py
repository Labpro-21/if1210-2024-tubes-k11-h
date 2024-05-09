def exit():
    global sudah_login, program
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    choice = input("Enter your choice: ")

    if choice == "y":
        save() #diarahkan ke function save (GANTI)
    elif choice == "n":
        program = False #harusnya balik lagi ke interface awal game/ program
    else:
        print("Invalid choice. Please try again", end="")
        for i in range(10):
            print(".", end="")
            # time.sleep(0.1)