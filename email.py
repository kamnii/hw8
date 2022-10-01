import re


while True:
    email = input("Введите почту: ")
    pattern = r"^[a-zA-Zа-яА-ЯёЁ]+@(?:mail.ru\b|gmail.com\b)"
    result = re.findall(r"^[a-zA-Zа-яА-ЯёЁ0-9]+@[a-z]+[.][a-z]+$", email)
    print(result)
    if result:
        print("Ok")
    else:
        print("Error!")
