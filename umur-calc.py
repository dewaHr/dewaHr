import datetime
tanggal=datetime.date.today()
tahunini=tanggal.year
bulanini=tanggal.month
print("Tanggal Hari ini:",tanggal)
d,m,y=input("Masukan Tanggal Lahir Anda(ddmmyyyy):").split()
y=int(y)
print("Umur Anda:",tahunini-y,"Tahun")
x=365
print("atau",y*x,"hari")
