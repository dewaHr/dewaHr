import math
# # Menghitung Luas Persegi Panjang
# def hitungLuaspp(masukanPanjang,masukanLebar):
#     return masukanPanjang*masukanLebar
    
# masukanPanjang = int(input("Masukan Panjang Persegi : "))
# masukanLebar = int(input("Masukan Lebar Persegi : "))
# print("Luas Persegi adalah : ", hitungLuaspp(masukanPanjang,masukanLebar))

# # Menghitung Suhu Celsius ke Reamur, Farenheit, dan Kelvin
# print("++++++++++ Program Konversi Suhu ++++++++++")


def suhuReamur(celsius):
    suhuReamurs = 4/5*celsius
    return suhuReamurs
def suhuFarenheit(celsius):
    suhuFarenheit = (9/5*celsius)+32
    return suhuFarenheit
def suhuKelvin(celsius):
    suhuKelvin = 273+celsius
    return suhuKelvin
def reamurkeCelsius(reamur):
    reamurkeCelsius = 5/4*reamur
    return reamurkeCelsius
def reamurkeFarenheit(reamur):
    reamurkeFarenheit = (9/4 * reamur)+32
    return reamurkeFarenheit
def reamurkeKelvin(reamur):
    reamurkeKelvin = (reamur*5/4)+273
    return reamurkeKelvin
def farenheitkeCelsius(farenheit):
    farenheitkeCelsius= 5/9*(farenheit-32)
    return farenheitkeCelsius
def farenheitkeReamur(farenheit):
    farenheitkeReamur =(farenheit-32)*4/9
    return farenheitkeReamur
def farenheitkeKelvin(farenheit):
    farenheitkeKelvin =(farenheit-32)*5/9+273
    return farenheitkeKelvin
def kelvinkeCelcius(kelvin):
    kelvinkeCelcius=kelvin-273
    return kelvinkeCelcius
def kelvinkeFarenheit(kelvin):
    kelvinkeFarenheit=(kelvin - 273)*9/5+32
    return kelvinkeFarenheit
def kelvinkeReamur(kelvin):
    kelvinkeReamur =(kelvin-273.15)*4/5
    return kelvinkeReamur

# celsius = int(input("Masukan Suhu Celsius : "))
# print("Hasil Konversi Suhu",celsius, "C" ,suhuReamur(celsius),"Reamur")
# print("Hasil Konversi Suhu",celsius, "C" ,suhuFarenheit(celsius),"Farenheit")
# print("Hasil Konversi Suhu",celsius, "C" ,suhuKelvin(celsius),"Kelvin")
# print("++++++++++++++++++++++++++++++++++++++++++++++++++")






print('Jenis suhu yang ingin di Konversi')
print("1. Celcius")
print("2. Reamur")
print("3. Kelvin")
print("4. Farenheit")
while True:
    opsiPilihan = input("Pilih Suhu Yang Ingin di Konversi :")
    jumlahSuhu = int(input("Masukan Jumlah Suhu : "))
    if opsiPilihan in ("1","2","3","4"):
        if opsiPilihan == "1":
            print("Hasil Konversi adalah : ",suhuReamur(jumlahSuhu),"Reamur")
            print("Hasil Konversi adalah : ",suhuKelvin(jumlahSuhu),"Kelvin")
            print("Hasil Konversi adalah : ",suhuFarenheit(jumlahSuhu),"Farenheit")
        elif opsiPilihan == "2":
            print("Hasil Konversi adalah : ",reamurkeCelsius(jumlahSuhu),"Celcius")
            print("Hasil Konversi adalah : ",reamurkeKelvin(jumlahSuhu),"Kelvin")
            print("Hasil Konversi adalah : ",reamurkeFarenheit(jumlahSuhu),"Farenheit")
        elif opsiPilihan== "3":
            print("Hasil Konversi adalah : ",kelvinkeCelcius(jumlahSuhu),"Celcius")
            print("Hasil Konversi adalah : ",kelvinkeReamur(jumlahSuhu),"Reamur")
            print("Hasil Konversi adalah : ",kelvinkeFarenheit(jumlahSuhu),"Farenheit")
        elif opsiPilihan=="4":
            print("Hasil Konversi adalah : ",farenheitkeCelsius(jumlahSuhu),"Celcius")
            print("Hasil Konversi adalah : ",farenheitkeReamur(jumlahSuhu),"Reamur")
            print("Hasil Konversi adalah : ",farenheitkeKelvin(jumlahSuhu),"Kelvin")