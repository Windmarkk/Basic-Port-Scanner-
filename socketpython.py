#!/usr/bin/env python3
import socket
import time
import threading
import concurrent.futures

lock = threading.Lock()

def portTara(hedef,hedefPort):
    #Tekli port tarayici, eger port aciksa numarayi dondurecek.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        s.connect((hedef,hedefPort))
        return hedefPort
    except (TimeoutError,ConnectionAbortedError,ConnectionRefusedError,OSError):
        return None
    finally:
        s.close()


def cokluTara():
    hedef = input("\n\nHedef adres giriniz: ")
    try:
        baslangicPort = int(input("Baslangic Portunu Giriniz:"))
        bitisPort = int(input("Bitis Portunu Giriniz:"))
    except ValueError:
        print("Gecerli bir port numarasi girin!")
        return
    
    if baslangicPort > bitisPort:
        print("Hata,baslangic portu , bitis portundan buyuk olamaz.")
        return
    if baslangicPort>65535 or baslangicPort<1 or bitisPort > 65535 or bitisPort<1:
        print("Port araliklarinin disinda deger girdiniz!") 
        return

    baslamaSure = time.time()
    acikportlar = []

    #concurrent.futures ile rahatca threading ayarlamasi yapiyoruz. Herhangi bir problem olmayacagina inanarak max_workers=none yaptim.
    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as yonetici:
        futures ={
            yonetici.submit(portTara,hedef,port): port
            for port in range(baslangicPort,bitisPort + 1)
        }
        for future in concurrent.futures.as_completed(futures):
            sonuc = future.result()
            if sonuc is not None:
                with lock:
                    acikportlar.append(sonuc)
    
    acikportlar.sort()
    bitisSure = time.time()
    gecenSure = bitisSure - baslamaSure
    print(f"\nAcik Portlar: {acikportlar} \n\ngecen sure: {gecenSure}")

def tekliTara():
    hedef = input("\n\nHedef Adresi Giriniz: ")

    try:
        portNum = int(input("Hedef Portu Giriniz: "))
    except ValueError:
        print("Sayi girmen lazim abicim")
        return
    
    sonuc = portTara(hedef,portNum)

    if sonuc is not None:
        print(f"Port {sonuc} Acik!")
    else:
        print(f"Porta ulasamadik :(")
    

def menu():
    print("Port scanner'a hos geldiniz, islem secin\n1-Tek port tarama\n2-Coklu port tarama")
    secim = int(input())
    if secim == 1:
        tekliTara()
    elif secim==2:
        cokluTara()
    else:
        print("Gecersiz islem!")

if __name__ == "__main__":
    menu()