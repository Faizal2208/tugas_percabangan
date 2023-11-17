from datetime import datetime

# Meminta pengguna untuk memasukkan estimasi waktu selesai proyek (dalam format tanggal: 'YYYY-MM-DD')
estimasi_selesai = input("Masukkan estimasi waktu selesai (YYYY-MM-DD): ")

# Meminta pengguna untuk memasukkan tanggal target selesai (dalam format tanggal: 'YYYY-MM-DD')
tanggal_target = input("Masukkan tanggal target selesai (YYYY-MM-DD): ")

# Mengubah string menjadi objek datetime
estimasi_selesai_date = datetime.strptime(estimasi_selesai, '%Y-%m-%d')
tanggal_target_date = datetime.strptime(tanggal_target, '%Y-%m-%d')

# Membandingkan tanggal estimasi dengan tanggal target
if estimasi_selesai_date <= tanggal_target_date:
    print("Tepat waktu")
else:
    print("Terlambat")
