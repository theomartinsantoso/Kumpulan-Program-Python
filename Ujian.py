def menu():

    print '''
    ============== MENU =============
    1. PROGRAM KALKULATOR
    2. PROGRAM LUAS SEGITIGA
    3. PROGRAM LUAS PERSEGI
    4. PROGRAM GAJI
    5. PROGRAM SUHU
    6. PROGRAM GANJIL
    7. PROGRAM GENAP
    8. PROGRAM RANGE
    9. PROGRAM KOPI
    10. EXIT
    ================================== '''
    pil = input ("Masukkan Pilihan Anda: ")
    if pil == 1:
        kalkulator()
        menu()
    elif pil == 2:
        segitiga()
        menu()
    elif pil == 3:
        persegi()
        menu()
    elif pil == 4:
        gaji()
        menu()
    elif pil == 5:
        suhu()
        menu()
    elif pil == 6:
        ganjil()
        menu()
    elif pil == 7:
        genap()
        menu()
    elif pil == 8:
        jarak()
        menu()
    elif pil == 9:
        kopi()
        menu()
    elif pil == 10:
        exit()
    else:
        print "Pilihan Anda Tidak Tersedia"
        menu()

def kalkulator():
    print "======= PROGRAM KALKULATOR ======="
    a = input ("Masukkan Angka 1 : ")
    b = input ("Masukkan Angka 2 : ")
    print a,'+' ,b, '=',a+b
    print a,'-' ,b, '=',a-b
    print a,'*' ,b, '=',a*b
    print a,'/' ,b, '=',a/b
    
def segitiga():
    print "======= PROGRAM SEGITIGA ======="
    a = input ("Masukkan Angka 1: ")
    b = input ("Masukkan Angka 2: ")
    l = (a*b)/2
    print "Luas Segitiga Adalah " ,l

def persegi():
    print "======== PROGRAM PERSEGI ========"
    s = input ("Masukkan Sisi : ")
    l = s*s
    print "Luas Persegi Adalah " ,l

def ganjil():
    i = 0
    for i in range (1,20,i+2):
        print i

def genap():
    i = 0
    for i in range (0,20,i+2):
        print i

def jarak():
    a = input ("Masukkan Angka : ")
    for i in range (0,a) :
        print i

def gaji():
    print "======= PROGRAM GAJI ======="
    a = raw_input ("Nama : ")
    b = input ("Jumlah Anak : ")
    c = input ("Gaji : ")
    t = (b*c*0.1)
    g = (c+t)
    print ' '
    print "Nama         : " ,a
    print "Jumlah Anak  : " ,b
    print "Gaji         : " ,c
    print "Tunjangan    : " ,t
    print "Gaji Total   : " ,g

def suhu():
    print "========== PROGRAM SUHU ==========="
    c = float (input ("Masukkan Celcius : "))
    f = float (input ("Masukkan Fahrenheit : "))
    r = float (input ("Masukkan Reamur : "))
    k = float (input ("Masukkan Kelvin : "))
    print "Hasil Celcius ke Fahrenheit adalah " ,5/9*(f-32)
    print "Hasil Celcius ke Kelvin adalah " ,k-273
    print "Hasil Celcius ke Reamur adalah " ,(5/4)*r

def kopi():
    kopi = ["Torabika Susu","ABC Susu","Good Day","Top Coffe"]
    print '''
    ========= PROGRAM KOPI =======
    1. Torabika Susu
    2. ABC Susu
    3. Good Day
    4. Top Coffe
    5. Exit
    ============================== '''
    pil = input ("Masukkan Pilihan Anda : ")
    if pil == 1:
        print kopi[0], "Siap diantar"
    elif pil == 2:
        print kopi[1], "Siap diantar"
    elif pil == 3:
        print kopi[2], "Siap diantar"
    elif pil == 4:
        print kopi[3], "Siap diantar"
    elif pil == 5:
        exit()
    else:
        print "Tidak Ada Yang Anda Pilih"

menu()
        
