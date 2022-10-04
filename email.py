import re


while True:
    email = input("Введите почту: ")
    pattern = r"^[a-zA-Zа-яА-ЯёЁ]+@(?:mail.ru\b|gmail.com\b)"
    result = re.findall(r"^[a-zA-Z]+@[a-z]+[.][a-z]+$", email)

    if result:
        print("It's okay")
    else:
        print("Incorrect email")
