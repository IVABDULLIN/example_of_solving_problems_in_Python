from random import randint

# Задача №1

list_banknotes = [1, 2, 4, 8, 16, 32, 64]

n = int(input('Введите натуральное число: '))

if n == 0:
    print('0 - не является натуральным числом.\n'
          'Введите натуральное число отличное от числа - 0.')


k = 128 # Для удобства расчета вводим пременную k = 128

while 1 <= (k := k // 2):
    m, n = divmod(n, k)
    if m > 0:
        print('Купюр номиналом в', k, 'у.е.', 'необходимо', m, 'шт.')

print()


# Задача №2

str_1 = input('Введите целые числа через пробелл: ')

if str_1 == '':
    print('Введена пустая строка!\n'
          'Попробуйте ввести данные в строку str_1 снова!')

str_2 = input('Введите целые числа через пробелл: ')

if str_2 == '':
    print('Введена пустая строка!\n'
          'Попробуйте ввести данные в строку str_2 снова!')

str_3 = input('Введите целые числа через пробелл: ')

if str_3 == '':
    print('Введена пустая строка!\n'
          'Попробуйте ввести данные в строку str_3 снова!')


list_1 = list(map(str, str_1.split()))
list_2 = list(map(str, str_2.split()))
list_3 = list(map(str, str_3.split()))
list_1.extend(list_2)
list_1.extend(list_3)
list_4 = [[int(i)] for i in list_1]
print('Новый двумерный список:', list_4)

print()


# Задача №3

M, N = 3, 4

array = [[randint(1, 99) for j in range(N)] for i in range(M)]
print('Сформированная матрица M*N:', *array, sep='\n')
print()

mas = []

if array[0][0] in array[1] or array[0][1] in array[1] or array[0][2] in array[1] or array[0][3] in array[1]:
    mas.append(1)
    mas.append(2)
elif array[0][0] in array[2] or array[0][1] in array[2] or array[0][2] in array[2] or array[0][3] in array[2]:
    mas.append(1)
    mas.append(3)
elif array[1][0] in array[0] or array[1][1] in array[0] or array[1][2] in array[0] or array[1][3] in array[0]:
    mas.append(2)
    mas.append(1)
elif array[1][0] in array[2] or array[1][1] in array[2] or array[1][2] in array[2] or array[1][3] in array[2]:
    mas.append(2)
    mas.append(3)
elif array[2][0] in array[0] or array[2][1] in array[0] or array[2][2] in array[0] or array[2][3] in array[0]:
    mas.append(3)
    mas.append(1)
elif array[2][0] in array[1] or array[2][1] in array[1] or array[2][2] in array[1] or array[2][3] in array[1]:
    mas.append(3)
    mas.append(2)
elif (array[0][0] in array[1]) and (array[0][0] in array[2]) or (array[0][1] in array[1]) and (array[0][1] in array[2]):
    mas.append(1)
    mas.append(2)
    mas.append(3)
elif (array[0][2] in array[1]) and (array[0][2] in array[2]) or (array[0][3] in array[1]) and (array[0][3] in array[2]):
    mas.append(1)
    mas.append(2)
    mas.append(3)
elif (array[1][0] in array[0]) and (array[1][0] in array[2]) or (array[1][1] in array[0]) and (array[1][1] in array[2]):
    mas.append(2)
    mas.append(1)
    mas.append(3)
elif (array[1][2] in array[0]) and (array[1][2] in array[2]) or (array[1][3] in array[0]) and (array[1][3] in array[2]):
    mas.append(2)
    mas.append(1)
    mas.append(3)
elif (array[2][0] in array[0]) and (array[2][0] in array[1]) or (array[2][1] in array[0]) and (array[2][1] in array[1]):
    mas.append(3)
    mas.append(1)
    mas.append(2)
elif (array[2][2] in array[0]) and (array[2][2] in array[1]) or (array[2][3] in array[0]) and (array[2][3] in array[1]):
    mas.append(3)
    mas.append(1)
    mas.append(2)


if mas != []:
    print('Список с номерами строк матрицы M*N,\n'
          'где есть одинаковые элементы:', mas)
else:
    print('Одинаковые элементы в строках матрицы M*N, отсутствуют!')

print()


# Задача №4

integer_1 = input('Введите любые целые числа(не менее 5) '
                     'через пробелл: ')
integer_2 = input('Введите целые числа(не менее 5) '
                     'через пробелл: ')

int_list_1 = list(map(int, integer_1.split()))
int_list_2 = list(map(int, integer_2.split()))
new_list = list(zip(int_list_1, int_list_2))

final_list = list(map(lambda x: x[0]+x[1], new_list))
iterator = iter(list(map(lambda x: x[0]+x[1], new_list)))
print('Первое значение:', next(iterator))
print('Второе значение:', next(iterator))
print('Третье значение:', next(iterator))
print('Четвертое значение:', next(iterator))
print('Пятое значение:', next(iterator))

print()


# Задача №5

class Сartoon_characters:
    '''Мультфильм "Люди Икс(Marvel)".'''
    look = 10
    __mask = 2


    def __init__(self, name, power, food):
        Сartoon_characters.look = 10
        Сartoon_characters.__mask = 2
        self.__name = name
        self.power = power
        self.food = food
        print("Создали новый персонаж -", self.__name)


    @property
    def read(self):
         return self.look

    @property
    def r(self):
        return self.__mask

    @r.setter
    def r(self, value):
        self.__mask = value


    def look_in_the_mask(self):
        if self.look == 0 and self._Сartoon_characters__mask == 0:
            print('У героев нет масок.')
        else:
            print('У обоих героев есть маски!')


    def __str__(self):
        print(f'Герой {self._Сartoon_characters__name} -\n'
              f'является персонажем мультфильма "Люди Икс!"')


    def __del__(self):
        print(f'Персонаж {self.__name} - удален!')


wolverine = Сartoon_characters('Росомаха', 100, 100)
cyclops = Сartoon_characters('Циклоп', 110, 110)
print('Мое имя -', wolverine._Сartoon_characters__name)
print('А меня зовут -', cyclops._Сartoon_characters__name)
print('Способность видеть в темноте у Росомахи -',
      wolverine.look)
print('Эффективность маски у Росомахи-',
      wolverine._Сartoon_characters__mask)
cyclops.look += 10
cyclops._Сartoon_characters__mask += 1
print('Способность видеть в темноте у Циклопа -',
      cyclops.look)
print('Эффективность маски у Циклопа -',
      cyclops._Сartoon_characters__mask)
wolverine.look_in_the_mask()
Сartoon_characters.__str__(wolverine)
Сartoon_characters.__str__(cyclops)
print('Режим чтения первого атрибута персонажа\n'
      '"Росомаха" look =', wolverine.read, '- активен!')
print('Режим чтения первого атрибута персонажа\n'
      '"Циклоп" look =', cyclops.read, '- активен!')
print('Режимы: чтения, записи атрибута\n'
      '__mask =', wolverine.r, '- активны!')
print('Режимы: чтения, записи атрибута\n'
      '__mask =', cyclops.r, '- активны!')
del Сartoon_characters