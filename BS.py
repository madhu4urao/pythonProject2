#Banking system using oop
#parent class: User
#Holds details about user
#Has a function to show_user_details
#Child class:Bank
#stores details about the account balance
#stores details about the amount
#allows for deposits, withdraw and view balance

class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show_details(self):
        print("personal details")
        print(" ")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


# Child Bank
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0
    def deposit(self, amount):
        self.amount= amount
        self.balance = self.balance+amount
        print("account balance has been updated: $", self.balance)

    def withdraw(self, amount):
        self.amount= amount
        if self.amount > self.balance:
            print("insufficient funds: Balance available: $", self.balance)
        else:
            self.balance= self.balance - self.amount
            print("account balance has been updated: $", self.balance)

    def view_balance(self):
        self.show_details()
        print("account balance has been updated: $", self.balance)

amit = Bank('amit', 25, 'Male')
amit.deposit(100)
amit.withdraw(50)
amit.view_balance()