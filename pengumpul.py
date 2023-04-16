# file yang berisi fungsi-fungsi utama yang dimiliki jin_pengumpul
import var
from util import *
from typing import *
import random

# def commandPengumpul(command: str) -> None:
#     if (command == "kumpul"):
#         kumpul()

# fungsi untuk mengumpulkan bahan bangunan
def kumpul() -> None:
    if (var.currentUser[2] != "jin_pengumpul"):# pengecekan role apakah sudah sesuai atau belum
        print("Kumpul hanya dapat diakses oleh akun Jin Pengumpul.")
    else:
        # penentuan jumlah bahan yang dikumpulkan oleh satu jin
        pasir = random.randint(0, 5)
        batu = random.randint(0, 5)
        air = random.randint(0, 5)

        print("Jin menemukan " + str(pasir) + " pasir, " + str(batu) + " batu, dan " + str(air) + " air.")
        
        # penambahan jumlah bahan pada array of bahan
        var.bahanBangunan[0][0] = ("pasir", "", var.bahanBangunan[0][0][2] + pasir)
        var.bahanBangunan[0][1] = ("batu", "", var.bahanBangunan[0][1][2] + batu)
        var.bahanBangunan[0][2] = ("air", "", var.bahanBangunan[0][2][2] + air)
        print(var.bahanBangunan)