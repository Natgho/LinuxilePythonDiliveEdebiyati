def donem_sonu_ortalama_notu(vize_1, vize_2, final):
    """Bazi islemler"""
    sonuc = (vize_1 + vize_2) * 0.3 + final * 0.4
    return sonuc


vize_1_notlari = [80, 40, 100]
vize_2_notlari = [10, 80, 20]
final_notlari = [50, 90, 60]

print(donem_sonu_ortalama_notu(vize_1_notlari[0],
                               vize_2_notlari[0],
                               final_notlari[0]))
# for - while
"""
for ogr_num in range(3):
    print(f"{ogr_num+1}. ogrencinin:",
          vize_1_notlari[ogr_num],
          vize_2_notlari[ogr_num],
          final_notlari[ogr_num]
          )
"""