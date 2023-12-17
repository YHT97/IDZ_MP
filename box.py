import random
import pprint

class Box:
    def func(self, x, y):
        return x ** 2 + y ** 2

    # классовые переменные со стандартными параметрами
    x_min = -10  # Минимальное значение переменной x
    x_max = 10  # Максимальное значение переменной x
    y_min = -10  # Минимальное значение переменной y
    y_max = 10  # Максимальное значение переменной y
    population_size = 100  # Размер популяции
    generations = 50  # Количество поколений
    mutation_rate = 0.1  # Вероятность мутации
    function_1 = func
    filename = "out.txt"

    def __init__(self, x_min, x_max, y_min, y_max, population_size, generations, mutation_rate, function_1, filename):
        self.filename = filename
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.function_1 = function_1

    # Генерация случайного начального решения
    def generate_solution(self):
        x = random.uniform(self.x_min, self.x_max)
        y = random.uniform(self.y_min, self.y_max)
        return x, y

    # Операция скрещивания
    def crossover(self, parent1, parent2):
        x_avg = (parent1[0] + parent2[0]) / 2.0
        y_avg = (parent1[1] + parent2[1]) / 2.0
        return x_avg, y_avg

    # Операция мутации
    def mutate(self, solution):
        x = solution[0]
        y = solution[1]

        if random.random() < self.mutation_rate:
            x += random.uniform(self.x_min, self.x_max) * self.mutation_rate
            y += random.uniform(self.y_min, self.y_max) * self.mutation_rate

        return x, y

    def combined_box_optimization(self):
        population = []
        with open(self.filename, 'a') as file:

            # Генерация начальной популяции
            pprint.pprint("Генерация начальной популяции", stream=file)
            pprint.pprint("Генерация начальной популяции")
            for _ in range(self.population_size):
                solution = self.generate_solution()
                population.append(solution)
            pprint.pprint(population, stream=file)
            pprint.pprint(population)
            pprint.pprint("Вычисление приспособленности для каждого решения в популяции", stream=file)
            pprint.pprint("Вычисление приспособленности для каждого решения в популяции")
            for _ in range(self.generations):
                # Вычисление приспособленности
                fitness_scores = []
                for solution in population:
                    fitness = self.function_1(solution[0], solution[1])
                    fitness_scores.append(fitness)
                pprint.pprint("Вычисление приспособленности", stream=file)
                pprint.pprint("Вычисление приспособленности")
                pprint.pprint(fitness_scores, stream=file)
                pprint.pprint(fitness_scores)
                # Выбор лучших решений (элитных) для сохранения
                elite_indices = sorted(range(len(fitness_scores)), key=lambda k: fitness_scores[k])[
                                :int(self.population_size / 2)]
                elite_population = [population[i] for i in elite_indices]
                pprint.pprint("Выбор лучших решений (элитных)", stream=file)
                pprint.pprint("Выбор лучших решений (элитных)")
                pprint.pprint(elite_population, stream=file)
                pprint.pprint(elite_population)
                # Создание следующего поколения
                next_generation = elite_population

                # Операция скрещивания для создания потомков
                while len(next_generation) < self.population_size:
                    parent1 = random.choice(elite_population)
                    parent2 = random.choice(elite_population)
                    child = self.crossover(parent1, parent2)
                    next_generation.append(child)
                pprint.pprint("Вывод потомков после скрещивания", stream=file)
                pprint.pprint("Вывод потомков после скрещивания")
                pprint.pprint(next_generation, stream=file)
                pprint.pprint(next_generation)
                # Операция мутации
                next_generation = [self.mutate(solution) for solution in next_generation]
                pprint.pprint("Вывод потомков после мутации", stream=file)
                pprint.pprint("Вывод потомков после мутации")
                pprint.pprint(next_generation, stream=file)
                pprint.pprint(next_generation)
                # Замена текущей популяции следующим поколением
                population = next_generation

            # Находим решение с минимальным значением приспособленности
            best_solution = min(population, key=lambda x: self.function_1(x[0], x[1]))

            return best_solution