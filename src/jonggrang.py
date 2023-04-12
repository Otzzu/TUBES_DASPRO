import var
from util import *
from typing import *
from norole import *


# def commandJonggrang(command: str) -> None:
#     if (command == "hancurkancandi"):
#         hancurkanCandi()
#     elif (command == "ayamberkokok"):
#         ayamBerkokok()


def hancurkanCandi() -> None:
    if (var.currentUser[2] != "roro_jonggrang"):
        print("Hancurkan candi hanya dapat diakses oleh akun Roro Jonggrang.")
    else:
        idCandi = int(input("Masukkan ID candi: "))

        index = getIndex(var.candi, idCandi, lambda x, y: x[0] == y)

        if index != -1:
            pilihan = input(
                "Apakah anda yakin ingin menghancurkan candi ID: " + str(idCandi) + " (Y/N)?")

            if pilihan == "Y":
                var.candi = delete(var.candi, idCandi, lambda x, y: x[0] == y)
                print("")
                print("Candi telah berhasil dihancurkan.")
        else:
            print("Tidak ada candi dengan ID tersebut.")

        print(var.candi)


def ayamBerkokok() -> None:
    if (var.currentUser[2] != "roro_jonggrang"):
        print("Ayam berkokok hanya dapat diakses oleh akun Roro Jonggrang.")
    else:
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
