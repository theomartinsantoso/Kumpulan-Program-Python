import math,random
 
pil_min=1
pil_max=1000
pilihan=0
 
def mulaiGame():
	jawaban=pil_min+math.floor(random.random()*(pil_max-pil_min))
	dipilih=''
	menebak=0
	print "Silahkan tebak angka antara "+str(pil_min)+" sampai "+str(pil_max)
	while(dipilih!=jawaban):
		menebak+=1
		dipilih=input('Jawaban Kamu: ')
		if(dipilih>jawaban):
			print "Angka terlalu besar"
		elif(dipilih<jawaban):
			print "Angka terlalu kecil"
 
	print "Kamu benar, jawabannya adalah "+str(jawaban)+". "+str(menebak)+"x Tebakan"
 
while(pilihan!=2):
	print "=============="
	print "= MENU UTAMA ="
	print "=============="
	print "(1) Mulai Game"
	print "(2) Keluar"
	print "\nMasukan nomor yang dipilih"
	pilihan=input("==> ")
	if(pilihan==1):
		mulaiGame()
 
 
print "================"
print "= GAME SELESAI ="
print "================"
