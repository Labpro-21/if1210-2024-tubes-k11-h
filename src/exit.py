import time
from typing import Dict, List, Tuple, Union, Optional
from save_and_load import save

DictOfArr = Dict[str, List[Union[str, int]]]

def exit(program:bool, 
         id: str, 
         user_data: DictOfArr,
         monster_inventory_data: DictOfArr,
         item_inventory_data:DictOfArr, 
         monster_shop:DictOfArr,
         item_shop:DictOfArr,
         monster_data:DictOfArr, 
         is_admin:bool) -> bool:
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