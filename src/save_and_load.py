import argparse
import os
from utils import write_dict_of_arr, write_dict_of_dict,write_item_inventory,write_monst_inventory
from func import make_inventory,separate_monster_item_inventory

def load():
    parser = argparse.ArgumentParser(description="Jalankan game dengan folder progres yang diberikan.")
    parser.add_argument('folder_name', type=str, nargs='?', default='default_data', help="Nama folder tempat progres pemain disimpan")

    args = parser.parse_args()
    result=args.folder_name
    parent_directory = '../main/data'
    path=parent_directory+'/'+result
    return path


def save(id, user_data,monster_inventory_data,item_inventory_data, monster_shop,item_shop, monster_data):

    parent_directory = '../main/data'
    folder=input("Masukkan nama folder: ")
    result = f'/{folder}'
    new_folder = parent_directory+result
    print("Saving...")
    if not (os.path.exists(new_folder)):
        print(f"Membuat folder data/{result}")
        os.makedirs(new_folder, exist_ok=True)

    file_path_monster=os.path.join(new_folder, "monster_inventory.csv")
    file_path_item=os.path.join(new_folder, "item_inventory.csv")
    file_path_item_shop=os.path.join(new_folder, "item_shop.csv")
    file_path_monster_shop=os.path.join(new_folder, "monster_shop.csv")
    file_path_monster_data=os.path.join(new_folder, "monster.csv")
    file_path_user_data=os.path.join(new_folder, "user.csv")

    invent=make_inventory(id)
    monster,item=separate_monster_item_inventory(invent)

    item_in_inventory=write_item_inventory(item_inventory_data, item, id)
    monster_in_inventory=write_monst_inventory(monster_inventory_data, monster, id)
    monster_in_shop=write_dict_of_arr(monster_shop)
    item_in_shop=kalimat=write_dict_of_arr(item_shop)
    new_monster=write_dict_of_arr(monster_data)
    new_user=write_dict_of_arr(user_data)
    

    with open(file_path_monster, mode='w', newline='') as file:
        file.write(monster_in_inventory)
    with open(file_path_item, mode='w', newline='') as file:
        file.write(item_in_inventory)
    with open(file_path_item_shop, mode='w', newline='') as file:
        file.write(item_in_shop)
    with open(file_path_monster_shop, mode='w', newline='') as file:
        file.write(monster_in_shop)
    with open(file_path_monster_data, mode='w', newline='') as file:
        file.write(new_monster)
    with open(file_path_user_data, mode='w', newline='') as file:
        file.write(new_user)