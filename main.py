def asal_mi(sayi):
    """Girilen sayının asal olup olmadığını kontrol eden fonksiyon."""
    
    # 1'den büyük sayılar asal olabilir. Eğer sayı 1 veya daha küçükse, asal değildir.
    if sayi < 2:
        return False
    
    # 2, tek asal sayıdır. Eğer sayı 2 ise, asaldır.
    if sayi == 2:
        return True
    
    # Sayı 2'den büyük ve çiftse, asal değildir.
    if sayi % 2 == 0:
        return False
    
    # Sayının 2'den büyük bir asal olup olmadığını kontrol etmek için,
    # sayıyı 3'ten başlayarak kareköküne kadar olan tek sayılarla bölmeye çalışıyoruz.
    for i in range(3, int(sayi**0.5) + 1, 2):
        if sayi % i == 0:
            return False
    
    return True

# Kullanıcıdan bir sayı girmesini isteriz.
sayi = int(input("Bir sayı girin: "))

# Asal olup olmadığını kontrol ederiz.
if asal_mi(sayi):
    print(f"{sayi} bir asal sayıdır.")
else:
    print(f"{sayi} bir asal sayı değildir.")
