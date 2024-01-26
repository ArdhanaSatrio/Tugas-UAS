class AplikasiPencatatanKesehatan:
    def __init__(self):
        self.catatan_kesehatan = []

    def tambah_data_kesehatan(self, berat_badan, tinggi_badan, aktivitas_fisik):
        """
        Fungsi untuk menambahkan data kesehatan baru ke dalam aplikasi.
        """
        data_kesehatan = {'Berat Badan': berat_badan, 'Tinggi Badan': tinggi_badan, 'Aktivitas Fisik': aktivitas_fisik}
        self.catatan_kesehatan.append(data_kesehatan)
        print("Data kesehatan berhasil ditambahkan.")

    def tampilkan_catatan_kesehatan(self):
        """
        Fungsi untuk menampilkan semua data kesehatan yang ada dalam aplikasi.
        """
        if not self.catatan_kesehatan:
            print("Tidak ada data kesehatan.")
        else:
            print("Daftar Data Kesehatan:")
            for data_kesehatan in self.catatan_kesehatan:
                print(f"Berat Badan: {data_kesehatan['Berat Badan']} kg, "
                      f"Tinggi Badan: {data_kesehatan['Tinggi Badan']} cm, "
                      f"Aktivitas Fisik: {data_kesehatan['Aktivitas Fisik']}")

# Penggunaan Aplikasi Pencatatan Kesehatan
aplikasi_kesehatan = AplikasiPencatatanKesehatan()

while True:
    print("\nMenu:")
    print("1. Tambah Data Kesehatan")
    print("2. Tampilkan Catatan Kesehatan")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == '1':
        berat_badan = float(input("Masukkan berat badan (kg): "))
        tinggi_badan = float(input("Masukkan tinggi badan (cm): "))
        aktivitas_fisik = input("Masukkan tingkat aktivitas fisik (rendah/normal/tinggi): ")
        aplikasi_kesehatan.tambah_data_kesehatan(berat_badan, tinggi_badan, aktivitas_fisik)
    elif pilihan == '2':
        aplikasi_kesehatan.tampilkan_catatan_kesehatan()
    elif pilihan == '3':
        print("Aplikasi pencatatan kesehatan selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")