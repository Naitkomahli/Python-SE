 
# Class induk
class Mahasiswa:
    def __init__(self, nama, NIM):
        self.nama = nama
        self.NIM = NIM

    def tampilkan_info(self):
        print(f"Nama: {self.nama}") 
        print(f"NIM: {self.NIM}")

# Class anak
class MahasiswaInternational(Mahasiswa):
    def __init__(self, nama, NIM, negara_asal):
        super().__init__(nama, NIM) # Panggil constructor class induk
        self.negara_asal = negara_asal

    def tampilkan_info(self):
        super().tampilkan_info() # panggil method class induk
        print(f"Negara Asal: {self.negara_asal}")

# Membuat objek
mhs1 = MahasiswaInternational("Oktian", "14034", "Indonesia")

print("=== INHERITANCE ===")
mhs1.tampilkan_info()