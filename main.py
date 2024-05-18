import sys
sys.path.append('src')
import argparse

from battle_and_arena import battle, arena
from func import *
from utils import fetch_data
from menu_and_help import help
from laboratory import laboratory
from monster_management import monster_management
from save_and_load import save, load
from globevar import *
from shop_and_currency import shop

sudah_login=False
is_admin=False
program = True
id,username,user_monster,user_potion = 0,"",{},{}


while program:
    
    masukan = input(">>>").upper()
    if masukan == "REGISTER":
        sudah_login,username,id,user_data,user_monster,user_potion, monster_inventory_data = register_user(id,username,user_monster,user_potion,sudah_login, user_data,monster_inventory_data, monster_data, item_inventory_data)
        current_oc = 10000
        
    elif masukan =="LOGIN":
        sudah_login, username, is_admin, id,current_oc = login_user(id, username, is_admin, current_oc, sudah_login, user_data)
        user_monster, user_potion = separate_monster_item_inventory(make_inventory(id, monster_inventory_data, monster_data, item_inventory_data))
    elif masukan =="HELP":
        sudah_login, username = help(sudah_login, is_admin, username)
    elif masukan == "LOGOUT":
        sudah_login = logout_user(sudah_login)
    elif masukan == "EXIT":
        program = exit(program)

    if sudah_login:
        if masukan == "SAVE":
            save(id, user_data,monster_inventory_data,item_inventory_data, monster_shop_data,item_shop_data, monster_data, is_admin)
        if is_admin:#AKSES: ADMIN
            if masukan == "SHOP":
                monster_shop_data,item_shop_data=shop_management(monster_data,monster_shop_data,item_shop_data, item_inventory_data) #aman
            elif masukan == "MONSTER":
                monster_data = monster_management(monster_data) #AMAN
        else: #AKSES: AGENT   
            if masukan=="INVENTORY": #AMAN
                inventory(id, current_oc, monster_inventory_data, monster_data, item_inventory_data) #AMAN
            elif masukan=="BATTLE": #AMAN
                user_potion, current_oc = battle(username, user_monster, user_potion, monster_data,current_oc) #aman
            elif masukan=="ARENA": #AMAN
                user_potion, current_oc = arena(username, user_monster, user_potion, monster_data,current_oc=0)
            elif masukan=="SHOP":
                user_monster, user_potion, current_oc, item_shop_data =shop(monster_shop_data,user_data, item_shop_data, user_monster, monster_data, current_oc, user_potion) #aman
            elif masukan=="LABORATORY":
                user_monster, current_oc = laboratory(username,current_oc, user_monster) #AMAN
        
        


