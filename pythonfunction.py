def fungsi():
    print ("Ini adalah Fungsi")
fungsi()

# # Function calling Function
def suaraAyam():
    print("Kukuruyuk")

def hargaAyam():
    suaraAyam()
    print("harga ayam 1kg 20.000")
hargaAyam()

# # Count with function
def hargatotalAyam(kg):
    hargaAyam = 20000
    hargaTotal = kg*hargaAyam
    print("harga",kg,"kg ayam adalah", hargaTotal)

hargatotalAyam(int(input("Masukan Berat ayam : ")))

