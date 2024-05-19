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
    while index<=len(data[key]) and data[key][index] != value:
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

def in_game_validate_input(masukan:str, condition, pesan,warning=''):
    while True:
        if isallnumber(masukan) and 0<int(masukan)<=condition :
            return masukan
        print(warning)
        masukan = input(pesan)