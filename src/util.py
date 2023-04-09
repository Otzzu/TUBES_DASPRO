import var
from typing import *

def getIndex(arr, by, func):
    for i in range(0, arr[1]):
        if func(arr[0][i], by):
            return i

    return -1

def add(data, arr):
    temp = ["" for i in range(arr[1] + 1)]

    for i in range(0, arr[1]+1):
        if i != arr[1]:
            temp[i] = arr[0][i]
        else:
            temp[i] = data

    return (temp, arr[1] + 1)

def delete(arr, by, func):
    temp = ["" for i in range(arr[1])]

    pengurang: int = 0
    for i in range(0, arr[1]):
        if func(arr[0][i], by):
            pengurang = pengurang + 1
        else:
            temp[i - pengurang] = arr[0][i]

    temp2 = temp
    temp = [temp2[i] for i in range(arr[1]-pengurang)]

    return (temp, arr[1] - pengurang)    

def generateIdCandi() -> int:
    idCandi: int = 1
    while True:
        ada: bool = False
        for i in range(var.candi[1]):
            if var.candi[0][i][0] == idCandi:
                ada = True
                break
        if ada:
            idCandi = idCandi + 1
        else:
            break
    return idCandi

def filterArr(arr, func):
    temp = ([],0)
    
    for i in range(arr[1]):
        if (func(arr[0][i])):
            temp = add(arr[0][i], temp)
    
    return temp

def validasiPassword(password: str) -> bool:
    passwordTemp = password + "@"

    panjangPass = 0
    while True:
        if passwordTemp[panjangPass] != "@":
            panjangPass = panjangPass + 1
        elif passwordTemp[panjangPass] == "@":
            break

    return (5 <= panjangPass <= 25)

def logout():
    var.currentUser = ("", "", "")
    print(var.currentUser)
    
def readCSV(path, tipe):
    panjangSatuData: int = 0;
    if tipe == "user" or tipe == "bahan": panjangSatuData = 3
    elif tipe == "candi": panjangSatuData = 5
    
    file = open(path, "r")
    
    line: str= file.readline() + "@"
    
    temp = ([], 0)
    while line != "@":
        i: int = 0
        data: List[str] = ["" for i in range(panjangSatuData)]
        indexData: int = 0
        word: str = ""
        while indexData < panjangSatuData:
            if line[i] == ";" or line[i] == "@" or line[i] == "\n":
                data[indexData] = word
                indexData = indexData + 1
                word = ""
            else:
                word = word + line[i]
            i = i + 1
        
        if tipe == "bahan": 
            data[2] = int(data[2])
        elif tipe == "candi": 
            data[0] = int(data[0])
            data[2] = int(data[2])
            data[3] = int(data[3])
            data[4] = int(data[4])
            
        temp = add(tuple(data), temp)
        line = file.readline() + "@"
        
    print(temp)
    return temp
    
def readCSVUser(url: str):
    file = open(url, "r")
    
    line: str= file.readline() + "@"
    
    user: Tuple[List[Tuple[str,str,str]], int] = ([], 0)
    while line != "@":
        i: int = 0
        data: List[str] = ["","",""]
        indexData: int = 0
        word: str = ""
        while indexData < 3:
            if line[i] == ";" or line[i] == "@" or line[i] == "\n":
                data[indexData] = word
                indexData = indexData + 1
                word = ""
            else:
                word = word + line[i]
            i = i + 1
            
        user = add(tuple(data), user)
        line = file.readline() + "@"
        
    print(user)
    return user

def readCSVCandi(url: str):
    file = open(url, "r")
    
    line: str= file.readline() + "@"
    
    candi: Tuple[List[Tuple[int,str,int,int,int]], int] = ([], 0)
    while line != "@":
        i: int = 0
        data: List[str] = ["","","","",""]
        indexData: int = 0
        word: str = ""
        while indexData < 5:
            if line[i] == ";" or line[i] == "@" or line[i] == "\n":
                data[indexData] = word
                indexData = indexData + 1
                word = ""
            else:
                word = word + line[i]
            i = i + 1
        
        data[0] = int(data[0])
        data[2] = int(data[2])
        data[3] = int(data[3])
        data[4] = int(data[4])
            
        candi = add(tuple(data), candi)
        line = file.readline() + "@"
        
    print(candi)
    return candi

def readCSVBahan(url: str):
    file = open(url, "r")
    
    line: str= file.readline() + "@"
    
    bahanBangunan: Tuple[List[Tuple[int,str,int,int,int]], int] = ([], 0)
    while line != "@":
        i: int = 0
        data: List[str] = ["","",""]
        indexData: int = 0
        word: str = ""
        while indexData < 3:
            if line[i] == ";" or line[i] == "@" or line[i] == "\n":
                data[indexData] = word
                indexData = indexData + 1
                word = ""
            else:
                word = word + line[i]
            i = i + 1
        
        data[2] = int(data[2])
            
        bahanBangunan = add(tuple(data), bahanBangunan)
        line = file.readline() + "@"
        
    print(bahanBangunan)
    return bahanBangunan
  
def writeCSV(url: str, data: str):
    file = open(url, "w")  
    file.write(data)
    
    
# readCSV("data/user.csv")
# writeCSV("data/user.csv", "basi;12345678;pengemis\nbadi;12345678;pengemis")
# readCSVUser("data/user.csv")
# readCSVCandi("data/candi.csv")
# readCSVBahan("data/bahan_bangunan.csv")
