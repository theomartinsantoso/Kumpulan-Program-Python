import random
def hitung(x,y):
    a = random.randint(1,100)
    b = random.randint(1,100)
    jawab = int(input(str(a)+" - "+str(b)+" = "))

    if(x==10):
        print "Anda menjawab semua dengan benar!"
    elif(jawab==a-b):
        x += 1
        print "Anda benar, jawab sebanyak ",10-(x-1), "lagi"
        hitung (x,y)
    elif(jawab != a+b and y == 3):
        print "Anda sudah salah sebanyak 3x"
        print "Anda dinyatakan gagal"
    else:
        print "Jawaban salah!!"
        print "yang benar adalah ",a-b
        y += 1
        hitung(x,y)

x = 1
y = 1
print "Masukkan jawaban yang benar sebanyak 10x"
print "============Untuk Menang================"
print "========================================"
hitung (x,y
