import argparse
import os
from utils import write_dict_of_arr, write_dict_of_dict,write_item_inventory,write_monst_inventory,fetch_data
from func import make_inventory,separate_monster_item_inventory

def load():
    parser = argparse.ArgumentParser(description="Jalankan game dengan folder progres yang diberikan.")
    parser.add_argument('folder_name', type=str, nargs='?', default='default_data', help="Nama folder tempat progres peif1210-2024-tubes-k11-h disimpan")

    args = parser.parse_args()
    result=args.folder_name
    parent_directory = '../if1210-2024-tubes-k11-h/data'
    path=parent_directory+'/'+result

    item_shop_data= fetch_data(f'{parent_directory}/item_shop_inventory.csv')
    monster_shop_data= fetch_data(f'{parent_directory}/monster_shop.csv')
    monster_data= fetch_data(f'{parent_directory}/monster.csv')
    user_data = fetch_data(f'{path}/user.csv')
    monster_inventory_data = fetch_data(f'{path}/monster_inventory.csv')
    item_inventory_data = fetch_data(f'{path}/item_inventory.csv')

    return user_data,monster_data,monster_inventory_data,item_inventory_data,item_shop_data,monster_shop_data


def save(id: str, user_data: dict,monster_inventory_data: dict,item_inventory_data:dict, monster_shop:dict,item_shop:dict, monster_data:dict, is_admin:bool):

    parent_directory = '../if1210-2024-tubes-k11-h/data'
    
    if is_admin:

        file_path_monster_shop=os.path.join(parent_directory, "monster_shop.csv")
        file_path_item_shop=os.path.join(parent_directory, "item_shop.csv")
        file_path_monster_data=os.path.join(parent_directory, "monster.csv")

        monster_in_shop=write_dict_of_arr(monster_shop)
        item_in_shop=write_dict_of_arr(item_shop)
        new_monster=write_dict_of_arr(monster_data)

        with open(file_path_item_shop, mode='w', newline='') as file:
            file.write(item_in_shop)
        with open(file_path_monster_shop, mode='w', newline='') as file:
            file.write(monster_in_shop)
        with open(file_path_monster_data, mode='w', newline='') as file:
            file.write(new_monster)

    else:
        folder=input("Masukkan nama folder: ")
        result = f'/{folder}'
        new_folder = parent_directory+result

        if not (os.path.exists(new_folder)):
            print(f"Membuat folder data/{result}")
            os.makedirs(new_folder, exist_ok=True)

        file_path_monster=os.path.join(new_folder, "monster_inventory.csv") 
        file_path_item=os.path.join(new_folder, "item_inventory.csv")
        file_path_user_data=os.path.join(new_folder, "user.csv")

        invent=make_inventory(id)
        monster,item=separate_monster_item_inventory(invent)

        item_in_inventory=write_item_inventory(item_inventory_data, item, id)
        monster_in_inventory=write_monst_inventory(monster_inventory_data, monster, id)
        new_user=write_dict_of_arr(user_data)
        

        with open(file_path_monster, mode='w', newline='') as file:
            file.write(monster_in_inventory)
        with open(file_path_item, mode='w', newline='') as file:
            file.write(item_in_inventory)
        with open(file_path_user_data, mode='w', newline='') as file:
            file.write(new_user)
    print("Saving...")


