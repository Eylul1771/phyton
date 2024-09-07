kitaplar = []

def kitap_ekle(kitap_adı, yazar):
    kitap = {"Kitap Adı": kitap_adı, "Yazar": yazar}
    kitaplar.append(kitap)
    print(f"'{kitap_adı}' kitabı eklendi.")

def kitapları_göster():
    if kitaplar:
        print("Kütüphanedeki Kitaplar:")
        for i, kitap in enumerate(kitaplar, 1):
            print(f"{i}. {kitap['Kitap Adı']} - {kitap['Yazar']}")
    else:
        print("Kütüphanede hiç kitap yok.")

def kitap_sil(kitap_adı):
    for kitap in kitaplar:
        if kitap["Kitap Adı"] == kitap_adı:
            kitaplar.remove(kitap)
            print(f"'{kitap_adı}' kitabı silindi.")
            return
    print(f"'{kitap_adı}' kitabı bulunamadı.")

def kütüphane_yönetimi():
    while True:
        print("\nKütüphane Yönetim Sistemi")
        print("1. Kitap Ekle")
        print("2. Kitapları Göster")
        print("3. Kitap Sil")
        print("4. Çıkış")
        
        seçim = input("Seçiminizi yapın: ")
        
        if seçim == '1':
            kitap_adı = input("Kitap adı girin: ")
            yazar = input("Yaz
