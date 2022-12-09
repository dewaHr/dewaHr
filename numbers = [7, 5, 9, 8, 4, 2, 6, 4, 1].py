kalimat="Saya cinta RO"
for i in (kalimat):
    print(i)

 
for i in range(10):
    print("aku")


count = 0
while (count < 5):
 print('The count is:', count)
 count = count + 1
print('Good bye!')



for letter in "Programming":
    if letter == "g":
        break
    print("Huruf sekarang:", letter)
print("Good bye")


for i in range(3,1500):
    if i%3==0 and i%5 == 0:
        print(i)
#continue
nama=[1,2,3,4,5,6,7,8,10]
for i in nama:
    if i == 1 and 5:
        continue
#     else:print(i)


total=0
a=1
while (a<2501):
    if a%5==0 and a%8==0:
        total=total+1
    a= a+1
print(total)
