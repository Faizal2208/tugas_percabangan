# Menerima input informasi pembaruan (contoh: True jika pembaruan memerlukan restart, False jika tidak)
pembaruan_memerlukan_restart = input("Apakah pembaruan memerlukan restart? (True/False): ")

# Menentukan apakah sistem perlu di-restart berdasarkan informasi pembaruan
if pembaruan_memerlukan_restart.lower() == "true":
    print("Sistem perlu di-restart.")
elif pembaruan_memerlukan_restart.lower() == "false":
    print("Sistem tidak perlu di-restart.")
else:
    print("Informasi pembaruan tidak valid. Harap masukkan 'True' atau 'False'.")
