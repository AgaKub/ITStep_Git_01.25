
def pierwsza_funkcja():
    pass

class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Car:

    def __init__(self, color, reg_number, model):
        self.color = color
        self.reg_number = reg_number
        self.model = model

if __name__ == "__main__":
    jk = Employee("Jan", "Kowalski")
    audi = Car("Red", "ADB 12345", "A4")
    print(jk)
    print(audi)
    print(color)
    print(model)


