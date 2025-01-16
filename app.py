#Hitung Luas Segitiga Sederhana
def luas_segitiga():
    a = int (input("Masukkan Alas Segitiga:"))
    t = int (input("Masukkan Tinggi Segitiga:"))
    luas = a * t / 2
    print("Luas Segitiga adalah;", luas)

luas_segitiga()

#Hitung Luas Persegi Panjang
def luas_persegi_panjang ():
    p = int(input("Masukkan Panjang Persegi:"))
    l = int(input("Masukkan Lebar Persegi:"))
    luas = p * l
    print ("Luas Persegi adalah:", luas)

luas_persegi_panjang()

#Hitung Luas Lingkaran 
def luas_lingkaran():
    r = int(input("Masukkan jari -jari lingkaran:"))
    luas = 3.14 * r * r
    print("Luas Lingkaran adalah :", luas)

luas_lingkaran()