import re

us_in = input('Введите имя и фамилию: ')
surname = re.findall(r'[A-zА-Яа-я]+(?:ев|ов|ова|ева)', us_in)
name = re.split(r'[A-zА-Яа-я]+(?:ев|ов|ова|ева)', us_in)

surname = (''.join(surname))
name = (''.join(name))

print(f'Фамилия: {surname}\n Имя: {name}')
