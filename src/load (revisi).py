import argparse
import sys
import os

#Argparse untuk pemanggilan program
parser = argparse.ArgumentParser()
parser.add_argument('Parent_Folder', metavar='folder', type=str, help='Masukkan Folder Penyimpanan')
args = parser.parse_args()
folder = args.Parent_Folder

#Inisiasi Dictionary
user={} #Dict user.csv
monster={} #Dict monster.csv
monster_inventory={} #Dict monster_shop.csv
item_inventory={} #Dict item_inventory.csv
item_shop={} #Dict item_shop.csv
monster_shop={} #Dict monster_shop.csv

def split(str, separator):
    hasil = []
    kata = ''
    for char in str:
        if char == separator:
            hasil.append(kata)
            kata = ''
        else:
            kata += char
    hasil.append(kata)
    return hasil

def data(nama):
    with open(f'{folder}/{nama}.csv', 'r') as file:
        data = file.read()
    rows=split(data,"\n")

    return rows

def userr():
    rows=data("user")
    for row in rows:
        info=split(row, ',')
        if info[0] != "":
            user_id=info[0]
            username=info[1]
            password=info[2]
            role=info[3]
            oc=info[4]
            if user_id =="id":
                next
            else:
                user[user_id] = {'username': username, 'password': password, 'role': role, 'oc': oc}

def monsterr():
    rows=data("monster")
    for row in rows:
        info=split(row, ',')
        if info[0] != "":        
            id=info[0]
            type=info[1]
            atk_power=info[2]
            def_power=info[3]
            hp=info[4]
            if id =="id":
                next
            else:
                monster[id] = {'type': type, 'atk_power': atk_power, 'def_power': def_power, 'hp': hp}

def itemi():
    rows=data("item_inventory")
    for row in rows:
        info=split(row, ',')
        if info[0] != "":
            user_id=info[0]
            type=info[1]
            quantity=info[2]
            if user_id =="user_id":
                next
            elif user_id in item_inventory:
                item_inventory[user_id].append({'type': type, 'quantity': quantity})
            else:
                item_inventory[user_id] = [{'type': type, 'quantity': quantity}]

def monsteri():
    rows=data("monster_inventory")
    for row in rows:
        info=split(row, ',')
        if info[0] != "":
            user_id=info[0]
            monster_id=info[1]
            level=info[2]
            if user_id =="user_id":
                next
            elif user_id in monster_inventory:
                monster_inventory[user_id].append({'monster_id': monster_id, 'level': level})
            else:
                monster_inventory[user_id] = [{'monster_id': monster_id, 'level': level}]

def items():
    rows=data("item_shop")
    for row in rows:
        info=split(row, ',')
        if info[0] != "":
            id=info[0]
            type=info[1]
            stock=info[2]
            price=info[3]
            if id =="id":
                next
            elif id in item_shop:
                item_shop[id].append({'type': type, 'stock': stock, 'price': price})
            else:
                item_shop[id] = {'type': type, 'stock': stock, 'price': price}

def monsters():
    rows=data("monster_shop")
    for row in rows:
        info=split(row, ',')
        if info[0] != "":
            monster_id=info[0]
            stock=info[1]
            price=info[2]
            if monster_id =="monster_id":
                next
            elif monster_id in monster_shop:
                monster_shop[monster_id].append({'stock': stock, 'price': price})
            else:
                monster_shop[monster_id] = {'stock': stock, 'price': price}

print("Loading ... ")
if not os.path.exists(folder) :
        print('Folder "%s" tidak ditemukan!'%folder)
        sys.exit()
elif not folder : 
    print("Tidak ada nama folder yang diberikan!") 
    sys.exit()

userr()
monsterr()
itemi()
monsteri()
items()
monsters()

if os.path.exists(folder) : 
        print("Folder ditemukan!")
        os.chdir(folder)
        print("Selamat datang di OWCA!")