import var
from util import *
from typing import *
import random

def commandPembangun(command: str) -> None:
    if (command == "bangun"):
        bangun()
    elif (command == "logout"):
        logout()
    elif (command == "summonjin"):
        print("Summon jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "hapusjin"):
        print("Hapus jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "ubahjin"):
        print("Ubah jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "kumpul"):
        print("Kumpul hanya dapat diakses oleh akun Jin Pengumpul.")
    elif (command == "batchkumpul"):
        print("Batch Kumpul hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "batchbangun"):
        print("Batch Bangun hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif(command == "laporanjin"):
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif(command == "laporancandi"):
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")

        
def bangun():
    pasir: int = random.randint(1, 5)
    batu: int = random.randint(1, 5)
    air: int = random.randint(1, 5)
    
    cukup: bool = True
    if var.bahanBangunan[0][0][2] < pasir:
        cukup = False
    if var.bahanBangunan[0][1][2] < batu:
        cukup = False
    if var.bahanBangunan[0][2][2] < air:
        cukup = False
    
    if cukup:
        var.bahanBangunan[0][0] = ("pasir", "", var.bahanBangunan[0][0][2] - pasir)
        var.bahanBangunan[0][1] = ("batu", "", var.bahanBangunan[0][1][2] - batu)
        var.bahanBangunan[0][2] = ("air", "", var.bahanBangunan[0][2][2] - air)
        idCandi: int = generateIdCandi()
                
        if var.candi[1] >= 100:
            print("Candi berhasil dibangun!")
            print("Sisa candi yang perlu dibangun: 0.")
        else:
            var.candi = add((idCandi, var.currentUser[0], pasir, batu, air), var.candi) 
            print("Candi berhasil dibangun.") 
            print("Sisa candi yang perlu dibangun: " + str(100 - var.candi[1]))
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    print(var.candi)
    print(var.bahanBangunan)