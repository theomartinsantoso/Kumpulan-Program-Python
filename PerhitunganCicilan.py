tagihan=input("Jumlah Tagihan: ")

jumlah_cicilan=input("Jumlah Angsuran: ")
uang_muka=input("Uang Muka: ")
 
sisa_t=tagihan-uang_muka
sisa_c=jumlah_cicilan
jumlah_bunga=0
bunga=2.00/100

def get_bunga():
  return sisa_t*bunga
 
def get_cicilan():
  return sisa_t/sisa_c
 
def get_total_bayar():
  return get_bunga()+get_cicilan()
 
print "Tagihan %d, diangsur %dx dengan uang muka %d \n" % (tagihan,jumlah_cicilan,uang_muka)
 
for i in range(jumlah_cicilan):
  print "Cicilan ke-%d: %d + %d = %d" % (i+1,get_cicilan(),get_bunga(),get_total_bayar())
  jumlah_bunga+=get_bunga()
  sisa_t-=get_cicilan()
  sisa_c-=1
 
print "\nBayar Uang Muka: %d\nTotal Bayar Cicilan: %d\nTotal Bunga: %d\nTotal: %d" %(uang_muka,tagihan-uang_muka,jumlah_bunga,tagihan+jumlah_bunga)
