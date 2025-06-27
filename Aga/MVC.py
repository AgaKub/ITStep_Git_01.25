class Model:
    def __init__(self):
        self.list_tasks = []

    def add_task(self, task ):
        self.list_tasks.append(task)


    def get_list_tasks(self):
        return self.list_tasks

class View:
    @staticmethod
    def input_task():
        return input("wprowadz zadanie:\n")

    @staticmethod
    def show_list_tasks(list_tasks):
        for task in list_tasks:
            print("Twoja lista zadań:")
            print(f"\t{task}")

    @staticmethod
    def show_menu():
        print("*" * 20)
        print("1 - Dodaj zadanie.")
        print("2- Pokaz zadanie.")
        print("3 - Wyjdz.")
        result = input("wybierz co chcesz zrobić:\n")
        print("*" * 20)
        return result


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def action_input_task(self):
        task = self.view.input_task()
        self.model.add_task(task)

    def action_show_list_tasks(self):
        task = self.model.get_list_tasks()
        self.view.show_list_tasks(task)



obj_controller = Controller(Model(), View())

while True:
    result = obj_controller.view.show_menu()
    match result:
        case "1":
            obj_controller.action_input_task()
        case "2":
            obj_controller.action_show_list_tasks()
        case "3":
            print("Do zobaczenia")
            break
        case _:
            print("\nZly wybor. Sprobuj ponownie.\n")

