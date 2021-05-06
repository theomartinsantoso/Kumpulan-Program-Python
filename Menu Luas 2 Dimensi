def menu():
    print """
    =================================
                MENU UTAMA
    =================================
    1. Kalkulator
    2. Segitiga
    3. Persegi
    4. Keluar
    =================================
    """
    pil= input("Masukkan Pilihan : ")
    print " "
    if pil == 1:
        kalkulator()
        menu()
    elif pil==2:
        segitiga()
        menu()
    elif pil==3:
        persegi()
        menu()
    elif pil==4:
        keluar()
    else:
        print "Maaf Inputan Anda Tidak Tersedia" ,menu()

def kalkulator():
    print "**********PROGRAM KALKULATOR**********"
    print "======================================"
    a = input("Masukkan Angka 1: ")
    b = input("Masukkan Angka 2: ")
    c = a+b
    d = a-b
    e = a*b
    f = a/b
    print a, "+" ,b, "=" ,c
    print a, "-" ,b, "=" ,d
    print a, "x" ,b, "=" ,e
    print a, ":" ,b, "=" ,f
    print " "

def segitiga():
    print "***********PROGRAM SEGITIGA***********"
    print "======================================"
    print "Menghitung Luas Segitiga"
    alas = input("Masukkan Alas : ")
    tinggi = input("Masukkan Tinggi : ")
    luas = (alas*tinggi)/2
    print "Luasnya adalah " ,luas
    print " "

def persegi():
    print "***********PROGRAM PERSEGI************"
    print "======================================"
    print "Menghitung Luas Persegi"
    sisi = input("Masukkan Angka : ")
    luas = sisi*sisi
    print "Luas Persegi adalah " ,luas
    print " "

def keluar():
    exit()

menu()
