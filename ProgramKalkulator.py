def tambah () :
    print '1.Penjumlahan'
    a = input ('Masukkan nilai 1 = ')
    b = input ('Masukkan nilai 2 = ')
    c = a+b
    print 'x + y = ',c
    print (' ')
    tanya ()

def kurang () :
    print '2.Pengurangan'
    a = input ('Masukkan nilai 1 = ')
    b = input ('Masukkan nilai 2 = ')
    c = a-b
    print 'x – y = ',c
    print (' ')
    tanya ()

def kali () :
    print '3.Perkalian'
    a = input ('Masukkan nilai x = ')
    b = input ('Masukkan nilai y = ')
    c = a*b
    print 'x . y = ',c
    print (' ')
    tanya ()

def bagi () :
    print '4.Pembagian'
    a = input ('Masukkan nilai x = ')
    b = input ('Masukkan nilai y = ')
    c = a/b
    print 'x : y = ',c
    print (' ')
    tanya ()

def tanya () :
    lagi = raw_input ('Ulangi lagi (Y/T)? ')
    if lagi == 'Y' or lagi=='y' :
        menu ()
    elif lagi == 'T' or lagi=='t' :
        print 'Terima kasih sudah menggunakan program ini'
        quit()
    else :
        print 'Maaf, input yang Anda masukkan salah'
        print 'Silahkan masukkan Y atau T'

def menu():
    print ('Program Kalkulator Sederhana')
    print ('============================')
    print ('1. Penjumlahan')
    print ('2. Pengurangan')
    print ('3. Perkalian')
    print ('4. Pembagian')
    print ('============================')
    print ('Silahkan pilih 1-4')
    print (' ')
    pilihan()
    
def pilihan ():
    pil = raw_input ('Masukkan pilihan : ')
    if pil == '1':
        tambah ()
        menu ()
    elif pil == '2':
        kurang ()
        menu ()
    elif pil == '3':
        kali ()
        menu()
    elif pil  == '4':
        bagi ()
        menu ()
    else :
        print ('Maaf, input yang Anda masukkan salah')
        print ('coba ulangi lagi')
        tanya()
        
pilihan()
