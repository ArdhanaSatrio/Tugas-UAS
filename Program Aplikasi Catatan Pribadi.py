class PerekamanKeuangan:
    def __init__(self):
        self.saldo = 0
        self.transaksi = []

    def tambah_pendapatan(self, jumlah, keterangan):
        """
        Fungsi untuk menambahkan pendapatan ke dalam sistem.
        """
        self.saldo += jumlah
        self.transaksi.append({'Jenis': 'Pendapatan', 'Jumlah': jumlah, 'Keterangan': keterangan})
        print("Pendapatan berhasil ditambahkan.")

    def tambah_pengeluaran(self, jumlah, keterangan):
        """
        Fungsi untuk menambahkan pengeluaran ke dalam sistem.
        """
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi. Pengeluaran dibatalkan.")
        else:
            self.saldo -= jumlah
            self.transaksi.append({'Jenis': 'Pengeluaran', 'Jumlah': jumlah, 'Keterangan': keterangan})
            print("Pengeluaran berhasil ditambahkan.")

    def tampilkan_laporan(self):
        """
        Fungsi untuk menampilkan laporan keuangan.
        """
        print("\nLaporan Keuangan:")
        print("Saldo Saat Ini:", self.saldo)

        if not self.transaksi:
            print("Tidak ada transaksi.")
        else:
            print("Daftar Transaksi:")
            for transaksi in self.transaksi:
                print(f"{transaksi['Jenis']}: {transaksi['Jumlah']} ({transaksi['Keterangan']})")


# Penggunaan Sistem Perekaman Keuangan
keuangan_pribadi = PerekamanKeuangan()

while True:
    print("\nMenu:")
    print("1. Tambah Pendapatan")
    print("2. Tambah Pengeluaran")
    print("3. Tampilkan Laporan")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        jumlah_pendapatan = float(input("Masukkan jumlah pendapatan: "))
        keterangan_pendapatan = input("Tambahkan keterangan (opsional): ")
        keuangan_pribadi.tambah_pendapatan(jumlah_pendapatan, keterangan_pendapatan)
    elif pilihan == '2':
        jumlah_pengeluaran = float(input("Masukkan jumlah pengeluaran: "))
        keterangan_pengeluaran = input("Tambahkan keterangan (opsional): ")
        keuangan_pribadi.tambah_pengeluaran(jumlah_pengeluaran, keterangan_pengeluaran)
    elif pilihan == '3':
        keuangan_pribadi.tampilkan_laporan()
    elif pilihan == '4':
        print("Sistem perekaman keuangan selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")