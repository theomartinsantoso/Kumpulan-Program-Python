print '''

TIKET KERETA
------------
Bekasi - Manggarai = Rp. 3000
Bekasi - Kota = Rp. 5000
------------
'''
asal = raw_input('Masukkan Lokasi Masuk (Bekasi) : ')

if asal=='bekasi':
    tujuan = raw_input('Masukkan Lokasi Tujuan (Manggarai/Kota) : ')
    print '--------------------'
    if asal=='bekasi' and tujuan=='manggarai':
        print 'Harga Tiket = Rp. 3000'
    elif asal=='bekasi' and tujuan=='kota':
        print 'Harga Tiket = Rp. 5000'
    else:
        print 'Tujuan Tidak Ada'
else:
    print 'Lokasi Masuk Salah'
