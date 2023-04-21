# file yang berisi fungsi-fungsi utama yang dimiliki role jin_pembangun
import var
from util import *
from typing import *
from norole import *
import random

# def commandPembangun(command: str) -> None:
#     if (command == "bangun"):
#         bangun()
    
# fungsi untuk membangun candi
# bangun akan gagal jika jumlah bahan bangunan tidak mencukupi
def bangun() -> None:
    if (var.currentUser[2] != "jin_pembangun"):# pengecekan role apakah sudah sesuai atau belum
        print("Bangun hanya dapat diakses oleh akun Jin Pembangun.")
    else:
        # penentuan jumlah bahan bangunan yang digunakan untuk membangun 1 candi
        pasir = randomAngka(1, 5)
        batu = randomAngka(1, 5)
        air = randomAngka(1, 5)

        # pengecekan apakah bahan bangunan yang dimiliki cukup atau tidak
        cukup: bool = True
        if var.bahanBangunan[0][0][2] < pasir:
            cukup = False
        if var.bahanBangunan[0][1][2] < batu:
            cukup = False
        if var.bahanBangunan[0][2][2] < air:
            cukup = False

        if cukup:
            # mengurangi jumlah bahan bangunan pada array of bahan
            var.bahanBangunan[0][0] = ("pasir", "", var.bahanBangunan[0][0][2] - pasir)
            var.bahanBangunan[0][1] = ("batu", "", var.bahanBangunan[0][1][2] - batu)
            var.bahanBangunan[0][2] = ("air", "", var.bahanBangunan[0][2][2] - air)
            
            # pembangunan candi
            idCandi = generateIdCandi()
            if var.candi[1] >= 100: # pengecekan jumlah candi, jika >= 100 candi dibangun tapi tidak dicatat
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