# Metode append() adalah salah satu metode bawaan Python yang digunakan dengan list. 
# Metode ini berfungsi untuk menambahkan elemen baru ke akhir list.

class Buku:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang

# Membuat daftar kosong
daftar_buku = []

# Membuat buku baru
buku1 = Buku("Pemrograman Python", "John Doe")
buku2 = Buku("Algoritma", "Jane Smith")

# Menambahkan buku ke daftar
daftar_buku.append(buku1)
daftar_buku.append(buku2)

# Menampilkan jumlah buku
print(f"Total buku: {len(daftar_buku)}")
