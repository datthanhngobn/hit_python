class Character :
    def __init__(self, name, __hp, _level):
        self.name = name
        self.__hp = __hp
        self._level = _level

    def get_hp(self) :
        return self.__hp

    def take_damage(self, damage) :
        if (self.__hp >= 0) :
            self.__hp -= damage

    def heal(self, amount) :
        self.__hp += amount

    def attack(self) :
        return 

    def show_info(self) :
        return f"Nhan vat {self.name} co {self.__hp} hp va co level {self._level}"

class Warrior(Character) :
    def __init__(self, name, __hp, _level, strength):
        super().__init__(name, __hp, _level)
        self.strength = strength

    def attack(self):
        return self._level * 5 + self.strength

class Mage(Character) :
    def __init__(self, name, __hp, _level, __mana, magic_power):
        super().__init__(name, __hp, _level)
        self.__mana = __mana
        self.magic_power = magic_power

    def attack(self):
        if (self.__mana > 10) :
            self.__mana -= 10
            return self._level * 3 + self.magic_power
        else :
            return 0

ls = [
    Warrior("Yasuo", 1500, 10, 50),
    Warrior("Jax", 1400, 12, 55),
    Mage("Mixi", 800, 15, 200, 85),
    Mage("Sylas", 900, 14, 250, 90)
]

for x in range(4) :
    for y in range(4) :
        if (x == y) :
            continue

        damage = ls[x].attack()
        ls[y].take_damage(damage)

countWarr, countMage = 0, 0

for i in ls :
    print(i.show_info())
    if (isinstance(i, Warrior)) :
        countWarr += 1
    else :
        countMage += 1

a = max(ls, key=lambda x : x.get_hp())

print(f"Nhan vat co nhieu mau nhat la {a.show_info()}")

print(f"Co {countWarr} Warrior va co {countMage} Mage")