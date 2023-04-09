from typing import *

global currentUser, users, candi, bahan_bangunan
currentUser: Tuple[str,str,str] = ("", "", "")
users: Tuple[List[Tuple[str,str,str]], int] = ([], 0)
candi: Tuple[List[Tuple[int,int,int,int]], int]= ([],0)
bahanBangunan: Tuple[List[Tuple[str,str,int]], int] = ([],0)
gameEnd: bool = False
