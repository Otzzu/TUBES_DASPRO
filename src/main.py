from util import *
import var
from typing import *
from bondowoso import *
from norole import *
from pembangun import *
from jonggrang import *
from pengumpul import *


load()

while not var.gameEnd:
    masukan: str = input(">>> ")
    if (masukan == "help"):
        help(var.currentUser[2])
    elif (masukan == "save"):
        save()
    elif (masukan == "exit"):
        exitProgram()
    else:
        if (var.currentUser[2] == "bandung_bondowoso"):
            commandBondowoso(masukan)
        elif (var.currentUser == ("", "", "")):
            commandNoRole(masukan)
        elif (var.currentUser[2] == "jin_pengumpul"):
            commandPengumpul(masukan)
        elif (var.currentUser[2] == "jin_pembangun"):
            commandPembangun(masukan)
        elif (var.currentUser[2] == "roro_jonggrang"):
            commandJonggrang(masukan)
    
    