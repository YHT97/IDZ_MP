import pprint

from box import Box
import inputmaster as im

x_min = -10  # Минимальное значение переменной x
x_max = 10  # Максимальное значение переменной x
y_min = -10  # Минимальное значение переменной y
y_max = 10  # Максимальное значение переменной y
population_size = 100  # Размер популяции
generations = 50  # Количество поколений
mutation_rate = 0.1  # Вероятность мутации
func_str = "x**2 + y**2"

if __name__ == '__main__':

    switcher = input("Получить данные из файла(y): ")

    if switcher == 'y':
        out_file = "out.txt"
        file_name = input("Введите имя файла: ")
        with open(file_name, 'r') as file:
            # Читаем каждую строку из файла
            for line in file:
                # Разделяем строку на элементы, используя пробел в качестве разделителя
                key, value = line.strip().split()
                # Проверяем ключ и сохраняем значение соответствующей переменной
                if key == 'function':
                    func_str = str(value)
                elif key == 'x_min':
                    x_min = float(value)
                elif key == 'x_max':
                    x_max = float(value)
                elif key == 'y_min':
                    y_min = float(value)
                elif key == 'y_max':
                    y_max = float(value)
                elif key == 'population_size':
                    population_size = int(value)
                elif key == 'generations':
                    generations = int(value)
                elif key == 'mutation_rate':
                    mutation_rate = float(value)
    else:
        func_str = input("Введите функцию: ")
        x_min = float(input("Введите минимальное значение переменной x: "))
        x_max = float(input("Введите максимальное значение переменной x: "))
        y_min = float(input("Введите минимальное значение переменной y: "))
        y_max = float(input("Введите максимальное значение переменной y: "))
        population_size = int(input("Введите размер популяции: "))
        generations = int(input("Введите количество поколений: "))
        mutation_rate = float(input("Введите вероятность мутации: "))

    func = im.input_from_text(func_str)

    box = Box(x_min, x_max, y_min, y_max, population_size, generations, mutation_rate, func, out_file)

    best_solution = box.combined_box_optimization()
    with open(out_file, 'a') as file:
        pprint.pprint("Функция: ", stream=file)
        pprint.pprint(func_str, stream=file)
        pprint.pprint("Оптимальное решение: ", stream=file)
        pprint.pprint("x = " + str(best_solution[0]), stream=file)
        pprint.pprint("y = " + str(best_solution[1]), stream=file)
        pprint.pprint("Значение функции: " + str(box.function_1(best_solution[0], best_solution[1])), stream=file)

        pprint.pprint("Функция: ")
        pprint.pprint(func_str)
        pprint.pprint("Оптимальное решение: ")
        pprint.pprint("x = " + str(best_solution[0]))
        pprint.pprint("y = " + str(best_solution[1]))
        pprint.pprint("Значение функции: " + str(box.function_1(best_solution[0], best_solution[1])))
        print("Данные записаны в " + out_file)
