# Menerima input status persiapan proyek (Siap atau Tunda)
status_persiapan = input("Masukkan status persiapan proyek (Siap/Tunda): ")

# Menentukan apakah proyek dapat diluncurkan
if status_persiapan == "Siap":
    print("Proyek diluncurkan")
elif status_persiapan == "Tunda":
    print("Proyek ditunda")
else:
    print("Status persiapan tidak valid. Harap masukkan 'Siap' atau 'Tunda'.")
