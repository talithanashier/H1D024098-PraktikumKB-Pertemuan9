import random

# Tournament Selection
def tournament_selection(
    populasi,
    fitness_populasi,
    k=3
):

    peserta_index = random.sample(
        range(len(populasi)),
        k
    )

    peserta = []

    for i in peserta_index:

        peserta.append(
            (populasi[i], fitness_populasi[i])
        )

    peserta.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return peserta[0][0]