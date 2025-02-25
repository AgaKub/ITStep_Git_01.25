class Book:

    total_number_of_books = 0



    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_number_of_books += 1
        self.id = Book.total_number_of_books


if __name__ == "__main__":
    nad_niemnem = Book("Nad Niemnem:", "E.Orzeszkowa")
    pan_tadeusz = Book("Pan Tadeusz", "A. Mickiewicz")


    print("Ilosc ksiązek:", Book.total_number_of_books)

    print("ID Nad Niemnem:", nad_niemnem.id)
    print("ID Pan Tadeusz:", pan_tadeusz.id)
