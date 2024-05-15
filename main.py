import sys
sys.path.append('src')

from battle_and_arena import battle, arena
from func import *
from globevar import *
from utils import fetch_data
from menu_and_help import help
from laboratory import laboratory
from monster_management import monster_management

id='5' #dummy id
sudah_login=False
is_admin=False
program = True
user_data = fetch_data('../main/data/user.csv')
user_inventory = make_inventory(id)
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


    #AKSES: AGENT
    elif masukan=="INVENTORY":
        inventory(sudah_login, is_admin, username)
    elif masukan=="BATTLE":
        battle(sudah_login, is_admin, username, user_inventory)
    elif masukan=="ARENA":
        arena(sudah_login, is_admin, username)
    # elif masukan=="SHOP & CURRENCY":
    #     shop_currency(sudah_login, username)
    elif masukan=="LABORATORY":
        laboratory(sudah_login, is_admin, username)
    
        
    #AKSES: ADMIN
    elif masukan == "SHOP":
        shop_management(sudah_login, is_admin)
    elif masukan == "MONSTER":
        monster_management(sudah_login, is_admin)


