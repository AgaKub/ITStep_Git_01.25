def say_hello(name):
    print(f"Siemka {name}!")

def say_goodbye(name):
    print(f"Trzymaj się, {name}!")

def greet_kryska(greeting):
    return greeting("Kryska")

greet_kryska(say_hello)
greet_kryska(say_goodbye)

def outer_function(text):
    print("outer function")

    def inner_function(txt):
        print("inner function")
        return txt.upper()
    return inner_function((text))

print(outer_function("ala ma kota"))



def greeting(time):

    def morning_greeting(name):
        return f"Good mornng, {name}!"
    def afternoon_greeting(name):
        return f"Good afternoon, {name}!"
    def late_night_greeting(name):
        return f"Good night, {name}!"

    if time == "morning":
        return morning_greeting
    if time == "afternoon":
        return afternoon_greeting
    return late_night_greeting
greeting_time = greeting("afternoon")

print(greeting_time("John"))
