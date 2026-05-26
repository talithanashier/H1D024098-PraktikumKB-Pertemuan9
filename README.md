Talitha Maharani Nashier-H1D024098-ShiftC

# Deskripsi

Program ini merupakan implementasi Algoritma Genetika (Genetic Algorithm) untuk menyelesaikan masalah Knapsack Problem.

Metode yang digunakan berdasarkan NIM:
- Seleksi : Tournament Selection
- Crossover : Uniform Crossover
- Mutasi : Inversion Mutation

---

# Struktur Folder

```bash
H1D024098-PraktikumKB-Pertemuan9/
│
├── main.py
├── inisiasipopulasi.py
├── evaluasifitness.py
├── selection.py
├── crossover.py
└── mutation.py
```

---

# Install Library

Install matplotlib terlebih dahulu:

```bash
pip install matplotlib
```

---

# Cara Menjalankan Program

Masuk ke folder project:

```bash
cd Pertemuan9
```

Jalankan program:

```bash
python main.py
```

---

# Data Barang

| Barang | Keuntungan | Ukuran |
|---|---|---|
| Barang1 | 10 | 5 |
| Barang2 | 40 | 4 |
| Barang3 | 30 | 6 |
| Barang4 | 50 | 3 |
| Barang5 | 35 | 7 |

Kapasitas maksimum:
15

---

# Hasil Program

Contoh output:

```bash
===== HASIL TERBAIK =====
Kromosom : [0, 1, 1, 1, 0]
Fitness  : 120

Barang Terpilih:
Barang2
Barang3
Barang4

Total Ukuran: 13
```

---

# Penjelasan Hasil

Kromosom:
```bash
[0, 1, 1, 1, 0]
```

Artinya:
- Barang1 tidak dipilih
- Barang2 dipilih
- Barang3 dipilih
- Barang4 dipilih
- Barang5 tidak dipilih

Total keuntungan:
```bash
40 + 30 + 50 = 120
```

Total ukuran:
```bash
4 + 6 + 3 = 13
```

Karena total ukuran tidak melebihi kapasitas maksimum, maka solusi valid.

---

# Kesimpulan

Algoritma Genetika berhasil diterapkan pada Knapsack Problem menggunakan:
- Tournament Selection
- Uniform Crossover
- Inversion Mutation

Fitness terbaik yang diperoleh:
```bash
120
```
