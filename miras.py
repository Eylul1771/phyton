# Ana sınıf olan Insan sınıfı
class Insan:
    def __init__(self, isim, yas):
        self.isim = isim  # İnsan nesnesinin ismini saklar
        self.yas = yas  # İnsan nesnesinin yaşını saklar
    
    def tanit(self):
        print(f"Benim adım {self.isim}, {self.yas} yaşındayım.")  # Kişiyi tanıtır

# Calisan sınıfı, Insan sınıfından miras alır
class Calisan(Insan):
    def __init__(self, isim, yas, meslek, maas):
        super().__init__(isim, yas)  # Ana sınıfın (Insan) __init__ fonksiyonunu çağırır
        self.meslek = meslek  # Çalışanın mesleğini saklar
        self.maas = maas  # Çalışanın maaşını saklar
    
    def calis(self):
        print(f"{self.isim}, {self.meslek} olarak çalışıyor ve maaşı {self.maas}.")  # Çalışanın iş bilgilerini gösterir

# Ogrenci sınıfı, Insan sınıfından miras alır
class Ogrenci(Insan):
    def __init__(self, isim, yas, sinif, not_ortalamasi):
        super().__init__(isim, yas)  # Ana sınıfın (Insan) __init__ fonksiyonunu çağırır
        self.sinif = sinif  # Öğrencinin sınıfını saklar
        self.not_ortalamasi = not_ortalamasi  # Öğrencinin not ortalamasını saklar
    
    def ders_calis(self):
        print(f"{self.isim}, {self.sinif}. sınıfta ve not ortalaması {self.not_ortalamasi}.")  # Öğrencinin ders çalışmasını ve not ortalamasını gösterir

