from random import randint

bulunacak_sayi = randint(1,100)
print(f"###Yazman gereken sayi: {bulunacak_sayi}###")

print("*"*10 , "Sayi bulma programına hoşgeldiniz.", "*"*10)
denenen_sayi = None
for deneme_miktari in range(3):
    denenen_sayi = int(input("Lütfen tahmininizi giriniz?"))
    if denenen_sayi == bulunacak_sayi:
        print("Bravo! buldunuz.")
        break
    elif denenen_sayi < bulunacak_sayi:
        print("Aradığın sayi daha buyuk.")
    else:
        print("Aradıgın sayi daha kucuk.")
if denenen_sayi != bulunacak_sayi:
    print("Kaybettin bro!")