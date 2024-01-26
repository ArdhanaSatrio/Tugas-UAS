class ManajemenInventori:
    def __init__(self):
        self.inventori = {}

    def tambah_barang(self, nama_barang, jumlah):
        """
        Fungsi untuk menambahkan barang ke dalam inventori.
        """
        if nama_barang in self.inventori:
            self.inventori[nama_barang] += jumlah
        else:
            self.inventori[nama_barang] = jumlah
        print(f"{jumlah} {nama_barang} berhasil ditambahkan ke dalam inventori.")

    def hapus_barang(self, nama_barang, jumlah):
        """
        Fungsi untuk menghapus barang dari inventori.
        """
        if nama_barang in self.inventori and self.inventori[nama_barang] >= jumlah:
            self.inventori[nama_barang] -= jumlah
            print(f"{jumlah} {nama_barang} berhasil dihapus dari inventori.")
        else:
            print(f"Tidak cukup {nama_barang} dalam inventori.")

    def perbarui_barang(self, nama_barang, jumlah_baru):
        """
        Fungsi untuk memperbarui jumlah barang dalam inventori.
        """
        if nama_barang in self.inventori:
            self.inventori[nama_barang] = jumlah_baru
            print(f"Jumlah {nama_barang} dalam inventori berhasil diperbarui menjadi {jumlah_baru}.")
        else:
            print(f"{nama_barang} tidak ditemukan dalam inventori.")

    def tampilkan_inventori(self):
        """
        Fungsi untuk menampilkan isi inventori.
        """
        if not self.inventori:
            print("Inventori kosong.")
        else:
            print("Inventori:")
            for barang, jumlah in self.inventori.items():
                print(f"{barang}: {jumlah}")

# Penggunaan Sistem Manajemen Inventori
sistem_inventori = ManajemenInventori()

while True:
    print("\nMenu:")
    print("1. Tambah Barang ke Inventori")
    print("2. Hapus Barang dari Inventori")
    print("3. Perbarui Jumlah Barang di Inventori")
    print("4. Tampilkan Inventori")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        nama_barang = input("Masukkan nama barang: ")
        jumlah_barang = int(input("Masukkan jumlah barang: "))
        sistem_inventori.tambah_barang(nama_barang, jumlah_barang)
    elif pilihan == '2':
        nama_barang = input("Masukkan nama barang: ")
        jumlah_barang = int(input("Masukkan jumlah barang yang akan dihapus: "))
        sistem_inventori.hapus_barang(nama_barang, jumlah_barang)
    elif pilihan == '3':
        nama_barang = input("Masukkan nama barang: ")
        jumlah_baru = int(input("Masukkan jumlah baru: "))
        sistem_inventori.perbarui_barang(nama_barang, jumlah_baru)
    elif pilihan == '4':
        sistem_inventori.tampilkan_inventori()
    elif pilihan == '5':
        print("Sistem manajemen inventori selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")

### __init__: Konstruktor kelas, digunakan untuk inisialisasi objek ManajemenInventori dengan dictionary kosong (self.inventori). ###
### tambah_barang: Fungsi untuk menambahkan barang ke dalam inventori. Jika barang sudah ada, jumlahnya akan diupdate. ###
### hapus_barang: Fungsi untuk menghapus barang dari inventori. Mengecek apakah jumlah barang yang akan dihapus tidak melebihi jumlah yang ada dalam inventori.
### perbarui_barang: Fungsi untuk memperbarui jumlah barang dalam inventori.###
### tampilkan_inventori: Fungsi untuk menampilkan isi inventori.
### Penggunaan Sistem Manajemen Inventori: Program memberikan menu kepada pengguna untuk menambah, menghapus, memperbarui, menampilkan inventori, atau keluar dari sistem. Setiap menu diimplementasikan dengan memanggil fungsi yang sesuai.