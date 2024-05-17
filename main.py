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

id='5' #dummy id
sudah_login=False
is_admin=False
program = True

user_data,monster_data,monster_inventory_data,item_inventory_data,item_shop_data,monster_shop_data=load()

while program:
    
    masukan = input(">>>").upper()
    if masukan == "REGISTER":
        sudah_login, username = register_user(sudah_login, user_data)
    elif masukan =="LOGIN":
        sudah_login, username, is_admin = login_user(sudah_login)
    elif masukan =="HELP":
        sudah_login, username = help(sudah_login, is_admin, username)
    elif masukan == "LOGOUT":
        sudah_login = logout_user(sudah_login)
    elif masukan == "EXIT":
        program = exit(program)

    if sudah_login:
        if is_admin:#AKSES: ADMIN
            if masukan == "SHOP":
                shop_management()
            elif masukan == "MONSTER":
                monster_management()
        else: #AKSES: AGENT   
            if masukan=="INVENTORY":
                inventory(username)
            elif masukan=="BATTLE":
                battle(username, user_inventory)
            elif masukan=="ARENA":
                arena(username)
            # elif masukan=="SHOP & CURRENCY":
            #     shop_currency(sudah_login, username)
            elif masukan=="LABORATORY":
                laboratory(username)
        
        


