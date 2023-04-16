# file utama di mana program akan berjalan (entry point) 
from util import *
import var
from typing import *
from bondowoso import *
from norole import *
from pembangun import *
from jonggrang import *
from pengumpul import *


# menjalankan fungsi load untuk mengambil data dari file csv sebelum game dimulai
load()

# main loop dari game
while not var.gameEnd:
    command: str = input(">>> ")
    if command == "login":
        login()
    elif (command == "exit"):
        exitProgram()
    elif (command == "help"):
        help()
    elif (command == "logout"):
        logout()
    elif (command == "save"):
        save()
    elif (command == "summonjin"):
        summonJin()
    elif (command == "hapusjin"):
        hapusJin()
    elif (command == "ubahjin"):
        ubahJin()
    elif (command == "batchkumpul"):
        batchKumpul()
    elif (command == "batchbangun"):
        batchBangun()
    elif (command == "laporanjin"):
        laporanJin()
    elif (command == "laporancandi"):
        laporanCandi()
    elif (command == "undo"):
        undo()
    elif (command == "hancurkancandi"):
        hancurkanCandi()
    elif (command == "ayamberkokok"):
        ayamBerkokok()
    elif (command == "bangun"):
        bangun()
    elif (command == "kumpul"):
        kumpul()
    else:
        print("Tidak ada command tersebut")
    
    
    