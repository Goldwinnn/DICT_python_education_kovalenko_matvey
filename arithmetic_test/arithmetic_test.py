counter = 0
edited_text = ""
import random

def test_2_lvl(counter):
    for j in range(5):
        num3 = random.randint(11, 29)

        print(num3)
        answer = input(">")

        while not (answer.lstrip('-').isdigit()):
            answer = input("Incorrect format.\n>")

        answer = int(answer)

        if answer == num3 ** 2:
            print("Right!")
            counter += 1
        else:
            print("Wrong!")

    print("Your mark is", counter, "/5")
    return counter


def test_1_lvl(counter):
    for i in range(5):
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operator = random.choice(["+", "-", "*"])

        print(num1, operator, num2)
        answer = input(">")

        while not answer.lstrip('-').isdigit():
            answer = input("Incorrect format.\n>")

        answer = int(answer)

        if operator == "+":
            if answer == num1 + num2:
                print("Right!")
                counter += 1
            else:
                print("Wrong!")

        elif operator == "-":
            if answer == num1 - num2:
                print("Right!")
                counter += 1
            else:
                print("Wrong!")

        elif operator == "*":
            if answer == num1 * num2:
                print("Right!")
                counter += 1
            else:
                print("Wrong!")

    print("Your mark is", counter, "/5")
    return counter


level = input(
    "Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9 \n2 - integral squares of 11-29\n>")
while level not in ["1", "2"]:
    level = input("Incorrect format.\n>")

counter = 0

if level == "1":
    counter = test_1_lvl(counter)
else:
    counter = test_2_lvl(counter)

y_n = input("Would you like to save your result to the file?. Write yes/no\n>")
if y_n.lower() == "yes":
    name = input("Enter your name:\n>")
    if level == "1":
        level_desc = "simple operations with numbers 2-9"
    else:
        level_desc = "integral squares of 11-29"
    edited_text += f"{name}: {counter}/5 in level {level} ({level_desc})."
    edited_text += "\n"
    f = open('results.txt', 'a')
    f.write(edited_text)
    f.close()
    print("Your results have been saved to results.txt")
else:
    print("Your results have not been saved.")
