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

def make_arr(file_name):
    with open(f'{file_name}', 'r') as file:
        next(file)
        arr=[]
        for line in file:
            b=parser(line)
            arr.append(b)
    return arr

def write_data(dictionary:dict ):
    
    first_key = next(iter(dictionary))
    many_row=len(dictionary[f'{first_key}'])
    many_column=len(dictionary)
    sentence=''
    idx=0

    for key in dictionary: 
        if  idx!=many_column-1:
            sentence=sentence+f'{key}'+';'
        else:
            sentence=sentence+f'{key}'+'\n'
        idx+=1
    for i in range(many_row):
        idx=0
        for key in dictionary:
            if  idx!=many_column-1:
                sentence += f"{dictionary[key][i]};"
            else:
                sentence=sentence + f"{dictionary[key][i]}\n"
            idx+=1
    return sentence