from abc import ABC, abstractmethod


class BooksModel:
    def __init__(self):
        self.list_books = []


    def add_book(self, book):
        self.list_books.append(book)

    def get_books(self):
        return self.list_books


class BooksView:
    def __init__(self, model):
        self.model = model

    def render(self, template):
        books = self.model.get_books()
        return template.render(books)



class BooksTemplate(ABC):
    @abstractmethod
    def render(self, books):
        pass


class BooksTemplateTable(BooksTemplate):
    def render(self, books):
        result = "\n&&&&&&&&&&\n"
        result += "\n".join(books)
        result += "\n&&&&&&&&&&\n"
        return result


class BooksTemplateSimple(BooksTemplate):
    def render(self, books):
        result = "".join(books)
        return result


def show_menu():
    print("*"*20)
    print("1 - Dodaj ksiązkę")
    print("2 - Pokaj Ksiązki w formie tabeli")
    print("3 - Pokaż ksiązki w stylu prostym")
    print("4 - Wyjdź")
    result = int(input("wybierz co chcesz zrobić:\n"))
    print("*"*20)
    return result


obj_model = BooksModel()
obj_view = BooksView(obj_model)
obj_table = BooksTemplateTable()
obj_simple = BooksTemplateSimple()

while True:
    result = show_menu()
    match result:
        case 1:
            new_book = input("Wprowadź nową książkę:")
            obj_model.add_book(new_book)
        case 2:
            print(obj_view.render(obj_table))
        case 3:
            print(obj_view.render(obj_simple))
        case 4:
            print("Do widzenia!")
            break
        case _:
            print("n\Zy wybór. Sprawdź ponownie!\n")


