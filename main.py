import random
Karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Lütfen Parolanızın Uzunluğunu Seçin: "))
psswrd = ""
for i in range(uzunluk):
    selected = random.choice(Karakterler)
    psswrd += selected
print(psswrd)
