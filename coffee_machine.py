class CoffeeMachine:
    def __init__(self):
        self.materials = ["water", "milk", "coffee beans", "disposable cups", "money"]
        self.balances = [400, 540, 120, 9, 550]
        self.espresso = [250, 0, 16, 1, 4]
        self.latte = [350, 75, 20, 1, 7]
        self.cappuccino = [200, 100, 12, 1, 6]

    def status(self):
        print("The coffee machine has:")
        for b in range(4):
            print(self.balances[b], "of", self.materials[b])
        print("$" + str(self.balances[4]), "of money")

    def calculate(self, cname):
        for c in range(4):
            if self.balances[c] < cname[c]:
                print("Sorry, not enough", self.materials[c] + "!")
                return
        print("I have enough resources, making you a coffee!")
        for d in range(4):
            self.balances[d] -= cname[d]
        self.balances[4] += cname[4]

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee = input()
        if coffee == "1":
            self.calculate(self.espresso)
        elif coffee == "2":
            self.calculate(self.latte)
        elif coffee == "3":
            self.calculate(self.cappuccino)
        else:
            return

    def fill(self):
        for f in range(4):
            print("Write how many ml of", self.materials[f], "do you want to add:")
            self.balances[f] += int(input())

    def take(self):
        print("I gave you $" + str(self.balances[4]), self.materials[4])
        self.balances[4] = 0

    def handle_user_input(self, action):
        print()
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.status()


coffee_machine = CoffeeMachine()

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    user_action = input()
    if user_action == "exit":
        break
    coffee_machine.handle_user_input(user_action)
    print()
