

def not_ekle(notlar, yeni_not):
    notlar.append(yeni_not)
    print(f"'{yeni_not}' notu eklendi.")

def notlari_goruntule(notlar):
    if notlar:
        print("Notlarınız:")
        for i, not_ in enumerate(notlar, 1):
            print(f"{i}. {not_}")
    else:
        print("Henüz not eklenmedi.")

def not_sil(notlar, sira):
    if 0 < sira <= len(notlar):
        silinen_not = notlar.pop(sira - 1)
        print(f"'{silinen_not}' notu silindi.")
    else:
        print("Geçersiz not numarası.")

def not_defteri():
    notlar = []

    while True:
        print("\nBir işlem seçin:")
        print("1. Not ekle")
        print("2. Notları görüntüle")
        print("3. Not sil")
        print("4. Çıkış")

        secim = input("Seçiminiz (1/2/3/4): ")

        if secim == '1':
            yeni_not = input("Eklemek istediğiniz notu girin: ")
            not_ekle(notlar, yeni_not)

        elif secim == '2':
            notlari_goruntule(notlar)

        elif secim == '3':
            notlari_goruntule(notlar)
            sira = int(input("Silmek istediğiniz notun numarasını girin: "))
            not_sil(notlar, sira)

        elif secim == '4':
            print("Not Defterinden çıkılıyor.")
            break

        else:
            print("Geçersiz seçim. Lütfen 1, 2, 3 veya 4 seçin.")

not_defteri()

