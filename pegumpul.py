import var
from util import *
from typing import *
import random

def commandPengumpul(command: str) -> None:
    if (command == "kumpul"):
        kumpul()
        
def kumpul() -> None:
    pasir: int = random.randint(0, 5)
    batu: int = random.randint(0, 5)
    air: int = random.randint(0, 5)
    
    print("Jin menemukan " + str(pasir) + " pasir, " + str(batu) + " batu, dan " + str(air) + "air")
    var.bahanBangunan[0][0] = ("pasir", "", var.bahanBangunan[0][0][2] + pasir)
    var.bahanBangunan[0][1] = ("batu", "", var.bahanBangunan[0][1][2] + batu)
    var.bahanBangunan[0][2] = ("air", "", var.bahanBangunan[0][2][2] + air)
    print(var.bahanBangunan)
    
    