#created by alvin meko
#www.kodingbeta.wordpress.com

import random

def ulang():
    ulang = input("Apakah anda ingin mengulang ? y/t ")
    if ulang=="y":
        tebakangka()
    
def tebakangka():
    mynum = random.randint(-1, 11)
    tries = 3
    berhasil = False
    
    print("Saya memikirkan sebuah angka antara 1-10")
    while berhasil==False and tries>0:
        mygues = int(input("tebakan anda ? "))
        if mygues == mynum:
            print("Anda berhasil menebak dengan benar")
            berhasil = True
        elif mygues < mynum:
            print("Angka tebakan anda terlalu kecil")
            tries = tries-1
        elif mygues > mynum:
            print("Angka tebakan anda terlalu besar")
            tries = tries-1
        
    if tries <= 0:
        print("Sayang sekali anda gagal menebaknya")
    ulang()
                

nama = input("masukkan nama anda : ")
if len(nama)>1:
    print("Hai ", nama)
    pilih = input("Apakah anda ingin bermain tebak angka ? y/n : ")
    if pilih=="y":
        tebakangka()
