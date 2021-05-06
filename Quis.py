class tahun:
    def selamat(self):
        print 'Selamat Datang'
        pilih = raw_input ('Apakah Anda Ingin Mendaftar ? [y atau n] : ')
        if pilih == "y" :
            print ' '
            menu()
        elif pilih == "n" :
            exit()
        else :
            print 'Program Berhenti'
               
                
def menu() :
    jum = input ('Mau Daftar untuk berapa orang ? : ')
    print '========================================'
    for i in range (1,jum+1,1) :    
        nama = raw_input ('Masukkan Nama Anda : ')
        pekerjaan = raw_input ('Masukkan Pekerjaan Anda : ')
        umur = input ('Masukkan Umur Anda : ')
        tlp = raw_input ('Masukkan Nomer Telepon Anda : ')
        print '''==========================================
        Selamat Anda Sudah daftar 
        Dengan Nama ''' ,nama
        print '=========================================='
        
    

org = tahun()
org.selamat()
