from abc import ABC, abstractmethod

class Weapon(ABC) :
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo

    def reload(self, add_ammo = 0) :
        if (add_ammo == 0) :
            self.ammo = 30
        else :
            self.ammo += add_ammo

    @abstractmethod
    def shoot(self) :
        pass

class Vandal(Weapon) :
    def __init__(self, name, ammo):
        super().__init__(name, ammo)
    def shoot(self):
        return "Bum Bum"

class Operator(Weapon) :
    def __init__(self, name, ammo):
        super().__init__(name, ammo)

    def shoot(self):
        return "Bow Bow"

class JettSkill() :
    def __init__(self,name, ammo):
        self.name = name
        self.ammo = ammo

    def shoot(self) :
        return "Hasagi"

def perform_attack(entity, times) :
    for i in range(times) :
        print(f"{type(entity).__name__} {entity.shoot()} - Dan con {entity.ammo - 1}")
        entity.ammo -= 1

ls = [Vandal("Vandal", 30), Operator("Operator", 5), JettSkill("JettSkill", 5)]

for i in ls :
    perform_attack(i, 2)

ls[0].reload(10)
print(f"Vandal nap 10 vien -> Dan: {ls[0].ammo}")

ls[0].reload()
print(f"Vandal nap day -> Dan: {ls[0].ammo}")
