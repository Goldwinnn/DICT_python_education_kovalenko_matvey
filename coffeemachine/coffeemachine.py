class CoffeeMachine:
    running = False

    def init(self, water, milk, coffee_beans, cups, money):
        """Basic resources of the coffee machine"""
        self.water = water
        self.milk = milk
        self.coffee = coffee_beans
        self.cups = cups
        self.money = money

        if not CoffeeMachine.running:
            self.main_menu()

    def main_menu(self):
        """Choose what you want to do"""
        self.running = True
        self.action = input("\n(buy, fill, take, remaining, exit)\nSelect: ")
        print()
        action_choices = {"buy": self.buy_action, "fill": self.fill_action, "take": self.take_action,
                          "exit": exit, "remaining": self.remaining_action}
        if self.action in action_choices:
            action_choices[self.action]()
        else:
            exit()

    def menu_return(self):
        """Returns to the menu(choosing) after an action"""
        print()
        self.main_menu()

    def check_action(self):
        """Checks the availability of ingredients"""
        self.not_available = ""
        if self.water - self.reduced[0] < 0:
            self.not_available = "water"
        elif self.milk - self.reduced[1] < 0:
            self.not_available = "milk"
        elif self.coffee - self.reduced[2] < 0:
            self.not_available = "beans"
        elif self.cups - self.reduced[3] < 0:
            self.not_available = "cups"

        if self.not_available != "":
            print(f"Sorry, not enough {self.not_available}! 😥")
            return False
        else:
            print("I have enough resources to make you a coffee! 👍")
            return True

    def action_str(self):
        """Starts an action"""
        self.water -= self.reduced[0]
        self.milk -= self.reduced[1]
        self.coffee -= self.reduced[2]
        self.cups -= self.reduced[3]
        self.money += self.reduced[4]

    def buy_action(self):
        """Buy a specific coffee and check the availability of ingredients"""
        self.choice = input("What do you want to buy? \n1 - espresso \n2 - latte "
                            "\n3 - cappuccino \nexit - to main menu:\n")
        if self.choice == '1':
            self.reduced = [250, 0, 16, 1, 4]
            if self.check_action():
                self.action_str()

        elif self.choice == '2':
            self.reduced = [350, 75, 20, 1, 7]
            if self.check_action():
                self.action_str()

        elif self.choice == "3":
            self.reduced = [200, 100, 12, 1, 6]
            if self.check_action():
                self.action_str()

        elif self.choice == "back":
            self.menu_return()

        self.menu_return()

    def fill_action(self):
        """Filling the coffee machine with different ingredients"""
        self.water += int(input("how many ml of water 🧺 do you want to add:\n"))
        self.milk += int(input("how many ml of milk 🥛 do you want to add::\n"))
        self.coffee += int(input("how many grams of coffee beans ☕️ do you want to add:\n"))
        self.cups += int(input("how many disposable cups 🥤 of coffee do you want to add:\n"))
        self.menu_return()

    def take_action(self):
        """Collect money from the coffee machine"""
        print(f"I gave you ${self.money}")
        self.money -= self.money
        self.menu_return()

    def remaining_action(self):
        """Displays the remaining ingredients in the coffee machine"""
        print(f"The coffee machine has:")
        print(f"{self.water} of water 🧺")
        print(f"{self.milk} of milk 🥛")
        print(f"{self.coffee} of coffee beans ☕️")
        print(f"{self.cups} of disposable cups 🥤")
        print(f"${self.money} of money 💵")
        self.menu_return()


CoffeeMachine(400, 540, 120, 9, 550)
