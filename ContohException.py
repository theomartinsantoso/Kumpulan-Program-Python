try:

    x = 'Gunadarma'
    input1 = input ("Masukan inputan 1 : ")
    print x [input1]
except IndexError:
    print 'Index tidak ada'
except NameError:
    print 'Tidak boleh karakter'
