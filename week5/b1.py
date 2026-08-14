class Employee :
    def __init__(self, name, __salary, _department) :
        self.name = name
        self.__salary = __salary
        self._department = _department

    def get_salary(self) :
        return self.__salary

    def increase_salary(self, amount) :
        if (amount > 0) :
            self.__salary += amount

    def calculate_bonus(self) :
        return (self.__salary * 0.05)

    def show_info(self) :
        print(f"Nhan vien {self.name} co luong la {self.__salary} thuoc bo phan {self._department}")

class Developer(Employee) :
    def __init__(self, name, __salary, _department, programming_language, overtime_hours):
        super().__init__(name, __salary, _department)
        self.programming_language = programming_language
        self.overtime_hours = overtime_hours

    def calculate_bonus(self):
        return (self.get_salary() * 0.1 + self.overtime_hours * 100000)

class Manager(Employee) :
    def __init__(self, name, __salary, _department, number_of_employess):
        super().__init__(name, __salary, _department)
        self.number_of_employess = number_of_employess

    def calculate_bonus(self):
        return (self.get_salary() * 0.15 + self.number_of_employess * 200000)


ls = [
    Developer("Nguyễn Văn A", 15000000, "IT", "Python", 10),
    Developer("Trần Thị B", 18000000, "IT", "Java", 15),
    Manager("Lê Văn C", 30000000, "IT", 5),
    Manager("Phạm Thị D", 40000000, "Sales", 12)
]

sum = 0
countDev, countMana = 0, 0

for i in ls :
    i.show_info()
    sum += i.calculate_bonus()
    if (isinstance(i, Developer)) :
        countDev += 1
    else :
        countMana += 1

a = max(ls, key=lambda x : x.get_salary())
print(f"Nhan vien co luong cao nhat la {a}")

print(f"Tong tien thuong cua tat ca nhan vien la {sum}")

print(f"So Dev la {countDev}, so Manager la {countMana}")