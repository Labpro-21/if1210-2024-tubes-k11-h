import time
from utils import search_index,outputDict,isallnumber,validate_input, in_game_validate_input
from typing import Dict, List, Tuple, Union, Optional

DictOfArr = Dict[str, List[Union[str, int]]]
DictOfDict = Dict[str, Dict[str, Union[str, int]]]

#REALISASI FUNGSI-FUNGSI
def inventory(id, current_oc:int,
              monster_inventory_data: DictOfArr, 
              monster_data: DictOfArr, 
              item_inventory_data: DictOfArr):#F07
    
    output(f"=======INVENTORY LIST (User ID: {id})=======")
    output(f"Jumlah O.W.C.A. Coin-mu sekarang {current_oc}.")
    inventory = make_inventory(id, monster_inventory_data, monster_data, item_inventory_data)
    key traversal inventory
        if inventory[key]['Type']=='Monster' then 
            tipe=inventory[key]['Type']
            nama=inventory[key]['Name']
            lvl=inventory[key]['Level']
            hp=inventory[key]['HP']
            output(f"{key}. {tipe} (Name: {nama}, Lvl: {lvl}, HP: {hp}) ")
        else
            tipe=inventory[key]['Type']
            potion_name=inventory[key]['Potion_Name']
            quantity=inventory[key]['Quantity']
            output(f"{key}. {tipe} (Type: {potion_name}, Qty: {quantity}) ")

    output()
    output("Ketikkan id untuk menampilkan detail item: ")
    pilihan = input(">>> ").upper()
    output()
    
    while pilihan!="KELUAR" do
        if isallnumber(pilihan) and int(pilihan)<=(len(inventory)) then
            outputDict(inventory[int(pilihan)])
        else
            output("Tidak dapat menampilkan detail item")

        output()
        output("Ketikkan id untuk menampilkan detail item: ")
        pilihan = input(">>> ").upper()
        output()

def calc_stats(level:int, base_stats:int) ->int:
    battle_stats=int(base_stats)+(level-1)*0.1*int(base_stats)
    return int(battle_stats)        

def make_inventory(user_id, monster_inventory_data: DictOfArr, 
                   monster_data: DictOfArr, 
                   item_inventory_data: DictOfArr) -> DictOfArr:
    id=1
    inventory = {}
    i traversal [0..len(monster_inventory_data["user_id"])] #iterasi semua data pada monster_inventory
        if int(monster_inventory_data["user_id"][i])==int(user_id) then
            monster_id = monster_inventory_data["monster_id"][i]
            index=None
            j=0
            item traversal monster_data['id']
                if item==monster_id then
                    index=j
                j+=1
                    break
            monster_name = monster_data["type"][index]
            monster_level = int(monster_inventory_data["level"][i])
            monster_hp = calc_stats(monster_level, int(monster_data["hp"][index]))
            monster_atk = calc_stats(monster_level, int(monster_data["atk_power"][index]))
            monster_def = calc_stats(monster_level, int(monster_data["def_power"][index]))

            inventory[id] = {'Type': 'Monster',
                                'Name'      : monster_name,
                                'ATK_Power' : monster_atk,
                                'DEF_Power' : monster_def,
                                'HP'        : monster_hp,
                                'Level'     : monster_level}

            id+=1


    i traversal [0..len(item_inventory_data["user_id"])] #iterasi semua data pada item_inventory
        if int(item_inventory_data["user_id"][i])==int(user_id) then
            item_type = item_inventory_data["type"][i]
            item_quantity = item_inventory_data["quantity"][i]

            inventory[id] = {'Type': 'Potion',
                                'Potion_Name'    : item_type, 
                                'Quantity': item_quantity}

            id+=1
    return inventory


def separate_monster_item_inventory (inventory: DictOfArr) -> DictOfDict:
    potion_dict:dict={}
    user_monster:dict={}

    id_monst=1
    id_potion=1
    key traversal (inventory)
        if inventory[key]['Type']=='Potion' then
            potion_dict[id_potion]={}
            potion_dict[id_potion]['Type']=inventory[key]['Potion_Name']
            potion_dict[id_potion]['Quantity']=inventory[key]['Quantity']
            id_potion=id_potion+1
        else
            user_monster[id_monst]={}
            user_monster[id_monst]['Name']=inventory[key]['Name']
            user_monster[id_monst]['ATK_Power']=inventory[key]['ATK_Power']
            user_monster[id_monst]['DEF_Power']=inventory[key]['DEF_Power']
            user_monster[id_monst]['HP']=inventory[key]['HP']
            user_monster[id_monst]['Level']=inventory[key]['Level']
            id_monst=id_monst+1
    return user_monster,potion_dict

