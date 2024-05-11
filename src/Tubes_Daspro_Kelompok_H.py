from func import logout,login_user,register_user,inventory,calc_stats,battle
from func import get_seed,linear_congruential_method_int,RNG,potion,make_arr,shop_management

from globevar import user_data,monster_inventory_data,item_inventory_data,monster_data
from globevar import arr_glob_monst,arr_item,arr_monst_inventory
from utils import *




id='5'
sudah_login=False
program = True
while program:
    
    masukan = input(">>>").upper()
    '''
    if masukan == "REGISTER":
        register_user()
    elif masukan =="LOGIN":
        login_user()
    elif masukan=="INVENTORY":
        inventory()
    elif masukan == "LOGOUT":
        logout()
    '''

    # if masukan=="BATTLE":
    #     battle(id,arr_monst_inventory,arr_glob_monst,arr_item)
    if masukan == "SHOP":
        shop_management()


