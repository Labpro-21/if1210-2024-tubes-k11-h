import sys
sys.path.append('src')

from battle import *
from func import *
from globevar import *
from utils import *


id='5' #dummy id
sudah_login=False
program = True
user_inventory = make_inventory(id)
while program:
    
    masukan = input(">>>").upper()
    '''
    if masukan == "REGISTER":
        register_user()
    
    elif masukan=="INVENTORY":
        inventory()
    elif masukan == "LOGOUT":
        logout()
    '''
    if masukan =="LOGIN":
        username = login_user()
    elif masukan=="BATTLE":
        battle(user_inventory, username)
    elif masukan=="ARENA":
        arena(username)
    # if masukan == "SHOP":
    #     shop_management()


