class Coffee_machine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
    def Message(self):
        print(f'The coffee machine has:\n'
              f'{self.water} ml of water\n'
              f'{self.milk} ml of milk\n'
              f'{self.beans} g of coffee beans\n'
              f'{self.cups} of disposable cups\n'
              f'${self.money} of money\n')


    def Making_coffee(self,chosen_coffee):
        self.chosen_coffee = chosen_coffee
        if self.chosen_coffee == '1':
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                print('I have enough resources, making you a coffee!\n')
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
            elif self.water < 250:
                print('Sorry, not enough water!\n')
            elif self.beans < 16:
                print('Sorry, not enough water!\n')
            elif self.cups < 1:
                print('Sorry, not enough water!\n')
        elif self.chosen_coffee == '2':
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
                print('I have enough resources, making you a coffee!\n')
            elif self.water < 350:
                print('Sorry, not enough water!\n')
            elif self.milk < 75:
                print('Sorry, not enough milk!\n')
            elif self.beans < 12:
                print('Sorry, not enough coffee beans!\n')
            elif self.cups < 1:
                print('Sorry, not enough disposable cups!\n')
        elif self.chosen_coffee == '3':
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                print('I have enough resources, making you a coffee!\n')
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
            elif self.water < 200:
                print('Sorry, not enough water!\n')
            elif self.milk < 100:
                print('Sorry, not enough milk!\n')
            elif self.beans < 12:
                print('Sorry, not enough coffee beans!\n')
            elif self.cups < 1:
                print('Sorry, not enough disposable cups!\n')

    def Filling(self):
        add_water = input('Write how many ml of water you want to add: \n')
        self.water += int(add_water)
        add_milk = input('Write how many ml of milk you want to add: \n')
        self.milk += int(add_milk)
        add_beans = input('Write how many grams of coffee beans you want to add: \n')
        self.beans += int(add_beans)
        add_cups = input('Write how many disposable cups of coffee you want to add: \n')
        self.cups += int(add_cups)
        print('')

    def Withdrawal(self):
        print(f'I gave you {self.money}\n')
        self.money -= self.money

a = Coffee_machine(400,540,120,9,550)
while True:
    action = input('Write action (buy, fill, take, remaining, exit): \n')
    print('')
    if action == 'buy':
        choosing_action = a.Making_coffee(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n'))
        if choosing_action == 'back':
            continue
        else:
            a.Making_coffee(choosing_action)
    elif action == 'fill':
        a.Filling()
    elif action == 'take':
        a.Withdrawal()
    elif action == 'remaining':
        a.Message()
    elif action == 'exit':
        exit()
