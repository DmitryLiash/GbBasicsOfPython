# 1: Запросите от пользователя число, сохраните в переменную,
#  прибавьте к числу 2 и выведите результат на экран. 
# Если возникла ошибка, прочитайте ее, вспомните урок и 
# постарайтесь устранить ошибку.

# valueFromUser = int(input("Enter the number: "))
# print(valueFromUser + 2)

# 2: Используя цикл, запрашивайте у пользователя число, 
# пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число,
#  возведите его в степень 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете
# ему, что число неверное, и говорите о диапазоне допустимых.
#  И просите ввести заново.
# Допустим, пользователь ввел 2, оно подходит.
#  Возводим его в степень 2 и выводим 4.

# numberFromUser = None
# while True:
#     numberFromUser = int(input("Enter the numbers. 0 < numbers < 10:  "))
#     if numberFromUser > 0 and numberFromUser < 10:
#         break
#     print("Oshibka.")
# print("Vvedenoe vami chislo vo 2 stepeni ravno: " + str(numberFromUser ** 2))

# 3: Создайте программу “Медицинская анкета”,
#  где вы запросите у пользователя следующие данные:
#  имя, фамилия, возраст и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 
# лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему 
# более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему
#  более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать
#  на ваш вкус и полет фантазии.
def ScanUserMetric(weight, age, user):
    if age < 30 and 50 <= weight <= 120:
        return user + " - Вы богатырь, может 50 килограммовый, но богатырь"
    elif 30 <= age < 40  and (weight < 50 or weight > 120):
        return user + " - Вы исчезаете или же у вас есть своя собственная орбита "
    elif 40 <= age < 100  and (weight < 50 or weight > 120):
        return user + " - Срочно обратитесь к лекарю" 
    elif age >= 100:
        return user + " - Jesus Christ, That's Jason Bourne"
firstName = input("Введите свое имя: ")
secondName = input("Введите свою фамилию: ")
user = firstName + " " + secondName
weight = int(input("Введите свой вес: "))
age = int(input("Введите свой возраст: "))
print(ScanUserMetric(weight, age, user))





