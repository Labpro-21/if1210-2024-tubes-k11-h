#HELPER FUNCTION
def fetch_data(path):
    data = {}

    file = open(path, 'r')
    lines = []
    for i in file:
        lines.append(i)
    keys = parser(lines[0])

    for i in keys:
        data[i] = []
    for i in range(1, len(lines)):
        array = parser(lines[i])
        
        for j, key in enumerate(keys):
            data[key].append(array[j])

    file.close()
    
    return data

def parser(value, splitter=";"):
    arr = []
    kata=""
    for i in value:
        if i!=splitter and i!='\n':
            kata+=i
        else:
            arr.append(kata)
            kata=""
    if kata:
        arr.append(kata)
    return arr

def search_index(data, key, value):
    index = 0
    while index<=len(data) and data[key][index] != value:
        index+=1
    if index == len(data)+1: #kalau gak ketemu
        return -9999
    else:
        return index #indeks kalau ketemu
    
def printDict(dictionary):
    for key in dictionary:
        print(f"{key}: {dictionary[key]}")


def write_dict_of_arr(dictionary:dict ):
    first_elem=None

    for key in dictionary:
        first_elem=key
        break

    many_row=len(dictionary[first_elem])
    many_column=len(dictionary)
    sentence=''

    idx=0
    for key in dictionary: 
        if  idx!=many_column-1:
            sentence=sentence+f'{key}'+';'
        else:
            sentence=sentence+f'{key}'+'\n'
        idx+=1

    idx=0

    for i in range(many_row):
        idx=0
        for key in dictionary:

            if  idx!=many_column-1:
                sentence += f"{dictionary[key][i]}"+';'
            else:
                sentence=sentence + f"{dictionary[key][i]}"+"\n"
            idx+=1
    return sentence


def write_monst_inventory(monster_inventory_data, monst, id, monster_data):
    arr_modified=[]
    print(monst)

    for key in monst:   #aku pengen outputnya agar bentuknya [id, monst_id, level]
        monst_id=str(search_index(monster_data, 'type', monst[key]["Name"])+1)
        monst_level=str(monst[key]['Level'])
        arr_modified.append([id, monst_id, monst_level])
    
    sentence=write_dict_of_dict(monster_inventory_data, arr_modified, 'level', id)
    return sentence

def write_item_inventory(item_inventory_data , item, id ):
    arr_modified=[]

    for key in item:   #aku pengen outputnya agar bentuknya [id, monst_id, level]
        potion_name=str(item[key]["Type"])
        quantity=str(item[key]['Quantity'])
        arr_modified.append([id, potion_name, quantity])
    sentence=write_dict_of_dict(item_inventory_data, arr_modified, 'quantity', id)
    return sentence

def write_dict_of_dict(data, arr_modified, last_column, id):
    sentence=''
    many_column=len(data)
    already_modified=False
    first_elem=None
    idx=0

    for key in data:
        first_elem=key
        break

    for key in data: 
        if  idx!=many_column-1:
            sentence=sentence+f'{key}'+';'
        else:
            sentence=sentence+f'{key}'+'\n'
        idx+=1

    idx=0

    for i in  range (len(data[f'{first_elem}'])):
        for key in data:
            item=data[key][idx]
            user_id=data[f'{first_elem}'][idx]
            if not already_modified and int(user_id) == int(id):
                for elem in arr_modified:
                    sentence=sentence + elem[0]+';'+ elem[1]+ ';'+ elem[2]+ '\n'
                already_modified=True
            elif key==f'{last_column}' and int(user_id) != int(id):
                sentence=sentence +f"{item}"+ "\n" 
            elif int(user_id) != int(id) and idx!=many_column-1:
                sentence= sentence + f'{item}' + ';'

            continue
        idx+=1
    return sentence


def isallnumber(string):
    angka = ['0','1','2','3','4','5','6','7','8','9']
    for i in string:
        if i not in angka:
            return False
    return True

def validate_input(user_input):
    # Check if input is not all digits
    if isallnumber(user_input):
        return False

    # Check for allowed characters (alphanumeric, _, -)
    allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
    
    for char in user_input:
        if char not in allowed_characters:
            return False

    return True
