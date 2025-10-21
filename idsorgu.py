# SNAPELANG
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """ 

 -  SNAPELANG ID SORGULAMA PANELI  -


""" + Fore.LIGHTCYAN_EX)
print(banner)
userid = input(" [SNAPELANG] SORGULANCAK ID : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [SNAPELANG] TOKENININ İLK PARTI : {encodedStr}')
os.system('pause >nul') 
