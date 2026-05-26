import random

# Uniform Crossover
def uniform_crossover(parent1, parent2):

    mask = [
        random.randint(0, 1)
        for _ in range(len(parent1))
    ]

    anak1 = []
    anak2 = []

    for i in range(len(parent1)):

        if mask[i] == 0:

            anak1.append(parent1[i])
            anak2.append(parent2[i])

        else:

            anak1.append(parent2[i])
            anak2.append(parent1[i])

    return anak1, anak2