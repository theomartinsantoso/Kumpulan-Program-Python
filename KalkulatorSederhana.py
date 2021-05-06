print "Selamat datang di program kalkulator python"
print "==========================================="
print "1.Penjumlahan"
print "2.Pengurangan"
print "3.perkalian"
print "4.Pembagian"
print "==========================================="
n=input("Masukkan pilihan= ")

if n==1:
    x=input("Angka pertama= ")
    y=input("Angka kedua= ")
    print(x+y)
#(^) yang diatas itu namanya indentasi. dibawah percabangan harus ada spasi(tab).
elif n==2:
    x=input("Angka pertama= ")
    y=input("Angka kedua= ")
    print(x-y)
elif n==3:
    x=input("Angka pertama= ")
    y=input("Angka kedua= ")
    print(x*y)
elif n==4:
    x=input("Angka pertama= ")
    y=input("Angka kedua= ")
    print(x/y)
else:
    print "Pilihan tidak ditemukan"
