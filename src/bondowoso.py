import var
from util import *
from typing import *
import random


def commandBondowoso(command: str) -> None:
    if (command == "summonjin"):
        summonJin()
    elif (command == "hapusjin"):
        hapusJin()
    elif (command == "ubahjin"):
        ubahJin()
    elif (command == "batchkumpul"):
        batchKumpul()
    elif (command == "batchbangun"):
        batchBangun()
    elif (command == "logout"):
        logout()
    elif (command == "laporanjin"):
        laporanJin()
    elif (command == "laporancandi"):
        laporanCandi()
    elif (command == "bangun"):
        print("bangun hanya dapat diakses oleh akun Jin Pembangun.")
    elif (command == "kumpul"):
        print("Kumpul hanya dapat diakses oleh akun Jin Pengumpul.")
    elif (command == " hancurkancandi"):
        print("Hancurkan Candi hanya dapat diakses oleh akun Roro Jonggrang.")
    elif (command == "ayamberkokok"):
        print("Aya Berkokok hanya dapat diakses oleh akun Roro Jonggrang.")


def summonJin() -> None:
    totalJin: int = filterArr(var.users, lambda x: x[2] == "jin_pengumpul" or x[2] == "jin_pembangun" )[1]

    if (totalJin >= 100):
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")
        print("")

        roleJin: str = ""
        while True:
            noJin: str = (
                input("Masukkan nomor jenis jin yang ingin dipanggil: "))

            if (noJin == "1" or noJin == "2"):
                break
            else:
                print('Tidak ada jenis jin bernomor “' + noJin + '”!')

        if (noJin == "1"):
            roleJin = "jin_pengumpul"
            print('Memilih jin “Pengumpul”.')
        elif (noJin == "2"):
            roleJin = "jin_pembangun"
            print('Memilih jin “Pembangun”.')

        print("")
        while True:
            usernameJin: str = input("Masukkan username jin: ")
            if filterArr(var.users, lambda x: x[0] == usernameJin)[1] == 0:
                break
            else:
                print('Username “' + usernameJin + '” sudah diambil!')
        while True:
            passwordJin: str = input("Masukkan password jin: ")
            if validasiPassword(passwordJin):
                break
            else:
                print("Password panjangnya harus 5-25 karakter!")

        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print("")
        print("Jin " + usernameJin + " berhasil dipanggil!")

        var.users = add((usernameJin, passwordJin, roleJin), var.users)
    print(var.users)


def hapusJin() -> None:
    usernameJin: str = input("Masukkan username Jin: ")
    if filterArr(var.users, lambda x: x[0] == usernameJin)[1] != 0:
        masukan: str = input(
            "Apakah anda yakin ingin menghapus jin dengan username " + usernameJin + " (Y/N)? ")
        if (masukan == "Y"):
            var.users = delete(var.users, usernameJin, lambda x, y: x[0] == y)
            var.candi = delete(var.candi, usernameJin, lambda x, y: x[1] == y)
            print("Jin telah berhasil dihapus dari alam gaib.")
    else:
        print("Tidak ada jin dengan username tersebut.")
    print(var.users)
    print(var.candi)


def ubahJin() -> None:
    usernameJin: str = input("Masukkan username Jin: ")
    index: int = getIndex(var.users, usernameJin, lambda x, y: x[0] == y)
    if index != -1:
        jin = var.users[0][index]
        tipeJin = "Pengumpul" if jin[2] == "jin_pengumpul" else "Pembangun"
        masukan: str = input('Jin ini bertipe "' + tipeJin + '" . Yakin ingin mengubah ke tipe "' +
                             ("Pengumpul" if tipeJin == "Pembangun" else "Pembangun") + '" (Y/N)? ')
        if (masukan == "Y"):
            var.users[0][index] = (
                jin[0], jin[1], ("jin_pengumpul" if tipeJin == "Pembangun" else "jin_pembangun"))
            print("Jin telah berhasil diubah")
    else:
        print("Tidak ada jin dengan username tersebut.")
    print(var.users)


def batchKumpul():
    jins: Tuple[List[Tuple[str, str, str]], int] = filterArr(var.users, lambda x: x[2] == "jin_pengumpul")

    if jins[1] == 0:
        print(
            "Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        sumPasir: int = 0
        sumBatu: int = 0
        sumAir: int = 0
        print("Mengerahkan " + str(jins[1]) + " jin untuk mengumpulkan bahan.")
        for i in range(jins[1]):
            pasir: int = random.randint(0, 5)
            batu: int = random.randint(0, 5)
            air: int = random.randint(0, 5)

            sumPasir = sumPasir + pasir
            sumBatu = sumBatu + batu
            sumAir = sumAir + air

        print("Jin menemukan total " + str(sumPasir) + " pasir, " +
              str(sumBatu) + " batu, dan " + str(sumAir) + " air.")
        var.bahanBangunan[0][0] = (
            "pasir", "", var.bahanBangunan[0][0][2] + sumPasir)
        var.bahanBangunan[0][1] = (
            "batu", "", var.bahanBangunan[0][1][2] + sumBatu)
        var.bahanBangunan[0][2] = (
            "air", "", var.bahanBangunan[0][2][2] + sumAir)
        print(var.bahanBangunan)


def batchBangun():
    jins: Tuple[List[Tuple[str, str, str]], int] = filterArr(var.users, lambda x: x[2] == "jin_pembangun" )
    bahan = [(0, 0, 0) for i in range(jins[1])]

    if jins[1] == 0:
        print(
            "Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        sumPasir: int = 0
        sumBatu: int = 0
        sumAir: int = 0
        for i in range(jins[1]):
            pasir: int = random.randint(1, 5)
            batu: int = random.randint(1, 5)
            air: int = random.randint(1, 5)

            bahan[i] = (pasir, batu, air)

            sumPasir = sumPasir + pasir
            sumBatu = sumBatu + batu
            sumAir = sumAir + air
        print("Mengerahkan " + str(jins[1]) + " jin untuk membangun candi dengan total bahan " + str(
            sumPasir) + " pasir, " + str(sumBatu) + " batu, dan " + str(sumAir) + " air.")

        cukup: bool = True
        if var.bahanBangunan[0][0][2] < sumPasir:
            cukup = False
        if var.bahanBangunan[0][1][2] < sumBatu:
            cukup = False
        if var.bahanBangunan[0][2][2] < sumAir:
            cukup = False

        if cukup:
            var.bahanBangunan[0][0] = (
                "pasir", "", var.bahanBangunan[0][0][2] - sumPasir)
            var.bahanBangunan[0][1] = (
                "batu", "", var.bahanBangunan[0][1][2] - sumBatu)
            var.bahanBangunan[0][2] = (
                "air", "", var.bahanBangunan[0][2][2] - sumAir)
            for i in range(jins[1]):
                idCandi: int = generateIdCandi()
                if var.candi[1] < 100:
                    var.candi = add(
                        (idCandi, jins[0][i][0], bahan[i][0], bahan[i][1], bahan[i][2]), var.candi)
            print("Jin berhasil membangun total " + str(jins[1]) + " candi.")
        else:
            pasirKurang = sumPasir - var.bahanBangunan[0][0][2]
            batuKurang = sumBatu - var.bahanBangunan[0][1][2]
            airKurang = sumAir - var.bahanBangunan[0][2][2]

            if pasirKurang < 0:
                pasirKurang = 0
            if batuKurang < 0:
                batuKurang = 0
            if airKurang < 0:
                airKurang = 0
            print("Bangun gagal. Kurang " + str(pasirKurang) + " pasir, " +
                  str(batuKurang) + " batu, dan " + str(airKurang) + " air.")
    print(var.candi)


def laporanJin():
    jinPengumpul = filterArr(var.users, lambda x: x[2] == "jin_pengumpul")
    jinPembangun = filterArr(var.users, lambda x: x[2] == "jin_pembangun")
    totalJinPengumpul: int = jinPengumpul[1]
    totalJinPembangun: int = jinPembangun[1]
    totalJin: int = totalJinPembangun + totalJinPengumpul

    jinTerajin: str = "-"
    jinTermalas: str = "-"
    maxCandi: int = 0
    minCandi: int = 0
    if (totalJinPembangun > 0):
        jinTerajin = jinPembangun[0][0][0]
        jinTermalas = jinPembangun[0][0][0]
        maxCandi = filterArr(var.candi, lambda x: x[1] == jinPembangun[0][0][0])[1]
        minCandi = maxCandi
        for i in range(1, totalJinPembangun):
            banyakCandi: int = filterArr(var.candi, lambda x: x[1] == jinPembangun[0][i][0])[1]
            if banyakCandi > maxCandi:
                maxCandi = banyakCandi
                jinTerajin = jinPembangun[0][i][0]
            elif banyakCandi == maxCandi:
                if jinPembangun[0][i][0] < jinTerajin:
                    jinTerajin = jinPembangun[0][i][0]

            if banyakCandi < minCandi:
                minCandi = banyakCandi
                jinTermalas = jinPembangun[0][i][0]
            elif banyakCandi == minCandi:
                if jinPembangun[0][i][0] > jinTermalas:
                    jinTermalas = jinPembangun[0][i][0]

    totalPasir: int = var.bahanBangunan[0][0][2]
    totalBatu: int = var.bahanBangunan[0][1][2]
    totalAir: int = var.bahanBangunan[0][2][2]

    print("")
    print("> Total Jin: " + str(totalJin))
    print("> Total Jin Pengumpul: " + str(totalJinPengumpul))
    print("> Total Jin Pembangun: " + str(totalJinPembangun))
    print("> Jin Terajin: " + jinTerajin)
    print("> Jin Termalas: " + jinTermalas)
    print("> Jumlah Pasir: " + str(totalPasir) + " unit")
    print("> Jumlah Batu: " + str(totalBatu) + " unit")
    print("> Jumlah Air: " + str(totalAir) + " unit")


def laporanCandi():
    totalCandi: int = var.candi[1]

    totalPasir: int = 0
    totalBatu: int = 0
    totalAir: int = 0

    idTermahal: str = "-"
    idTermurah: str = "-"
    hargaTermahal: int = 0
    hargaTermurah: int = 0

    if totalCandi != 0:
        for i in range(totalCandi):
            totalPasir = totalPasir + var.candi[0][i][2]
            totalBatu = totalBatu + var.candi[0][i][3]
            totalAir = totalAir + var.candi[0][i][4]

        idTermahal = str(var.candi[0][0][0])
        idTermurah = str(var.candi[0][0][0])
        hargaTermahal = 10000 * \
            (var.candi[0][0][2]) + 15000 * \
            (var.candi[0][0][3]) + 7500 * (var.candi[0][0][4])
        hargaTermurah = hargaTermahal
        for i in range(1, totalCandi):
            harga = 10000 * (var.candi[0][i][2]) + 15000 * \
                (var.candi[0][i][3]) + 7500 * (var.candi[0][i][4])
            if harga > hargaTermahal:
                hargaTermahal = harga
                idTermahal = str(var.candi[0][i][0])

            if harga < hargaTermurah:
                hargaTermurah = harga
                idTermurah = str(var.candi[0][i][0])

    print("> Total Candi: " + str(totalCandi))
    print("> Total Pasir yang digunakan: " + str(totalPasir))
    print("> Total Batu yang digunakan: " + str(totalBatu))
    print("> Total Air yang digunakan: " + str(totalAir))
    if totalCandi != 0:
        print("> ID Candi Termahal: " + str(idTermahal) +
              " (Rp " + str(hargaTermahal) + ")")
        print("> ID Candi Termurah: " + str(idTermurah) +
              " (Rp " + str(hargaTermurah) + ")")
    else:
        print("> ID Candi Termahal: " + str(idTermahal))
        print("> ID Candi Termurah: " + str(idTermurah))
