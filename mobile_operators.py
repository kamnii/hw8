import re
# MegaCom: 550, 990, 755
# O!: 500, 700
# Beeline: 770, 220


lst = '+996555800393, +996999800393, +996755800393, +996505800393, +996707800393, +996777800393, +996222800393'

megacom = re.findall(r"\S99655[0-9]{7}|\S99699[0-9]{7}|\S996755[0-9]{6}", lst)
o = re.findall(r"\S99670[0-9]{7}|\S99650[0-9]{7}", lst)
beeline = re.findall(r"\S99677[0-9]{7}|\S99622[0-9]{7}", lst)


print(f'MegaCom => {megacom} \nO! => {o} \nBeeline => {beeline}')
