import random
import matplotlib.pyplot as plt

from inisiasipopulasi import inisialisasi_populasi
from evaluasifitness import hitung_fitness
from selection import tournament_selection
from crossover import uniform_crossover
from mutation import inversion_mutation

# Data barang
barang = [
    ("Barang1", 10, 5),
    ("Barang2", 40, 4),
    ("Barang3", 30, 6),
    ("Barang4", 50, 3),
    ("Barang5", 35, 7)
]

kapasitas_tas = 15


def run_ga():

    jumlah_generasi = 20
    jumlah_populasi = 10
    jumlah_gen = len(barang)

    populasi = inisialisasi_populasi(
        jumlah_populasi,
        jumlah_gen
    )

    best_fitness_list = []

    best_solution = None
    best_fitness = 0

    for generasi in range(jumlah_generasi):

        # Hitung fitness
        fitness_populasi = [
            hitung_fitness(
                individu,
                barang,
                kapasitas_tas
            )
            for individu in populasi
        ]

        # Fitness terbaik
        fitness_terbaik = max(fitness_populasi)

        best_fitness_list.append(fitness_terbaik)

        index_best = fitness_populasi.index(
            fitness_terbaik
        )

        # Simpan solusi terbaik
        if fitness_terbaik > best_fitness:

            best_fitness = fitness_terbaik

            best_solution = populasi[index_best]

        print(f"\nGenerasi {generasi+1}")
        print("Fitness Terbaik:", fitness_terbaik)

        # Populasi baru
        new_populasi = []

        while len(new_populasi) < jumlah_populasi:

            # Seleksi
            parent1 = tournament_selection(
                populasi,
                fitness_populasi
            )

            parent2 = tournament_selection(
                populasi,
                fitness_populasi
            )

            # Crossover
            anak1, anak2 = uniform_crossover(
                parent1,
                parent2
            )

            # Mutasi
            anak1 = inversion_mutation(anak1)
            anak2 = inversion_mutation(anak2)

            # Tambah ke populasi baru
            new_populasi.extend(
                [anak1, anak2]
            )

        populasi = new_populasi[:jumlah_populasi]

    # Hasil terbaik
    print("\n===== HASIL TERBAIK =====")
    print("Kromosom :", best_solution)
    print("Fitness  :", best_fitness)

    print("\nBarang Terpilih:")

    total_ukuran = 0

    for i in range(len(best_solution)):

        if best_solution[i] == 1:

            print(barang[i][0])

            total_ukuran += barang[i][2]

    print("Total Ukuran:", total_ukuran)

    # Grafik
    plt.plot(best_fitness_list)

    plt.title("Perkembangan Fitness")

    plt.xlabel("Generasi")

    plt.ylabel("Fitness")

    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    run_ga()