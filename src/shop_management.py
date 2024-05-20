from utils import search_index, isallnumber,in_game_validate_input
from typing import Dict, List, Tuple, Union, Optional

DictOfArr = Dict[str, List[Union[str, int]]]
DictOfDict = Dict[str, Dict[str, Union[str, int]]]

def shop_management(monster_data: DictOfArr,
                    monster_shop_data: DictOfArr,
                    item_shop_data: DictOfArr) -> Tuple[DictOfArr,DictOfArr]:

    shop = True
    print("Irasshaimase! Selamat datang kembali, Mr. Monogram!")
    while shop==True:
        aksi = input(">>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")
        if aksi=="lihat":
            lihat_apa = input(">>> Mau lihat apa? (monster/potion): ")
            if lihat_apa=="monster":
                print("ID | Type | ATK Power | DEF Power | HP | Stok | Harga")
                for i in range(len(monster_shop_data["monster_id"])):
                    id = monster_shop_data["monster_id"][i]
                    index = search_index(monster_data, "id",id)
                    print(f"{id} | {monster_data['type'][index]} | {monster_data['atk_power'][index]} | {monster_data['def_power'][index]} | {monster_data['hp'][index]} | {monster_shop_data['stock'][i]} | {monster_shop_data['price'][i]}")
            elif lihat_apa=="potion":
                print("ID | Type | Stok | Harga")
                for i in range(len(item_shop_data["type"])):
                    print(f" {i+1} | {item_shop_data['type'][i]} | {item_shop_data['stock'][i]} | {item_shop_data['price'][i]}")
        elif aksi=="tambah":
            tambah_apa = input(">>> Mau tambah apa? (monster/potion): ")
            
            if tambah_apa=="monster":
                monster_not_in_shop_data = { #inisiasi untuk data monster yang tidak ada pada shop
                    "id":[],
                    "type":[],
                    "atk_power":[],
                    "def_power":[],
                    "hp":[]
                }
                for i in range(len(monster_data["id"])): #isi data monster yang tidak ada pada shop
                    if not(monster_data["id"][i] in monster_shop_data["monster_id"]):
                        monster_not_in_shop_data["id"].append(monster_data["id"][i])
                        monster_not_in_shop_data["type"].append(monster_data["type"][i])
                        monster_not_in_shop_data["atk_power"].append(monster_data["atk_power"][i])
                        monster_not_in_shop_data["def_power"].append(monster_data["def_power"][i])
                        monster_not_in_shop_data["hp"].append(monster_data["hp"][i])

                for i in range(len(monster_not_in_shop_data["id"])): #print data monster yang tidak ada pada shop
                    print(f"{monster_not_in_shop_data['id'][i]} | {monster_not_in_shop_data['type'][i]} | {monster_not_in_shop_data['atk_power'][i]} | {monster_not_in_shop_data['def_power'][i]} | {monster_not_in_shop_data['hp'][i]} | ")

                
                if len(monster_not_in_shop_data["id"])==0:
                    print("Tidak ada monster yang dapat ditambahkan!")
                else: #isi data monster yang tidak ada pada shop
                    while True:
                        id = input(">>> Masukkan id monster: ")
                        stock = input(">>> Masukkan stok awal: ")
                        price = input(">>> Masukkan harga: ")
                        if (id in monster_not_in_shop_data["id"] and isallnumber(id) and isallnumber(stock) and isallnumber(price)):
                            break
                        else: print("Masukan salah! id tidak ditemukan!")

                    #update monster di shop
                    monster_shop_data["monster_id"].append(id)
                    monster_shop_data["stock"].append(stock)
                    monster_shop_data["price"].append(price)

                    index = search_index(monster_not_in_shop_data, 'id', id)
                    print(f"{monster_not_in_shop_data['type'][index]} telah berhasil ditambahkan ke dalam shop!")

                    monster_not_in_shop_data['type'].pop(index)
                    monster_not_in_shop_data['atk_power'].pop(index)
                    monster_not_in_shop_data['def_power'].pop(index)
                    monster_not_in_shop_data['hp'].pop(index)
                    monster_not_in_shop_data['id'].pop(index)


            elif tambah_apa=="potion":
                potion_database=['Strength', 'Resilience', 'Healing']
                item_not_in_shop_data = { #inisiasi untuk data item yang tidak ada pada shop
                    "type":[],
                }
                for i in range(len(potion_database)): #isi data potion yang tidak ada pada shop
                    if not(potion_database[i] in item_shop_data["type"]):
                        item_not_in_shop_data["type"].append(potion_database[i])

                for i in range(len(item_not_in_shop_data["type"])): #print data potion yang tidak ada pada shop
                    print(f"{i+1} | {item_not_in_shop_data['type'][i]} ")

                if len(item_not_in_shop_data["type"])==0:
                    print("Tidak ada item yang dapat ditambahkan!")
                else: #isi data item yang tidak ada pada shop
                    while True:
                        id = input(">>> Masukkan id potion: ")
                        id= in_game_validate_input(id, len(item_not_in_shop_data), ">>> Masukkan id potion: ", "Masukan salah, silahkan input ulang")
                        tipe = item_not_in_shop_data["type"][int(id)-1]
                        stock = input(">>> Masukkan stok awal: ")
                        price = input(">>> Masukkan harga: ")
                        if (tipe in item_not_in_shop_data["type"] and isallnumber(stock) and isallnumber(price)):
                            break
                        else: print("Masukan salah! id tidak ditemukan!")
                    #isi data item yang tidak ada pada shop
                    

                    #update item di shop
                    item_shop_data["type"].append(tipe)
                    item_shop_data["stock"].append(stock)
                    item_shop_data["price"].append(price)


                    print(f"{item_not_in_shop_data['type'][int(id)-1]} telah berhasil ditambahkan ke dalam shop!")
                    item_not_in_shop_data['type'].pop(int(id)-1)


        elif aksi=="ubah":
            ubah_apa = input(">>> Mau ubah apa? (monster/potion): ")
            
            if ubah_apa=="monster":
                print("ID | Type | ATK Power | DEF Power | HP | Stok | Harga")
                for i in range(len(monster_shop_data["monster_id"])):
                    id = monster_shop_data["monster_id"][i]
                    index = search_index(monster_data, "id",id)
                    print(f"{id} | {monster_data['type'][index]} | {monster_data['atk_power'][index]} | {monster_data['def_power'][index]} | {monster_data['hp'][index]} | {monster_shop_data['stock'][i]} | {monster_shop_data['price'][i]}")
                
                if len(monster_shop_data["monster_id"])==0:
                    print("Tidak ada monster yang dapat diubah!")
                else: #isi data monster yang tidak ada pada shop
                    while True:
                        id = input(">>> Masukkan id monster: ")
                        stock = input(">>> Masukkan stok baru: ")
                        price = input(">>> Masukkan harga baru: ")
                        if (id in monster_shop_data["monster_id"] and ((stock and isallnumber(stock)) or (price and isallnumber(price))) and isallnumber(id)):
                            break
                        else: print("Masukan salah! silahkan ulang!")

                    #update monster di shop
                    if stock:
                        monster_shop_data["stock"][int(id)-1] = stock
                    if price:
                        monster_shop_data["price"][int(id)-1] = price

                    # index = search_index(monster_shop_data, 'monster_id', id)
                    
                    if stock and price:
                        print(f"{monster_data['type'][int(id)-1]} telah berhasil diubah ke dalam shop dengan stok baru {stock} dan harga baru {price}!")
                    elif stock:
                        print(f"{monster_data['type'][int(id)]-1} telah berhasil diubah ke dalam shop dengan stok baru {stock}!")
                    elif price:
                        print(f"{monster_data['type'][int(id)]-1} telah berhasil diubah ke dalam shop dengan harga baru {price}!")

            elif ubah_apa=="potion":
                print("ID | Type | Stok | Harga")
                for i in range(len(item_shop_data["type"])):
                    tipe = item_shop_data["type"][i]
                    print(f"{i+1} | {item_shop_data['type'][i]} | {item_shop_data['stock'][i]} | {item_shop_data['price'][i]}")
                
                if len(item_shop_data["type"])==0:
                    print("Tidak ada item yang dapat diubah!")
                else: #isi data item yang tidak ada pada shop
                    while True:
                        id = input(">>> Masukkan id item: ")
                        stock = input(">>> Masukkan stok baru: ")
                        price = input(">>> Masukkan harga baru: ")
                        if (isallnumber(id) and int(id) <= len(item_shop_data["type"]) and ((stock and isallnumber(stock)) or (price and isallnumber(price))) and isallnumber(id)):
                            break
                        else: print("Masukan salah! silahkan ulang!")

                    #update item di shop
                    if stock:
                        item_shop_data["stock"][int(id)-1] = stock
                    if price:
                        item_shop_data["price"][int(id)-1] = price

                    # id = search_index(item_shop_data, 'item_id', id)
                    
                    if stock and price:
                        print(f"{item_shop_data['type'][int(id)-1]} telah berhasil diubah ke dalam shop dengan stok baru {stock} dan harga baru {price}!")
                    elif stock:
                        print(f"{item_shop_data['type'][int(id)]-1} telah berhasil diubah ke dalam shop dengan stok baru {stock}!")
                    elif price:
                        print(f"{item_shop_data['type'][int(id)]-1} telah berhasil diubah ke dalam shop dengan harga baru {price}!")
        
        elif aksi=="hapus":
            hapus_apa = input(">>> Mau hapus apa? (monster/potion): ")
            if hapus_apa=="monster":
                print("ID | Type | ATK Power | DEF Power | HP | Stok | Harga")
                for i in range(len(monster_shop_data["monster_id"])):
                    id = monster_shop_data["monster_id"][i]
                    index = search_index(monster_data, "id",id)
                    print(f"{id} | {monster_data['type'][index]} | {monster_data['atk_power'][index]} | {monster_data['def_power'][index]} | {monster_data['hp'][index]} | {monster_shop_data['stock'][i]} | {monster_shop_data['price'][i]}")

                if len(monster_shop_data["monster_id"])==0:
                    print("Tidak ada monster yang dapat dihapus!")
                else: #isi data monster yang tidak ada pada shop
                    while True:
                        id = input(">>> Masukkan id monster: ")
                        if (id in monster_shop_data["monster_id"]):
                            index = search_index(monster_data, "id",id)
                            monster_name = monster_data["type"][int(index)]
                            yakin = input(f">>> Apakah anda yakin ingin menghapus {monster_name} dari shop (y/n)? ")
                            if yakin == "y":
                                index = search_index(monster_data, "id", id)
                                print(f"{monster_data['type'][index]} telah berhasil dihapus dari shop!")
                                index = search_index(monster_not_in_shop_data, 'id', id)
                                monster_shop_data["monster_id"].pop(index)
                                monster_shop_data["stock"].pop(index)
                                monster_shop_data["price"].pop(index)
                                break
                        else: print("Masukan salah! silahkan ulang!")
            elif hapus_apa=="potion":
                print("ID | Type | Stok | Harga")
                for i in range(len(item_shop_data["type"])):
                    print(f"{i+1} | {item_shop_data['type'][i]} | {item_shop_data['stock'][i]} | {item_shop_data['price'][i]}")

                if len(item_shop_data["type"])==0:
                    print("Tidak ada item yang dapat dihapus!")
                else: #isi data item yang tidak ada pada shop
                    while True:
                        id = input(">>> Masukkan id item: ")
                        if isallnumber(id) and (int(id) <=len(item_shop_data["type"])):
                            item_name = item_shop_data["type"][int(id)-1]
                            yakin = input(f">>> Apakah anda yakin ingin menghapus {item_name} dari shop (y/n)? ").upper()
                            if yakin == "Y":
                                print(f"{item_shop_data['type'][int(id)-1]} telah berhasil dihapus dari shop!")
                                item_shop_data["type"].pop(int(id)-1)
                                item_shop_data["stock"].pop(int(id)-1)
                                item_shop_data["price"].pop(int(id)-1)
                                break
                            elif yakin =='N':
                                print(f"{item_shop_data['type'][int(id)-1]} tidak jadi dihapus dari shop!")
                                break
                            else:
                                print("Masukan salah, silahkan ulangi lagi")
                        else: print("Masukan salah! silahkan ulang!")

                    # index = search_index(monster_shop_data, 'monster_id', id)
                    
        elif aksi=="keluar":
            shop=False
            return monster_shop_data,item_shop_data
