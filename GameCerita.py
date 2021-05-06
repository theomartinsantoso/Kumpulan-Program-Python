def MENU():
    print """
Kamu tersesat dalam hutan dan hujan pun turun.
Kamu melihat goa dan rumah kecil terbuka sedikit pintunya,
Kamu akan berteduh dimana?
"""
    pilih = raw_input('Pilih rumah atau goa : ')
    if pilih == 'rumah':
        RUMAH()
    elif pilih == 'goa':
        GOA()
    else:
        print 'Game Berakhir'

def RUMAH():
    print """
Atap rumah bocor tapi keadaan rumah terlihat rapi
Apa yang akan kamu lakukan?
1. Masuk rumah
2. Berteduh diluar rumah
"""
    rumah = input('Masukkan pilihan : ')
    if rumah == 1:
        print """
Kamu melihat sekelebat bayangan
Apa yang akan kamu lakukan?
1. Menuju arah bayangan
2. Kembali keluar rumah
"""
        pil = input('Masukkan pilihan : ')
        if pil == 1:
            print 'Tiba-tiba seseorang dibelakangmu dan menikammu dengan pisau'
            MENU()
        elif pil == 2:
            print 'Pintu terkunci tiba-tiba dan seseorang melemparimu dengan batu dan kamu mati'
            MENU()
        else:
            print 'Silahkan pilih dengan benar'
            RUMAH()
    elif rumah == 2:
        print 'Kamu mati kedinginan'
        MENU()
    else:
        print 'Pilihan salah'
        MENU()

def GOA():
    print """
Goa terlihat menyeramkan dan kumuh
Apakah kamu ingin tetap masuk?
1. Ya
2. Tidak
"""
    goa = input('Masukkan pilihan : ')
    if goa == 1:
        print 'Selamat kamu mendapatkan harta karun'
    elif goa == 2:
        print 'Apakah kamu kembali ke rumah?'
        pil = input('Ketik ya/tidak : ')
        if pil == 1:
            RUMAH()
        elif pil == 2:
            print 'Selamat kamu mendapatkan harta karun'
        else:
            print 'Silahkan pilih dengan benar'
            GOA()
    else:
        print 'Kamu mati kedinginan'

MENU() 
