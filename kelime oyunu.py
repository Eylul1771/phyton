import random

# 1. Gizli kelime havuzu oluşturuyoruz
kelimeler = ['elma', 'armut', 'muz', 'çilek', 'kiraz']

# 2. Rastgele bir kelime seçiyoruz
gizli_kelime = random.choice(kelimeler)
tahmin_edilen = ['_' for _ in gizli_kelime]  # Kelimenin uzunluğu kadar _ koyuyoruz

# 3. Oyuncuya verilen haklar
haklar = 6  # Oyuncunun yanlış tahmin yapabileceği hak sayısı

# 4. Oyunun döngüsü
while haklar > 0 and '_' in tahmin_edilen:
    print(f"\nKelimede: {' '.join(tahmin_edilen)}")
    print(f"Kalan Hakkın: {haklar}")
    
    tahmin = input("Bir harf tahmin et: ").lower()  # Harf tahminini al
    
    if tahmin in gizli_kelime:
        # Doğru tahmin, kelimedeki harflerin yerini açıyoruz
        for i, harf in enumerate(gizli_kelime):
            if harf == tahmin:
                tahmin_edilen[i] = tahmin
        print(f"Doğru! '{tahmin}' harfi kelimede var.")
    else:
        # Yanlış tahmin, hak bir azalıyor
        haklar -= 1
        print(f"Yanlış! '{tahmin}' harfi kelimede yok.")
    
# 5. Oyunun Sonu
if '_' not in tahmin_edilen:
    print(f"Tebrikler! Kelimeyi doğru tahmin ettin: {gizli_kelime}")
else:
    print(f"Üzgünüm, hakkın bitti! Kelime: {gizli_kelime}")

