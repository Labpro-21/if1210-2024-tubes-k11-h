import time
from save_and_load import save

def exit(program, id: str, user_data: dict,monster_inventory_data: dict,item_inventory_data:dict, monster_shop:dict,item_shop:dict, monster_data:dict, is_admin:bool):
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    choice = input("Enter your choice: ").upper()

    if choice == "Y":
        save(id, user_data,monster_inventory_data,item_inventory_data, monster_shop,item_shop, monster_data, is_admin)
    elif choice == "N":
        program = False
    else:
        print("Invalid choice. Please try again", end="")
        for i in range(10):
            print(".", end="")
            time.sleep(0.1)
        print()
    return program