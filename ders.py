class Öğrenci:
        def __init__(self, isim):
        self.isim = isim
        self.notlar = {}
    def not_ekle(self, ders, not_):
        self.notlar[ders] = not_
def not_görüntüle(self):
        # Öğrencinin tüm ders notlarını ekrana basar
        print(f"{self.isim} Öğrenci Notları:")
        for ders, not_ in self.notlar.items():
            print(f"{ders}: {not_}")
öğrenci1 = Öğrenci("Ahmet")  # "Ahmet" isminde bir öğrenci nesnesi oluşturur
öğrenci1.not_ekle("Matematik", 85)  # Matematik dersine 85 notu ekler
öğrenci1.not_ekle("Fizik", 90)  # Fizik dersine 90 notu ekler
öğrenci1.not_görüntüle()  # Öğrencinin notlarını ekrana basar