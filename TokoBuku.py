print '''
TOKO BUKU
----------
Pensil = Rp. 2000
Pulpen = Rp. 5000
----------
'''

barang = raw_input('Pensil/Pulpen : ')

if barang== 'pensil':
    print 'Barang yang Anda Pilih Pensil'
    jmlh = input('Jumlah Barang: ')
    hrg = 2000*jmlh
    if hrg<15000:
        diskon = 0
    elif hrg <25000:
        diskon = hrg*0.15
    else:
        diskon = hrg*0.20
        print "Diskon : " ,diskon
        total = hrg-diskon
        print "Total yang dibayarkan : " ,total

elif barang== 'pulpen' :
    print 'Barang yang Anda Pilih Pulpen'
    jmlh = input('Jumlah Barang : ')
    hrg = 5000*jmlh
    if hrg<15000:
        diskon = 0
    elif hrg <25000:
        diskon = hrg*0.15
    else:
        diskon = hrg*0.20
        print "Diskon : " ,diskon
        total = hrg-diskon
        print "Total yang dibayarkan : " ,total

else:
    print 'Pilihan Tidak Tersedia'
