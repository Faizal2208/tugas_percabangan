# Menerima input nilai performa karyawan (1 hingga 5)
performa = int(input("Masukkan nilai performa karyawan (1-5): "))

# Menerima input gaji tahunan karyawan
gaji_tahunan = float(input("Masukkan gaji tahunan karyawan: "))

# Menghitung bonus berdasarkan performa dengan percabangan ternary
bonus = (20 if performa == 5 else
         10 if performa == 4 else
         5 if performa == 3 else
         2 if performa == 2 else
         0) / 100 * gaji_tahunan

# Mencetak bonus tahunan
print("Bonus tahunan: $", bonus)
