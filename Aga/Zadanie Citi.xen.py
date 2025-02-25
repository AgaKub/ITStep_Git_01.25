class Citizen:
    total_number_of_citizens = 0
    nationality = None

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        Citizen. total_number_of_citizens += 1

    def fullname(self):
        return f"{self.first_name} {self.last_name}"


    @classmethod
    def set_nationality(cls, nationality):
        cls.nationality = nationality


if __name__ == "__main__":
    kubczak = Citizen("Agnieszka", "Kubczak")
    print(kubczak.fullname())

    Citizen.set_nationality("Polskie")

    print("narodowość obywatela:")
    johnson = Citizen( "Chris", "Johnson")
    print(johnson.fullname())
