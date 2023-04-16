# file yang berisi fungsi-fungsi pendukung fungsi utama
import var
from typing import *
from collections.abc import Callable

# fungsi untuk mendapatkan index dari suatu elemen di dalam array
# arr: array yang berisi elemen yang mau dicari
# func: fungsi untuk menentukan kriteria elemen seperti apa yang dicari di dalam arr
# return: index suatu elemen atau -1 jika tidak ada elemen yang memenuhi kriteria
# fungsi ini akan mengembalikan index saat func mengembalikan nilai true
def getIndex(arr: Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int], func: Callable[[int], bool] | Callable[[str], bool]) -> int:
    for i in range(0, arr[1]):
        if func(arr[0][i]):
            return i

    return -1


# fungsi untuk menambah data pada suatu array, data akan ditambahkan di akhir dari suatu array
# data: data yang mau ditambahkan ke arr
# arr: array dimana data akan ditambahkan
# return: sebuah array yang sudah ditambahkan data baru didalamnya
def add(data: Tuple[str, str, str] | Tuple[int, str, int, int, int] | Tuple[Tuple[str, str, str], Tuple[List[Tuple[int, str, int, int, int]], int]], arr: Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int] | Tuple[List[Tuple[Tuple[str, str, str], Tuple[List[Tuple[int, str, int, int, int]], int]]], int]) -> Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int] | Tuple[List[Tuple[Tuple[str, str, str], Tuple[List[Tuple[int, str, int, int, int]], int]]], int]:
    temp = ["" for i in range(arr[1] + 1)] # inisialisasi array sementara dengan panjang + 1 dari panjang array arr

    # penyalinan data pada array arr ke array temp dan penambahan data pada array temp
    for i in range(0, arr[1]+1):
        if i != arr[1]: 
            temp[i] = arr[0][i] # penyalinan
        else:
            temp[i] = data # penambahan data

    return (temp, arr[1] + 1) # panjang array ditambah 1

# fungsi untuk menghapus elemen dalam suatu array berdasarkan kriteria tertentu
# arr: array yang elemennya mau dihapus
# func: fungsi untuk menentukan kriteria elemen apa yang mau dihapus
# return: array yang sudah dihapus beberapa elemen didalamnya
# fungsi ini akan menghapus elemen dalam array ketika fungsi func mengembalikan nilai true
# fungsi ini bisa menghapus lebih dari satu elemen asalkan elemen tersebut masih memenuhi kriteria yang ditentukan
def delete(arr: Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int], func: Callable[[str], bool] | Callable[[int], bool]) -> Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int]:
    temp = ["" for i in range(arr[1])]# inisialisasi array sementara

    pengurang = 0 # banyak elemen yang di hapus dalam array arr
    
    # penyalinan dan penggeseran elemen pada array arr ke array temp
    for i in range(0, arr[1]):
        if func(arr[0][i]):
            pengurang = pengurang + 1 #persiapan penggeseran (penghapusan elemen)
        else:
            temp[i - pengurang] = arr[0][i] # penyalinan

    temp2 = temp
    temp = [temp2[i] for i in range(arr[1]-pengurang)] # pembuatan array dengan panjang yang sesuai

    return (temp, arr[1] - pengurang) # panjang array dikurangkan sesuai dengan banyak elemen yang dihapus

# fungsi ini mengembalikan elemen terakhir pada array stackUndo
# return: elemen terakhir array stackUndo
def getLast() -> Tuple[Tuple[str, str, str], Tuple[List[Tuple[int, str, int, int, int]], int]]:
    data = var.stackUndo[0][var.stackUndo[1]-1] #pengambilan data terakhir
    
    # penghapusan data terakhir
    temp = ([var.stackUndo[0][i]
            for i in range(var.stackUndo[1] - 1)], var.stackUndo[1] - 1)
    var.stackUndo = temp

    return data

# fungsi untuk menentukan id Candi dari candi yang akan dibangun
# return: id candi, id candi berada pada rentang 1-100
def generateIdCandi() -> int:
    idCandi = 1
    while True:
        ada = False
        for i in range(var.candi[1]):
            if var.candi[0][i][0] == idCandi: #pengecekan id candi sudah ada atau belum
                ada = True
                break
        if ada: #id candi sudah anda pencarian dilanjutkan
            idCandi = idCandi + 1
        else: #id candi belum ada pencarian id selesai
            break
    return idCandi

# fungsi untuk memfilter isi dari suatu array
# arr: array yang mau difilter isinya
# func: fungsi untuk menentukan kriteria dari filter yang akan dilakukan, ketika fungsi func mengembalikan false maka suatu elemen akan dihapuskan dari dalam array
# return: array yang sudah difilter, array ini berisi semua elemen yang memenuhi kriteria yang sudah ditentukan pada fungsi func
def filterArr(arr: Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int], func: Callable[[str], bool] | Callable[[int], bool]) -> Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int]:
    temp = ([], 0) # inisialisasi array sementara

    for i in range(arr[1]):
        if (func(arr[0][i])):# elemen pada array arr yang memenuhi kriteria akan ditambahkan pada array temp
            temp = add(arr[0][i], temp)

    return temp


# fungsi untuk mengecek apakah password yang dibuat sudah memenuhi kriteria yang ditentukan atau belum
# password: password yang mau dicek
# return: true jika panjang password berada pada rentang 5-25, selain itu false
def validasiPassword(password: str) -> bool:
    # passwordTemp = password + "@"
    # panjangPass = 0
    # while True:
    #     if passwordTemp[panjangPass] != "@":
    #         panjangPass = panjangPass + 1
    #     elif passwordTemp[panjangPass] == "@":
    #         break

    return (5 <= len(password) <= 25)

# fungsi untuk membaca file CSV kemudian menyimpannya dalam sebuah array
# path: alamat dari file CSV yang mau dibaca
# tipe: data file CSV apa yang mau dibaca, ada 3 tipe yaitu bahan, candi, dan user
# return: array yang berisi data dari file CSV yang dibaca
def readCSV(path: str, tipe: str) -> Tuple[List[Tuple[str, str, str]], int] | Tuple[List[Tuple[int, str, int, int, int]], int]:
    # pengecekan tipe
    panjangSatuData = 0
    if tipe == "user" or tipe == "bahan":
        panjangSatuData = 3
    elif tipe == "candi":
        panjangSatuData = 5

    # pembacaan file
    file = open(path, "r")
    line = file.readline() + "@" # membaca 1 baris pada file dan diberi mark
    temp = ([], 0)
    while line != "@": # pengecekan mark (akhir file)
        i = 0
        data = ["" for i in range(panjangSatuData)]
        indexData = 0
        word = ""
        while indexData < panjangSatuData:
            if line[i] == ";" or line[i] == "@" or line[i] == "\n": #pengecekan mark (akhir baris) dan pengecekan separator
                data[indexData] = word
                indexData = indexData + 1
                word = ""
            else:
                word = word + line[i]
            i = i + 1

        # penyesuaian tipe data
        if tipe == "bahan":
            data[2] = int(data[2])
        elif tipe == "candi":
            data[0] = int(data[0])
            data[2] = int(data[2])
            data[3] = int(data[3])
            data[4] = int(data[4])

        temp = add(tuple(data), temp) # memasukan data pada array
        
        line = file.readline() + "@" # membaca 1 baris pada file dan diberi mark

    print(temp)
    return temp

# fungsi untuk menuliskan data ke file CSV
# path: alamat file CSV yang mau dituliskan
# data: data yang mau dituliskan ke file CSV
# menghasilkan sebuah file CSV yang sudah berisi suatu data
def writeCSV(path: str, data: str) -> None:
    file = open(path, "w")
    file.write(data)

# fungsi Linear Congruential Generator untuk membantu menghasilkan bilangan acak
def lcg(modulus: int, a: int, b: int, seed: int) -> Generator[int, None, None]:
    while True:
        seed = (a * seed + b) % modulus # rumus lcg
        yield seed / (modulus) # dibagi modulus mengembalikan hasil pada rentang [0,1]


x = lcg(2**31, 1103515245, 12345, 123)

# fungsi untuk mengenerate random int pada suatu rentang
# min: batas bawah random integer (inklusif)
# max: batas atas random integer (inklusif)
# return: sebuah random integer di antara min dan max
def randomAngka(min: int, max: int) -> int:
    return int(next(x) * ((max+1)-min) + min) # menyesuaikan dengan batas yang ditentukan

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
