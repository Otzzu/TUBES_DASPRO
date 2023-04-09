import var
from util import *
from typing import *
import argparse
import os

def commandNoRole(command: str) -> None:
    if command == "login":
        login()
    elif (command == "exit"):
        exitProgram()
    elif (command == "summonjin"):
        print("Summon jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "hapusjin"):
        print("Hapus jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "ubahjin"):
        print("Ubah jin hanya dapat diakses oleh akun Bandung Bondowoso.")

def login():
    username = input("Username: ")
    password = input("Password: ")

    user = filterArr(var.users, lambda x: x[0] == username)
    print(user)
    if user[1] != 0:
        if password == user[0][0][1]:
            var.currentUser = user[0][0]
            print("")
            print("Selamat datang, " + username + "!")
            print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
        else:
            print("Password salah!")
    else:
        print("Username tidak terdaftar!")

def help(role: str = "") -> None:
    print("=========== HELP ==========")
    if (role == ""):
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. load")
        print("   Untuk memuat file eksternal ke dalam permainan")
        print("3. save")
        print("   Untuk menyimpan data permainan ke dalam sebuah file")
    elif (role == "bandung_bondowoso"):
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. summonjin")
        print("   Untuk menghapus jin")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin")
        print("5. save")
        print("   Untuk menyimpan data permainan ke dalam sebuah file")
    elif (role == "roro_jonggrang"):
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. save")
        print("   Untuk menyimpan data permainan ke dalam sebuah file")


def save():
    inputPath: str = input("Masukkan nama folder: ") + "@"
    print("")
    
    path: str = ""
    
    i: int = 0
    word: str = ""
    while True:
        if inputPath[i] == "/" or inputPath[i] == "@" :
            
            if path == "" :
                path = path + word
            else :
                path = path + "/" + word
                
            if not (os.path.isdir(path)):
                print("Membuat folder " + path + "...")
            word = ""
            
            if inputPath[i] == "@": break
        else:
            word = word + inputPath[i]
        i = i + 1
        
    os.makedirs(path)
        
    dataUsers: str = ""
    for i in range(var.users[1]):
        dataUser: str = var.users[0][i][0] + ";" + var.users[0][i][1] + ";" +  var.users[0][i][2] + "\n"
        dataUsers = dataUsers + dataUser
        
    dataCandis: str = ""
    for i in range(var.candi[1]):
        dataCandi: str = str(var.candi[0][i][0]) + ";" + var.candi[0][i][1] + ";" +  str(var.candi[0][i][2]) + ";" + str(var.candi[0][i][3]) + ";" + str(var.candi[0][i][4]) + "\n"
        dataCandis = dataCandis + dataCandi

    dataBahans: str = ""
    for i in range(var.bahanBangunan[1]):
        dataBahan: str = var.bahanBangunan[0][i][0] + ";" + var.bahanBangunan[0][i][1] + ";" +  str(var.bahanBangunan[0][i][2]) + "\n"
        dataBahans = dataBahans + dataBahan
    
    writeCSV(path + "/user.csv", dataUsers)
    writeCSV(path + "/candi.csv", dataCandis)
    writeCSV(path + "/bahan_bangunan.csv", dataBahans)
    
    print("")
    print("Saving...")
    print("Berhasil menyimpan data di folder " + path + "!")

def load():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("folderPath")
    
    args = parser.parse_args()
    folderPath = args.folderPath
    
    if folderPath == "":
        print("Tidak ada nama folder yang diberikan!")
        print("")
        print("Usage: python main.py <nam_folder>")
        exit()
    
    if not os.path.isdir(folderPath):
        print('Folder "' + folderPath + '" tidak ditemukan.' )
        exit()
    
    print("Loading...")
    
    var.users = readCSV(folderPath + "/user.csv", "user")
    var.candi = readCSV(folderPath + "/candi.csv", "candi")
    var.bahanBangunan = readCSV(folderPath + "/bahan_bangunan.csv", "bahan")
    
    print('Selamat datang di program "Manajerial Candi"')
    print('Silahkan masukkan username anda')
    
    print(var.users)
    print(var.candi)
    print(var.bahanBangunan)
    
def exitProgram():
    pilihan: str = ""
       
    while True:
        pilihan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if pilihan == "y" or pilihan == "Y" or pilihan == "n" or pilihan == "N": break
    
    if pilihan == "y" or pilihan == "Y":
        save()
        exit()
    elif pilihan == "n" or pilihan == "N":
        exit()
    

    
    