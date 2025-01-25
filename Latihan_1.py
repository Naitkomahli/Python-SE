# Definisi class
class Mahasiswa:
    # Constractor: Fungsi yang dijalankan saat objek dibuat
    def __init__(self, nama, NIM, jurusan):
        self.nama = nama # ATRIBUT NAMA
        self.NIM = NIM #ATRIBUT NIM
        self.jurusan = jurusan #ATRIBUT JURUSAN

    # Method untuk menampilkan informasi mahasiswa
    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.NIM}")
        print(f"Jurusan: {self.jurusan}")

    # Menambah method baru
    def update_jurusan(self, jurusan_baru):
        self.jurusan = jurusan_baru

# Membuat object dari class Mahasiswa
mhs1 = Mahasiswa("Oktian", "14034", "Teknik Informatikan")
mhs2 = Mahasiswa("Ramadhan", "13040222140105", "Antropologi")

# Memanggil method tampilkan_info
mhs1.tampilkan_info()
print("------------")
mhs2.tampilkan_info()
print(" ")
print("===Setelah di Update===")
# Update jurusan
mhs1.update_jurusan("Sastra Inggris")
mhs1.tampilkan_info()