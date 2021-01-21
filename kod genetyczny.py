from random import random, randint, choices


class Polynomial:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def value(self, x):
        return a * x * x * x + b * x * x + c * x + d

    def find_maximum(self, begin, end):
        maximum = 0
        xpos = 0
        for x in range(begin, end):
            val = max(maximum, self.value(x))
            if maximum < val:
                maximum = val
                xpos = x
        return (xpos, maximum)


class GeneticAlgorithm:
    def __init__(self, function, Pk, Pm, starting_pool):
        self.function = function
        self.crossing_rate = Pk
        self.mutation_rate = Pm
        self.starting_pool = starting_pool
        self.pool = starting_pool.copy()
        self.chromosome_length = len(starting_pool[0])
        self.calculate_fitness()

    def iterate(self):
        # Metoda iteracji wykonująca kolejno selekcje, krzyżowanie, mutacje i wyliczenia funkcji dopasowania
        self.selection()
        self.crossing()
        self.mutation()
        self.calculate_fitness()

    def calculate_fitness(self):
        # Pula chromosomów to lista stringów które wystarczy zamienić przekonwertować z zapisu binarnego na dziesiętny
        # int("101", 2) == 5
        self.fenotypes = list(map(lambda el: int(el, 2), self.pool))
        # Wyliczenie funkcji dopasowania
        self.fitness_values = list(map(lambda el: self.function.value(el), self.fenotypes))

    def selection(self):
        # Funkcja choice losuje nową pulę. Pierwszy parametr funkcji to populacja startowa, drugi paramtr to lista wag
        # Wagi nie muszą być określone w procentach czy sumie prawdopodobieństwa <0, 1>
        # parametr k określa wielkość wylosowanej listy
        self.pool = choices(self.pool, self.fitness_values, k=len(self.pool))

    def crossing(self):
        # pętlę for iterujemy index i od 0 do rozmiaru puli o 2 wartości (0, 2, 4, 6, ...)
        for i in range(0, len(self.pool), 2):
            locus = randint(1, 1 + self.chromosome_length)  # losowanie od 1 do 1 + długość_chromosumu
            rate = random()  # losowanie prawdopodobieństwa od 0 do 1
            if (
                    rate < self.mutation_rate):  # Jeżeli wylosowane prawdopodobieństwo jest większe równe od prawdopodobieństwa mutacji to następuje mutacja
                # Utworzenie nowego chromosomu odbywa się poprzez połączenie części i oraz i + 1 (gdy i = 0, i + 1 = 1, itd.)
                # Do utworzenie łańcuchów użyłem notacji slice. Przykład prostego użycia:
                # str = "Adam Małysz"
                # str[1:4] == "Adam"
                self.pool[i], self.pool[i + 1] = self.pool[i][:locus] + self.pool[i + 1][locus:], self.pool[i + 1][
                                                                                                  :locus] + self.pool[
                                                                                                                i][
                                                                                                            locus:]

    def mutation(self):
        for i in range(len(self.pool)):
            locus = randint(0, self.chromosome_length - 1)
            rate = random()
            if (rate < self.mutation_rate):
                mutated = list(self.pool[i])
                if (mutated[locus] == '1'):
                    mutated[locus] = '0'
                else:
                    mutated[locus] = '1'
                self.pool[i] = ''.join(mutated)

    def sum_of_fitness(self):
        return sum(self.fitness_values)


# Pobieramy parametry programu:
a, b, c, d, Pk, Pm, maximum_value_occurencies = map(float, input("Podaj a, b, c, d, Pk, Pm, N: ").split())
# Jeżeli wartość zwrócona przez funkcję input jest równa "tak" zmienna save_to_file ma wartość True:
save_to_file = "tak" == input("Czy chcesz zapisać iteracje do pliku? [tak/nie]? ")
f = open("iterations.txt", "w")

function = Polynomial(a, b, c, d)
# Tworzenie losowej puli startowej:
starting_pool = [''.join(choices("01", k=5)) for x in range(6)]
# starting_pool = ["00000", "10010", "11101", "00110", "10101", "11001"]
algorithm = GeneticAlgorithm(function, Pk, Pm, starting_pool)
xmax, maximum = function.find_maximum(0, 31 + 1)

occurencies = 0  # zmienna zliczająca wystąpienia maksymalnej sumy funkcji przystosowania
iteration = 0;
# Główna pętla programu która będzie trwać do wystąpienia maksymalnej sumy funkcji przystosowania
while occurencies != maximum_value_occurencies:
    iteration = iteration + 1
    algorithm.iterate()

    # Sprawdzenie czy suma jest sumą maksymalną
    new_sum = algorithm.sum_of_fitness()
    max_sum = maximum * len(algorithm.pool)
    if (new_sum == max_sum):
        occurencies = occurencies + 1
    else:
        occurencies = 0

    # Zapis do pliku wszystkich puli
    if save_to_file == True:
        print("\nIteracja:", iteration, file=f)
        for id, chromosome in enumerate(algorithm.pool):
            print("Chromosom", 1 + id, ":", chromosome, file=f)
            print("\tFenotyp:", algorithm.fenotypes[id], file=f)
            print("\tFunkcja przystosowania:", algorithm.fitness_values[id], file=f)
            print("\tPrawdopodobieństwo selekcji:", algorithm.fitness_values[id] * 100 / algorithm.sum_of_fitness(),
                  "%", file=f)
        print()

f.close()

print()
print("Pula początkowa:", algorithm.starting_pool)
print("Pula końcowa:   ", algorithm.pool)

print()
for id, chromosome in enumerate(algorithm.pool):
    print("Chromosom", 1 + id, ":", chromosome)
    print("\tFenotyp:", algorithm.fenotypes[id])
    print("\tFunkcja przystosowania:", algorithm.fitness_values[id])
    print("\tPrawdopodobieństwo selekcji:", algorithm.fitness_values[id] * 100 / algorithm.sum_of_fitness(), "%")
print()

print("Wartość maksymalna funkcji w przedziale <0, 31>:", maximum)
print("Wartość x dla maksymalnej wartości:", xmax)
print("Liczba iteracji:", iteration)