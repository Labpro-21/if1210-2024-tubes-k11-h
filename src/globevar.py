from utils import fetch_data,make_arr


sudah_login = False
user_data = fetch_data('../main/data/user.csv')
monster_inventory_data = fetch_data('../main/data/monster_inventory.csv')
item_inventory_data = fetch_data('../main/data/item_inventory.csv')
monster_data = fetch_data('../main/data/monster.csv')
arr_glob_monst=make_arr('../main/data/monster.csv')
arr_monst_inventory=make_arr('../main/data/monster_inventory.csv')
arr_item=make_arr('../main/data/item_inventory.csv')

