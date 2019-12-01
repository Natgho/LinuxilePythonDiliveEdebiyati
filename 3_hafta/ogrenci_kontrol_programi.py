ogrenciler = {
    "1": {"isim": "Sezer",
        "soyisim": "Bozkir",
        "d_tarihi": "1970"
    },
    "2": {
        "isim": "Fayz",
        "soyisim": "Bin Fayz",
        "d_tarihi": "1999"
    }
}
olmayan_ogrenci = {
        "isim": "John",
        "soyisim": "Doe",
        "d_tarihi": ""
    }
# print(ogrenciler['4'])
response = ""
print(response)
print(type(response))
istedigim_ogrenci = ogrenciler.get('4')
if istedigim_ogrenci:
    print("Bu ogrenci var.")
else:
    print("bu ogrenci yok")


