class Car:
    acceleration = 10
    def __init__(self, color, reg_number, model):
        self.color = color
        self.reg_number = reg_number
        self.model = model
        self.in_motion = False
        self.speed = 0

    def drive(self):
        self.in_motion = True


    def accelerate(self):
        self.drive()
        self.speed += self.acceleration


    def stop(self):
        self.in_motion = False
        self.speed = 0


if __name__ == "__main__":
    audi = Car("Red", "ADB 12345", "A4")
    print(audi.reg_number)
    audi.accelerate()
    print(audi.speed)
    print(audi.in_motion)
