import random


def lucky_process(amount_user, names, price, amount):
    """ Вдача, при обирані YES(y) функція обирає одного щасливчика якому не протрібно платити,
     при вборі NO(n) нічого не відбуваеться"""
    print("Do you want to use the 🎰 \"Who is lucky?\" 🎰 feature? Write y/n:")
    luck = str(input('>'))
    while luck != "luck":
        if luck == "n":
            print("No one is going to be lucky")
            dict_1 = dict.fromkeys(names, price)
            print(dict_1)
            print('See you next time')
            return
        elif luck == "y":
            lucky_user = random.choice(names)
            print(lucky_user + "is the lucky one!")
            new_price = amount / (amount_user - 1)
            dict_1 = dict.fromkeys(names, new_price)
            dict_1[lucky_user] = 0
            print(dict_1)
            print('Goodbye!')
            return


def get_dictionary():
    """ Фінкція проводить розрахунки після вводу данних та виводу значення ключа """
    names = []
    print("Enter number of party members (including you)")
    amount_user = int((input(">")))
    if amount_user > 0:
        print("Enter the name of every friend (including you), each on a new line:")
    if amount_user == 0:
        print("You have no friends 💀")
        return
    for i in range(amount_user):
        names.append(str(input(">")))

    dict_1 = dict.fromkeys(names, 0)
    print(dict_1)
    print("💰Enter the total amount💰")
    amount = float(input(">"))
    price = amount / amount_user
    dict_1 = dict.fromkeys(names, round(price, 2))
    print(dict_1)
    lucky_process(amount_user, names, price, amount)


get_dictionary()
