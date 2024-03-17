import caesar

ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' #алфавит
lang='ru'
diff = [0] * 33

def analyse(text): # считаем процент содержания букв в тексте

    encPers = [0] * 33 #процентное распределение букв в зашифрованном тексте
    cnt = 0

    for i in range(len(encPers)):
        for x in text:
            if x == ru[i]:
                encPers[i] += 1
                cnt += 1
                
    for i in range(len(encPers)):
        encPers[i] = (encPers[i]/cnt)*100 #процент для i-й буквы алфавита        

    return encPers



def main():

    file = open('encrypted.txt', encoding="UTF-8") #открываем два текста
    file1 = file.read().upper()
    file0 = file1

    ffile = open('native.txt', encoding="UTF-8") 
    ffile1 = ffile.read().upper()

    file.close()
    ffile.close()

    arrEnc = analyse(file1)
    arrNat = analyse(ffile1)

    print('\tENC   NAT   DIF') #вывод итоговой таблицы
    for i in range(len(arrEnc)):
        diff[i] = abs(arrEnc[i]-arrNat[i])
        print(f'{i+1})',ru[i], ' - ', '%.4f' % arrEnc[i],'%.4f' % arrNat[i],'%.4f' % diff[i])

    key = int(input("Введите ключ: "))
    print(caesar.decrypt(lang,key,file0)) #расшифровка текста  

if __name__ == "__main__":
    main()