class Buku:
    def __init__(self, judul, pengarang, tahun):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun = tahun

    def tampilkan_detail(self):
        print("-" * 30)
        print(f"Judul : {self.judul}")
        print(f"Pengarang : {self.pengarang}")
        print(f"Tahun terbit : {self.tahun}")
        print("-" * 30)

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku) 
        print(f"Berhasil menambahkan buku {buku.judul}")

    def tampilkan_buku(self):
        if not self.daftar_buku:
            print("Tidak ada buku di perpustakaan")
        else:
            print("Daftar buku di perpustakaan")
            for buku in self.daftar_buku:
                buku.tampilkan_detail()

    def hapus_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower:
                self.daftar_buku.remove(buku)
                print(f"Buku {judul} telah dihapus")
                return
        print(f"Buku dengan judul {judul} tidak ditemukan")

    def cari_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower():
                print("Buku ditemukan : ")
                buku.tampilkan_detail()
                return
        print (f"Buku {judul} tidak ditemukan")
    
# ==== Program Utama ====
perpustakaan = Perpustakaan()

while True:
    print("\n=== Sistem Manajemen Perpustakaan ===")
    print("1. Tambah Buku")
    print("2. Tampilkan Semua Buku")
    print("3. Cari Buku")
    print("4. Hapus Buku")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        judul = input("Masukkan judul buku: ")
        pengarang = input("Masukkan pengarang buku: ")
        tahun = input("Masukkan tahun terbit: ")
        buku_baru = Buku(judul, pengarang, tahun)
        perpustakaan.tambah_buku(buku_baru)
    elif pilihan == "2":
        perpustakaan.tampilkan_buku()
    elif pilihan == "3":
        judul = input("Masukkan judul buku yang dicari: ")
        perpustakaan.cari_buku(judul)
    elif pilihan == "4":
        judul = input("Masukkan judul buku yang akan dihapus: ")
        perpustakaan.hapus_buku(judul)
    elif pilihan == "5":
        print("Keluar dari program. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
