import os
from art import tprint #импортируем функцию для вывода шапки в терминале

#алфавиты
eu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
eu_low = 'abcdefghijklmnopqrstuvwxyz'

ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ru_low = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

#функция шифрования
def cipher(lang,key,mess,res=""):

    if lang == 'ru':
        for i in mess:#проходим циклом по сообщению
            #Проверка регистра
            if i in ru:
                rus = ru
            elif i in ru_low:
                rus = ru_low

            letter = rus.find(i)# находим индекс символа
            new_letter = (letter + key) % len(rus)# добавляем к этому индексу ключ
            if i in rus:# проверка на вхождение в алфавит
                res += rus[new_letter]
            else:
                res += i
    else:
        if lang == 'eu':
            for i in mess:

                if i in eu:
                    eur = eu
                elif i in eu_low:
                    eur = eu_low

                letter = eur.find(i)
                new_letter = (letter + key) % len(eur)
                if i in eur:
                    res += eur[new_letter]
                else:
                    res += i
                    
    return res


def decrypt(lang,key,mess):
    return cipher(lang,-key,mess)


def main():
    #Вывод логотипа
    tprint("Caesar's cipher", font='bulbhead')

    #проверка ввода
    language = input("Enter the language ('ru' or 'eu'): ")
    while language not in ('ru','eu'):
        print("Error!!! Please try again!")
        language = input("Enter the language ('ru' or 'eu'): ")
    
    while True:
        try:
            key = int(input("Please enter the key (number): "))
        except ValueError:
            print("Error!!! Please try again! Key is a number!")
        else:
            break

    #Ввод текста   
    message = input("Please enter the text: ")
    final = cipher(language, key, message)
    print("Message: ", message)
    print("Encrypted message: ", final)


if __name__ == "__main__":
    main()