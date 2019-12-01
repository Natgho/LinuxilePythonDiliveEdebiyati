# vize = %30 vize2 = % 30 final= %40
print("*"*30)
vize_1 = float(input('İlk vize notunuzu giriniz.'))
vize_2 = float(input('İkinci vize notunuzu giriniz.'))
"""print(type(vize_1), vize_1)
print(vize_1 + vize_2)
print("*"*30)"""
final = float(input('final notunuzu giriniz.'))
a=vize_1 + vize_2
a=a*30/100
b=final*40/100
c=a+b
print(c)

print("Sonuc:", vize_1*0.3 + vize_2*0.3 + final *0.4)

