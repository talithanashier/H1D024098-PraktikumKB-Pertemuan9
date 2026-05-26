import random

# Inversion Mutation
def inversion_mutation(kromosom):

    posisi1 = random.randint(
        0,
        len(kromosom)-2
    )

    posisi2 = random.randint(
        posisi1+1,
        len(kromosom)-1
    )

    kromosom[posisi1:posisi2] = list(
        reversed(
            kromosom[posisi1:posisi2]
        )
    )

    return kromosom