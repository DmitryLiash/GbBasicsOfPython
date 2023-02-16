def RandomCreate():
    import random
    try:
        minValue = int(input("Введите минимальное значение для рандома: "))
        maxValue = int(input("Введите максимальное значение для рандома: "))
        randomValue = random.randint(minValue, maxValue)
        return randomValue
    except:
        print('ошибка')
        RandomCreate()
        
        
def Serch(randomValue):
    print("Игра угадайка - введи число от 1 до 100")
    enterValue = None
    count = 0
    maxCount = 3
    try:
        while enterValue != randomValue:
            count += 1
            if count > maxCount:
                print("вы использовали все {} попыток. Игра закончена".format(maxCount))
                break
            enterValue = int(input('попытка {} Введите число: '.format(count)))
            if enterValue > randomValue:
                print('Загаданое значение меньше')
            else:
                print('Загаданное значеник больше')
        else:
            print('Победа !!! Загаданное число было равно {}'.format(randomValue))

    except:
        print('ошибка')
        Serch(randomValue)

Serch(RandomCreate())