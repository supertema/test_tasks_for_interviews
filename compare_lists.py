'''
Написать скрипт для сравнения двух списков с указанием что добавилось в список, что ушло, насколько позиций произошло смещение элемента в списке. Порядок элементов важен.
Список 1: A, B, C, D, E, F, G, H, I, J, K, L, M, N
Список 2: B, C, D, A, F, E, Z, M, N, J, K, L

результат в виде ссылки на github
Написать в телеграм @xinhuashe "Привет, я по поводу вакансии, вот моё решение тестового задания [ссылка на гитхаб]"
Все вопросы также можно задать в телеграм
'''

'''
*1    - позицию
*2-4  - позиции
*5-20 - позиций
'''

def pos(num):
    num = str(num)
    if 11 <= int(num[-2:]) <= 19:
        num = str(num)
        print(num + ' позиций')
    elif int(num[-1]) == 1:
        num = str(num)
        print(num + ' позицию')
    elif 2 <= int(num[-1]) <= 4:
        num = str(num)
        print(num + ' позиции')
    elif int(num[-1]) >= 5:
        num = str(num)
        print(num + ' позиций')


a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
b = ['B', 'C', 'D', 'A', 'F', 'E', 'Z', 'M', 'N', 'J', 'K', 'L']


inda = 0
indb = 0

list_sdvig = [] # список, в который будем помещать оставшиеся, но сдвинувшиеся элементы

while len(a) != 0:
    if b[indb] in list_sdvig: # если элемент попал в этот список, мы его уже учли, но оставили для порядка индекса, а когда дошли в цикле перебора списка b
        b.remove(b[indb]) # удаляем

    elif a[inda] != b[indb] and b[indb] not in a and a[inda] not in b:
        print(f'Элемент {a[inda]} ушел из списка b')
        a.remove(a[inda])

    elif  a[inda] != b[indb] and b[indb] not in a:
        print(f'Элемент {b[indb]} добавился в список b')
        b.remove(b[indb])

    elif  a[inda] != b[indb] and a[inda] in b:
        position = b.index(a[inda])
        print(f'Элемент {a[inda]} остался в списке b, но сдвинулся вперед на', end=' ')
        pos(position)
        list_sdvig.append(a[inda]) # добавляем в список сдвинувшиеся элементы, чтоб не посчитать их еще раз
        a.remove(a[inda])

    elif a[inda] != b[indb]:
        print(f'Элемент {a[inda]} ушел из списка b')
        a.remove(a[inda])

    elif a[inda] == b[indb]:
        print(f'Элемент {a[inda]} остался в списке b')
        a.remove(a[inda])
        b.remove(b[indb])
