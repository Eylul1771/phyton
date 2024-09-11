import random

def sayi_tahmin_oyunu():
    # Rastgele bir sayı seç (1 ile 100 arasında)
    rastgele_sayi = random.randint(1, 100)
    tahmin_hakki = 7  # Kullanıcının 7 tahmin hakkı var
    print("1 ile 100 arasında bir sayı tuttum. Bakalım bulabilecek misin?")
    
    while tahmin_hakki > 0:
        try:
            # Kullanıcıdan tahmin al
            tahmin = int(input(f"Bir tahmin yap ({tahmin_hakki} tahmin hakkın kaldı): "))
            
            # Tahmin sayısını kontrol et
            if tahmin < 1 or tahmin > 100:
                print("Lütfen 1 ile 100 arasında bir sayı gir!")
                continue
            
            # Tahmin doğru mu?
            if tahmin == rastgele_sayi:
                print("Tebrikler! Doğru tahmin ettin!")
                break
            # Tahmin küçük mü?
            elif tahmin < rastgele_sayi:
                print("Daha büyük bir sayı tahmin et!")
            # Tahmin büyük mü?
            else:
                print("Daha küçük bir sayı tahmin et!")
            
            tahmin_hakki -= 1  # Tahmin hakkını bir azalt
        
        except ValueError:
            print("Lütfen geçerli bir sayı gir!")

    # Eğer tahmin hakkı biterse
    if tahmin_hakki == 0:
        print(f"Üzgünüm, tahmin hakkın bitti. Doğru sayı {rastgele_sayi} idi.")

# Oyunu başlat
sayi_tahmin_oyunu()
