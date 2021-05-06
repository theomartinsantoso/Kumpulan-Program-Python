
print '==========MENU=========='
print '1. Pesan Kopi'
print '2. Data Mahasiswa'
print '========================'
pilihan = input ('Masukan Pilihan : ')

if pilihan==1:
    kopi=['1. Torabika Susu','2. ABC Susu','3. Good Day','4. Top Coffe']
    print '========PROGRAM PESAN KOPI========'
    print kopi[0]
    print kopi[1]
    print kopi[2]
    print kopi[3]
    print '=================================='
    pesan = input ('Masukkan Pesanan : ')
    if pesan==1:
        print kopi [0],'Kopi Siap Diantar'
    elif pesan==2:
        print kopi[1],'Kopi Siap Diantar'
    elif pesan==3:
        print kopi[2],'Kopi Siap Diantar'
    elif pesan==4:
        print kopi[3],'Kopi Siap Diantar'
    else:
        print 'Maaf Hanya Tersedia 4 Kopi Saja'

elif pilihan==2:
        x = input ('Masukkan Jumlah Mahasiswa : ')
        for i in range(1,x+1,1):
            print '============================='
            print '========Data ke - ',i,'========'
            print '============================='
            nama = raw_input('Masukkan Nama \t\t: ')
            matkul = raw_input('Masukkan Mata Kuliah \t: ')
            uts = input('Masukkan Nilai UTS \t: ')
            uu = input('Masukkan Nilai Ujian Utama \t: ')
            nilai = (uts*0.7)+(uu*0.3)

            print '==========DATA MAHASISWA=========='
            print 'Nama Anda \t: ',nama
            print 'Mata Kuliah \t: ',matkul
            print 'Nilai Rata-Rata Anda : ',nilai
            if nilai>=80:
                print 'Grade A'
            elif nilai>=70:
                print 'Grade B'
            else:
                print 'Grade C'

else:
    print 'Pilihan Tidak Tersedia'
