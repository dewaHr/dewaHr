def tambah(bilangan1,bilangan2):
    return bilangan1 + bilangan2
def kurang(bilangan1,bilangan2):
    return bilangan1 - bilangan2
def bagi(bilangan1,bilangan2):
    return bilangan1 / bilangan2
def kali(bilangan1,bilangan2):
    return bilangan1 * bilangan2
print("Pilih Operasi")
print("1.Pertambahan")
print("2.Pengurangan")
print("3.Pembagian")
print("4.Perkalian")
while True:
    operasi = input("Masukan Pilihan (1/2/3/4):")
    if operasi in("1","2","3","4"):
        bilangan1= float(input("Bilangan Pertama :"))
        bilangan2= float(input("Bilangan Kedua :"))
        if operasi == '1':
            print (bilangan1,"+", bilangan2, "=",tambah(bilangan1,bilangan2))
        elif operasi == '2':
            print (bilangan1,"-", bilangan2, "=",kurang(bilangan1,bilangan2))
        elif operasi == '3':
            print (bilangan1,"/", bilangan2, "=",bagi(bilangan1,bilangan2))
        elif operasi == '4':
            print (bilangan1,"×", bilangan2, "=",kali(bilangan1,bilangan2))