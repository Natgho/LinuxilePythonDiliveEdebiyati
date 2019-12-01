from pprint import pprint
ogrenciler = {}
ogrenciler['1'] = {
    "isim": "Sezer",
    "soyisim": "Bozkir"
}
for ogr_no in range(3):
    if ogr_no not in ogrenciler.keys():
        isim = input(f"{ogr_no+1}. ogrencinin ismi?")
        soyisim = input(f"{ogr_no+1}. ogrencinin soyisim?")
        ogrenciler[ogr_no+1] = {
            "isim": isim,
            "soyisim": soyisim
        }
    else:
        print("Bu ogrenci zaten var abi!")
pprint(ogrenciler)

