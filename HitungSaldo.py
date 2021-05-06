print ("")
print ("------ PROGRAM UNTUK MENGHITUNG SALDO ------")
print ("")
print ("by : Theo Martin Santoso (NPM 57418046)")
print ("")

tabungan = int(input("Masukkan jumlah tabungan :"))
lama = int(input("Masukkan jumlah lama menabung (bulan) :"))
 
if tabungan > 15000000 :
     sukuBunga = 0.05
     saldoAkhir = (tabungan * sukuBunga) * lama + tabungan
     print("")
     print("Karena tabungan anda diatas 15.000.000, bunga yang anda dapatkan adalah 5%")
     print("")
     print("Maka setelah menabung selama " + str (lama) + " bulan, saldo anda adalah " +str (saldoAkhir))
 
elif tabungan <= 10000000 and tabungan >=15000000 :
     sukuBunga = 0.03
     saldoAkhir = (tabungan * sukuBunga) * lama + tabungan
     print("")
     print("Karena tabungan anda dibawah 10.000.000, bunga yang anda dapatkan adalah 3%")
     print("")
     print("Maka setelah menabung selama " + str (lama) + " bulan, saldo anda adalah " +str (saldoAkhir))

elif tabungan <= 3000000 and tabungan >=1000000 :
     sukuBunga = 0.02
     saldoAkhir = (tabungan * sukuBunga) * lama + tabungan
     print("")
     print("Karena tabungan anda dibawah 3.000.000, bunga yang anda dapatkan adalah 2%")
     print("")
     print("Maka setelah menabung selama " + str (lama) + " bulan, saldo anda adalah " +str (saldoAkhir))

else :
    sukuBunga = 0.00
    saldoAkhir = (tabungan * sukuBunga) * lama + tabungan
    print("Karena tabungan anda dibawah 3.000.000, bunga yang anda dapatkan adalah 0%")
    print("")
    print("Maka setelah menabung selama " + str (lama) + " bulan, saldo anda adalah " +str (saldoAkhir))
