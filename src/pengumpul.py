import var
from util import *
from typing import *
import random

def commandPengumpul(command: str) -> None:
    if (command == "kumpul"):
        kumpul()
    elif (command == "logout"):
        logout()
    elif (command == "summonjin"):
        print("Summon jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "hapusjin"):
        print("Hapus jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "ubahjin"):
        print("Ubah jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "bangun"):
        print("bangun hanya dapat diakses oleh akun Jin Pembangun.")
    elif (command == " hancurkancandi"):
        print("Hancurkan Candi hanya dapat diakses oleh akun Roro Jonggrang.")
    elif (command == "ayamberkokok"):
        print("Aya Berkokok hanya dapat diakses oleh akun Roro Jonggrang.")
    elif(command == "laporanjin"):
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif(command == "laporancandi"):
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
        
def kumpul() -> None:
    pasir: int = random.randint(0, 5)
    batu: int = random.randint(0, 5)
    air: int = random.randint(0, 5)
    
    print("Jin menemukan " + str(pasir) + " pasir, " + str(batu) + " batu, dan " + str(air) + " air.")
    var.bahanBangunan[0][0] = ("pasir", "", var.bahanBangunan[0][0][2] + pasir)
    var.bahanBangunan[0][1] = ("batu", "", var.bahanBangunan[0][1][2] + batu)
    var.bahanBangunan[0][2] = ("air", "", var.bahanBangunan[0][2][2] + air)
    print(var.bahanBangunan)