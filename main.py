import sys
sys.path.append('src')
import argparse

from battle_and_arena import battle, arena
from inventory import *
from utils import fetch_data
from menu_and_help import help
from laboratory import laboratory
from monster_management import monster_management
from save_and_load import save, load
from globevar import *
from shop_and_currency import shop
from exit import exit
from shop_management import shop_management
from register import register_user
from login_logout import login_user,logout_user


sudah_login=False
is_admin=False
program = True
id,username,user_monster,user_potion = 0,"",{},{}


while program:
    
    masukan = input(">>>").upper()
    if masukan == "REGISTER": #aman100
        sudah_login,username,id,user_data,user_monster,user_potion, monster_inventory_data = register_user(id,username,user_monster,user_potion,sudah_login, user_data,monster_inventory_data, monster_data, item_inventory_data)
        current_oc = 1000
    elif masukan =="LOGIN": #aman100
        sudah_login, username, is_admin, id,current_oc = login_user(id, username, is_admin, sudah_login, user_data)
        user_monster, user_potion = separate_monster_item_inventory(make_inventory(id, monster_inventory_data, monster_data, item_inventory_data))
    elif masukan =="HELP": #aman100
        help(sudah_login, is_admin, username)
    elif masukan == "LOGOUT": #aman100
        sudah_login = logout_user(sudah_login)
    elif masukan == "EXIT":
        program = exit(program, id, user_data,monster_inventory_data,item_inventory_data, monster_shop_data, item_inventory_data, monster_data, is_admin)

    if sudah_login:
        if masukan == "SAVE":
            save(id, user_data,monster_inventory_data,item_inventory_data, monster_shop_data,item_shop_data, monster_data, is_admin)
        if is_admin:#AKSES: ADMIN
            if masukan == "SHOP":
                monster_shop_data,item_shop_data=shop_management(monster_data,monster_shop_data,item_shop_data, item_inventory_data) #aman
            elif masukan == "MONSTER":
                monster_data = monster_management(monster_data) #AMAN
        else: #AKSES: AGENT   
            if masukan=="INVENTORY": #AMAN100
                inventory(id, current_oc, monster_inventory_data, monster_data, item_inventory_data) #AMAN
            elif masukan=="BATTLE": #AMAN100
                user_potion, current_oc = battle(id, username, monster_inventory_data, item_inventory_data, monster_data,current_oc) #aman
            elif masukan=="ARENA": #AMAN100
                user_potion, current_oc = arena(id, username, monster_inventory_data, item_inventory_data, monster_data,current_oc)
            elif masukan=="SHOP": #aman100
                monster_inventory_data, item_inventory_data, current_oc, item_shop_data =shop(monster_shop_data, item_shop_data, monster_data, current_oc, monster_inventory_data, item_inventory_data, id) 
            elif masukan=="LABORATORY":#aman100
                user_monster, current_oc = laboratory(username,current_oc, monster_inventory_data, item_inventory_data, id,monster_data) #AMAN
        
        


