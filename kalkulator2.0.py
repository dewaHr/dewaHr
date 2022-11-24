def tambah(bilangan1, bilangan2):
    return bilangan1 + bilangan2


def kurang(bilangan1, bilangan2):
    return bilangan1 - bilangan2


def bagi(bilangan1, bilangan2):
    return bilangan1 / bilangan2


def kali(bilangan1, bilangan2):
    return bilangan1 * bilangan2


print("========== Pilih Menu ==========")
print("Pilih Operasi")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
while True:
    operasi = input("Masukan Pilihan (1/2/3/4):")
    if operasi in ("1", "2", "3", "4"):
        bilangan1 = int(input("Masukan Angka Pertama :"))
        bilangan2 = int(input("Masukan Angka Kedua :"))
        if operasi == '1':
            print("Hasil =", tambah(bilangan1, bilangan2))
        elif operasi == '2':
            print("Hasil =", kurang(bilangan1, bilangan2))
        elif operasi == '3':
            print("Hasil =", kali(bilangan1, bilangan2))
        elif operasi == '4':
            print("Hasil =", bagi(bilangan1, bilangan2))
