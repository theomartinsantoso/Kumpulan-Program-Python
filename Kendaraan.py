class Kendaraan(object):
  
  def __init__(self, nama):
    self.nama = nama
    self.penumpang = []
    
  def tambah_penumpang(self, nama_penumpang):
    self.penumpang.append(nama_penumpang)
    
class Motor(Kendaraan):
  
  # melakukan definisi ulang terhadap metode ini
  def tambah_penumpang(self, nama_penumpang):
    if len(self.penumpang) < 4:
      # memanggil kembali metode asli dari Kendaraan
      super(Motor, self).tambah_penumpang(nama_penumpang)
    else:
      # Jika sudah ada dua penumpang maka kita tidak masukkan
      print "Maaf {}, anda tidak bisa masuk".format(nama_penumpang) 
    
motor = Motor('CSMotor')
motor.tambah_penumpang('Raisa')
motor.tambah_penumpang('Isyana')
motor.tambah_penumpang('Afgan')

print "Penumpang : " + str(motor.penumpang)
