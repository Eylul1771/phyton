def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    return a / b

print("İşlem seçiniz: \n1.Toplama\n2.Çıkarma\n3.Çarpma\n4.Bölme")
secim = input("Seçiminiz (1/2/3/4): ")

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

if secim == '1':
    print("Sonuç: ", toplama(sayi1, sayi2))
elif secim == '2':
    print("Sonuç: ", cikarma(sayi1, sayi2))
elif secim == '3':
    print("Sonuç: ", carpma(sayi1, sayi2))
elif secim == '4':
    print("Sonuç: ", bolme(sayi1, sayi2))
else:
    print("Geçersiz seçim!")
