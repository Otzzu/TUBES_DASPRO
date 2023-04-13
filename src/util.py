import var
from typing import *
from collections.abc import Callable


def getIndex(arr: Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int], func: Callable[[int], bool] | Callable[[str], bool]) -> int:
    for i in range(0, arr[1]):
        if func(arr[0][i]):
            return i

    return -1


def add(data: Tuple[str, str, str] | Tuple[int, str, int, int, int] | Tuple[Tuple[str, str, str], Tuple[List[Tuple[int, str, int, int, int]], int]], arr: Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int] | Tuple[List[Tuple[Tuple[str, str, str], Tuple[List[Tuple[int, str, int, int, int]], int]]], int]) -> Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int] | Tuple[List[Tuple[Tuple[str, str, str], Tuple[List[Tuple[int, str, int, int, int]], int]]], int]:
    temp = ["" for i in range(arr[1] + 1)]

    for i in range(0, arr[1]+1):
        if i != arr[1]:
            temp[i] = arr[0][i]
        else:
            temp[i] = data

    return (temp, arr[1] + 1)


def delete(arr: Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int], func: Callable[[str], bool] | Callable[[int], bool]) -> Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int]:
    temp = ["" for i in range(arr[1])]

    pengurang: int = 0
    for i in range(0, arr[1]):
        if func(arr[0][i]):
            pengurang = pengurang + 1
        else:
            temp[i - pengurang] = arr[0][i]

    temp2 = temp
    temp = [temp2[i] for i in range(arr[1]-pengurang)]

    return (temp, arr[1] - pengurang)

def getLast() -> Tuple[Tuple[str, str, str], Tuple[List[Tuple[int, str, int, int, int]], int]]:
    data = var.stackUndo[0][var.stackUndo[1]-1]
    temp = ([var.stackUndo[0][i] for i in range(var.stackUndo[1] - 1)], var.stackUndo[1] - 1)
        
    var.stackUndo = temp
    
    return data
    
    
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


def filterArr(arr: Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int], func: Callable[[str], bool] | Callable[[int], bool]) -> Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int]:
    temp = ([], 0)

    for i in range(arr[1]):
        if (func(arr[0][i])):
            temp = add(arr[0][i], temp)

    return temp


def validasiPassword(password: str) -> bool:
    # passwordTemp = password + "@"
    # panjangPass = 0
    # while True:
    #     if passwordTemp[panjangPass] != "@":
    #         panjangPass = panjangPass + 1
    #     elif passwordTemp[panjangPass] == "@":
    #         break
    
    return (5 <= len(password) <= 25)


def readCSV(path: str, tipe: str) -> Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int]:
    panjangSatuData: int = 0
    if tipe == "user" or tipe == "bahan":
        panjangSatuData = 3
    elif tipe == "candi":
        panjangSatuData = 5

    file = open(path, "r")

    line = file.readline() + "@"

    temp = ([], 0)
    while line != "@":
        i = 0
        data = ["" for i in range(panjangSatuData)]
        indexData = 0
        word = ""
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


def writeCSV(path: str, data: str) -> None:
    file = open(path, "w")
    file.write(data)


def lcg(modulus: int, a: int, b: int, seed: int) -> Generator[int, None, None]:
    while True:
        seed = (a * seed + b) % modulus
        yield seed / (modulus)


x = lcg(2**31, 1103515245, 12345, 123)


def randomAngka(min: int, max: int) -> int:
    # print(next(lcg(2**31, 1103515245, 12345, 7)))
    return int(next(x) * ((max+1)-min) + min)

# def readCSVUser(url: str):
#     file = open(url, "r")

#     line: str= file.readline() + "@"

#     user: Tuple[List[Tuple[str,str,str]], int] = ([], 0)
#     while line != "@":
#         i: int = 0
#         data: List[str] = ["","",""]
#         indexData: int = 0
#         word: str = ""
#         while indexData < 3:
#             if line[i] == ";" or line[i] == "@" or line[i] == "\n":
#                 data[indexData] = word
#                 indexData = indexData + 1
#                 word = ""
#             else:
#                 word = word + line[i]
#             i = i + 1

#         user = add(tuple(data), user)
#         line = file.readline() + "@"

#     print(user)
#     return user

# def readCSVCandi(url: str):
#     file = open(url, "r")

#     line: str= file.readline() + "@"

#     candi: Tuple[List[Tuple[int,str,int,int,int]], int] = ([], 0)
#     while line != "@":
#         i: int = 0
#         data: List[str] = ["","","","",""]
#         indexData: int = 0
#         word: str = ""
#         while indexData < 5:
#             if line[i] == ";" or line[i] == "@" or line[i] == "\n":
#                 data[indexData] = word
#                 indexData = indexData + 1
#                 word = ""
#             else:
#                 word = word + line[i]
#             i = i + 1

#         data[0] = int(data[0])
#         data[2] = int(data[2])
#         data[3] = int(data[3])
#         data[4] = int(data[4])

#         candi = add(tuple(data), candi)
#         line = file.readline() + "@"

#     print(candi)
#     return candi

# def readCSVBahan(url: str):
#     file = open(url, "r")

#     line: str= file.readline() + "@"

#     bahanBangunan: Tuple[List[Tuple[int,str,int,int,int]], int] = ([], 0)
#     while line != "@":
#         i: int = 0
#         data: List[str] = ["","",""]
#         indexData: int = 0
#         word: str = ""
#         while indexData < 3:
#             if line[i] == ";" or line[i] == "@" or line[i] == "\n":
#                 data[indexData] = word
#                 indexData = indexData + 1
#                 word = ""
#             else:
#                 word = word + line[i]
#             i = i + 1

#         data[2] = int(data[2])

#         bahanBangunan = add(tuple(data), bahanBangunan)
#         line = file.readline() + "@"

#     print(bahanBangunan)
#     return bahanBangunan


# readCSV("data/user.csv")
# writeCSV("data/user.csv", "basi;12345678;pengemis\nbadi;12345678;pengemis")
# readCSVUser("data/user.csv")
# readCSVCandi("data/candi.csv")
# readCSVBahan("data/bahan_bangunan.csv")
