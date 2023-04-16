# file yang berisi fungsi-fungsi utama yang dimiliki role roro_jonggrang
import var
from util import *
from typing import *
from norole import *


# def commandJonggrang(command: str) -> None:
#     if (command == "hancurkancandi"):
#         hancurkanCandi()
#     elif (command == "ayamberkokok"):
#         ayamBerkokok()

# fungsi untuk menghancurkan candi yang telah dibangun bandung bondowoso
# hancurkanCandi akan gagal jika id candi yang diinputkan tidak ada
def hancurkanCandi() -> None:
    if (var.currentUser[2] != "roro_jonggrang"):# pengecekan role apakah sudah sesuai atau belum
        print("Hancurkan candi hanya dapat diakses oleh akun Roro Jonggrang.")
    else:
        idCandi = int(input("Masukkan ID candi: ")) # input id candi yang mau dihancurkan

        index = getIndex(var.candi, lambda x: x[0] == idCandi)

        if index != -1: # pengecekan apakah candi dengan id tersebut ada atau tidak
            pilihan = input(
                "Apakah anda yakin ingin menghancurkan candi ID: " + str(idCandi) + " (Y/N)?")

            if pilihan == "Y" or pilihan == "y":
                # menghapus candi dari array of candi
                var.candi = delete(var.candi, lambda x: x[0] == idCandi)
                print("")
                print("Candi telah berhasil dihancurkan.")
        else:
            print("Tidak ada candi dengan ID tersebut.")

        print(var.candi)

# fungsi untuk menyelesaikan permainan
# ketika jumlah candi sudah 100 maka bandung bondowoso yang menang
# ketika jumlah candi kurang dari 100 maka roro jonggrang yang menang
def ayamBerkokok() -> None:
    if (var.currentUser[2] != "roro_jonggrang"):# pengecekan role apakah sudah sesuai atau belum
        print("Ayam berkokok hanya dapat diakses oleh akun Roro Jonggrang.")
    else:
        jumlahCandi: int = var.candi[1]

        print("Kukuruyuk.. Kukuruyuk..")
        print("")
        print("Jumlah Candi: " + str(jumlahCandi))
        print("")

        if jumlahCandi == 100: # bandung bondowoso menang
            print("Yah, Bandung Bondowoso memenangkan permainan!")
        else: # roro jonggrang menang
            print("Selamat, Roro Jonggrang memenangkan permainan!")
            print("")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")

        var.gameEnd = True
