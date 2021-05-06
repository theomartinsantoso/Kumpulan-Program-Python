def menu():
    print '''
    ========== MENU ========== 
    1. PROGRAM PANGGIL NAMA
    2. PROGRAM NILAI MAHASISWA
    3. PROGRAM KALKULATOR
    4. PROGRAM BITWISE
    5. PROGRAM BANGUN DATAR
    6. PROGRAM ANGKA
    7. PROGRAM TEH
    8. KELUAR
    ==========================
    '''
    a = input ("Masukkan Pilihan Anda : ")
    if a == 1:
        nama()
        tanyamenu()
    elif a == 2:
        mhs()
        tanyamenu()
    elif a == 3:
        kalkulator()
        tanyamenu()
    elif a == 4:
        bitwise()
        tanyamenu()
    elif a == 5:
        bangundatar()
        tanyamenu()
    elif a == 6:
        angka()
        tanyamenu()
    elif a == 7:
        teh()
        tanyamenu()
    elif a == 8:
        exit()
    else:
        print "Pilihan Tidak Tersedia"

def nama():
    print "==== PROGRAM PANGGIL NAMA ===="
    a = raw_input ("Masukkan Nama Anda : ")
    print "Hai",a
    
def mhs():
    print "==== PROGRAM NILAI MAHASISWA ===="
    nama = raw_input("Masukkan Nama : ")
    npm = raw_input("Masukkan NPM : ")
    matkul = raw_input("Mata Pelajaran : ")
    uts = input("Nilai UTS : ")
    uas = input("Nilai UAS : ")
    hasil = (uts*0.7)+(uas*0.3)
    print "Nama : ",nama
    print "NPM : ",npm
    print "Saya Mendapat Nilai ",hasil," pada mata kuliah ",matkul

def bangundatar():
    print "==== PROGRAM BANGUN DATAR ===="
    print '''
    ===================
    1. Segitiga
    2. Persegi
    3. Lingkaran
    4. Kembali ke Menu
    =================== '''
    g = input('Masukkan bangun Datar yang di Inginkan : ')
    if g == 1:
        print "==Menghitung Luas Segitiga=="
        alas = input ("Masukkan Alas : ")
        tinggi = input ("Masukkan Tinggi : ")
        print "Hasilnya adalah : ",float(alas*tinggi)/2
        bangundatar()
    elif g == 2:
        print "==Menghitung Luas Persegi=="
        sisi = input("Masukkan Sisi :")
        print "Hasilnya adalah : ",sisi*sisi
        bangundatar()
    elif g == 3:
        print "==Menghitung Luas Lingkaran=="
        jari = input("Masukkan Jari Jari : ")
        print "Hasilnya adalah : ",float(22/7*jari*jari)
        bangundatar()
    elif g == 4:
        menu()
    else:
        print "Maaf Pilihan Tidak Tersedia"

def kalkulator():
    print "====== PROGRAM KALKULATOR ======"
    a = input ("Masukkan Angka 1 : ")
    b = input ("Masukkan Angka 2 : ")
    print a,'+' ,b, '=',a+b
    print a,'-' ,b, '=',a-b
    print a,'*' ,b, '=',a*b
    print a,'/' ,b, '=',a/b

def bitwise():
    print "==== PROGRAM BITWIISE ===="
    a = input("Masukkan Nilai 1: ")
    b = input("Masukkan Nilai 2: ")
    print "Operasi AND = ",a&b
    print "Operasi OR = ",a|b
    print "Operasi XOR = ",a^b
    print "Operasi NOT = ",~a

def angka():
    print "==== PROGRAM ANGKA ===="
    a = input("Masukkan Angka: ")
    for i in range (a):
        print(i)

def teh():
    print "==== PROGRAM TEH ===="
    teh = ["Coklat" , "Greentea" , "Original" , "Kopi"]
    print '''
    ============
    Pilihan Rasa
    1. Coklat
    2. Greentea
    3. Original
    4. Kopi
    ============ '''
    pil = input("Masukkan Pilihan Anda : ")
    if pil == 1:
        print 'Thaitea Rasa' ,teh [0], 'Siap Diantar'
    elif pil == 2:
        print 'Thaitea Rasa' ,teh [1], 'Siap Diantar'
    elif pil == 3:
        print 'Thaitea Rasa' ,teh [2], 'Siap Diantar'
    elif pil == 4:
        print 'Thaitea Rasa' ,teh [3], 'Siap Diantar'
    else:
        print "Pilihan Anda Tidak Tersedia"

def tanyamenu() :
    tanya = raw_input("Kembali ke menu (y/t)? ")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print "Salah Input"

menu()
