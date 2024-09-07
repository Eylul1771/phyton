kitaplar=[]
def kitap_ekle(kitap_adı ,yazar):
    kitap ={"kitap adı " :kitap_adı ,"yazar":yazar}
kitaplar.append(kitap)
  print(f"'{kitap_adı}' kitabı eklendi.")
  def kitapları_goster():
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
