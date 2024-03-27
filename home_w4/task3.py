class Bankomat:
    def __init__(self):
        self.balance = 0
        self.operations_count = 0
        self.tax_threshold = 5000000
        self.tax_rate = 0.1

    def deposit(self, amount):
        if self.balance >= self.tax_threshold:
            self.balance -= self.balance * self.tax_rate
        self.balance += amount
        self.operations_count += 1
        if self.operations_count % 3 == 0:
            self.balance -= self.balance * 0.03
        print("Баланс: ", self.balance)

    def withdraw(self, amount):
        if self.balance >= self.tax_threshold:
            self.balance -= self.balance * self.tax_rate
        if amount > self.balance:
            print("Недостаточно средств на счете")
            return
        if amount > 600:
            amount = 600
        elif amount < 30:
            amount = 30
        withdrawal_fee = amount * 0.015
        self.balance -= amount + withdrawal_fee
        self.operations_count += 1
        if self.operations_count % 3 == 0:
            self.balance -= self.balance * 0.03
        print("Баланс: ", self.balance)

    def leave(self):
        print("Баланс: ", self.balance)
        print("До свидания!")


bankomat = Bankomat()

while True:
    action = input("Выберите действие: (пополнить, снять, уйти): ")
    if action == "пополнить":
        amount = 50
        bankomat.deposit(amount)
    elif action == "снять":
        amount = 50
        bankomat.withdraw(amount)
    elif action == "уйти":
        bankomat.leave()
        break
    else:
        print("Некорректное действие. Повторите ввод.")
