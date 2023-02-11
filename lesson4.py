#1  STROKA
# type str  like name = "blabla" or name = 'blabla'
# stroka str sostoit iz simvolov
### mojno poluchiti simvol iz stroki po indeksu like name[1] it would be "l"
# indeks s konca nachinaetsia -1 like name[-1] it would be "a"
### SREZ stroki(poluchaem srazu chasti stroki) f.e. name[start:end]
# name = 'blabla' => name[2:4] => 'abl'    
# name[:5] srez s nachala stroki   and    name[1:] srez s konca stroki
### funkcia len  i metody stroki
# len(name) => dilina stroki skoliko v nei simvolov
# name.find('a')  => ishem simvol a v stroke
# name.split() => razbivka stroki cherez probeli
# name.isdigit() => proveriaet chto stroka sostoit iz chesel toliko
# name.upper() => priv stroki k verhnemu registru
# name.lower() => k nijnemu registry
###drugie methody stroki  help(str) ili pythonworld.ru
# FORMAT STROKI
# 1 sposob konkatenacia + sleivaem  NE REKOMEND
# 2 % op
# name = 'oleg'
# age = 30
# hiname = 'privet %s tebe %d let' %(name, age)
# print(hiname)
# 3 format funkcia best of the best
# name = 'oleg'
# age = 30
# hiname = 'privet {} tebe {} let'.format(name, age)
# print(hiname)
####### ZADACHA
# top4 = 'Первые 5 мест на соревнованиях: 1. Иванов 2. Петров 3. Сидоров 4. Хзов' 
# viviod pozdravlerm pervie 3 mesta s uspehom
# start = top4.find('1')
# end = top4.find('4')
# top3 = top4[start: end]
# print('Поздравляем {} c успехом !!!'.format(top4[top4.find('1'): top4.find('4')]))

# 4 Списки коллекции обьектов произвольных типов
# some_list = ['hello', 123, True] но чаще в список вкл обьекты одного типо
# friends = ['leo', 'max', 'Kate']      emtry_list = []
# len(friends) - длина списка
# friends.append() - добавление нового элемента и возрат его
# friends.pop() - удаляем последний элемент и возвращаем его
# friends.clear() -очищаем весь список
# friends.remove() - удаление обьекта из списка
# del friends[0] - удаление эллемента по индексу
# fr = ['Max', 'Leo', 'Don-Don']
# print(fr)
# print(len(fr))
# fr.append('Ron')
# print(fr)
# print(len(fr))
# print(fr.pop())
# print(fr)
# fr.clear()
# print(fr)
# fr = ['Max', 'Leo', 'Don-Don']
# fr.remove('Leo')
# print(fr)
# del fr[0]
# print(fr)
# опператор in (проверка наличия эллемента в списке)   'max' in friend => True or False
# Работает и со строчками: 'S' in 'Sup'
### tuple(кортедж) список который нельзя изменять name = ('Sasha', 'Oleg', 'Dima')

# hi = 'Supa'
# if hi.find('up') != -1:  #print(hi.find('up'))
#     print('Est')
#   # ==>
# if 'up' in hi:
#     print('Est')

# goals = ['50 очков англ', 'курс python gb', 'ДЗ gb 5']
# if 'помыть посуду' in goals:
#     print('Есть')
# else:
#     goals.append('помыть посуду')
# print(goals)


#print('Соревнования')
# count = int(input('Введите колличество участиников: '))
# allusers = []
# i = 0
# while i < count:
#     allusers.append(input('Введите имя участника заневшего {} место:'.format(i + 1)))
#     i += 1
# print(allusers)
# print('Победили: 1. {} 2. {} 3. {} Поздравляем победителей.'.format(allusers[1], allusers[2], allusers[3]))
# print('По алфавиту: {}'.format(sorted(allusers)))

### Последовательность
# контенер. элементы которого представляют некую последовательность
# могут быть изменяемые(список). так и не измн.(кортедж. строка)
# реализует методы(индесация, взятие длины, цикл for итд)

# Утиная типизация
# если это плавает как устка, крякает как утка, то это, возможно, утка.
#Если обьект содержит реализацию методов последов. - он счит. послед.
# friends = ['Max', 'Leo', 'Kate']

# # i = 0
# # while i < len(friends):
# #     friend = friends[i]
# #     print(friend)
# #     i += 1

# for friend in friends:
#     print(friend)

# friends_name = 'Maximus'
# for leter in friends_name:
#    Print(leter)     

# roles = ('userd', 'admin', 'noob')
# for role in roles:
#     print(role)

# Range позволяет создать последовательности целых чисел
# чаще всего используется с циклом for

# winners = ['Max', 'Leo', 'Kate']
# perebor prost 
# for winner in winners:
#     print(winner)

# for i in range(len(winners)):
#     print(i + 1,'.', winners[i])

# фунцкия range параметры
# range(start_or_stop,stop[,step])
# start_or_stop - начало или конец последовательности
# stop -конец
# step -шаг

# nums = range(1, 30, 2)  #(начало. конец не вкл, шаг)
# print(nums)
# for num in nums:
#     print(num)

# print(list(range(5, 21, 2)))

### for - перебор последовательности. индекс не нужен
### for range - перебор последовательности. индекс нужен
### for range - необходимо пропуст элементы или идти с конца
### while - цикл связан с условием, но не с последовательностью.


# Словари. Определение, методы и перебор

### Словарь dict
# неупоряд. колек. произвольных обьектов с доступом по ключу.

# обьяв словаря
# my-dict = {key1: val, key2: val2, ...}   (ключ: значение)
# friends = ['Max', 'Leo', 'Puk']
# friend = friends[0]
# print(friend)
# friend = {
#     'name' : 'Max',
#     'age' : 23
    
# }
# print(friend)

## Основные дествия со словарем
# получение эллемента по ключу friend['name']
# добавление значения friend['has_car'] = True
# изменения значения friend['has_car'] = False
# удаление значения remove friend['age]
# оператор in 'age' in friend

# friend = {
#     'name' : 'Max',
#     'age' : 23
    
# }
# print(friend)
# print(type(friend))

# print(friend['age'])

# + dobav

# friend['has_car'] = True
# print(friend)
# friend['has_car'] = False
# print(friend)
# # - udal
# del friend['age']
# print(friend)

# if 'age' in friend:
#     print('Da')
# else: print('no')

# Варианты перебора словаря
# по ключам
# по значениям
# по парам ключ, значение

# friend = {
#     'name' : 'Max',
#     'age' : 23,
#     'has_car' : True
    
# }
# # po klucham
# for key in friend.keys():
#     print(key)
#     print(friend[key])

# # po znach
# for val in friend.values():
#     print(val)
# #pari kluck znachenie
# for item in friend.items():
#     print(item)
# for key, val in friend.items():
#     print(key)
#     print(val)

# множество set
# неупоряд. коллекции. содержат не повтор элементы
# Во множесте не может быть 2х одинаковых эллементов
# cities = {'Las Vegas', 'Paris', 'Moscow'}

# cities =['Las Vegas', 'Paris', 'Moscow', 'Paris']
# print(type(cities))
# print(cities)

# citiesNew = set(cities)
# print(type(citiesNew))
# print(citiesNew)

# citiesC = {'Las Vegas', 'Paris', 'Moscow'}
# print(type(citiesC))
# print(citiesC)

# Действия со множествами
#добавление эллементов cities.add('nameSitie')
#удаление эллементов cities.remove('Moscow')
#длина множеста len
#оператор in, цикл for
#работа с несколькими множествами(обед., пересеч., итд)
# citiesC = {'Las Vegas', 'Paris', 'Moscow'}
# print(citiesC)
# citiesC.add('Astana')
# print(citiesC)
# citiesC.remove('Moscow')
# print(citiesC) 
# print(len(citiesC))
# print('Paris' in citiesC)
# for city in citiesC:
#     print(city)

## Операции со множествами
#обьединение |
#пересечение &
#разность -

# # Каждый из супругов собирает вещи в поездку
# max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
# kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}
# # 1 какие вещи взяли супруги
# # 2 найти повторяющиеся вещи
# # 3 какие вещи взял макс, но не взяла кейт
# # 4 какие вещи взяла кейт, но не взял макс
# print(max_things)
# print(kate_things)
# print('---------------------')
# #1 
# print(max_things | kate_things)
# print('---------------------')
# #2
# print(max_things & kate_things)
# print('---------------------')
# #3
# print(max_things - kate_things)
# print('---------------------')
# #4
# print(kate_things - max_things)






