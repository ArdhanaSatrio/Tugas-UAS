class AplikasiManajemenTugas:
    def __init__(self):
        # Inisialisasi dictionary untuk menyimpan tugas dan statusnya (selesai/belum selesai)
        self.tugas = {}

    def tambah_tugas(self, nama_tugas):
        """
        Fungsi untuk menambahkan tugas ke dalam daftar.
        """
        if nama_tugas not in self.tugas:
            self.tugas[nama_tugas] = False  # Set status tugas menjadi belum selesai
            print(f"Tugas '{nama_tugas}' telah ditambahkan.")
        else:
            print(f"Tugas '{nama_tugas}' sudah ada dalam daftar.")

    def hapus_tugas(self, nama_tugas):
        """
        Fungsi untuk menghapus tugas dari daftar.
        """
        if nama_tugas in self.tugas:
            del self.tugas[nama_tugas]
            print(f"Tugas '{nama_tugas}' telah dihapus.")
        else:
            print(f"Tugas '{nama_tugas}' tidak ditemukan dalam daftar.")

    def tandai_selesai(self, nama_tugas):
        """
        Fungsi untuk menandai suatu tugas sebagai selesai.
        """
        if nama_tugas in self.tugas:
            self.tugas[nama_tugas] = True  # Set status tugas menjadi selesai
            print(f"Tugas '{nama_tugas}' telah ditandai selesai.")
        else:
            print(f"Tugas '{nama_tugas}' tidak ditemukan dalam daftar.")

    def tampilkan_tugas(self):
        """
        Fungsi untuk menampilkan semua tugas beserta statusnya.
        """
        if not self.tugas:
            print("Tidak ada tugas dalam daftar.")
        else:
            print("Daftar Tugas:")
            for tugas, selesai in self.tugas.items():
                status = "Selesai" if selesai else "Belum Selesai"
                print(f"- {tugas} ({status})")


# Penggunaan Aplikasi Manajemen Tugas
aplikasi = AplikasiManajemenTugas()

while True:
    print("\nMenu:")
    print("1. Tambah Tugas")
    print("2. Hapus Tugas")
    print("3. Tandai Selesai")
    print("4. Tampilkan Tugas")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        nama_tugas = input("Masukkan nama tugas: ")
        aplikasi.tambah_tugas(nama_tugas)
    elif pilihan == '2':
        nama_tugas = input("Masukkan nama tugas yang akan dihapus: ")
        aplikasi.hapus_tugas(nama_tugas)
    elif pilihan == '3':
        nama_tugas = input("Masukkan nama tugas yang selesai: ")
        aplikasi.tandai_selesai(nama_tugas)
    elif pilihan == '4':
        aplikasi.tampilkan_tugas()
    elif pilihan == '5':
        print("Aplikasi selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")

###  __init__: Konstruktor kelas, digunakan untuk inisialisasi objek AplikasiManajemenTugas dengan dictionary kosong (self.tugas). ###
### tambah_tugas: Fungsi untuk menambahkan tugas ke dalam dictionary tugas. Mengecek apakah tugas sudah ada sebelumnya. ###
### hapus_tugas: Fungsi untuk menghapus tugas dari dictionary tugas. Mengecek apakah tugas tersebut ada sebelum dihapus. ###
### tandai_selesai: Fungsi untuk menandai suatu tugas sebagai selesai dengan mengubah nilai statusnya dalam dictionary tugas. ###
### tampilkan_tugas: Fungsi untuk menampilkan semua tugas beserta statusnya. Jika tidak ada tugas, memberikan pesan bahwa tidak ada tugas dalam daftar. ###