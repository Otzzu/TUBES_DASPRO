# file yang berisi fungsi-fungsi utama yang dimiliki role bandung_bondowoso
import var
from util import *
from norole import *
from typing import *
import random


# def commandBondowoso(command: str) -> None:
#     if (command == "summonjin"):
#         summonJin()
#     elif (command == "hapusjin"):
#         hapusJin()
#     elif (command == "ubahjin"):
#         ubahJin()
#     elif (command == "batchkumpul"):
#         batchKumpul()
#     elif (command == "batchbangun"):
#         batchBangun()
#     elif (command == "logout"):
#         logout()
#     elif (command == "laporanjin"):
#         laporanJin()
#     elif (command == "laporancandi"):
#         laporanCandi()

# fungsi untuk mensummon jin, summon akan gagal ketika jumlah jin sudah lebih besar sama dengan 100
def summonJin() -> None:
    if (var.currentUser[2] != "bandung_bondowoso"):# pengecekan role apakah sudah sesuai atau belum
        print("Summon jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        totalJin = filterArr(var.users, lambda x: x[2] == "jin_pengumpul" or x[2] == "jin_pembangun")[1]

        if (totalJin >= 100): # pengecekan apakah jin sudah >= 100 atau belum
            print(
                "Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        else:
            print("Jenis jin yang dapat dipanggil:")
            print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            print(" (2) Pembangun - Bertugas membangun candi")
            print("")

            # pemilihan role jin yang akan disummon
            roleJin = ""
            while True:
                noJin = (
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

            # penentuan username dan password jin yang mau disummon
            print("")
            while True:
                usernameJin = input("Masukkan username jin: ")
                if filterArr(var.users, lambda x: x[0] == usernameJin)[1] == 0:
                    break
                else:
                    print('Username “' + usernameJin + '” sudah diambil!')
            while True:
                passwordJin = input("Masukkan password jin: ")
                if validasiPassword(passwordJin):
                    break
                else:
                    print("Password panjangnya harus 5-25 karakter!")
                    
            # jin disummon
            print("Mengumpulkan sesajen...")
            print("Menyerahkan sesajen...")
            print("Membacakan mantra...")
            print("")
            print("Jin " + usernameJin + " berhasil dipanggil!")

            # jin baru ditambahkan ke array users
            var.users = add((usernameJin, passwordJin, roleJin), var.users)
        print(var.users)

# fungsi untuk menghapus jin yang sudah dipanggil sebelumnya, hapus jin akan gagal jika username jin yang diinputkan tidak ada
# saat jin dihapus maka semua candi yang sudah dibangun oleh jin tersebut juga akan dihapus 
def hapusJin() -> None:
    if (var.currentUser[2] != "bandung_bondowoso"):# pengecekan role apakah sudah sesuai atau belum
        print("Hapus jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        usernameJin = input("Masukkan username Jin: ")# pengambilan input username jin yang mau dihapus
        if filterArr(var.users, lambda x: x[0] == usernameJin)[1] != 0:# pengecekan apakah username jin tersebut ada atau tidak
            masukan = input("Apakah anda yakin ingin menghapus jin dengan username " + usernameJin + " (Y/N)? ")
            if (masukan == "Y"):
                deletedUser = filterArr(var.users, lambda x: x[0] == usernameJin)[0][0]
                if deletedUser[2] == "jin_pembangun":
                    deletedCandi = filterArr(var.candi, lambda x: x[1] == usernameJin)
                    dataUndo = (deletedUser, deletedCandi)
                elif deletedUser[2] == "jin_pengumpul":
                    dataUndo = (deletedUser, [(), 0])
                    
                # menambah data jin yang dihapus ke stack undo
                var.stackUndo = add(dataUndo, var.stackUndo)

                # menghapus jin dari array of user dan menghapus candi yang telah dibangunnya dari array of candi
                var.users = delete(var.users,
                                   lambda x: x[0] == usernameJin)
                var.candi = delete(var.candi,
                                   lambda x: x[1] == usernameJin)
                print("Jin telah berhasil dihapus dari alam gaib.")
        else:
            print("Tidak ada jin dengan username tersebut.")
        print(var.users)
        print(var.candi)
        print(var.stackUndo)

# fungsi untuk menghidupkan kembali jin yang sudah di hapus sebelumnya
# undo akan gagal jika tidak ada jin yang bisa dibangkitkan kembali
# undo juga akan gagal jika username dari jin yang dibangkitkan sudah dipakai
# undo juga akan gagal jika jumlah jin yang ada sudah lebih besar sama dengan 100
# ketika jin dibangkitkan kembali maka candi yang mereka bangun sebelumnya juga akan dibangun kembali dengan id candi yang akan disesuaikan
def undo() -> None:
    if (var.currentUser[2] != "bandung_bondowoso"):# pengecekan role apakah sudah sesuai atau belum
        print("Undo hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        if var.stackUndo[1] >= 1: # pengecekan apakah ada jin yang bisa dibangkitkan kembali
            last = getLast()
            user = last[0]
            candis = last[1]
            if filterArr(var.users, lambda x: x[0] == user[0])[1] != 0 or filterArr(var.users, lambda x: x[2] == "jin_pembangun" or x[2] == "jin_pengumpul")[1] >= 100:# pengecekan apakah jumlah jin sudah >= 100 atau belum dan pengecekan apakah username jin yang mau dibangkitkan sudah ada atau belum
                print("Undo gagal")
            else:
                # jin dibangkitkan kembali
                var.users = add(user, var.users)# menambah jin pada array of user
                if candis[1] != 0:# pengecekan apakah ada candi yang dibangun oleh jin ini atau tidak
                    # pembangunan ulang candi
                    for i in range(candis[1]):
                        id = generateIdCandi()
                        candi = (id, candis[0][i][1], candis[0][i]
                                 [2], candis[0][i][3], candis[0][i][4])
                        var.candi = add(candi, var.candi)
                print("Undo berhasil")
        else:
            print("Tidak ada yang bisa di undo")
    print(var.users)
    print(var.candi)
    print(var.stackUndo)

# fungsi untuk mengubah role jin dari pembangun ke pengumpul atau sebaliknya
# ubah jin akan gagal jika username jin yang diinputkan tidak ada
# ketika jin pembangun diubah rolenya, candi yang dibangunnya akan tetap ada dan jin tersebut masih berpeluang untuk menjadi jin terajin atau termalas
def ubahJin() -> None:
    if (var.currentUser[2] != "bandung_bondowoso"):# pengecekan role apakah sudah sesuai atau belum
        print("Ubah jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        usernameJin = input("Masukkan username Jin: ")
        index = getIndex(var.users, lambda x: x[0] == usernameJin)
        if index != -1: # pengecekan apakah username jin yang diinputkan ada atau tidak
            #mengubah tipe jin
            jin = var.users[0][index]
            tipeJin = "Pengumpul" if jin[2] == "jin_pengumpul" else "Pembangun"
            masukan = input('Jin ini bertipe "' + tipeJin + '" . Yakin ingin mengubah ke tipe "' +
                            ("Pengumpul" if tipeJin == "Pembangun" else "Pembangun") + '" (Y/N)? ')
            if (masukan == "Y"):
                var.users[0][index] = (
                    jin[0], jin[1], ("jin_pengumpul" if tipeJin == "Pembangun" else "jin_pembangun"))
                print("Jin telah berhasil diubah")
        else:
            print("Tidak ada jin dengan username tersebut.")
        print(var.users)

# fungsi untuk mengumpulkan bahan dengan semua jin pengumpul yang dimiliki oleh bandung bondowoso
# fungsi ini akan gagal jika bandung bondowoso tidak memiliki jin pengumpul sama sekali
def batchKumpul() -> None:
    if (var.currentUser[2] != "bandung_bondowoso"):# pengecekan role apakah sudah sesuai atau belum
        print("Batch kumpul hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        jins = filterArr(
            var.users, lambda x: x[2] == "jin_pengumpul")# mendapatkan semua jin pengumpul

        if jins[1] == 0:# pengecekan apakah jin pengumpul ada atau tidak
            print(
                "Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        else:
            sumPasir = 0
            sumBatu = 0
            sumAir = 0
            print("Mengerahkan " + str(jins[1]) +
                  " jin untuk mengumpulkan bahan.")
            for i in range(jins[1]):
                # penentuan jumlah bahan yang berhasil dikumpulkan oleh satu orang jin
                pasir = random.randint(0, 5)
                batu = random.randint(0, 5)
                air = random.randint(0, 5)

                sumPasir = sumPasir + pasir
                sumBatu = sumBatu + batu
                sumAir = sumAir + air

            # menambah bahan yang didapat ke dakam array of nahan
            print("Jin menemukan total " + str(sumPasir) + " pasir, " +
                  str(sumBatu) + " batu, dan " + str(sumAir) + " air.")
            var.bahanBangunan[0][0] = (
                "pasir", "", var.bahanBangunan[0][0][2] + sumPasir)
            var.bahanBangunan[0][1] = (
                "batu", "", var.bahanBangunan[0][1][2] + sumBatu)
            var.bahanBangunan[0][2] = (
                "air", "", var.bahanBangunan[0][2][2] + sumAir)
            print(var.bahanBangunan)

# fungsi untuk membangun candi dengan semua jin pembangun yang dimiliki bandung bondowoso
# fungsi ini akan gagal ketika jumlah bahan bangunan tidak cukup
# ketika candi yang dibangun sudah lebih besar sama dengan 100 maka candi pada fungsi ini akan tetap dibangun namun tidak akan tercatat
def batchBangun() -> None:
    if (var.currentUser[2] != "bandung_bondowoso"):# pengecekan role apakah sudah sesuai atau belum
        print("Batch bangun hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        jins = filterArr(
            var.users, lambda x: x[2] == "jin_pembangun")# mendapatkan semua jin pembangaun dari array user
        bahan = [(0, 0, 0) for i in range(jins[1])]

        if jins[1] == 0:# pengecekan apakah jin pengumpul ada atau tidak
            print(
                "Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        else:
            sumPasir = 0
            sumBatu = 0
            sumAir = 0
            for i in range(jins[1]):
                # penentuan jumlah bahan bangunan yang digunakan untuk membangun 1 candi
                pasir = random.randint(1, 5)
                batu = random.randint(1, 5)
                air = random.randint(1, 5)

                bahan[i] = (pasir, batu, air)

                sumPasir = sumPasir + pasir
                sumBatu = sumBatu + batu
                sumAir = sumAir + air
            print("Mengerahkan " + str(jins[1]) + " jin untuk membangun candi dengan total bahan " + str(
                sumPasir) + " pasir, " + str(sumBatu) + " batu, dan " + str(sumAir) + " air.")

            # pengecekan apakah bahan bangunan yang dimiiiki cukup atau tidak
            cukup = True
            if var.bahanBangunan[0][0][2] < sumPasir:
                cukup = False
            if var.bahanBangunan[0][1][2] < sumBatu:
                cukup = False
            if var.bahanBangunan[0][2][2] < sumAir:
                cukup = False

            if cukup:
                # mengurangi jumlah bahan bangunan di array of bahan 
                var.bahanBangunan[0][0] = (
                    "pasir", "", var.bahanBangunan[0][0][2] - sumPasir)
                var.bahanBangunan[0][1] = (
                    "batu", "", var.bahanBangunan[0][1][2] - sumBatu)
                var.bahanBangunan[0][2] = (
                    "air", "", var.bahanBangunan[0][2][2] - sumAir)
                
                # membangun candi
                for i in range(jins[1]):
                    idCandi = generateIdCandi()
                    if var.candi[1] < 100:
                        var.candi = add(
                            (idCandi, jins[0][i][0], bahan[i][0], bahan[i][1], bahan[i][2]), var.candi)
                        
                
                print("Jin berhasil membangun total " +
                      str(jins[1]) + " candi.")
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

# fungsi untuk menampilkan informasi seputar jin seperti total jin, total jin pada setiap role, jin terajin, jin termalas, dan jumlah bahan bangunan yang dimiliki
# jin terajin adalah jin yang membangun candi paling banyak
# jin termalas adalah jin yang membangun candi paling sedikit
def laporanJin() -> None:
    if (var.currentUser[2] != "bandung_bondowoso"):# pengecekan role apakah sudah sesuai atau belum
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        jinPengumpul = filterArr(var.users, lambda x: x[2] == "jin_pengumpul")
        jinPembangun = filterArr(var.users, lambda x: x[2] == "jin_pembangun")
        totalJinPengumpul = jinPengumpul[1]
        totalJinPembangun = jinPembangun[1]
        totalJin = totalJinPembangun + totalJinPengumpul

        jinTerajin = "-"
        jinTermalas = "-"
        maxCandi = 0
        minCandi = 0
        if (totalJin > 0): # pengecekan apakah bandung bondowoso mempunyai jin atau tidak
            jinTerajin = var.users[0][0][0]
            jinTermalas = var.users[0][0][0]
            maxCandi = filterArr(
                var.candi, lambda x: x[1] == var.users[0][0][0])[1]
            minCandi = maxCandi
            for i in range(1, var.users[1]):
                banyakCandi = filterArr(
                    var.candi, lambda x: x[1] == var.users[0][i][0])[1]
                
                # mencari jin terajin
                if banyakCandi > maxCandi:
                    maxCandi = banyakCandi
                    jinTerajin = var.users[0][i][0]
                elif banyakCandi == maxCandi:
                    if var.users[0][i][0] < jinTerajin:
                        jinTerajin = var.users[0][i][0]

                # mencari jin termalas
                if banyakCandi < minCandi:
                    minCandi = banyakCandi
                    jinTermalas = var.users[0][i][0]
                elif banyakCandi == minCandi:
                    if var.users[0][i][0] > jinTermalas:
                        jinTermalas = var.users[0][i][0]

        totalPasir = var.bahanBangunan[0][0][2]
        totalBatu = var.bahanBangunan[0][1][2]
        totalAir = var.bahanBangunan[0][2][2]

        # menampilkan informasi ke layar
        print("")
        print("> Total Jin: " + str(totalJin))
        print("> Total Jin Pengumpul: " + str(totalJinPengumpul))
        print("> Total Jin Pembangun: " + str(totalJinPembangun))
        print("> Jin Terajin: " + jinTerajin)
        print("> Jin Termalas: " + jinTermalas)
        print("> Jumlah Pasir: " + str(totalPasir) + " unit")
        print("> Jumlah Batu: " + str(totalBatu) + " unit")
        print("> Jumlah Air: " + str(totalAir) + " unit")


# fungsi untuk menampilkan berbagai informasi mengenai candi seperti total candi yang dibangun, candi termahal, candi termurah, dan jumlah bahan bangunan yang digunakan\
# harga candi dihitung dengan rumus berikut: 10000 * pasir + 15000 * batu + 7500 * air
def laporanCandi() -> None:
    if (var.currentUser[2] != "bandung_bondowoso"):# pengecekan role apakah sudah sesuai atau belum
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        totalCandi = var.candi[1]

        totalPasir = 0
        totalBatu = 0
        totalAir = 0

        idTermahal = "-"
        idTermurah = "-"
        hargaTermahal = 0
        hargaTermurah = 0

        if totalCandi != 0:# pengecekan apakah bandung bondowoso sudah memiliki candi atau belum
            for i in range(totalCandi):
                totalPasir = totalPasir + var.candi[0][i][2]
                totalBatu = totalBatu + var.candi[0][i][3]
                totalAir = totalAir + var.candi[0][i][4]

            idTermahal = str(var.candi[0][0][0])
            idTermurah = str(var.candi[0][0][0])
            hargaTermahal = 10000 * \
                (var.candi[0][0][2]) + 15000 * \
                (var.candi[0][0][3]) + 7500 * (var.candi[0][0][4]) # menghitung harga candi
            hargaTermurah = hargaTermahal
            for i in range(1, totalCandi):
                harga = 10000 * (var.candi[0][i][2]) + 15000 * \
                    (var.candi[0][i][3]) + 7500 * (var.candi[0][i][4]) # menghitung harga candi
                
                # mencari harga termahal
                if harga > hargaTermahal:
                    hargaTermahal = harga
                    idTermahal = str(var.candi[0][i][0])
                    
                # mencari harga termurah
                if harga < hargaTermurah:
                    hargaTermurah = harga
                    idTermurah = str(var.candi[0][i][0])

        # menampikan informasi ke layar
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
