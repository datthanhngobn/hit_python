from abc import ABC, abstractmethod

class HomeAppliance(ABC) :
    @abstractmethod
    def turn_on(self) :
        pass

    @abstractmethod
    def operate(self) :
        pass

class KitchenAppliace(HomeAppliance) :
    def turn_on(self):
        print("Da cam dien va bat cong tac")

class RiceCooker(KitchenAppliace) :
    def operate(self):
        print("Dang nau chin gao")

class Microwave(KitchenAppliace) :
    def operate(self):
        print("Dang ham nong thuc an")

try :
    create = KitchenAppliace()
except TypeError :
    print(f"Khong the khoi tao KitchenAppliance vi chua khoi tao phuong thuc operate()")

ls = [Microwave(), RiceCooker()]

for i in ls:
    i.turn_on()
    i.operate()
