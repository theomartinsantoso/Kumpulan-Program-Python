while True:

    print '''
    Menu Makanan
    -------------------------
    paket A (baso&teh manis) = Rp.12.000
    Paket B (mie ayam&teh manis) = Rp. 15.000
    -------------------------
    '''

    makan = raw_input ('(baso/mie ayam) =')
    minum = raw_input ('(teh manis=)')

    a = 12000
    b = 15000

    if (makan =='baso' and minum =='teh manis'):
        print 'Paket yang anda pilih adalah Paket A'
        try:
            jumlah = float(input('jumlah paket yang dibeli ?'))
            print 'Total harga =Rp ' ,jumlah*a
            break
        except:
            print 'tidak boleh karakter'

    elif (makan =='mie ayam' and minum =='teh manis'):
        print 'Paket yang anda pilih adalah Paket B'
        jumlah = float(input('jumlah paket yang dibeli ?'))
        print 'Total harga =Rp ' ,jumlah*b
        break

    else :
        print 'Tidak ada paket yang anda pilih'
        pilih = raw_input('Apakah anda ingin mengulang (y/t)?')
        if (pilih=='y'):
            continue
        elif (pilih=='t'):
            quit()
        else :
            print 'anda yakin?'
