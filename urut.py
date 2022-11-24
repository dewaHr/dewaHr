print("tentukan pilihan") 
 print("1. Ascending") 
 print("2. Descending") 
  
 masukanPil = int(input("Masukan Pilihan : ")) 
 if masukanPil == 1: 
     bilPer = int(input("Bilangan Pertama : ")) 
     bilDua = int(input("Bilangan Kedua : ")) 
     bilGa = int(input("Bilangan Ketiga : ")) 
     bilPat = int(input("Bilangan Empat : ")) 
     semuaSatu = [bilPer,bilDua,bilGa,bilPat] 
     semuaSatu.sort() 
     print(semuaSatu) 
 elif masukanPil == 2: 
     bilPer = int(input("Bilangan Pertama : ")) 
     bilDua = int(input("Bilangan Kedua : ")) 
     bilGa = int(input("Bilangan Ketiga : ")) 
     bilPat = int(input("Bilangan Empat : ")) 
     semuaSatu = [bilPer,bilDua,bilGa,bilPat] 
     semuaSatu.reverse() 
     print(semuaSatu)