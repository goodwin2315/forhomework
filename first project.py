# Задание 1
age = int(input('Сколько Вам лет: '))
number = int(input('Укажите Ваше любимое число: '))
name = input('Как Вас зовут? ')

print('Спасибо большое {} Вам {} лет. Ваше любимое число {}'.format(name, age, number))

# Задание 2
# seconds = int(input('Введите количество секунд: '))
# hours = seconds // 3600
# minutes = (seconds // 60) % 60
# seconds = seconds % 60
# print('{:02d}:{:02d}:{:02d}' .format(hours, minutes, seconds))

# Задание 3
# n = int(input('Введите число n: '))
# number_2 = n * 11
# number_3 = n * 111
# number_4 = n + number_2 + number_3
# print(number_4)

# Задание 4

# number = int(input('Введите целое положительное число: '))
# c = -1
# while number > 10:
#     b = number % 10
#     number = number // 10
#     if b > c:
#         c = b
# print(c)

# Задание 5
# revenue = int(input('Укажите, какая была выручка за предыдущий квартал в вашей фирме: '))
# deb = int(input('Укажите, какой был убыток за предыдущий квартал в вашей фирме: '))
#
# if revenue > deb:
#     profit = (revenue - deb)
#     ror = int((profit / revenue) * 100)
#     print('Ваша фирма приносит прибыль! Так держать. Рентабельность составила ', ror)
#     staff = int(input('Сколько у Вас сотрудников в фирме? '))
#     profit_staff = profit / staff
#     print('Прибыль на одного сотрудника составляет', profit_staff)
# elif deb > revenue:
#     print('Ваша фирма убыточна. Примите меры')


# Задание 6

# first_day = int(input('Какое кол-во км вы пробежали сегдня? '))
# max_km = int(input('Сколько вы хотели бы пробежать км? '))
# day = 1
# while first_day <= max_km:
#     print(first_day)
#     first_day = first_day * (1 + 10 / 100)
#     day += 1
# print('Если увеличивать расстояние на 10% вы пробежите {} км через {} дней'.format(max_km, day))
