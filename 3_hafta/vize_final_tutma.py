ogrenci_notlari = []
for vize_no in range(2):
    tmp_not = []
    for ogr_no in range(3):
        ogr_vize = input(f"{ogr_no+1}. ogrencinin {vize_no+1} vize notunu girin")
        tmp_not.append(ogr_vize)
    ogrenci_notlari.append(tmp_not)
print(ogrenci_notlari)