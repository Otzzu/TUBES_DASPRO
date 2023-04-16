# file yang berisi variabel global yang digunakan dalam program game ini
from typing import *

# type user: <username: string; password: string; role: string>
# type arrUser: <arr: array of user; panjang: int>
# type candi: <id: int; pembuat: string; pasir: int, batu: int, air: int>
# type arrCandi: <arr: array of candi; panjang: int>
# type bahan: <nama: string; deskripsi: string; jumlah: int>
# type arrBahan: <arr: array of bahan; panjang: int>
# type undoData: <jin: user; candi: arrCandi>
# type stackUndo: <stack: array of undoData; panjang: int>


currentUser = ("", "", "") # tipe data: user
users = ([], 0) # tipe data: arrUser
candi= ([],0) # tipe data: arrCandi
bahanBangunan = ([],0) # tipe data: arrBahan
gameEnd = False # tipe data: boolean
stackUndo = [[], 0] # tipe data stackUndo

