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
        print(f"{key}: {dictionary[key][0]}")

def make_arr(file_name):
    with open(f'{file_name}', 'r') as file:
        next(file)
        arr=[]
        for line in file:
            b=parser(line)
            arr.append(b)
    return arr

def SPLIT (sentence, pemisah=','):
    arr=[]
    splitted=""
    for char in sentence:
        if char==pemisah:
            arr=arr+[splitted]
            splitted=""
        if char!=pemisah:
            splitted=splitted+char
    arr=arr+[splitted]
    return arr