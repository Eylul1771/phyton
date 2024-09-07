import random 
seçenekler =["taş","kağıt","makas"]
bilgisayar=random.choice(seçenekler)
kullanıcı=input("Taş, kağıt veya makas").lower()
print(f"Senin seçimin: {kullanıcı}")
print(f"Bilgisayarın seçimi: {bilgisayar}")
if kullanıcı ==bilgisayar :
    print("berabere")
    elif (kullanıcı == "taş" and bilgisayar == "makas") or \
     (kullanıcı == "kağıt" and bilgisayar == "taş") or \
     (kullanıcı == "makas" and bilgisayar == "kağıt"):
    print(f"Sen kazandın! {kullanıcı} {bilgisayar}'yı yener.")
else:
    print(f"Bilgisayar kazandı! {bilgisayar} {kullanıcı}'yı yener.")
