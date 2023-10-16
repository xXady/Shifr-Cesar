alfavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alfaviT = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
sdvig = int(input('Шаг шифровки от 1 до 33: ')) % 33
stroka = input("Сообщение для Дешифровки: ")
itog = ''
for i in stroka:
    mesto = alfavit.find(i)
    mestO = alfaviT.find(i)
    new_mesto = mesto + sdvig
    new_mestO = mestO + sdvig
    if i in alfavit:
        itog += alfavit[new_mesto]
    elif i in alfaviT:
        itog += alfaviT[new_mestO]
    else:
        itog += i
print(itog)