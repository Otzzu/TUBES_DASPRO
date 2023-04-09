import var
from util import *
from typing import *
import random


def commandJonggrang(command: str) -> None:
    if (command == "hancurkancandi"):
        hancurkanCandi()
    elif (command == "ayamberkokok"):
        ayamBerkokok()
    elif (command == "summonjin"):
        print("Summon jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "hapusjin"):
        print("Hapus jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "ubahjin"):
        print("Ubah jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "batchkumpul"):
        print("Batch Kumpul hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "batchbangun"):
        print("Batch Bangun hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "logout"):
        logout()
    elif (command == "bangun"):
        print("bangun hanya dapat diakses oleh akun Jin Pembangun.")
    elif (command == "kumpul"):
        print("Kumpul hanya dapat diakses oleh akun Jin Pengumpul.")
    elif (command == "laporanjin"):
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    elif (command == "laporancandi"):
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")


def hancurkanCandi():
    idCandi: int = int(input("Masukkan ID candi: "))

    index: int = getIndex(var.candi, idCandi, lambda x, y: x[0] == y)

    if index != -1:
        pilihan: str = input(
            "Apakah anda yakin ingin menghancurkan candi ID: " + str(idCandi) + " (Y/N)?")

        if pilihan == "Y":
            var.candi = delete(var.candi, idCandi, lambda x, y: x[0] == y)
            print("")
            print("Candi telah berhasil dihancurkan.")
    else:
        print("Tidak ada candi dengan ID tersebut.")

    print(var.candi)


def ayamBerkokok():
    jumlahCandi: int = var.candi[1]

    print("Kukuruyuk.. Kukuruyuk..")
    print("")
    print("Jumlah Candi: " + str(jumlahCandi))
    print("")

    if jumlahCandi == 100:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    else:
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")

    var.gameEnd = True
