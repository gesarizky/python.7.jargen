# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput alas , sisi miring , dan tinggi
alas = float(input('Tulis Alas Jajar Genjang: '))
tinggi = float(input('Tulis Tinggi Jajar Genjang: '))
sisi = float(input('Tulis Sisi Miring: '))

# Hitung Luas dan Keliling Lingkaran
luas = alas * tinggi
keliling = 2 * ( alas + sisi)

#Menampilkan Hasil Perhitungan
print('Luas Jajar Genjang  adalah %0.2f' %luas)
print('keliling Jajar Genjang adalah %0.2f' %keliling)
