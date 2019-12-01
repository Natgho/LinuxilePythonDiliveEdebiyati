ogrenci = []
for sira in range(3):
    vize_1 = input("{ogrenci}. ogrencinin 1. vize notunu girin:".format(ogrenci=sira+1))
    vize_2 = input(f"{sira+1}. ogrencinin 2. vize notunu girin:")
    final = input(str(sira+1) + ". ogrencinin final notunu girin:")
    ogrenci.append([vize_1, vize_2, final])
print(ogrenci)