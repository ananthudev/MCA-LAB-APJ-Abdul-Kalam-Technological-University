class bank:
    def __init__(self):
        self.accno = int(input("Enter your account number: "))
        self.acctype = input("Enter your account type: ")
        self.holdname = input("Enter your name: ")
        self.balance = int(input("Enter your balance: "))

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        self.balance += amount
        print("The account balance is:", self.balance)

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print("You withdraw Rs:", amount)
        else:
            print("Insufficient balance to withdraw")

    def display(self):
        print("Net available balance is:", self.balance)

a = bank()
a.deposit()
a.withdraw()
a.display()
12