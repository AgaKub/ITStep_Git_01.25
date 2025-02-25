class User:
    def __init__(self, first_name, last_name, email,):
        self. first_name = first_nam
        self.last_name = last_name


        if self.is_valid_email(email):
            self.email= email
        else:
            print("Nieprawidłowy email")

    @staticmethod
    def is_valid_email(email):
       return "@" in email

class Admin(User):
    def __init__(self, first_name, last_name, email, password):
        super.__init__(first_name, last_name, email)
        self.password = password

if __name__ == "__main__":
    user1 = User("Aga", "Kubczak", "kubczakagnieszka@gmail.com")
    user2 = Admin("Chris", "Johnson", "cj@avalineqgmail.com")
    print(user1,f"")


