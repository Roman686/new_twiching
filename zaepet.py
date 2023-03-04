 print('Хочешь купить удочку или катушку?(1 - удочка, 2 - катушка)')
 tackle = int(input())
 if tackle == 1:

    print('Звонить по телефону  8906868686')
    num = int(input('Введите 1 или 2: '))
    num1 = int(input('Введите 4 или 5: '))

    if num == 1:
        print('Лошадь')
        print('корова')
        print('говнарь Чича')

    elif num1 != 4 or 5:
        print('Тупой, сказали же ввести 4 или 5')

    else:
        print('Хеллло!')
        print('говнарь Боба')
