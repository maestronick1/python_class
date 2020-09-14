class CoffeeCup():
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0
    
    def fill(self):
        self.amount = self.capacity

    def empty(self):
        self.amount = 0

    def drink(self, amount):
        self.amount -= amount
        if (self.amount == 0):
            self.amount = 0
            print('Coffee cup is now empty')

adam_cup = CoffeeCup(8)
taylor_cup = CoffeeCup(16)
pete_cup = CoffeeCup(12)
rome_cup = CoffeeCup(2)

adam_cup.fill()
rome_cup.empty()

adam_cup.drink(8)
print(adam_cup.amount)


