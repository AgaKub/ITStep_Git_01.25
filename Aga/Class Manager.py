import datetime


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


    @staticmethod
    def is_workday(day):
        return day.weekday() not in (5,6)

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first_name, last_name, pay, programming_language):
        super().__init__(first_name, last_name, pay)
        self.programming_language = programming_language

class Manager(Employee):

    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(self, first_name, last_name, pay)
        if employees:
             self.employees = employees
        else:
            self.employees = set()


    def add_employee(self, employee):
        self.employee.add(employee)


    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print(f"{employee.fullname()}, nie jest podwłądnym"
                  f"{self.fullname()}")


    def print_employees(self):
        print(f"Pracownicy {self.first_name()}:")
        for employee in self.employees:
            print(f"\t- {employee.fullname()}")




if __name__ == "__main__":

    wisniewska = Employee("Anna", "Wisniewska", 6000)
    kowalski = Employee( "Jan", "Kowalski", 10000, "Python")
    michalska = Employee( "Magdalena", "Michalska", 20000, {wisniewska})
    michalska.print_employees()

    michalska.remove_employee(kowalski)
    wasiluk = Developer("Maciej"), "Wasiluk", 12000, "Java"
    michalska.add_employee(wasiluk)
    michalska.print_employees()

    michalska.apply_raise()
    print(michalska.pay)
