


def my_decorator(func):
    def wrapper(*args, **kwargs):
        return "DECORATED --> "+ func(*args, **kwargs) + "<-- DECORATED"
    return wrapper


def hello_name(name):
    return f"Hello {name}!"


def hello_2_names(first_name, second_name):
    return f"Hello {first_name} and {second_name}!"


hello_name("Krzysiek")


print(my_decorator(hello_name)("Krzysiek"))

print(hello_2_names("Krzysiek", "Olga"))
print(my_decorator(hello_2_names)("Krzysiek", "Olga"))



@my_decorator
def my_function(arg1, arg2):
    pass