
import os 
from colorama import *
def site_engeller():
    local = "127.0.0.1"
    print(Fore.GREEN+"Site Engelleyici")
    user = input(Fore.LIGHTYELLOW_EX+"Engellenecek Siteyi Girin :")
    try:
        os.chdir("/etc/")
        with open("hosts","a") as dosya:
            dosya.write("\n"+local+"    "+user+"\n")
            print(Fore.RED+"Site engellendi")
    except:
        print("Hata")

site_engeller()