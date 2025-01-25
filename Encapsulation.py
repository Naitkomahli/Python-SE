
class Mahasiswa:
    def __init__(self, nama, NIM):
        self.__nama = nama # Private attribute
        self.__NIM = NIM # Private attribute

    def tampilkan_info(self):
        print(f"Nama : {self.__nama}")
        print(f"NIM : {self.__NIM}")

    def ubah_nama(self, nama_baru):
        self.__nama = nama_baru

# membuat objek
mhs = Mahasiswa("Oktian", "14034")
mhs.tampilkan_info()

print("=== UPDATE NAMA ===")
# update nama
mhs. ubah_nama("Ramadhan")
mhs.tampilkan_info()