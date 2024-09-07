def gelir_ekle(gelirler, miktar):
    gelirler.append(miktar)
    print(f"{miktar} TL gelir eklendi.")

def gider_ekle(giderler, miktar):
    giderler.append(miktar)
    print(f"{miktar} TL gider eklendi.")

def bakiye_hesapla(gelirler, giderler):
    toplam_gelir = sum(gelirler)
    toplam_gider = sum(giderler)
    bakiye = toplam_gelir - toplam_gider
    return bakiye

def finans_takip():
    gelirler = []
    giderler = []
    
    while True:
        print("1. Gelir Ekle")
        print("2. Gider Ekle")
        print("3. Bakiye Hesapla")
        print("4. Çıkış")
        
        secim = input("Seçiminizi yapın: ")
        
        if secim == '1':
            miktar = float(input("Gelir miktarını girin: "))
            gelir_ekle(gelirler, miktar)
        elif secim == '2':
            miktar = float(input("Gider miktarını girin: "))
            gider_ekle(giderler, miktar)
        elif secim == '3':
            bakiye = bakiye_hesapla(gelirler, giderler)
            print(f"Mevcut bakiye: {bakiye} TL")
        elif secim == '4':
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

finans_takip()
