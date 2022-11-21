import random
dadu=[1,2,3,4,5,6]
angka=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
print("Random Pick Generator")
print("1. Dadu")
print("2. Angka (1-40)")
#print("3.Berhenti")
while True:
    mode = input("Pilih Mode :")
    if mode in("1","2"):
        if mode == "1":
            print(random.choice(dadu))
        else : print(random.choice(angka))
