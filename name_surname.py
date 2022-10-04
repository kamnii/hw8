import re

# us_in = input('Введите имя и фамилию: ')
# surname = re.findall(r'[A-zА-Яа-я]+(?:ев|ов|ова|ева)', us_in)
# name = re.split(r'[A-zА-Яа-я]+(?:ев|ов|ова|ева)', us_in)
#
# surname = (''.join(surname))
# name = (''.join(name))
#
# print(f'Фамилия: {surname}\n Имя: {name}')

txt = input("Введите имя и фамилию: ")
surname = re.findall(r"[А-Яа-я]+ев\b|[А-Яа-я]+ов\b|[А-Яа-я]+ова\b|[А-Яа-я]+ева\b|[А-Яа-я]+ава\b|[А-Яа-я]+ко\b"
                     r"|[А-Яа-я]+ин\b|[А-Яа-я]+ина\b|[А-Яа-я]+евна\b", txt)
surname_lst = ("".join(surname))

name = re.split(r"[А-Яа-я]+ев\b|[А-Яа-я]+ов\b|[А-Яа-я]+ова\b|[А-Яа-я]+ева\b|[А-Яа-я]+ава\b|[А-Яа-я]+ко\b"
                r"|[А-Яа-я]+ин\b|[А-Яа-я]+ина\b|[А-Яа-я]+евна\b", txt)
name_lst = ("".join(name))

print(f'Фамилия: {surname_lst}\nИмя: {name_lst[1:] if name_lst[0] == " " else name_lst}')
