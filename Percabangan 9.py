# Menerima input durasi peminjaman buku dalam hari
durasi_peminjaman = int(input("Masukkan durasi peminjaman buku (dalam hari): "))

# Menentukan jenis peminjaman berdasarkan durasi
if durasi_peminjaman <= 7:
    jenis_peminjaman = "Peminjaman Pendek"
elif 7 < durasi_peminjaman <= 30:
    jenis_peminjaman = "Peminjaman Menengah"
else:
    jenis_peminjaman = "Peminjaman Panjang"

# Mencetak jenis peminjaman
print("Jenis peminjaman:", jenis_peminjaman)
