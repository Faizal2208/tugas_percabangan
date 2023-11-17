# Menerima input penjualan bulanan produk (dalam unit)
penjualan_bulanan = int(input("Masukkan jumlah penjualan bulanan produk: "))

# Menentukan kategori produk berdasarkan penjualan
if penjualan_bulanan > 1000:
    kategori = "Produk Terlaris"
elif 500 <= penjualan_bulanan <= 1000:
    kategori = "Produk Populer"
else:
    kategori = "Produk Biasa"

# Mencetak kategori produk
print("Kategori produk:", kategori)
