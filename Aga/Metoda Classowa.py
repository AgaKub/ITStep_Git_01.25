class Employee:
    raise_amount = 1.04

    def __init__(self, first_nam, last_name, pay):
        self. first_name = first_nam
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_nam}.{last_name}@company.com"


    def fullname(self):
        return f"{self.first_name} {self.last_name}"


    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

    @classmethod
    def set_raise_amount(cls, new_raise_amount):
        cls.raise_amount = new_raise_amount


if __name__ == "__main__":

    wisniewska = Employee("Anna", "Wiśniewska", 6000)
    print(wisniewska.fullname())
    print(wisniewska.email)

    kowalski = Employee("Jan", "kowalski", 4000)


    wisniewska.raise_amount = 1.10

    Employee.set_raise_amount(1.05)

    print("Wysokość podwyżek pracownków", Employee.raise_amount)

    print("Wisniewska:", wisniewska.raise_amount)
    print("Kowalski:", kowalski.raise_amount)

    wisniewska.apply_raise()
    kowalski.apply_raise()

    print(wisniewska.pay)
    print(kowalski.pay)


    print("*"*25)

    print("Wysokość podwyżek pracowników", Employee.raise_amount)
    print("Wisniewska:", wisniewska.raise_amount)
    print("Kowalski:", kowalski.raise_amount)
