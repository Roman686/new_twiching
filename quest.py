print('Задача 6. Яйца')

def average_depth(start, stop):
    return start + (stop - start) / 2

def danger_formula(x):
    return x ** 3 - 3 * x ** 2 - 12 * x + 10

def main():
    danger_level = float(input('\nВведите максимально допустимый уровень опасности: '))
    surface = 0.0
    depth_ground = 4.0

    if danger_level <= 0:
        print(
            '\nЧто-то пошло ни так! \nМаксимально допустимый уровень опасности не должен быть меньше или равняться нулю! \nВведите заного.')
        main()
    else:
        depth = average_depth(surface, depth_ground)
        danger = danger_formula(depth)
        # print('Глубина:', depth, 'Опастность:', danger)
        while abs(danger) > danger_level:
            if danger > 0:
                surface = depth
            else:
                depth_ground = depth
            depth = average_depth(surface, depth_ground)
            danger = danger_formula(depth)
            # print('Глубина:', depth, 'Опастность:', danger)
        print(f'Приблизительная глубина безопасной кладки: {depth} m')


main()