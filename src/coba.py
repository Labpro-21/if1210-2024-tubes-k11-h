from func import make_inventory_list
from func import make_arr
from globevar import user_data,monster_inventory_data,item_inventory_data,monster_data
arr_glob_monst=make_arr('../main/data/monster.csv')
arr_monst_inventory=make_arr('../main/data/monster_inventory.csv')
arr_item=make_arr('../main/data/item_inventory.csv')
id='2'



monster_inventory_arr, item_inventory_array=make_inventory_list(id,arr_monst_inventory,arr_glob_monst,arr_item)
# for i in range (len(monster_arr)):
#     print(f"{i+1}. {monster_arr[i][0]}")

# print(monster_arr[0][0])
print(arr_monst_inventory)



input = "9-12-2023"

nama_folder = f"./data/save_and_load/{username}/{input}"