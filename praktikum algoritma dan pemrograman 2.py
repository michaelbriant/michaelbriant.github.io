print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')


import math

def hitung_a(b, c):
    return math.sqrt(c**2 - b**2)

def hitung_b(a, c):
    return math.sqrt(c**2 - a**2)

def hitung_c(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    print("Menghitung Pythagoras")
    print("a.) menghitung sisi a")
    print("b.) menghitung sisi b")
    print("c.) menghitung sisi c")

    opsi = input("masukkan opsi: ")

    # menghitung sisi a
    if opsi == "a":
        b = float(input("Masukkan sisi b: "))
        c = float(input("Masukkan sisi c: "))
        while c < b:
            print("Nilai c harus lebih besar atau sama dengan nilai b.")
            c = float(input("Masukkan nilai sisi c: "))
        sisi_a = hitung_a(b, c)
        print(f"Sisi a = {sisi_a}")

    # menghitung sisi b
    elif opsi == "b":
        a = float(input("Masukkan sisi a: "))
        c = float(input("Masukkan sisi c: "))
        while c < a:
            print("Nilai c harus lebih besar atau sama dengan nilai a.")
            c = float(input("Masukkan nilai sisi c: "))
        sisi_b = hitung_b(a, c)
        print(f"Sisi b = {sisi_b}")

    # menghitung sisi c
    elif opsi == "c":
        a = float(input("Masukkan sisi a: "))
        b = float(input("Masukkan sisi b: "))
        sisi_c = hitung_c(a, b)
        print(f"Sisi c = {sisi_c}")

    else:
        print("Opsi tidak valid.")

if __name__ == "__main__":
    main()


print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

# Menerima input dari pengguna untuk tiga angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
angka3 = float(input("Masukkan angka ketiga: "))

# Mencari angka terbesar
terbesar = angka1

if angka2 > terbesar:
    terbesar = angka2

if angka3 > terbesar:
    terbesar = angka3

# Menampilkan hasil
print(f"Angka terbesar adalah: {terbesar}")
