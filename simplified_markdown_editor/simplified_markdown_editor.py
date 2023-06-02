command_list = ["plain", "bold/italic", "inline-code", "header", "link", "new-line",
                "ordered-list", "unordered-list", "!help", "!done"]
main_text = []
main_text2 = []


def plain():
    user_str = input("Text: >")
    main_text.append(user_str + "\n")
    main_text2.append(user_str)


def bold_italic():
    user_str = input("Text: >")
    main_text.append(f"***{user_str}***\n")
    main_text2.append(f"***{user_str}***")


def inline_code():
    user_str = input("Text: >")
    main_text.append(f"`{user_str}`\n")
    main_text2.append(f"`{user_str}`")


def header():
    level = int(input("Level: >"))
    if level < 1 or level > 6:
        print("The level should be within the range of 1 to 6")
    else:
        user_str = input("Text: >")
        main_text.append("\n" + "#" * level + " " + user_str + "\n")
        main_text2.append("\n" + "#" * level + " " + user_str + "\n")


def new_line():
    main_text[-1] = main_text[-1] + " " * 2


def link():
    label = input("Label: >")
    url = input("URL: >")
    main_text.append(f"[{label}]({url})\n")
    main_text2.append(f"[{label}]({url})")


def ordered_list():
    rows = int(input("Number of rows: >"))
    if rows <= 0:
        print("The number of rows should be greater than zero")
    else:
        for i in range(1, rows + 1):
            user_text = input(f"Row #{i}:>")
            main_text.append(f"{i}.{user_text}\n")
            main_text2.append(f"{i}.{user_text}")


def unordered_list():
    rows = int(input("Number of rows: >"))
    if rows <= 0:
        print("The number of rows should be greater than zero")
    else:
        for i in range(1, rows + 1):
            user_text = input(f"Row #{i}:>")
            main_text.append(f"*{user_text}\n")
            main_text2.append(f"*{user_text}")


def write_to_file():
    file = open("output.md", "w", encoding="utf-8")
    for line in main_text:
        file.write(line)
    file.close()


user_formatter = None
while user_formatter != command_list[9]:
    user_formatter = input("Choose a formatter: > ")
    if user_formatter == command_list[0]:
        plain()
    elif user_formatter == command_list[1]:
        bold_italic()
    elif user_formatter == command_list[2]:
        inline_code()
    elif user_formatter == command_list[3]:
        header()
    elif user_formatter == command_list[4]:
        link()
    elif user_formatter == command_list[5]:
        new_line()
    elif user_formatter == command_list[6]:
        ordered_list()
    elif user_formatter == command_list[7]:
        unordered_list()
    for lines in main_text2:
        print(lines)
    if user_formatter not in command_list:
        print("Unknown formatting type or command")
    elif user_formatter == command_list[8]:
        print("Available formatters: plain, bold/italic, header, link, inline-code,"
              "ordered-list, unordered-list, new-line\nSpecial commands: !help !done")


write_to_file()
