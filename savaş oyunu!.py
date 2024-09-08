class Character:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, opponent):
        damage = self.attack_power - opponent.defense
        if damage < 0:
            damage = 0
        opponent.health -= damage
        print(f"{self.name}, {opponent.name}'a {damage} hasar verdi.")

    def is_alive(self):
        return self.health > 0

# İki karakter oluştur
karakter1 = Character(name="Savaşçı", health=100, attack_power=20, defense=5)
karakter2 = Character(name="Büyücü", health=80, attack_power=25, defense=3)

# Oyun döngüsü
while karakter1.is_alive() and karakter2.is_alive():
    karakter1.attack(karakter2)
    if karakter2.is_alive():
        karakter2.attack(karakter1)

# Kazananı yazdır
if karakter1.is_alive():
    print(f"{karakter1.name} kazandı!")
else:
    print(f"{karakter2.name} kazandı!")
