from random import randint
print(randint(1,100))
# rastgele bir sayi olustur.
# kullanicidan 3 kere sayi alacak sekilde bir dongu kur.
# kullanicinin girdigi sayiya gore her seferinde bilgi ver.

a = 10
if a == 10:
    print("Sayi 10 dur")
else:
    print("Sayi 10 degil.")

if a < 10:
    print("sayi 10 dan kucuktur")
elif a == 10:
    print("Sayi 10 dur.")
elif a == 20:
    print("Sayi 20dir.")
else:
    print("Bu nasil sayi?")

if a != 10:
    print("Sayi 10 dan farkli.")