class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_info(self, details=False):
        if details:
            print("Marka:", self.brand)
            print("Model:", self.model)
            print("Rok produkcji:", self.year)
        else:
            print(f"{self.brand} {self.model}")

    car1 = Car("Toyota", "Corolla", 2020)

    car1.show_info()  # działa jak wersja uproszczona
    car1.show_info(True)  # działa jak wersja szczegółowa
